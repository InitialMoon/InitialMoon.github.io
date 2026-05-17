# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

This is currently an Academic Pages / Jekyll GitHub Pages site.

- Install Ruby dependencies: `bundle install`
- Serve locally with live reload: `bundle exec jekyll serve -l -H localhost`
- Build the static site: `bundle exec jekyll build`
- Build with GitHub Pages compatibility: `bundle exec jekyll build --safe`
- Install JavaScript dependencies if editing bundled theme JS: `npm install`
- Rebuild minified theme JavaScript: `npm run build:js`
- Watch theme JavaScript while editing: `npm run watch:js`

The generated site goes to `_site/`, which is ignored. `Gemfile.lock`, `node_modules/`, and `package-lock.json` are also ignored in this repository.

## Current architecture

The repository is a detached Academic Pages template built on Jekyll and Minimal Mistakes-style layouts.

- `_config.yml` controls site metadata, author sidebar links, collections, defaults, Sass, and plugin configuration. Restart the Jekyll server after changing it.
- `_pages/` contains standalone pages. The homepage is `_pages/about.md` with `permalink: /`; CV is `_pages/cv.md`; publications index is `_pages/publications.md`.
- `_data/navigation.yml` controls top-level navigation. At present only Publications and CV are enabled.
- `_publications/`, `_portfolio/`, `_talks/`, `_teaching/`, and `_posts/` are Jekyll collections/content directories. Only `_publications/2024-10-28-ANFluid.md` appears to be real user content; many other collection entries are template examples.
- `_layouts/` and `_includes/` define the theme structure. Most pages use `layout: single` or `layout: archive`; author/sidebar rendering goes through `_includes/author-profile.html`.
- `_sass/` contains theme styling partials; `assets/` and `images/` contain JavaScript, CSS assets, profile images, favicons, and many template example images.
- `files/` stores downloadable public assets such as `ANFluid.pdf`.
- `markdown_generator/` and `talkmap.*` are Academic Pages helper scripts/notebooks for generating publications/talks and maps.

## Project direction

Before redesign or migration work, read `docs/superpowers/plans/2026-05-17-personal-homepage-redesign.md`. It captures the user-approved positioning, template shortlist, content weighting, current audit, and execution plan from the planning conversation.

The site is being reconsidered rather than merely cleaned up. The desired positioning is a personal homepage centered on research + engineering, with systems research as the current main line, graphics/AI as important prior expertise, and portfolio-style project presentation/contactability as supporting signals. Do not frame the site as seeking internships, even when making projects and contact routes prominent.

The current Academic Pages look is considered too official and stiff. Future work may migrate to another theme such as HugoBlox Academic CV or a minimalist Hugo academic site instead of continuing to heavily customize this template.

## Content notes

Known current cleanup targets:

- README is still the upstream Academic Pages template README.
- `_config.yml` still has placeholder metadata such as `description: personal description` and a likely incorrect `twitter: UniofOxford`.
- Several pages and collections are template leftovers, including example posts, talks, teaching entries, markdown guide pages, terms page, and portfolio examples.
- CV currently contains only education and generated publications, with commented Academic Pages examples.
- Publications contain ANFluid, but the body still includes template explanatory text.
