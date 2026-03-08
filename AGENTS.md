# amorphous-industries.github.io

Static website for Amorphous Industries, served at [amorphous-industries.com](https://amorphous-industries.com). Built with [Astro](https://astro.build/) and [Tailwind CSS](https://tailwindcss.com/), deployed to GitHub Pages via GitHub Actions.

## Project Structure

```
src/
  layouts/
    BaseLayout.astro        # Shared layout (header, nav, footer)
  pages/
    index.astro             # Home page
    about.astro             # About page
  styles/
    global.css              # Tailwind directives + custom gradient class
public/
  CNAME                     # Custom domain: amorphous-industries.com
  logo_no_text.png          # Background image (radial gradient overlay)
  slack_logo.svg            # Footer Slack link icon
  mail_icon.svg             # Footer email link icon
.github/
  workflows/
    deploy.yml              # Build + deploy to GitHub Pages on push to main
astro.config.mjs            # Astro config (Tailwind integration, site URL)
tailwind.config.mjs         # Tailwind config (content paths)
package.json                # Dependencies and scripts
```

## Key Concepts

- **Astro pages** (`.astro` files in `src/pages/`) map directly to routes: `index.astro` → `/`, `about.astro` → `/about/`.
- **BaseLayout** defines the shared structure (dark background, nav, footer). Pages fill the `<slot />` with their content.
- **Tailwind CSS** provides all styling via utility classes. The one custom class (`bg-cover-gradient` in `global.css`) handles the radial gradient + logo background that can't be expressed as utilities.
- **No rendered HTML is committed.** `dist/` is gitignored. GitHub Actions builds the site and deploys it.
- **Custom domain** is set via `public/CNAME` (Astro copies it to `dist/` on build). DNS is configured in Route53 via the `ai-infra` repo.

## Build

Requires Node.js 20+.

```bash
# Install dependencies (one-time)
npm install

# Dev server with hot reload (http://localhost:4321)
npm run dev

# Production build (outputs to dist/)
npm run build

# Preview production build locally
npm run preview
```

## Development Workflow

All changes to `main` must go through a pull request — direct pushes are blocked by branch protection.

1. **Create a feature branch** from `main`:
   ```bash
   git checkout main && git pull
   git checkout -b <branch-name>
   ```

2. **Edit `.astro` files** in `src/` — pages in `src/pages/`, layout in `src/layouts/`, styles in `src/styles/`.

3. **Preview with the dev server:**
   ```bash
   npm run dev
   ```

4. **Commit your changes:**
   ```bash
   git add src/ public/
   git commit -m "<description>"
   ```

5. **Push and open a PR:**
   ```bash
   git push -u origin <branch-name>
   gh pr create --title "<title>" --body "<description>"
   ```

6. **Merge when ready:**
   ```bash
   gh pr merge --merge
   ```

7. **Clean up:**
   ```bash
   git checkout main && git pull
   git branch -d <branch-name>
   ```

GitHub Actions builds and deploys automatically when PRs merge to `main`.
