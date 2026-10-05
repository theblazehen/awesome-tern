# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""Maintain awesome-tern: data in data/, README.md is generated.

Commands:
  check      validate data and fail if README.md or the issue form is stale
  build      regenerate README.md and the submission issue form
  refresh    fetch GitHub metadata for every entry into data/metadata.json
  discover   search GitHub for Tern projects not yet on the list (markdown to stdout)
  submit     turn a submission issue body into a new entry file
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ENTRIES = DATA / "entries"
METADATA = DATA / "metadata.json"
README = ROOT / "README.md"
ISSUE_FORM = ROOT / ".github" / "ISSUE_TEMPLATE" / "submission.yml"

GITHUB_REPO_URL = re.compile(r"^https://github\.com/([\w.-]+)/([\w.-]+)/?$")
INACTIVE_AFTER = dt.timedelta(days=180)
SORTS = {"stars", "manual"}

# --------------------------------------------------------------------------- data


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def dump_yaml(path: Path, data) -> None:
    text = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    path.write_text(text, encoding="utf-8")


def load_site() -> dict:
    return load_yaml(DATA / "site.yml")


def load_sections() -> list[dict]:
    """Sections as a flat, ordered list; children carry `parent`."""
    flat: list[dict] = []

    def walk(items, parent):
        for s in items:
            children = s.get("children", [])
            node = {k: v for k, v in s.items() if k != "children"}
            node["parent"] = parent
            node.setdefault("sort", "stars")
            flat.append(node)
            walk(children, s["id"])

    walk(load_yaml(DATA / "sections.yml"), None)
    return flat


def load_entries() -> dict[str, dict]:
    return {p.stem: load_yaml(p) for p in sorted(ENTRIES.glob("*.yml"))}


def load_metadata() -> dict:
    return json.loads(METADATA.read_text()) if METADATA.exists() else {}


def entry_repo(entry: dict) -> str | None:
    """owner/name for GitHub metadata: explicit `repo`, else a repo-root URL."""
    if entry.get("repo"):
        return entry["repo"]
    m = GITHUB_REPO_URL.match(entry["url"])
    return f"{m[1]}/{m[2]}" if m else None


# ----------------------------------------------------------------------- validate


def validate(sections, entries) -> list[str]:
    errors: list[str] = []
    ids = {s["id"] for s in sections}
    seen_urls: dict[str, str] = {}
    for s in sections:
        if s["sort"] not in SORTS:
            errors.append(f"section {s['id']}: sort must be one of {sorted(SORTS)}")
    for eid, e in entries.items():
        where = f"data/entries/{eid}.yml"
        for field in ("name", "url", "section", "description"):
            if not e.get(field):
                errors.append(f"{where}: missing {field}")
        if e.get("section") and e["section"] not in ids:
            errors.append(f"{where}: unknown section {e['section']!r}")
        url = e.get("url", "")
        if url in seen_urls:
            errors.append(f"{where}: duplicate url (also {seen_urls[url]})")
        seen_urls[url] = eid
        desc = (e.get("description") or "").strip()
        if desc:
            if desc[0].islower():
                errors.append(f"{where}: description must not start with a lowercase letter")
            if not desc.endswith("."):
                errors.append(f"{where}: description must end with a period")
            if "\n" in desc:
                errors.append(f"{where}: description must be one line")
    return errors


# -------------------------------------------------------------------------- build


def anchor(title: str) -> str:
    a = title.strip().lower()
    a = re.sub(r"[^\w\- ]", "", a)
    return a.replace(" ", "-")


def entry_flag(entry: dict, meta: dict) -> str:
    """Status marker from the last refresh: unavailable, archived or inactive."""
    repo = entry_repo(entry)
    status = (meta.get(repo) or {}).get("status") if repo else None
    return f" `{status}`" if status else ""


def sorted_entries(section: dict, items: list[tuple[str, dict]], meta: dict):
    if section["sort"] == "manual":
        return sorted(items, key=lambda kv: (kv[1].get("order", 1000), kv[1]["name"].lower()))

    def stars(kv):
        repo = entry_repo(kv[1])
        return (meta.get(repo) or {}).get("stars", -1) if repo else -1

    return sorted(items, key=lambda kv: (-stars(kv), kv[1]["name"].lower()))


def render_readme(site, sections, entries, meta) -> str:
    by_section: dict[str, list[tuple[str, dict]]] = {}
    for eid, e in entries.items():
        by_section.setdefault(e["section"], []).append((eid, e))

    out = [f"# {site['title']}", ""]
    out += [f"> {site['tagline']}", ""]
    if site.get("intro"):
        out += [site["intro"].strip(), ""]

    out += ["## Contents", ""]
    for s in sections:
        indent = "  " if s["parent"] else ""
        out.append(f"{indent}- [{s['title']}](#{anchor(s['title'])})")
    out.append("")

    for s in sections:
        out += [f"{'###' if s['parent'] else '##'} {s['title']}", ""]
        if s.get("blurb"):
            out += [s["blurb"].strip(), ""]
        items = sorted_entries(s, by_section.get(s["id"], []), meta)
        for _, e in items:
            out.append(f"- [{e['name']}]({e['url']}) - {e['description'].strip()}{entry_flag(e, meta)}")
        if items:
            out.append("")

    out += ["## Contributing", "", site["contributing"].strip(), ""]
    return "\n".join(out)


