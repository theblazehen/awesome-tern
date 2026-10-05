# Contributing

Thanks for helping out. Only add things related to [Stencil's Tern](https://stencil.so/tern); other projects called "tern" don't belong here.

## Adding an entry

Edit `list.yml` and open a pull request. Don't edit `README.md`; it's regenerated from `list.yml` after your PR is merged.

Add the entry under the section where it fits:

```yaml
    - name: tern-jj
      url: https://github.com/resYuto/tern-jj
      description: Renders `jj status` as a read-only, color-coded card inside Tern.
```

- `description` is one plain sentence that starts with a capital letter and ends with a period. Don't repeat the name.
- Most sections are sorted by GitHub stars, so the position you pick doesn't matter there. Sections marked `sort: manual` keep the order in the file.
- If the link points into a repository (a file in someone's dotfiles, say), add `repo: owner/name` so the entry gets stars and status.
- Social posts and videos go stale quickly, so they don't belong here.

CI checks the format of `list.yml` on every pull request. To check locally, run `mise run check`.

## What the automation does

- **CI** validates `list.yml` on pull requests and regenerates `README.md` when changes land on `main`.
- **Refresh** runs nightly. It fetches stars, re-sorts sections, and marks entries `archived`, `inactive` (no push in six months) or `unavailable`.
- **Links** checks every link weekly and opens an issue when something breaks.
- **Discover** searches GitHub weekly for Tern projects created that week that aren't listed, and posts them to a review issue.
