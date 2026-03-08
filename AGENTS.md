# amorphous-industries.github.io

Static GitHub Pages site for Amorphous Industries, served at [amorphous-industries.com](https://amorphous-industries.com). Pages are generated from Jinja2 templates and committed to the repo — GitHub Pages serves them directly from `main`.

## Project Structure

```
Makefile                    # Build automation (runs generate.py)
generate.py                 # Jinja2 rendering script
requirements-dev.txt        # Dev dependencies (jinja2)
CNAME                       # Custom domain: amorphous-industries.com
cover.css                   # Custom styles (dark theme, branded background)
logo_no_text.png            # Background image used in cover.css radial-gradient
slack_logo.svg              # Footer Slack link icon
mail_icon.svg               # Footer email link icon
templates/
  main.html                 # Base template (header, nav, footer)
  index.html                # Home page template
  about.html                # About page template
assets/dist/                # Bootstrap 4.5 CSS and JS (vendored, do not edit)
index.html                  # GENERATED — do not edit directly
about.html                  # GENERATED — do not edit directly
```

## Key Concepts

- **Edit templates, not output files.** `index.html` and `about.html` in the root are generated outputs. All content changes go in `templates/`.
- **Base template** (`templates/main.html`) defines the shared layout: `{% block navbar %}` and `{% block main %}` are overridden by page templates.
- **Build** is a single Python script (`generate.py`) that renders each page template and writes it to the root.
- **Deployment** is automatic: push to `main` and GitHub Pages serves the updated site within seconds.
- **Custom domain** is set via the `CNAME` file (`amorphous-industries.com`), configured in Route53 via the `ai-infra` repo.

## Build

```bash
# Install dev dependencies (one-time)
pip install -r requirements-dev.txt

# Regenerate index.html and about.html from templates
make
# or equivalently:
./generate.py

# Remove all untracked/generated files (nuclear clean)
make clean
```

## Development Workflow

1. **Edit templates** in `templates/` — never edit root `index.html` or `about.html` directly.

2. **Regenerate output files:**
   ```bash
   make
   ```

3. **Verify locally** by opening the rendered HTML files in a browser:
   ```bash
   open index.html
   open about.html
   ```

4. **Commit both templates and generated output** — GitHub Pages needs the rendered HTML in the repo:
   ```bash
   git add templates/ index.html about.html
   git commit -m "<description>"
   ```

5. **Push to main** to deploy:
   ```bash
   git push origin main
   ```

## Current State Warning

As of the last commit, `index.html` and `about.html` in the root are **out of sync** with `templates/index.html` and `templates/about.html`. The rendered files were hand-edited after the last `make` run. Before making any content changes, reconcile the templates with the current rendered output, then use `make` going forward.
