# Mearra PPTX — Asset Catalog & Extension Guide

This skill ships with a curated asset library extracted from the official Mearra brand template and brand identity materials. Use the assets via `deck.add_image()`, `deck.add_logo()`, `deck.add_icon()`, `deck.add_aquatic_form()` in `scripts/mearra_deck.py`.

Everything here is **on-brand by construction** — if you stay inside this library, you can't go wrong.

```
assets/
├── template.pptx           # THE template — always start here
├── logos/                  # 3 logo variants
├── aquatic-forms/          # 5 brand illustrations (soft rounded blobs + orb)
├── icons/                  # 47 named line icons
├── backgrounds/            # 5 atmospheric photos
├── portraits/              # 2 people photos (team / collage use)
├── mockups/                # 2 device mockups (laptop, phone-in-hand)
├── graphics/               # 2 decorative graphics (map, data donut)
├── misc/                   # 1 client logo (Luke)
├── layout-previews/        # PNGs of every example slide for picking a layout
└── fonts/                  # (reserved — Sofia Sans is from Google Fonts)
```

---

## 1. Template — `assets/template.pptx`

The single source of truth. Contains:

- **Slide master `simple-light-2`** with the Mearra color system, font definitions, logo chrome, and tagline baked in.
- **35 named slide layouts** (see `references/layout-catalog.md`).
- **47 example slides** that the builder strips on initialization. They stay in `layout-previews/` as PNGs so you can decide which layout matches your slide's job.

**Never modify `template.pptx` in place.** If you need a modified template (e.g., swapped brand colour for a subsidiary variant), save it under a new name and update `MearraDeck._template_path`.

---

## 2. Logos — `assets/logos/`

| File | When to use |
|---|---|
| `mearra-symbol-dark.png` | Symbol on light backgrounds (Mist, White, Blossom). Default for content slides (bottom-right). |
| `mearra-symbol-light.png` | Symbol on dark backgrounds (Indigo, Trench, dark photography). |
| `mearra-wordmark-light.png` | Full wordmark on dark backgrounds. Used on cover/closing slides. |

**Usage.**

```python
deck.add_logo(slide, variant="symbol-dark")     # content slide, light bg
deck.add_logo(slide, variant="symbol-light")    # dark section header
deck.add_logo(slide, variant="wordmark-light")  # cover or closing slide on dark bg
```

**Rules** (from `references/brand-bible.md §3`).

- Clearspace equal to the symbol's "leg" on all sides.
- Never recolor, rotate, or effect the logo.
- Never use the wordmark without the symbol nearby.
- Minimum size: 25 mm / 100 px primary; 8 mm / 25 px symbol.

---

## 3. Aquatic Forms — `assets/aquatic-forms/`

Mearra's signature illustration system — soft, water-inspired, gradient-mapped blobs and clusters. Use them to add visual personality and soften layouts.

### Current catalog (5 genuine forms)

| File | Feel | Best on |
|---|---|---|
| `aquatic-cluster-tall-01.png` | Multi-color cluster — Indigo / Coral / Current / Blossom | Right- or left-bleed on content slides (`accent="auto"` default). Warm and energetic. |
| `aquatic-cluster-tall-02.png` | Cool cluster — Trench / Lagoon / Current / green accent | Technical / data slides, cool emotional register. |
| `aquatic-cluster-tall-03.png` | Warm cluster — Blossom / Coral / Current / Lagoon | Client-empathy moments, team slides, pitch openings. |
| `aquatic-cluster-tall-04.png` | Similar to -02 with slightly different composition | Alternative to -02 for variety in long decks. |
| `aquatic-cluster-full-02.png` | Single soft orb — Indigo → Coral → White radial gradient | Quote slides, statement slides, bottom-right anchors. |

These are the only five shapes in this folder. Any other file that was previously here has been moved to a more appropriate sibling folder (see below) because it was not a true aquatic form.

### Usage

Most of the time you don't need to place these by hand — every content-slide method
(`add_title_body`, `add_title_only`, `add_big_number`, `add_quote`, etc.) accepts
an `accent` parameter that picks an appropriate form for its composition:

```python
# Default "auto" picks the right form for the slide style:
deck.add_title_body(title=..., body=..., accent="auto")

# Force a specific form (fuzzy match on the name):
deck.add_title_body(title=..., body=..., accent="cluster-tall-03")

# No accent — clean whitespace:
deck.add_title_body(title=..., body=..., accent=None)
```

For custom slides, place forms manually:

```python
deck.add_aquatic_form(
    slide,
    name="cluster-tall-01",
    left=7.6, top=-0.2,          # inches — negative values bleed off the slide
    width=2.8, height=5.9,
)
```

