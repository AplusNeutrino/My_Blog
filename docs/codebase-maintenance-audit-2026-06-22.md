# Codebase Maintenance Audit - 2026-06-22

Scope: Jekyll/Chirpy site repository for neutriverse.uk.

## Active runtime paths

- `_includes/metadata-hook.html` is the active Chirpy head hook.
- `_includes/metadata-hook.html` loads `assets/css/ChirpyDefault.css` with a build/version query string.
- `assets/css/ChirpyDefault.css` is the active custom stylesheet.
- `_layouts/default.html` loads the sidebar, topbar, right panel, footer, Neutriverse labels, and Probe Tracking Module.
- `_layouts/home.html` reads `_data/home_recommend.yml` and `_data/home_popular.yml`.
- `_layouts/post.html` loads `_includes/post-panel-stack.html`, `_includes/post-like.html`, sharing, comments, and read time.
- `_includes/trending-tags.html` reads `_data/middle_memory.yml` for the right-panel memory fragment module.
- `_hidden_pages/` remains an intentional hidden utility collection for Probe Tracking Module indexing unless `probe: false` is set.

## Archived after audit

These files had no active runtime include/link path and were moved out of live asset/include locations:

- `docs/archive/legacy-css/neutriverse.css`
  - Former high-saturation/light-mode experiment and old custom palette.
  - Do not treat as live site color evidence.
- `docs/archive/legacy-css/TSNight.css`
  - Retired night-mode experiment.
- `docs/archive/legacy-css/ExTSNight.css`
  - Retired outline-first night-mode experiment.
- `docs/archive/legacy-includes/head/custom-head.html`
  - Retired head hook candidate. Chirpy 7.5 currently calls `_includes/metadata-hook.html`, not this file.
- `docs/archive/legacy-includes/update-list.html`
  - Retired right-panel recent-update list. Current right panel uses `_includes/trending-tags.html` plus post panel includes.

## Left active intentionally

- _includes/favicons.html: active theme override for favicons.
- ssets/img/favicons/neutriverse.webmanifest: custom web app manifest. The filename avoids colliding with Chirpy's built-in ssets/img/favicons/site.webmanifest output.
- `_includes/inline-image.html`: active article authoring helper; currently used by draft/untracked content too.
- `_data/contact.yml` and `_data/share.yml`: consumed by Chirpy theme internals, even if local templates do not mention them directly.
- `_layouts/category.html` and `_layouts/categories.html`: category pages remain accessible even though sidebar navigation hides them.
- `_tabs/archives.md`, `_tabs/categories.md`, `_tabs/tags.md`, `_tabs/thoughts.md`: hidden from primary nav by CSS, but still intentional URL surfaces.
- `occult-atlas-app/`: used by `_hidden_pages/occult-atlas.md` through `_layouts/occult-atlas.html`.

## Deferred cleanup candidates

- `assets/css/ChirpyDefault.css` is large and mixes multiple modules. Split only when there is time to verify final load order across home, post, About, Probe, links, and occult atlas pages.
- `_layouts/home.html` repeats image URL normalization logic for front matter images, markdown images, and HTML images. This can be extracted later, but Liquid include refactors should be tested with representative posts.
- Documentation still contains historical sections. Keep them, but prefer pointing to archived paths when they describe non-runtime files.