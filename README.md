# amorphous-industries.github.io

Source for [amorphous-industries.com](https://amorphous-industries.com) — the Amorphous Industries company website, hosted on GitHub Pages.

## Stack

- [Astro](https://astro.build/) — static site generator
- [Tailwind CSS](https://tailwindcss.com/) — utility-first CSS
- [GitHub Actions](https://github.com/features/actions) — automated build and deployment

## Project layout

```
src/
  layouts/BaseLayout.astro  # Shared layout (header, nav, footer)
  pages/index.astro         # Home page
  pages/about.astro         # About page
  styles/global.css         # Tailwind + custom gradient
public/                     # Static assets (logo, icons, CNAME)
```

## Working on the site

Requires Node.js 20+.

```bash
npm install          # install dependencies
npm run dev          # dev server at http://localhost:4321
npm run build        # production build → dist/
npm run preview      # preview production build
```

Changes to `main` require a pull request:

```bash
git checkout -b <branch-name>
# edit src/, then:
git add src/ public/
git commit -m "<description>"
git push -u origin <branch-name>
gh pr create --title "<title>" --body "<description>"
gh pr merge --merge
```

GitHub Actions builds and deploys automatically when PRs merge to `main`. No rendered HTML is committed to the repo.
