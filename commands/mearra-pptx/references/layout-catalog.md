# Mearra Template — Layout Catalog

The Mearra template ships **35 named layouts** on a single master (`simple-light-2`). Every layout carries brand colours, fonts, logo, and tagline from the master — use one of these rather than drawing shapes from scratch.

This catalog maps each layout to:
- **Purpose** — what kind of slide it's for.
- **Preview** — the PNG rendered from the example deck (in `../assets/layout-previews/`).
- **Placeholders** — the `idx` values you can fill via `deck.add_custom_slide(layout_name, placeholders={idx: "text"})`.
- **Builder method** — the high-level `MearraDeck` method that wraps this layout, when one exists.

When in doubt, open the preview PNG before picking. The file names follow `slide-NN__LAYOUT_NAME.png`.

---

## 1. Cover & closing layouts

### `TITLE` (layout 00)
**Purpose.** Primary cover slide — the first slide of any deck. Big headline, subtitle line, Mearra brand presence.
**Preview.** `slide-01__TITLE.png`
**Placeholders.** `idx=0` title, `idx=1` subtitle, `idx=2` second subtitle (e.g., presenter line).
**Builder.** `deck.add_cover(title, subtitle, presenter_line, variant="indigo"|"light")`.

### `TITLE_1` (layout 34)
**Purpose.** Alternate cover / thank-you slide. Works great as the closing slide.
**Preview.** `slide-44__TITLE_1.png`
**Placeholders.** `idx=0` title, `idx=1` subtitle.
**Builder.** `deck.add_thank_you(subtitle="mearra.com")`.

---

## 2. Section headers

### `SECTION_HEADER` (layout 01)
**Purpose.** Major section divider between parts of a deck (e.g., "Agenda," "Case study," "Next steps").
**Preview.** `slide-02__SECTION_HEADER.png`, `slide-05__SECTION_HEADER.png`, `slide-45__SECTION_HEADER.png`.
**Placeholders.** `idx=0` title, `idx=1` eyebrow / subtitle.
**Builder.** `deck.add_section_header(title, eyebrow=None)`.

### `SECTION_HEADER_1_3_4_1_1_1` (layout 26)
**Purpose.** Rich section header with a decorative shape grid — use as a statement divider when you want more visual weight.
**Preview.** `slide-36__SECTION_HEADER_1_3_4_1_1_1.png`.
**Placeholders.** 21 — this layout is a heavily composed decorative divider. Use `deck.add_custom_slide("SECTION_HEADER_1_3_4_1_1_1")` if you need it; otherwise prefer `SECTION_HEADER`.

---

## 3. Title + body (single concept)

### `TITLE_AND_BODY` (layout 03)
**Purpose.** Classic single-concept slide — title, optional eyebrow/kicker, one body paragraph.
**Preview.** `slide-04__TITLE_AND_BODY.png`.
**Placeholders.** `idx=0` title, `idx=1` body, `idx=2` eyebrow.
**Builder.** `deck.add_title_body(title, body, eyebrow=None)`.

### `TITLE_AND_BODY_2` (layout 04)
**Purpose.** Title + subtitle + body — three levels of hierarchy on one slide for a concept that needs both a headline and a sub-claim.
**Preview.** `slide-06__TITLE_AND_BODY_2.png`.
**Placeholders.** `idx=0` title, `idx=1` body, `idx=2` eyebrow, `idx=3` subtitle.
**Builder.** `deck.add_title_subtitle_body(title, subtitle, body, eyebrow=None)`.

### `ONE_COLUMN_TEXT` (layout 15)
**Purpose.** A single column of body text with a title — use for manifesto/narrative slides.
**Preview.** (no example slide — use the builder and preview locally).
**Placeholders.** `idx=0` title, `idx=1` body.

---

## 4. Title only (image-led slides)

### `TITLE_ONLY` (layout 09)
**Purpose.** Big title with no body. Use when the title *is* the slide (bold claim, single-sentence concept).
**Preview.** `slide-12__TITLE_ONLY.png`, `slide-32__TITLE_ONLY.png`, `slide-33__TITLE_ONLY.png`, `slide-34__TITLE_ONLY.png`.
**Placeholders.** `idx=0` title, `idx=2` eyebrow.
**Builder.** `deck.add_title_only(title, eyebrow=None)`.

### `TITLE_ONLY_2` (layout 10)
**Purpose.** Title + subtitle, no body — good as a chapter opener inside a section, or a photo-heavy slide.
**Preview.** `slide-09__TITLE_ONLY_2.png`, `slide-13__TITLE_ONLY_2.png`.
**Placeholders.** `idx=0` title, `idx=2` eyebrow, `idx=3` subtitle.
**Builder.** `deck.add_title_subtitle_only(title, subtitle, eyebrow=None)`.

