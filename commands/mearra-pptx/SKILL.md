---
name: mearra-pptx
description: Produce unmistakably on-brand Mearra PowerPoint presentations — pitch decks, internal decks, strategy/board decks, product/marketing decks, and steering-group decks. Use this skill whenever the user wants to create, extend, rewrite, or restyle a Mearra slide deck. Trigger liberally on phrases like "Mearra deck", "pitch slides", "client slides", "board slides", "Mearra PPTX", "draft a deck for…", "slides for our meeting", or any time a presentation is needed and the context is Mearra (mearra.com, Wunder → Mearra, "Business. People. Tech. Together."). The skill ships with the official Mearra template (35 on-brand layouts), the Mearra logo marks, a library of Aquatic Form illustrations, a named icon set, brand photography, and helper scripts that guarantee the output uses the correct colors, typography, and layout grid. It can also build new layouts inside the brand system when the stock layouts don't fit.
---

# Mearra PPTX — Brand-Perfect Presentations

You are producing a presentation for **Mearra** (rebranded from Wunder in 2026). Tagline: **"Business. People. Tech. Together."**  Brand essence: human-led, business-focused, tech-enabled. Visual identity: warm + cool palette, flowing *Aquatic Forms*, Sofia Sans typography.

This skill guarantees brand fidelity by building every deck on top of the official template (`assets/template.pptx`) rather than hand-drawing slides. Use the helper library in `scripts/mearra_deck.py` to add slides by layout name and fill placeholders — the template's master slide handles colors, fonts, logo position, tagline, and background graphics automatically.

## Golden rules — read these first

1. **Always start from the template.** Open `assets/template.pptx` and strip it down. Never start from a blank deck. The master slide carries the colors, fonts, logo, and tagline — you lose all of that if you use a blank presentation.
2. **Pick a layout by name.** The template has 35 named layouts (see `references/layout-catalog.md`). Match the slide's purpose to a layout name — don't invent positioning.
3. **Brand adherence is strict.** Never introduce non-brand colors, fonts, or graphics. If the user's content doesn't fit an existing layout, build a new layout that still uses only Mearra colors, Sofia Sans, and Aquatic Forms from the asset library.
4. **Voice matters as much as visuals.** Every headline, every bullet must sound like Mearra: confident, optimistic, devoted, humane, quirky, active. Short. Direct. No hedging. See `references/tone-of-voice.md`.
5. **Use the asset library for richness.** Drop in aquatic forms, icons, and photos from `assets/` to elevate a slide from "correct" to "unmistakable." See `ASSETS.md` for the full catalog.

## Workflow

### Step 1 — Understand the ask

Before drafting, clarify (briefly, via the question tool if available):
- **Audience** — client, internal, steering group, board?
- **Purpose** — pitch, case study, status update, concept pitch, all-hands?
- **Length** — rough slide count or presentation time?
- **Content** — what's the story? Ask for the raw material if not provided.
- **Deliverable name** — what should the output .pptx be called?

If the user has already given enough detail, skip the questions and proceed.

### Step 2 — Load the brand context

**Always read these two files before writing slide copy:**
- `references/brand-bible.md` — full brand system (positioning, voice, color, type, illustration)
- `references/tone-of-voice.md` — voice rules and approved phrasings

Skim `references/layout-catalog.md` and the thumbnails in `assets/layout-previews/` to pick layouts.

### Step 3 — Plan the deck

Draft a slide-by-slide outline *in your head or as a quick list* before touching the builder. For each slide, decide:
1. **Layout** — pick the layout name that matches the content type (cover, section header, single concept, 2/3 columns, big number, timeline, team, etc.)
2. **Headline** — in Mearra voice (imperative, confident, short)
3. **Body copy** — short sentences, active voice, no hedging
4. **Visual element** — aquatic form? icon? photo? nothing (whitespace is a Mearra value)

If any slide needs something the stock layouts don't offer, plan a **custom layout** using the brand system (see "Building new layouts" below).

### Step 4 — Build the deck with `scripts/mearra_deck.py`