def render_issue_form(sections) -> str:
    options = [s["id"] for s in sections if s.get("submittable", True)]
    form = {
        "name": "Suggest a project",
        "description": "Add a plugin, app, tool or resource to the list.",
        "title": "Add: ",
        "labels": ["submission"],
        "body": [
            {"type": "markdown", "attributes": {"value": "This form is generated by `tools/awesome_tern.py build`. A bot turns it into a pull request."}},
            {"type": "input", "id": "url", "attributes": {"label": "Link", "description": "Repository, docs page or post."}, "validations": {"required": True}},
            {"type": "input", "id": "name", "attributes": {"label": "Name", "description": "Leave empty to use the repository name."}},
            {"type": "dropdown", "id": "section", "attributes": {"label": "Section", "options": options}, "validations": {"required": True}},
            {"type": "input", "id": "description", "attributes": {"label": "Description", "description": "One plain sentence ending in a period. Maintainers may reword it.", "placeholder": "Renders `kubectl get pods` as a native table."}, "validations": {"required": True}},
        ],
    }
    header = "# Generated by tools/awesome_tern.py build. Edit data/sections.yml instead.\n"
    return header + yaml.safe_dump(form, sort_keys=False, allow_unicode=True, width=100)


def generated() -> dict[Path, str]:
    site, sections, entries, meta = load_site(), load_sections(), load_entries(), load_metadata()
    return {
        README: render_readme(site, sections, entries, meta),
        ISSUE_FORM: render_issue_form(sections),
    }


def cmd_build(_args) -> int:
    for path, text in generated().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


def cmd_check(_args) -> int:
    errors = validate(load_sections(), load_entries())
    for path, text in generated().items():
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            errors.append(f"{path.relative_to(ROOT)} is stale (run `mise run build`)")
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    return 1 if errors else 0


# ------------------------------------------------------------------------- github


def github_token() -> str | None:
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def github(path: str, token: str | None, accept: str = "application/vnd.github+json"):
    req = urllib.request.Request(f"https://api.github.com{path}")
    req.add_header("Accept", accept)
    req.add_header("User-Agent", "awesome-tern")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read()
            break
        except urllib.error.HTTPError as err:
            # Search has a per-minute limit; GitHub says how long to wait.
            if err.code not in (403, 429) or attempt == 2 or "Retry-After" not in err.headers:
                raise
            time.sleep(min(int(err.headers["Retry-After"]), 90))
    return body.decode("utf-8", "replace") if accept.endswith(".raw") else json.loads(body)


def cmd_refresh(_args) -> int:
    token = github_token()
    repos = sorted({r for e in load_entries().values() if (r := entry_repo(e))})
    now = dt.datetime.now(dt.UTC)
    meta: dict = {}
    for repo in repos:
        try:
            info = github(f"/repos/{repo}", token)
        except urllib.error.HTTPError as err:
            if err.code != 404:
                raise
            meta[repo] = {"stars": 0, "status": "unavailable"}
            print(f"{repo}: unavailable", file=sys.stderr)
            continue
        pushed = dt.datetime.fromisoformat(info["pushed_at"])
        status = "archived" if info["archived"] else "inactive" if now - pushed > INACTIVE_AFTER else None
        meta[repo] = {"stars": info["stargazers_count"], "status": status}
    METADATA.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n")
    print(f"refreshed {len(repos)} repositories")
    return 0


# Searches cast a wide net; MARKERS decide what is really about Stencil's Tern.
# GitHub search matches substrings ("pattern plugin install", "stencil.so/terms"),
# and "tern" is also the old ternjs code-analysis engine.
DISCOVERY_REPO_QUERIES = [
    "topic:tern-plugin",
    "topic:stencil-tern",
    '"stencil.so/tern" in:readme',
    '"tern plugin install" in:readme',
    '"docs.stencil.so/tern" in:readme',
]
DISCOVERY_CODE_QUERIES = [
    '"tern.lens.define"',
    '"tern.block.define"',
    '"tern.chrome.status"',
    '"tern plugin install"',
    '"stencil.so/tern"',
]
MARKERS = re.compile(
    r"stencil\.so/tern\b|\btern plugin install\b|\btern\.(?:lens|block)\.define\b"
    r"|\btern\.chrome\.|Tern Surface Protocol|\bTERN_(?:DAEMON|WINDOW)_SOCKET\b"
)


def known_repos(entries) -> set[str]:
    known = {r.lower() for e in entries.values() if (r := entry_repo(e))}
    known.add(os.environ.get("GITHUB_REPOSITORY", "theblazehen/awesome-tern").lower())
    for e in entries.values():
        m = re.match(r"^https://github\.com/([\w.-]+)/([\w.-]+)", e["url"])
        if m:
            known.add(f"{m[1]}/{m[2]}".lower())
    return known