---

## 5. Two-column layouts

Use these when the story has a clean binary — before/after, us/them, problem/solution, seller/business.

### `TITLE_AND_TWO_COLUMNS` (layout 05)
**Purpose.** Title + two text columns. Left/right get equal weight.
**Preview.** `slide-08__TITLE_AND_TWO_COLUMNS.png`.
**Placeholders.** `idx=0` title, `idx=1` left body, `idx=2` right body, `idx=3` eyebrow.
**Builder.** `deck.add_two_columns(title, left_title, left_body, right_title, right_body, eyebrow=None)`.

### `TITLE_AND_TWO_COLUMNS_2` (layout 07)
**Purpose.** Two columns with column headings (left title + left body, right title + right body).
**Preview.** `slide-10__TITLE_AND_TWO_COLUMNS_2.png`.
**Placeholders.** `idx=0` title, `idx=1`/`idx=4` bodies, `idx=3` left column heading, `idx=2`/? right column heading.

### `TITLE_AND_TWO_COLUMNS_2_1` (layout 08)
**Purpose.** Same as _2 but with a small variant in spacing / icon placement.
**Preview.** `slide-11__TITLE_AND_TWO_COLUMNS_2_1.png`.

### `TITLE_AND_TWO_COLUMNS_3` (layout 06)
**Purpose.** Two columns with a strong visual anchor on one side — typically a photo or Aquatic Form right, text left.
**Preview.** `slide-07__TITLE_AND_TWO_COLUMNS_3.png`.

---

## 6. Three- and four-column layouts

### `TITLE_AND_TWO_COLUMNS_1_1_1` (layout 11)
**Purpose.** Three equal columns — "The Mearra Method: Idea · Vision · Implement"-style slides, three benefits, three phases.
**Preview.** `slide-14__TITLE_AND_TWO_COLUMNS_1_1_1.png`.
**Placeholders.** `idx=0` title, `idx=2`/`idx=3`/... column headings, `idx=1`/`idx=4`/... bodies.
**Builder.** `deck.add_three_columns(title, columns=[{"title":..., "body":...}, ...], eyebrow=None)`.

### `TITLE_AND_TWO_COLUMNS_1_1_1_2` (layout 12)
**Purpose.** Three columns with additional meta-text — longer variant.
**Preview.** `slide-15__TITLE_AND_TWO_COLUMNS_1_1_1_2.png`.

### `TITLE_AND_TWO_COLUMNS_1_1_1_2_1` (layout 13)
**Purpose.** Another three-column variant with slightly different alignment.
**Preview.** `slide-16__TITLE_AND_TWO_COLUMNS_1_1_1_2_1.png`.

### `TITLE_AND_TWO_COLUMNS_1_1_1_2_1_1` (layout 14)
**Purpose.** Four columns. Use for quadrants, four phases, four benefits.
**Preview.** `slide-17__TITLE_AND_TWO_COLUMNS_1_1_1_2_1_1.png`.
**Builder.** `deck.add_four_columns(title, columns=[...], eyebrow=None)`.

---

## 7. Text layouts (ONE_COLUMN variants)

Most of the `ONE_COLUMN_TEXT_*` variants are subtle positioning alternatives used in the sample deck to carry image-heavy case study slides. They are fine to use but for most slides `TITLE_AND_BODY` or `TITLE_ONLY` will serve.

### `ONE_COLUMN_TEXT_1` (layout 16)
**Purpose.** Image-led slide with no text placeholders — this is the layout the template uses for big full-bleed graphics (slides 46–47 with icons).
**Preview.** `slide-18__ONE_COLUMN_TEXT_1.png`, `slide-46__ONE_COLUMN_TEXT_1.png`, `slide-47__ONE_COLUMN_TEXT_1.png`.
**Builder.** `deck.add_custom_slide("ONE_COLUMN_TEXT_1", image_paths=[...])`.

### `ONE_COLUMN_TEXT_1_1_1` (layout 17)
**Purpose.** Title + body + subtitle — a richer narrative slide.
**Preview.** `slide-19__ONE_COLUMN_TEXT_1_1_1.png` and `slide-26`–`slide-31` (reused for case study sequence).

### `ONE_COLUMN_TEXT_1_1_1_4`, `_4_2`, `_2`, `_2_2`, `_2_2_1`, `_2_1` (layouts 18–23)
**Purpose.** Variants of the narrative slide with slightly different image framings. Use the preview PNGs to pick the right one.
**Previews.** `slide-20` … `slide-24`.

