---
description: Produce unmistakably on-brand Mearra PowerPoint presentations — pitch decks, internal decks, strategy/board decks, product/marketing decks, and steering-group decks. Use this skill whenever the user wants to create, extend, rewrite, or restyle a Mearra slide deck. Trigger liberally on phrases like "Mearra deck", "pitch slides", "client slides", "board slides", "Mearra PPTX", "draft a deck for…", "slides for our meeting", or any time a presentation is needed and the context is Mearra (mearra.com, Wunder → Mearra, "Business. People. Tech. Together."). The skill ships with the official Mearra template (35 on-brand layouts), the Mearra logo marks, a library of Aquatic Form illustrations, a named icon set, brand photography, and helper scripts that guarantee the output uses the correct colors, typography, and layout grid. It can also build new layouts inside the brand system when the stock layouts don't fit.
---

# Mearra PPTX — Brand-Perfect Presentations

You are producing a presentation for **Mearra** (rebranded from Wunder in 2026). Tagline: **"Business. People. Tech. Together."**  Brand essence: human-led, business-focused, tech-enabled. Visual identity: warm + cool palette, flowing *Aquatic Forms*, Sofia Sans typography.

This skill guarantees brand fidelity by building every deck on top of the official template (`assets/template.pptx`) rather than hand-drawing slides. Use the helper library in `scripts/mearra_deck.py` to add slides by layout name and fill placeholders — the template's master slide handles colors, fonts, logo position, tagline, and background graphics automatically.

All skill assets (template, scripts, references, icons, etc.) live in:
`~/.claude/commands/mearra-pptx/`

## Golden rules — read these first

1. **Always start from the template.** Open `~/.claude/commands/mearra-pptx/assets/template.pptx` and strip it down. Never start from a blank deck.
2. **Pick a layout by name.** The template has 35 named layouts (see `~/.claude/commands/mearra-pptx/references/layout-catalog.md`). Match the slide's purpose to a layout name — don't invent positioning.
3. **Brand adherence is strict.** Never introduce non-brand colors, fonts, or graphics.
4. **Voice matters as much as visuals.** Every headline, every bullet must sound like Mearra: confident, optimistic, devoted, humane, quirky, active. Short. Direct. No hedging. See `~/.claude/commands/mearra-pptx/references/tone-of-voice.md`.
5. **Use the asset library for richness.** Drop in aquatic forms, icons, and photos from `~/.claude/commands/mearra-pptx/assets/` to elevate a slide. See `~/.claude/commands/mearra-pptx/ASSETS.md` for the full catalog.
