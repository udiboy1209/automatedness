# automatedness

My personal website and blog: an about page with selected publications, a projects list, and a blog.

It is a static site built with [Astro](https://astro.build/) 5 and styled with [Tailwind CSS](https://tailwindcss.com/) 4 (plus the typography plugin for Markdown content). All content is Markdown; there is no client-side framework.

## Getting started

Requires Node.js and npm.

```sh
npm install
npm run dev      # dev server with hot reload, http://localhost:4321
npm run build    # static build into dist/
npm run preview  # serve the built dist/ locally
```

## Layout

```
src/
  config.js            site name, nav links, social links
  content/
    config.js          content collection schemas
    main/              sections of the home page
    projects/          one file per project
    blog/              one file per blog post
  pages/
    index.astro        home page
    projects/          /projects/ list and /projects/<slug>/ pages
    blog/              /blog/ list and /blog/<slug>/ pages
  layouts/
    Layout.astro       base HTML shell
    List.astro         shared list page for projects and blog
  components/          Header, Footer, Sidebar
  styles/global.css    Tailwind import and theme additions
public/
  images/              images referenced from content
  pdfs/                CV, papers, reports
```

Files in `public/` are served from the site root, so `public/images/foo.png` is `/images/foo.png`.

## Pages

| Route | Source | What it shows |
| --- | --- | --- |
| `/` | `src/pages/index.astro` | Sidebar with photo, bio and links, then every `main` entry as a section, then featured projects |
| `/projects/` | `src/pages/projects/index.astro` | All projects, newest first |
| `/projects/<slug>/` | `src/pages/projects/[slug].astro` | One project; only generated for projects without a `link` |
| `/blog/` | `src/pages/blog/index.astro` | All posts, newest first |
| `/blog/<slug>/` | `src/pages/blog/[slug].astro` | One post |

The slug is the Markdown filename without `.md`.

## Editing content

### Home page sections

Each file in `src/content/main/` becomes a section on the home page, sorted by `order`. The filename is the section's anchor id, which is what the `/index.html#about` style nav links point to.

```yaml
---
title: About Me
order: 0
---
```

### Projects and blog posts

Add a Markdown file to `src/content/projects/` or `src/content/blog/`. Both use the same frontmatter:

| Field | Required | Effect |
| --- | --- | --- |
| `title` | yes | Heading on the list and detail pages |
| `date` | yes | Sort order and the date shown; write as `YYYY-MM-DD` |
| `summary` | no | Text under the title on the list page and in the home page's featured section |
| `image` | no | Thumbnail on the list page and in the featured section; a `/images/...` path or a full URL |
| `link` | no | The list entry links here instead of to a detail page |
| `featured` | no | `true` shows a project in "Featured Projects" on the home page |
| `tag`, `category` | no | Accepted by the schema but not displayed anywhere yet |

A featured project should set both `summary` and `image`, since the home page renders both.

A project with a `link` gets no detail page, so its Markdown body is never shown.

### Site-wide settings

- Site name, navigation links and social links: `src/config.js`. The header, sidebar and footer all read from it.
- Sidebar bio: the `bio` constant in `src/components/Sidebar.astro`.
- CV: replace `public/pdfs/MeetUdeshi_cv.pdf`; the nav link points to that path.
- Profile photo: `public/images/profile.jpg`, used by both the sidebar and the header.
- Favicon: `public/favicon.png`.

## Styling

Tailwind is loaded through its Vite plugin in `astro.config.mjs`, and utility classes are written directly in the `.astro` files. Rendered Markdown is styled with the typography plugin's `prose` classes.

`src/styles/global.css` defines one custom animation, `animate-flash`. The home page applies it to a section when the URL hash points to it, so clicking "About" or "Publications" briefly highlights the target.

## Deployment

The site is served by Firebase Hosting. The Firebase project lives outside this repository, in `../firebase-hosting/`, which holds `firebase.json`, `.firebaserc` and the `public/` folder that gets uploaded.

That `public/` folder is shared with a second site, the expense tracker under `public/moneyman/`. Copy the build over the top of it rather than replacing the folder, so `moneyman/` is left alone.

```sh
npm run build
cp -r dist/. ../firebase-hosting/public/
cd ../firebase-hosting
firebase deploy --only hosting
```

`firebase` is the [Firebase CLI](https://firebase.google.com/docs/cli) (`npm install -g firebase-tools`); run `firebase login` first if the session has expired.

Because the copy only adds and overwrites, a page or asset deleted from this repo stays in `../firebase-hosting/public/` until it is removed there by hand.
