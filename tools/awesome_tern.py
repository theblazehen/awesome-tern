# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml>=6"]
# ///
"""Maintain awesome-tern. list.yml is the source; README.md is generated from it.

Commands:
  check      validate list.yml
  build      regenerate README.md
  refresh    fetch stars and status for GitHub entries into metadata.json
  discover   print recently created Tern repositories that aren't listed
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
from collections.abc import Iterator
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LIST = ROOT / "list.yml"
METADATA = ROOT / "metadata.json"
README = ROOT / "README.md"

GITHUB_REPO_URL = re.compile(r"^https://github\.com/([\w.-]+)/([\w.-]+)/?$")
INACTIVE_AFTER = dt.timedelta(days=180)
SORTS = {"stars", "manual"}


# --------------------------------------------------------------------------- data


def load_list() -> dict:
    try:
        with LIST.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as err:
        raise SystemExit(f"error: list.yml is not valid YAML\n{err}") from None


def load_metadata() -> dict:
    return json.loads(METADATA.read_text()) if METADATA.exists() else {}


def walk(sections: list[dict], depth: int = 0) -> Iterator[tuple[dict, int]]:
    for s in sections:
        yield s, depth
        yield from walk(s.get("sections", []), depth + 1)


def all_entries(data: dict) -> Iterator[dict]:
    for s, _ in walk(data["sections"]):
        yield from s.get("entries", [])


def entry_repo(entry: dict) -> str | None:
    """owner/name for GitHub metadata: explicit `repo`, else a repository URL."""
    if entry.get("repo"):
        return entry["repo"]
    m = GITHUB_REPO_URL.match(entry["url"])
    return f"{m[1]}/{m[2]}" if m else None


# ----------------------------------------------------------------------- validate


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    for key in ("title", "tagline", "sections"):
        if not data.get(key):
            errors.append(f"list.yml: missing {key}")
    seen: dict[str, str] = {}
    for s, _ in walk(data.get("sections", [])):
        title = s.get("title") or "?"
        if not s.get("title"):
            errors.append("a section is missing its title")
        if s.get("sort", "stars") not in SORTS:
            errors.append(f"{title}: sort must be one of {sorted(SORTS)}")
        for e in s.get("entries", []):
            where = f"{title} > {e.get('name') or e.get('url') or '?'}"
            for field in ("name", "url", "description"):
                if not e.get(field):
                    errors.append(f"{where}: missing {field}")
            unknown = set(e) - {"name", "url", "description", "repo"}
            if unknown:
                errors.append(f"{where}: unknown fields {sorted(unknown)}")
            url = e.get("url", "")
            if url and not url.startswith("https://"):
                errors.append(f"{where}: url must start with https://")
            if url in seen:
                errors.append(f"{where}: also listed under {seen[url]}")
            seen[url] = title
            desc = (e.get("description") or "").strip()
            if desc:
                if desc[0].islower():
                    errors.append(f"{where}: description must not start with a lowercase letter")
                if not desc.endswith("."):
                    errors.append(f"{where}: description must end with a period")
                if "\n" in desc:
                    errors.append(f"{where}: description must be one line")
    return errors


def cmd_check(_args) -> int:
    errors = validate(load_list())
    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    return 1 if errors else 0


# -------------------------------------------------------------------------- build


def anchor(title: str) -> str:
    return re.sub(r"[^\w\- ]", "", title.strip().lower()).replace(" ", "-")


def entry_flag(entry: dict, meta: dict) -> str:
    """Marker from the last refresh: unavailable, archived or inactive."""
    repo = entry_repo(entry)
    status = (meta.get(repo) or {}).get("status") if repo else None
    return f" `{status}`" if status else ""


def ordered(section: dict, meta: dict) -> list[dict]:
    entries = section.get("entries", [])
    if section.get("sort", "stars") == "manual":
        return entries

    def stars(e):
        repo = entry_repo(e)
        return (meta.get(repo) or {}).get("stars", -1) if repo else -1

    return sorted(entries, key=lambda e: (-stars(e), e["name"].lower()))


def render(data: dict, meta: dict) -> str:
    out = [
        "<!-- Generated from list.yml by tools/awesome_tern.py. Edit list.yml, not this file. -->",
        "",
        f"# {data['title']}",
        "",
        f"> {data['tagline'].strip()}",
        "",
    ]
    if data.get("intro"):
        out += [data["intro"].strip(), ""]
    out += ["## Contents", ""]
    for s, depth in walk(data["sections"]):
        out.append(f"{'  ' * depth}- [{s['title']}](#{anchor(s['title'])})")
    out.append("")
    for s, depth in walk(data["sections"]):
        out += [f"{'#' * (depth + 2)} {s['title']}", ""]
        if s.get("blurb"):
            out += [s["blurb"].strip(), ""]
        items = ordered(s, meta)
        for e in items:
            out.append(f"- [{e['name']}]({e['url']}) - {e['description'].strip()}{entry_flag(e, meta)}")
        if items:
            out.append("")
    if data.get("contributing"):
        out += ["## Contributing", "", data["contributing"].strip(), ""]
    return "\n".join(out)


def cmd_build(_args) -> int:
    data = load_list()
    errors = validate(data)
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1
    README.write_text(render(data, load_metadata()), encoding="utf-8")
    print("wrote README.md")
    return 0


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
    repos = sorted({r for e in all_entries(load_list()) if (r := entry_repo(e))})
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


def listed_repos(data: dict) -> set[str]:
    known = {os.environ.get("GITHUB_REPOSITORY", "theblazehen/awesome-tern").lower()}
    for e in all_entries(data):
        if repo := entry_repo(e):
            known.add(repo.lower())
        if m := re.match(r"^https://github\.com/([\w.-]+)/([\w.-]+)", e["url"]):
            known.add(f"{m[1]}/{m[2]}".lower())
    return known


def cmd_discover(args) -> int:
    """Print Tern repositories created in the last `--days` days that aren't listed.

    The window keeps reports short and stateless: anything not added simply ages out.
    """
    token = github_token()
    known = listed_repos(load_list())
    cutoff = dt.datetime.now(dt.UTC) - dt.timedelta(days=args.days)
    found: dict[str, dict] = {}
    failed: list[str] = []

    def add(repo: dict, query: str):
        name = repo["full_name"]
        if name.lower() in known or repo.get("fork"):
            return None
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
            # Code search results omit fork, stars and creation date.
            if "created_at" not in hit["repo"]:
                hit["repo"] = github(f"/repos/{name}", token)
            created = dt.datetime.fromisoformat(hit["repo"]["created_at"])
            if hit["repo"].get("fork") or created < cutoff:
                del found[name]
                continue
            if not hit["verified"]:
                readme = github(f"/repos/{name}/readme", token, accept="application/vnd.github.raw")
                if not MARKERS.search(readme):
                    del found[name]
        except urllib.error.HTTPError:
            del found[name]

    if failed:
        print("queries that failed: " + "; ".join(failed), file=sys.stderr)
    if found:
        print(f"Tern-related repositories created in the last {args.days} days that aren't on the list:\n")
        for name, hit in sorted(found.items(), key=lambda kv: -kv[1]["repo"].get("stargazers_count", 0)):
            r = hit["repo"]
            desc = (r.get("description") or "").strip() or "no description"
            print(
                f"- [{name}]({r['html_url']}) ★{r.get('stargazers_count', '?')}: {desc}"
                f" _(matched: {', '.join(sorted(set(hit['queries'])))})_"
            )
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
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