```python
from scripts.mearra_deck import MearraDeck

deck = MearraDeck()                        # loads assets/template.pptx, strips example slides
deck.add_cover(
    title="Wunder is now Mearra — a new era is here",
    subtitle="Maija Helminen & Vesa Palmu — 20.4.2026",
    variant="indigo",                      # or "light"
)
deck.add_section_header("Agenda")
deck.add_title_body(
    title="We know media business",
    body="From processes, to concepts, to technology — for 15+ years.",
    accent="auto",                         # places an aquatic form on the right-bleed
)
deck.add_two_columns(
    title="Making media better across the board",
    left_title="Self-service channels",
    left_body="B2B self-service products that reach hard-to-reach groups.",
    right_title="Sales workflow automation",
    right_body="Cross-system automation for smoother internal workflows.",
    left_icon="client",                    # optional icons above each column
    right_icon="recycle",
)
deck.add_big_number(
    number="15+", label="years dismantling complexity",
    context="For Finland's largest media houses — processes, concepts, and tech.",
)
deck.add_thank_you(subtitle="mearra.com")
deck.save("/sessions/$SESSION_ID/mnt/outputs/mearra-deck.pptx")  # session outputs folder
```

See `scripts/mearra_deck.py` for the full API. Every `add_*` method maps to a specific layout in the template.

### Slide types at a glance

| Method | When to use |
|---|---|
| `add_cover(variant="indigo"\|"light")` | Opening slide with date/presenter line. |
| `add_section_header(title, eyebrow)` | Full-bleed indigo divider between sections. |
| `add_title_body(title, body, accent)` | Single concept explained in one paragraph. |
| `add_title_subtitle_body(title, subtitle, body, accent)` | Concept with a tagline under the title. |
| `add_title_only(title, accent)` | Statement slide — one line, strong. |
| `add_title_subtitle_only(title, subtitle, accent)` | Chapter opener with a supporting line. |
| `add_two_columns(..., left_icon, right_icon)` | Wins vs. risks, for vs. against, before/after. |
| `add_three_columns(columns=[{title, body, icon}])` | Mearra Method, 3-phase process, 3 options. |
| `add_four_columns(columns=[{title, body, icon}])` | Four-phase engagement, 4 pillars. |
| `add_big_number(number, label, context)` | Single dominant metric ("15+ years"). |
| `add_metric_strip(title, metrics=[{number, label}])` | 2–4 KPIs in a row. |
| `add_hero(title, subtitle, photo)` | Full-bleed photo with overlay title — chapter openers. |
| `add_quote(quote, attribution)` | Testimonial or founding principle. |
| `add_split_image_text(title, body, image, image_side)` | Photo on one half, concept on the other — modelled on brand slide-38. |
| `add_team_member(name, role, bio, photo, contact)` | Single-person profile with a big portrait and short bio — slide-35. |
| `add_team_grid(title, people)` | Circular avatars in a 3-column grid — slide-36. Up to 9 people. |
| `add_timeline(title, milestones)` | Horizontal milestones on an Indigo rail with dots in warm/cool brand colours. |
| `add_table(title, headers, rows)` | Indigo-header + Mist-body zebra table. |
| `add_pie_chart(title, slices)` | Native doughnut with brand-coloured wedges and a left-side legend. |
| `add_pyramid(title, levels)` | 3–5 stacked trapezoids with side captions; colours pulled from a brand-safe gradient. |
| `add_circular_lifecycle(title, phases, center_label)` | Four-phase engagement ring with labelled quadrants — slide-41. Requires exactly 4 phases. |
| `add_thank_you(subtitle)` | Closing slide. |

### Design heuristics — when to add visual richness

A Mearra deck should feel **composed, not just typeset**. Use these rules of thumb:

- **Roughly half of your content slides** should carry an Aquatic Form accent. The rest should rely on whitespace and strong typography. A deck that has a form on every slide looks busy; one with zero forms looks tentative.
- **Use `accent="auto"`** for most content slides — it picks the right form for the slot. Override with `accent="cluster-tall-03"` (pink/coral) for warmer moments or `accent="cluster-tall-02"` (teal/indigo) for cooler, more technical ones.
- **Use icons on column slides** when each column represents a distinct category or phase. Skip them if columns are continuous (e.g. "before / after"). Icons should be single-concept per column.
- **Use `add_big_number`** when one stat carries the slide. Don't cram multiple.
- **Use `add_metric_strip`** for "by the numbers" slides — max 4 metrics.
- **Use `add_hero`** sparingly — once or twice per deck at most, as emotional punctuation.
- **Use `add_quote`** for testimonials or when a single sentence is the point.
- **Use `add_split_image_text`** when a portrait or product shot earns half the slide — makes the concept feel human. Great for belief/value statements.
- **Use `add_team_member`** for one person (hiring pitch, key-role introduction) and `add_team_grid` for the "meet the crew" slide. Grid supports up to 9 people; anything more should split across two slides.
- **Use `add_timeline`** for sequenced milestones when dates matter. Keep it to 3–6 stops; more and the copy crowds.
- **Use `add_table`** sparingly — only when the *structure* is the point. If the table has only 2 columns, consider two columns or bullets instead.
- **Use `add_pie_chart`** for breakdown / share-of-time / share-of-budget slides. Max 5 slices; more and the legend gets busy.
- **Use `add_pyramid`** for strategic layers (vision → strategy → execution) or maturity stages. 3 levels reads best; 5 is the upper limit.
- **Use `add_circular_lifecycle`** for the engagement model / service lifecycle slide. Requires exactly 4 phases — the geometry is designed around a 4-quadrant layout.