### Rules

- **Crop tight, let them bleed.** Aquatic Forms are designed to extend beyond the frame — at least one edge should bleed off the slide.
- **Don't stack incompatible forms.** One form per slide, usually. Two only if they're compositionally balanced.
- **Keep grain consistent.** The shipped PNGs already carry the correct 5–25% grain texture. Don't re-compress or re-render.
- **Don't recolor.** If you need a different color treatment, add a new file (see "Adding new assets" below) rather than applying filters in pptx.

---

## 4. Icons — `assets/icons/`

47 line icons in Mearra's soft rounded style, all consistently sized and stroked.

### Current catalog

**Tech & craft:** `ai`, `robot`, `code`, `programming-browser`, `database`, `cloud`, `module`, `computer-bug`, `continuous-development`, `drupal`, `react`, `wordpress`

**UX & design:** `accessibility`, `design`, `image`, `mobile`, `laptop`, `navigation-menu`, `pencil`, `search`

**Data & analytics:** `analytics-graph`, `chart`, `data-security`, `gdpr`, `text-file`, `euro`

**People:** `client`, `end-user`, `man`, `team`, `team-2`, `group`, `collaboration`, `smiley`, `thumb-up`

**System & flow:** `arrow-up`, `arrow-down`, `hierarchy`, `recycle`, `download`, `export`, `delete`, `close`

**Concept markers:** `audit`, `diamond`, `earth`, `question`, `star`

### Usage

```python
deck.add_icon(slide, name="ai", left_in=1.0, top_in=3.0, size_in=1.0)
deck.add_icon(slide, name="collaboration", left_in=5.0, top_in=3.0, size_in=1.0)
```

The builder does fuzzy matching on names, so `"ai"`, `"AI"`, `"icon-ai"`, and `"icon-ai.png"` all resolve to the same icon.

### Rules

- **One icon per concept.** Don't stack 4 icons on a slide — it's decoration, not information.
- **Consistent sizes.** Pick one icon size per slide (0.8 in for small, 1.2 in for medium, 2.0 in for hero).
- **Don't recolor.** Icons are pre-rendered. If you need a different color treatment, add a new file.

---

## 5. Backgrounds — `assets/backgrounds/`

5 atmospheric photos for use as full-bleed heroes or softened overlays.

| File | Mood |
|---|---|
| `photo-atmospheric-02.jpg` | Blue/teal atmospheric light |
| `photo-atmospheric-03.jpg` | Moody, warm-dark |
| `photo-atmospheric-04.jpg` | Cool tonal, depth |
| `photo-atmospheric-orange.jpg` | Warm orange/coral atmospheric |
| `photo-person-01.png` | Person-focused, human element |

### Usage

```python
deck.add_image(
    slide,
    path="assets/backgrounds/photo-atmospheric-orange.jpg",
    full_bleed=True,               # fills entire slide
    overlay_color="TRENCH",        # optional darkening overlay for text contrast
    overlay_opacity=0.4,
)
```

### Rules

- **Tight crops only** (per `brand-bible.md §7`).
- **Always put text on a readable area** — use overlay or constrain text to a dark part of the image.
- **Dynamic feel.** Avoid static, stock-looking photos. These 5 all have movement built in.

---

## 6. Layout previews — `assets/layout-previews/`

47 PNGs rendered from the template's original example deck. Filenames follow `slide-NN__LAYOUT_NAME.png`.

These aren't used at runtime — they exist so you (or whoever's using this skill) can visually pick the right layout before building. See `references/layout-catalog.md` for the full index.

---

## 7. Fonts — `assets/fonts/`

Reserved. Sofia Sans and Sofia Sans Extra Condensed are Google Fonts. The template references them by name; end users see them if Sofia Sans is installed locally or if the deck is viewed in Google Slides / Keynote with font substitution that honours the Google Fonts fallback. For print-fidelity export to PDF, install Sofia Sans from https://fonts.google.com/specimen/Sofia+Sans on the rendering machine.

If you need to ship embedded fonts in the .pptx, drop the `.ttf` files here and extend `MearraDeck` to embed them — but note that PowerPoint's font embedding is lossy and sometimes unreliable.

---

## 8. Adding new assets (extension guide)

The asset library is **designed to grow over time**. When Mearra commissions a new illustration, ships a new icon, or adds a photo to the brand library, it should be trivial to drop the file in here and have the skill use it.

### Adding an icon

