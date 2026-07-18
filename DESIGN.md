# Neutriverse Prospero Light

## 1. Visual Theme

Neutriverse has two states of one facility. Night mode is the existing deep-space observation console. Light mode is a modern arcane archive: sandstone paper, lapis instruments, old gold rules, and rare turquoise signals. It is scholarly and operational, never theatrical or promotional.

## 2. Color Roles

- Canvas: `#EEE5CE`
- Primary paper: `#F8F1DD`
- Secondary surface: `#E4D7B8`
- Lapis sidebar: `#124D68` to `#0C354D`
- Standard rule: `#C5AD70`
- Active gold: `#AD7D29`
- Ink: `#2C3436`
- Muted ink: `#6C7575`
- Accessible small-text ink: `#536060`
- Accessible text gold: `#78551D` on paper, `#D1B975` on lapis
- Heading: `#17445A`
- Link: `#086D80`
- Signal cyan: `#197F93`
- Anomaly purple: `#744B87`, limited to exceptional states

The base muted and gold values remain decorative tokens; small rendered text uses the darker contrast-safe derivatives. Gold is never body text. Cyan marks interaction and status. Purple remains below roughly 2% of a page.

## 3. Typography

- Chinese article text: `Noto Serif SC` 400, 17px, line-height 1.9.
- Chinese headings: `Noto Serif SC` 600.
- UI and navigation: `Noto Sans SC` 400/500/600.
- English inscriptions: `Cinzel` 500/600, uppercase, 0.10em to 0.14em tracking.
- Dates, status, code, versions: `IBM Plex Mono` 400/500 with tabular numerals.
- Night typography remains unchanged.

## 4. Components

Cards are paper records with 1px gold rules, 4px to 8px radii, and almost imperceptible blue-gray shadows. Buttons are compact controls, not calls to action. Focus uses a 2px turquoise outline plus offset. Tags and status colors occupy only dots, short rules, or small labels.

## 5. Layout

Keep Chirpy's current information architecture, sidebar dimensions, content widths, pagination, and panels. Use an 8px spacing rhythm. Article reading width stays near 700px to 740px. Mobile layouts collapse without horizontal page overflow.

## 6. Depth

Depth comes primarily from surface layering: sandstone canvas, ivory paper, then secondary archive drawers. Shadows use several low-opacity blue-gray layers and are reserved for actual raised or floating elements. The featured image remains dark as the light theme's anchor.

## 7. Do / Do Not

- Do preserve the current night mode and all content logic.
- Do use gold for rules, numbering, and active markers.
- Do keep decorative geometry subordinate to reading.
- Do not use official franchise symbols, names, characters, or copied motifs.
- Do not use pure white, bright yellow gold, neon glow, heavy texture, or persistent particles.
- Do not add `transition: all` or decorative motion that competes with text.

## 8. Responsive

Validate at 1366px, 1024px, 768px, and 390px. Keep desktop sidebar collapse behavior. On small screens, controls may wrap or scroll internally, tables remain horizontally scrollable, and PTM stays within the visual viewport.

## 9. Motion

Theme color, background, border, shadow, and opacity transitions use 180ms to 250ms. Hover movement is at most 1px and only on fine pointers. The optional logo astrolabe ring rotates extremely slowly. `prefers-reduced-motion: reduce` removes decorative rotation and movement.

## 10. Ravenis Public Intelligence

Ravenis is a quiet, unlisted reading room inside Neutriverse rather than a second product shell. It inherits Chirpy's sidebar, top bar, breadcrumb, footer, typography, and saved day/night preference. Its visual adventure is 3/10, motion 2/10, and information density 6/10.

- The first viewport answers three questions in order: what changed, what matters, and what to verify next.
- Search controls are an archive instrument panel, not a dashboard. The keyword field is primary; secondary filters wrap on an 8px rhythm and never overflow the viewport.
- A persistent day/slot rail sits directly below the hero: previous day, actual manifest date, next day, then A 06:00 / Digest 10:00 / B 14:05 / C 17:10. Missing runs are absent or disabled; migration-only days are called `全天归档`.
- Search scope is explicit and quiet: `新闻` is the default, while AI Digest and valid multi-source clusters require an intentional scope change. Search results always report the true match count before the 200-item display cap.
- Night mode uses the existing deep-space console surfaces. Light mode uses sandstone paper, lapis structure, old-gold rules, and turquoise interaction states.
- Top signals use a numbered left rule, evidence chips, and compact `发生 / 影响 / 观察` labels. Full records use restrained archive rows with disclosure for records without a safe external URL.
- Five deliberate craft details are required: a mono date ledger, three-step signal grammar, evidence-count chips, category tally rules, and a small LKG/data-freshness seal.
- The page is public but deliberately quiet: no tab entry, no sitemap entry, `noindex,nofollow`, and no analytics-specific promotion.
- The browser loads only the manifest and selected day at first. The 30-day search index is lazy-loaded after a search or historical filter is requested.
- All interactive controls retain visible labels, 2px turquoise focus outlines, 44px mobile targets where practical, and reduced-motion behavior.
- Concrete reference DNA stays subordinate to Neutriverse: Notion contributes 1px whisper-weight divisions; Linear contributes the 8px spacing rhythm, 6px control / 8px panel radius split, and 160-180ms functional state transitions. Existing Ravenis colors and typography remain authoritative.