### Voice on every slide

Every slide's copy must sound like Mearra: short, active, specific, warm, unafraid of pauses. Before you call `deck.save()`, re-read every headline. If it could come from any generic consultancy, rewrite it.

### Step 5 — Validate

Before handing the deck back, check:
- [ ] Every headline is in Mearra voice (short, confident, active, specific)
- [ ] No non-brand colors anywhere (only Blossom, Coral, Indigo, Trench, Lagoon, Current, Mist, White, Black — see `references/brand-bible.md §4`)
- [ ] Cover slide has tagline "Business. People. Tech. Together." (handled automatically by template)
- [ ] Closing slide says "Thank you!" and "mearra.com"
- [ ] No placeholder lorem ipsum survived
- [ ] File saved to the current session's `mnt/outputs/` folder so the user can open it

Render the deck to PNG to visually verify (LibreOffice is available in the sandbox):
```bash
libreoffice --headless --convert-to pdf <output.pptx> --outdir /tmp/
# then use pymupdf to render PDF pages to PNG to review visually
```

### Step 6 — Deliver

Share a direct `computer://` link to the `.pptx` file with a one-sentence summary of what it contains. Don't explain the whole deck back to the user — let them open it.

## Building new layouts inside the brand system

When the 35 stock layouts don't fit the content (e.g., a novel infographic, a unique data visualization, a custom process diagram), **build within the brand system**:

- Colors: **only** the palette in `references/brand-bible.md §4`
- Typography: **only** Sofia Sans (body) and Sofia Sans Extra Condensed (headings, Bold/ExtraBold/Black, often italic)
- Background: Mist (`#ebe6e0`) for light slides, Indigo (`#4400f0`) or Trench (`#1e0050`) for dark slides
- Add an **Aquatic Form** from `assets/aquatic-forms/` as a graphic anchor — they are designed to be cropped beyond the frame (right edge, bottom-right corner, top-left bleeding off)
- Logo position: bottom-right (M symbol) for content slides; centered or left-anchored on cover slides
- Tagline position: bottom-left for title and section slides
- Grain texture on illustrations: 5–25% depending on scale

`scripts/mearra_deck.py` exposes `deck.add_custom_slide(layout_name, image_paths=...)` that uses the `TITLE_ONLY` or `ONE_COLUMN_TEXT_1` layouts as blank canvases with correct chrome — then you add custom shapes/text on top with the brand color and font constants from `scripts/colors.py`.

**Never invent colors, fonts, or fake logos.** If you need something that's not in the asset library, ask the user to supply it or use whitespace.

## Asset library

The assets library is designed to be **extended over time**. See `ASSETS.md` for:
- Current catalog (logos, aquatic forms, icons, photos, layout previews)
- How to add new assets and have the skill use them automatically
- File-naming conventions

When an asset is missing (e.g., user asks for a specific icon that isn't in `assets/icons/`), tell the user what you'd need and offer to proceed with the closest match or without the icon.

## Files in this skill

```
mearra-pptx/
├── SKILL.md                       # ← you are here
├── ASSETS.md                      # asset catalog + extension guide
├── references/
│   ├── brand-bible.md             # full brand system
│   ├── tone-of-voice.md           # quick voice guide
│   ├── layout-catalog.md          # 35 layouts described
│   └── copy-specimens.md          # approved headlines, phrasings, slogan variants
├── assets/
│   ├── template.pptx              # THE template — always start here
│   ├── logos/                     # Mearra M mark + wordmark
│   ├── aquatic-forms/             # 13 brand illustrations
│   ├── icons/                     # 48 named line icons
│   ├── backgrounds/               # 5 atmospheric photos
│   └── layout-previews/           # PNG of every example slide
└── scripts/
    ├── mearra_deck.py             # main builder library
    ├── colors.py                  # brand color constants
    └── build_example.py           # starter script demonstrating full API
```