---

## 8. Custom / decorative layouts

These are heavily composed layouts from the sample deck — typically case-study spreads or editorial pages. Use them when you want a richer visual moment.

### `CUSTOM_8_1_2_1_1` (layout 02)
**Purpose.** Cover-adjacent editorial layout with multiple text positions — used for the "who are we" title spread.
**Preview.** `slide-03__CUSTOM_8_1_2_1_1.png`.

### `CUSTOM_1_3_1_1_1_1_1_1_1_1_1_1_1_1` (layout 24) and the deeper `CUSTOM_1_3_*` series (layouts 25, 27, 28, 31, 32, 33)
**Purpose.** Editorial / case-study spreads. These carry imagery and text blocks positioned for a specific story beat. Use the matching preview to decide whether to reuse the layout or build a custom slide on top of a simpler layout.
**Previews.** `slide-25`, `slide-35`, `slide-39`–`slide-43`.

### `BIG_NUMBER_1_3_1_1_1_1_1_1` (layout 29) and `BIG_NUMBER_1_3_1_1_1_1_1_1_1` (layout 30)
**Purpose.** Metric-forward slides. Use for "15+ years," "4× conversion lift," "NPS 71" — the kind of single-number hero.
**Previews.** `slide-37__BIG_NUMBER_1_3_1_1_1_1_1_1.png`, `slide-38__BIG_NUMBER_1_3_1_1_1_1_1_1_1.png`.

---

## How to choose a layout — decision tree

```
What's the slide's job?
│
├── First slide of the deck?                 → TITLE (add_cover)
├── Last slide of the deck?                  → TITLE_1 (add_thank_you)
├── Divider between sections?                → SECTION_HEADER (add_section_header)
│                                             ↳ For extra weight: SECTION_HEADER_1_3_4_1_1_1
│
├── One concept, short body?                 → TITLE_AND_BODY (add_title_body)
├── One concept, with a sub-claim?           → TITLE_AND_BODY_2 (add_title_subtitle_body)
├── One strong statement, no body?           → TITLE_ONLY (add_title_only)
├── Big statement + subtitle, no body?       → TITLE_ONLY_2 (add_title_subtitle_only)
│
├── Two sides (us/them, before/after)?       → TITLE_AND_TWO_COLUMNS (add_two_columns)
├── Three phases, three benefits?            → TITLE_AND_TWO_COLUMNS_1_1_1 (add_three_columns)
├── Four items / quadrants?                  → TITLE_AND_TWO_COLUMNS_1_1_1_2_1_1 (add_four_columns)
│
├── A big number or metric?                  → BIG_NUMBER_*
├── An image-dominated slide?                → ONE_COLUMN_TEXT_1 (add_custom_slide + add_image)
└── Something none of the above fits?        → Build a custom slide on ONE_COLUMN_TEXT_1
                                               or TITLE_ONLY as a blank canvas with
                                               brand chrome — see SKILL.md §"Building
                                               new layouts inside the brand system".
```

---

## Working with placeholders directly

When you use `deck.add_custom_slide("LAYOUT_NAME", placeholders={idx: "text"})`, you fill placeholders by their `idx`. The conventions across the template are:

- **`idx=0`** → main title (Sofia Sans Extra Condensed, italic, Trench).
- **`idx=1`** → main body (Sofia Sans, Regular).
- **`idx=2`** → eyebrow / kicker OR left column heading depending on layout. Check placeholder's name or the preview PNG.
- **`idx=3`–`idx=n`** → additional titles / bodies for multi-column layouts.
- **`idx=12`** → slide number (leave alone — it's handled automatically).

To inspect a layout's placeholders interactively:

```python
from pptx import Presentation
p = Presentation('assets/template.pptx')
for layout in p.slide_masters[0].slide_layouts:
    if layout.name == 'TITLE_AND_TWO_COLUMNS_1_1_1':
        for ph in layout.placeholders:
            print(ph.placeholder_format.idx, ph.placeholder_format.type, ph.name)
```

---

## When the stock layouts don't fit

Build a custom slide on top of `ONE_COLUMN_TEXT_1` (no text placeholders — blank canvas with correct chrome) or `TITLE_ONLY` (title kept, nothing else). Then add brand-coloured shapes and text via `deck.add_heading_textbox(...)`, `deck.add_body_textbox(...)`, `deck.add_rect(...)`, `deck.add_aquatic_form(...)`, and `deck.add_icon(...)`.

Never introduce a non-brand colour, font, or mark. If you need something that isn't in `assets/`, ask the user before inventing it — see `../ASSETS.md`.