def cmd_discover(args) -> int:
    """Print Tern repositories created in the last `--days` days that aren't listed.

    The window keeps reports short and stateless: anything not added simply ages out.
    """
    token = github_token()
    known = known_repos(load_entries())
    cutoff = dt.datetime.now(dt.UTC) - dt.timedelta(days=args.days)
    found: dict[str, dict] = {}
    failed: list[str] = []

    def add(repo: dict, query: str):
        name = repo["full_name"]
        if name.lower() in known or repo.get("fork"):
            return
        hit = found.setdefault(name, {"repo": repo, "queries": [], "verified": False})
        hit["queries"].append(query)
        return hit

    for q in DISCOVERY_REPO_QUERIES:
        try:
            res = github(f"/search/repositories?per_page=100&q={urllib.parse.quote(q)}", token)
        except urllib.error.HTTPError as err:
            failed.append(f"{q} (HTTP {err.code})")
            continue
        for repo in res["items"]:
            add(repo, q)
    for q in DISCOVERY_CODE_QUERIES:
        time.sleep(7)  # code search allows about ten requests a minute
        try:
            res = github(
                f"/search/code?per_page=100&q={urllib.parse.quote(q)}", token,
                accept="application/vnd.github.text-match+json",
            )
        except urllib.error.HTTPError as err:
            failed.append(f"code: {q} (HTTP {err.code})")
            continue
        for item in res["items"]:
            fragments = " ".join(m.get("fragment", "") for m in item.get("text_matches", []))
            if MARKERS.search(fragments) and (hit := add(item["repository"], f"code: {q}")):
                hit["verified"] = True

    for name, hit in list(found.items()):
        try:
            if not hit["verified"]:
                readme = github(f"/repos/{name}/readme", token, accept="application/vnd.github.raw")
                if not MARKERS.search(readme):
                    del found[name]
                    continue
            # Code search results omit fork and stars.
            if "stargazers_count" not in hit["repo"]:
                hit["repo"] = github(f"/repos/{name}", token)
        except urllib.error.HTTPError:
            del found[name]
            continue
        created = dt.datetime.fromisoformat(hit["repo"]["created_at"])
        if hit["repo"].get("fork") or created < cutoff:
            del found[name]

    lines = []
    for name, hit in sorted(found.items(), key=lambda kv: -kv[1]["repo"].get("stargazers_count", 0)):
        r = hit["repo"]
        desc = (r.get("description") or "").strip() or "no description"
        lines.append(
            f"- [{name}]({r['html_url']}) ★{r.get('stargazers_count', '?')}: {desc}"
            f" _(matched: {', '.join(sorted(set(hit['queries'])))})_"
        )
    if failed:
        print("queries that failed: " + "; ".join(failed), file=sys.stderr)
    if lines:
        print(f"Tern-related repositories created in the last {args.days} days that aren't on the list:\n")
        print("\n".join(lines))
    return 0


# ------------------------------------------------------------------------- submit


def parse_issue_form(body: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for block in re.split(r"^### ", body, flags=re.M)[1:]:
        label, _, value = block.partition("\n")
        value = value.strip()
        fields[label.strip()] = "" if value == "_No response_" else value
    return fields


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def cmd_submit(args) -> int:
    fields = parse_issue_form(Path(args.body_file).read_text(encoding="utf-8"))
    url = fields.get("Link", "").strip()
    section = fields.get("Section", "").strip()
    description = " ".join(fields.get("Description", "").split())
    if description and description[-1] not in ".!?":
        description += "."
    if description:
        description = description[0].upper() + description[1:]
    if not url.startswith("https://") or not section or not description:
        raise SystemExit("submission needs a https link, a section and a description")
    m = re.match(r"^https://github\.com/([\w.-]+)/([\w.-]+)", url)
    name = fields.get("Name", "").strip() or (m[2] if m else "")
    if not name:
        raise SystemExit("submission needs a name for non-GitHub links")
    if m:
        try:
            github(f"/repos/{m[1]}/{m[2]}", github_token())
        except urllib.error.HTTPError as err:
            raise SystemExit(f"{url} isn't a public GitHub repository (HTTP {err.code})") from None

    entries = load_entries()
    if any(e["url"].rstrip("/") == url.rstrip("/") for e in entries.values()):
        raise SystemExit(f"{url} is already on the list")
    eid = slugify(f"{m[1]}-{m[2]}" if m else name)
    entry = {"name": name, "url": url, "section": section, "description": description}
    errors = validate(load_sections(), {eid: entry})
    if errors:
        raise SystemExit("\n".join(errors))
    dump_yaml(ENTRIES / f"{eid}.yml", entry)
    print(eid)
    return 0


# --------------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check").set_defaults(func=cmd_check)
    sub.add_parser("build").set_defaults(func=cmd_build)
    sub.add_parser("refresh").set_defaults(func=cmd_refresh)
    p = sub.add_parser("discover")
    p.add_argument("--days", type=int, default=7, help="only report repositories created this recently")
    p.set_defaults(func=cmd_discover)
    p = sub.add_parser("submit")
    p.add_argument("body_file", help="file holding the issue body")
    p.set_defaults(func=cmd_submit)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
