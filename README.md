# amorphous-industries.github.io

Source for [amorphous-industries.com](https://amorphous-industries.com) — the Amorphous Industries company website, hosted on GitHub Pages.

## How it works

Pages are written as [Jinja2](https://jinja.palletsprojects.com/) templates in `templates/`, rendered to plain HTML by `generate.py`, and committed to the repo. GitHub Pages serves the rendered HTML directly from `main`.

```
templates/main.html     # Shared layout (header, nav, footer)
templates/index.html    # Home page
templates/about.html    # About page
generate.py             # Renders templates → index.html, about.html
cover.css               # Custom styles
assets/                 # Vendored Bootstrap 4.5
```

## Working on the site

Install dependencies (one-time):

```bash
pip install -r requirements-dev.txt
```

Edit the templates in `templates/`, then regenerate:

```bash
make
```

Preview by opening the rendered files in a browser, then commit and push to `main`:

```bash
git add templates/ index.html about.html
git commit -m "<description>"
git push origin main
```

GitHub Pages deploys automatically on push. **Do not edit `index.html` or `about.html` directly** — they are generated outputs and will be overwritten by the next `make` run.
