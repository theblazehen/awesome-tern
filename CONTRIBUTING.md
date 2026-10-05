# Contributing

Thanks for helping out. Only add things related to [Stencil's Tern](https://stencil.so/tern); other projects called "tern" don't belong here.

## The easy way

Open a [submission issue](https://github.com/theblazehen/awesome-tern/issues/new?template=submission.yml). A bot turns it into a pull request, and a maintainer checks the wording before merging.

## By hand

`README.md` is generated, so don't edit it. Each entry is a file in `data/entries/`:

```yaml
name: tern-jj
url: https://github.com/resYuto/tern-jj
section: plugins-lenses
description: Renders `jj status` as a read-only, color-coded card inside Tern.
```

- `section` is an id from `data/sections.yml`.
- `description` is one plain sentence that starts with a capital letter and ends with a period. Don't repeat the name.
- Social posts and videos go stale quickly, so they don't belong here.
- For links into a repository (a file in someone's dotfiles, say), add `repo: owner/name` so the entry gets stars and status.

Then run `mise run build` and commit the regenerated files with your entry. `mise run check` is what CI runs.

## What the automation does

- **CI** validates every entry and fails if `README.md` is out of date.
- **Refresh** runs nightly. It fetches stars, sorts sections by them, and marks entries `archived`, `inactive` (no push in six months) or `unavailable`.
- **Links** checks every link weekly and opens an issue when something breaks.
- **Discover** searches GitHub weekly for Tern projects created that week that aren't listed, and posts them to a review issue. Add the good ones; the rest drop out of later reports on their own.
