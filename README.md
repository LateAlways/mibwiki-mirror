# Unofficial mirror of mibwiki.one

This repository is a read-only backup of the user-written documentation
from [https://mibwiki.one](https://mibwiki.one), preserved for educational and archival purposes
due to frequent downtime of the original site.

I am **NOT** the author of the original content

## Development

The site is built with [Docusaurus](https://docusaurus.io/) from the Markdown files in `docs/`.

```
npm install
npm start      # local dev server with live reload
npm run build  # production build into build/
```

Pushes to `main` build and publish the site automatically via GitHub Actions
(`.github/workflows/deploy.yml`) to the `gh-pages` branch.

`main.py` is a separate, unrelated tool that scrapes the source wiki
(mibwiki.one) into `docs/`; it requires a local `config.py` with API
credentials and is not part of the site build.