1. Place the PNG in `assets/icons/`. File name: `icon-<kebab-case-name>.png`. Follow existing size / stroke / color conventions.
2. (Optional) Add a one-line entry in the "Current catalog" table above.
3. That's it — `deck.add_icon(slide, name="<kebab-case-name>")` will find it via fuzzy match.

### Adding an aquatic form

1. Place the PNG in `assets/aquatic-forms/`. File name: `aquatic-<descriptor>.png` (e.g., `aquatic-blob-coral-wave.png`).
2. Add an entry in the catalog table above so future Claude invocations know when to use it.
3. Call via `deck.add_aquatic_form(slide, name="blob-coral-wave")`.

### Adding a background photo

1. Place the image in `assets/backgrounds/`. Prefer `.jpg` for photos, `.png` for graphics with transparency.
2. File name: `photo-<descriptor>.<ext>`.
3. Update the backgrounds table above.

### Adding a logo variant

1. Place in `assets/logos/`. File name: `mearra-<variant>.<ext>`.
2. Extend `MearraDeck.add_logo()` with the new variant key if you want it addressable by a short alias.

### Naming conventions (summary)

| Asset type | Pattern | Example |
|---|---|---|
| Icon | `icon-<name>.png` | `icon-cloud.png` |
| Aquatic form | `aquatic-<descriptor>.png` | `aquatic-blob-dark-01.png` |
| Background photo | `photo-<descriptor>.<ext>` | `photo-atmospheric-orange.jpg` |
| Logo | `mearra-<variant>.<ext>` | `mearra-symbol-dark.png` |
| Layout preview | `slide-NN__LAYOUT_NAME.png` | `slide-14__TITLE_AND_TWO_COLUMNS_1_1_1.png` |

Lowercase everywhere. Kebab-case for multi-word names. Two-digit zero-padded numbers for variants.

---

## 9. When an asset is missing

If the user asks for a specific icon / illustration / photo that isn't in the library:

1. **Tell them** what's needed and what's close ("I don't have a `stopwatch` icon. Closest matches: `continuous-development`, `recycle`.").
2. **Offer alternatives**:
   - Use the closest match.
   - Use no icon (whitespace is a Mearra value).
   - Ask them to drop the file in `assets/icons/` and proceed.
3. **Never invent** an icon by drawing one with pptx shapes — you'll produce something off-brand.
4. **Never introduce a non-brand asset** (public clipart, icon CDN, etc.).

---

## 10. Portraits — `assets/portraits/`

People photos extracted from the brand template. Use for team slides, client case
studies, or as collage elements on hero slides.

| File | Description |
|---|---|
| `person-warm-portrait.png` | Warm-toned portrait (coral/pink wash) of a bearded man — double-exposure effect. Use on hero slides or team sections. |
| `person-orange-sweater.png` | Cut-out headshot, orange sweater, neutral background — works well as a repeatable team grid element. |

```python
deck.add_portrait(slide, name="warm-portrait", left=6.5, top=0.8, width=3.0)
```

## 11. Mockups — `assets/mockups/`

Device mockups for product/concept slides.

| File | Description |
|---|---|
| `laptop-open.png` | Open silver laptop with blank white screen — drop your product screenshot on top. |
| `phone-in-hand.png` | Phone held in hand with blank screen — same idea for mobile. |

```python
deck.add_mockup(slide, name="laptop", left=3.0, top=1.2, width=5.5)
```

## 12. Graphics — `assets/graphics/`

Decorative graphics that aren't Aquatic Forms but are extracted from the brand template.

| File | Description |
|---|---|
| `map-europe-finland-highlight.png` | Map of Europe with Finland + Baltics highlighted in Indigo. Use on geography / "where we operate" slides. |
| `data-donut-colorful.png` | Indigo-gradient donut chart decoration. Use as a soft visual anchor on data slides (it's decorative, not a real chart). |

```python
deck.add_graphic(slide, name="map", left=5.5, top=0.5, width=4.0)
```

## 13. Misc — `assets/misc/`

| File | Description |
|---|---|
| `client-logo-luke.png` | Luke (Luonnonvarakeskus) client logo — example of a client logo at the right size/contrast for Mearra decks. Use as a reference when placing your own client logos. |

## 14. Asset inventory snapshot

_As of 20 April 2026:_

- 1 template (`template.pptx`)
- 3 logos
- 5 aquatic forms (genuine brand illustrations)
- 47 named icons
- 5 atmospheric backgrounds
- 2 portraits, 2 mockups, 2 graphics, 1 client-logo example
- 47 layout preview PNGs
- 0 embedded fonts (Sofia Sans via Google Fonts)

Run this to re-inventory programmatically:

```bash
find assets -type f -not -name "*.md" | sort | wc -l
```
