"""
Alignment / smoke tests for the Mearra PPTX skill.

Exercises:
  1. Every high-level `MearraDeck.add_*` method with realistic on-brand copy.
  2. Every layout in the template via `add_custom_slide(layout_name)` so we
     can visually verify each one still renders with brand chrome intact.

Outputs:
  - `/tmp/mearra-tests/01-api-tour.pptx`        — one slide per builder method
  - `/tmp/mearra-tests/02-all-layouts.pptx`     — one slide per named layout
  - `/tmp/mearra-tests/pngs/...`                — rendered slide thumbnails
  - `/tmp/mearra-tests/REPORT.md`               — summary with any rendering issues

Run: python -m scripts.run_alignment_tests
"""
from pathlib import Path
import subprocess
import sys
import traceback

from .mearra_deck import MearraDeck
from .colors import INDIGO, CORAL, BLOSSOM, CURRENT, LAGOON, TRENCH


OUT = Path("/tmp/mearra-tests")
PNGS = OUT / "pngs"
OUT.mkdir(parents=True, exist_ok=True)
PNGS.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Test 1 — API tour: one slide per high-level MearraDeck method
# ---------------------------------------------------------------------------

def build_api_tour() -> Path:
    deck = MearraDeck()

    deck.add_cover(
        title="Complexity gets us going",
        subtitle="A Mearra test cover — indigo variant",
        presenter_line="API tour · 20.4.2026",
        variant="indigo",
    )

    deck.add_cover(
        title="Playing tech as our instrument",
        subtitle="A Mearra test cover — light variant",
        presenter_line="API tour · 20.4.2026",
        variant="light",
    )

    deck.add_section_header(
        title="Agenda",
        eyebrow="Section divider test",
    )

    deck.add_title_body(
        title="We know media business",
        body="15+ years dismantling complexity for large media organisations. "
             "From processes to concepts to tech — with our hands on the keyboard "
             "and our eyes on the business.",
        eyebrow="Introduction",
    )

    deck.add_title_subtitle_body(
        title="Sales process for the AI era",
        subtitle="A live-listening assistant that turns meetings into media plans.",
        body="AI listens to the sales meeting with full client context, writes a "
             "candidate plan into the planner, and the seller tweaks it live. "
             "Faster hit rate, less double work, shorter learning curve.",
        eyebrow="The concept",
    )

    deck.add_title_only(
        title="You say difficult, we say \u2018where?\u2019",
        eyebrow="Statement slide",
    )

    deck.add_title_subtitle_only(
        title="Small talk, all action",
        subtitle="Mearra mindset, in four words.",
        eyebrow="Chapter opener",
    )

    deck.add_two_columns(
        title="Why it works",
        eyebrow="Outcomes that matter",
        left_title="For the seller",
        left_body="Real-time plan during the meeting. No post-call scramble. "
                  "Every client conversation compounds into better AI for the next one.",
        right_title="For the business",
        right_body="Higher hit rate, lower time-to-plan, portable process. "
                   "No vendor lock-in \u2014 your own people can continue the work.",
        left_icon="team",
        right_icon="chart",
    )

    deck.add_three_columns(
        title="The Mearra Method",
        eyebrow="How we tackle the hard stuff",
        columns=[
            {"title": "IDEA",       "body": "A working proof-of-direction in days, not months.",  "icon": "diamond"},
            {"title": "VISION",     "body": "Workshop-driven KPIs and a roadmap everyone signs up to.", "icon": "star"},
            {"title": "IMPLEMENT",  "body": "Agentic AI development with a human in the loop.",   "icon": "ai"},
        ],
    )

    deck.add_four_columns(
        title="Four phases",
        eyebrow="Engagement structure",
        columns=[
            {"title": "DISCOVER",  "body": "Understand the business reality.",  "icon": "search"},
            {"title": "SHAPE",     "body": "Co-design the target state.",       "icon": "design"},
            {"title": "SHIP",      "body": "Build, integrate, deploy.",         "icon": "cloud"},
            {"title": "EVOLVE",    "body": "Measure, adapt, hand over.",        "icon": "recycle"},
        ],
    )

    deck.add_big_number(
        number="15+",
        label="years dismantling complexity",
        context="For Finland's largest media houses — processes, concepts, and tech.",
        eyebrow="By the numbers",
    )

    deck.add_metric_strip(
        title="Q1 2026 in numbers",
        eyebrow="Mearra momentum",
        metrics=[
            {"number": "5",  "label": "new clients onboarded"},
            {"number": "8",  "label": "experts hired"},
            {"number": "12", "label": "shipped concepts"},
        ],
    )

    deck.add_hero(
        title="Small talk, all action.",
        subtitle="How Mearra shows up when the work gets real.",
        eyebrow="Chapter 3",
        photo="atmospheric-orange",
    )

    deck.add_quote(
        quote="You say difficult, we say 'where?'",
        attribution="Mearra team motto",
        eyebrow="A principle",
    )

    # --- New slide types added for the 2026 skill update -------------------
    deck.add_split_image_text(
        title="Human-led, tech-enabled",
        body="People move the needle; tech gets out of the way. "
             "We pair senior craft with AI where it earns its keep.",
        eyebrow="Our belief",
        image="warm-portrait",
        image_side="left",
    )

    deck.add_team_member(
        name="Jean Duckling",
        role="Tech Support",
        bio="Jean keeps our media clients live, green, and shipping. "
             "12 years of ops, three languages of tickets, zero ego.",
        contact="jean@mearra.com · +358 40 000 0000",
        photo="orange-sweater",
    )

    deck.add_team_grid(
        title="Meet the crew",
        eyebrow="Team",
        people=[
            {"name": "Maija Helminen", "role": "Managing Director"},
            {"name": "Vesa Palmu",     "role": "Founding Partner"},
            {"name": "Jean Duckling",  "role": "Tech Support"},
            {"name": "Noora Virta",    "role": "Experience Lead"},
            {"name": "Pekka Salo",     "role": "Principal Engineer"},
            {"name": "Aino Laaksonen", "role": "Service Design"},
        ],
    )

    # Timeline V1 — segmented colour bar with year pins and numbered blocks
    deck.add_timeline(
        eyebrow="Timeline V1",
        milestones=[
            {"date": "2020", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2021", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2022", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2023", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2024", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
        ],
    )

    # Timeline V2 — chevron arrow track with lollipop year pins
    deck.add_timeline_arrows(
        title="Ducks in a row",
        eyebrow="Timeline V2",
        milestones=[
            {"date": "2023", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2024", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2025", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
            {"date": "2026", "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Do nec lectus turpis."},
        ],
    )

    deck.add_table(
        title="Scope vs. stage",
        eyebrow="At a glance",
        headers=["Stage", "Focus", "Deliverable", "Duration"],
        rows=[
            ["Discovery", "Understand the business",  "Opportunity map",   "2 weeks"],
            ["Shape",     "Co-design target state",   "Target architecture", "3 weeks"],
            ["Ship",      "Build & integrate",        "Production release",  "6 weeks"],
            ["Evolve",    "Measure & hand over",      "KPI report + runbook", "Ongoing"],
        ],
    )

    deck.add_pie_chart(
        title="Where the time goes",
        eyebrow="Anatomy of an engagement",
        slices=[
            {"label": "Development", "value": 55, "color": INDIGO},
            {"label": "Design",      "value": 20, "color": CORAL},
            {"label": "Strategy",    "value": 15, "color": BLOSSOM},
            {"label": "Ops",         "value": 10, "color": CURRENT},
        ],
    )

    deck.add_pyramid(
        title="Strategy to delivery",
        eyebrow="How we think about the work",
        levels=[
            {"label": "Vision",    "description": "North star — where Mearra is headed."},
            {"label": "Strategy",  "description": "The plan to get there."},
            {"label": "Execution", "description": "The daily work."},
        ],
    )

    # Circular lifecycle (service-offering ring — brand slide 41 duplicate)
    deck.add_circular_lifecycle(
        phases=[
            {"title": "Research & Discovery", "items": ["Audits", "Proof-of-Concepts", "Prototypes"]},
            {"title": "Design & Delivery",    "items": ["Service Design", "Software", "Agile Methods"]},
            {"title": "Improve & Optimize",   "items": ["Web Analytics", "Continuous Development"]},
            {"title": "Maintain & Secure",    "items": ["Cybersecurity", "24/7 Support", "FinOps"]},
        ],
        center_label="Proactive strategic digital partner",
    )

    # Office locations (brand "Our offices" slide duplicate)
    deck.add_office_locations(
        eyebrow="Our offices",
        offices=[
            {"city": "Helsinki", "address": "Kalevankatu 30\n00100 Helsinki"},
            {"city": "Tampere",  "address": "Hämeenkatu 10\n33100 Tampere"},
            {"city": "Turku",    "note": "Coworking hub · on request"},
            {"city": "Tallinn",  "address": "Narva mnt 7\n10117 Tallinn"},
        ],
    )

    # Safe-space principles split (brand principles slide duplicate)
    deck.add_principles_split(
        eyebrow="Principles",
        title="Safe Space Principles",
        body=(
            "These are the working agreements that let us tackle hard problems "
            "together without stepping on each other.\n\n"
            "**Respect** the craft and the person doing it. **Care** about the "
            "outcome, not who gets the credit. **Think** before you ship, and "
            "**communicate** early when things drift.\n\n"
            "When in doubt, ask. When in deeper doubt, ask twice."
        ),
        statements=[
            "Respect. Care. Think.",
            "Communicate. Don't assume.",
            "Small talk, all action.",
        ],
    )

    # Reference logos grid (brand "Our references" duplicate).
    # We only ship one reference logo in the skill assets; the method de-duplicates
    # missing ones silently, so this exercises the code path with a realistic grid.
    deck.add_reference_logos(
        eyebrow="References",
        title="A few of the teams we've worked with",
        logos=[
            "luke", "luke", "luke", "luke",
            "luke", "luke", "luke", "luke",
        ],
        cols=4,
    )

    # --- add_chart_panel — brand slides 28–31 duplication (all four visuals) ---
    deck.add_chart_panel(
        title="Maslow's hierarchy for ducks",
        visual="pyramid",
        subtitle="Chart & text",
        intro="From pond to pride:",
        items=[
            {"label": "Safety"},
            {"label": "Food"},
            {"label": "Flock"},
            {"label": "Preening"},
            {"label": "Self-actualisation"},
        ],
    )

    deck.add_chart_panel(
        title="Where the day goes",
        visual="circles",
        subtitle="Chart & text",
        intro="Circle area \u2248 time spent:",
        items=[
            {"label": "Swimming", "value": 45},
            {"label": "Eating",   "value": 25},
            {"label": "Preening", "value": 18},
            {"label": "Sleeping", "value": 12},
        ],
    )

    deck.add_chart_panel(
        title="A day in the life",
        visual="cycle",
        subtitle="Chart & text",
        intro="Repeats every ~24 hours:",
        center_label="Daily rhythm",
        items=[
            {"label": "Morning swim"},
            {"label": "Foraging"},
            {"label": "Midday rest"},
            {"label": "Afternoon preen"},
            {"label": "Evening flock"},
            {"label": "Night roost"},
        ],
    )

    deck.add_chart_panel(
        title="How the pond is allocated",
        visual="donut",
        subtitle="Chart & text",
        intro="Pond real-estate breakdown:",
        show_values=True,
        items=[
            {"label": "Open water",     "value": 40},
            {"label": "Reeds",          "value": 25},
            {"label": "Lily pads",      "value": 15},
            {"label": "Muddy shallows", "value": 12},
            {"label": "Nesting bank",   "value":  8},
        ],
    )

    deck.add_thank_you(subtitle="mearra.com")

    out = OUT / "01-api-tour.pptx"
    deck.save(out)
    return out


# ---------------------------------------------------------------------------
# Test 2 — One slide per named layout in the template
# ---------------------------------------------------------------------------

def build_all_layouts() -> tuple[Path, list[str], list[tuple[str, str]]]:
    """
    Add one slide per named layout and return (path, ok_layouts, failed_layouts).
    Each slide has the layout name stamped into the title placeholder (idx=0)
    and an eyebrow at idx=2 so you can see how the layout positions its chrome.
    """
    deck = MearraDeck()
    ok = []
    failed = []

    for layout_name in deck.list_layouts():
        try:
            slide = deck._add_slide(layout_name)
            # Stamp the layout name into title + eyebrow, if those placeholders exist
            deck._fill_placeholder(slide, 0, layout_name.replace("_", " "))
            deck._fill_placeholder(slide, 2, f"Layout: {layout_name}")
            # Also fill idx=1 (body) and idx=3 (second title) with distinguishing text
            deck._fill_placeholder(slide, 1, "Body placeholder — Sofia Sans Regular. "
                                              "Lorem ipsum with Mearra voice is not ipsum, "
                                              "it's 'complexity gets us going.'")
            deck._fill_placeholder(slide, 3, "Subtitle slot")
            ok.append(layout_name)
        except Exception as exc:
            failed.append((layout_name, f"{type(exc).__name__}: {exc}"))

    out = OUT / "02-all-layouts.pptx"
    deck.save(out)
    return out, ok, failed


# ---------------------------------------------------------------------------
# Test 3 — Asset loading smoke test
# ---------------------------------------------------------------------------

def asset_smoke_test() -> list[str]:
    """Ensure every asset referenced by the builder can be found via the fuzzy lookup."""
    deck = MearraDeck()
    issues = []
    # Icons
    icon_names = ["ai", "robot", "collaboration", "accessibility", "star", "cloud"]
    for n in icon_names:
        try:
            deck._find_asset("icons", n, prefix="icon-")
        except FileNotFoundError as e:
            issues.append(f"icon {n}: {e}")
    # Aquatic forms — only these five are genuine brand illustrations.
    aq_names = ["cluster-tall-01", "cluster-tall-02", "cluster-tall-03",
                "cluster-tall-04", "cluster-full-02"]
    for n in aq_names:
        try:
            deck._find_asset("aquatic-forms", n)
        except FileNotFoundError as e:
            issues.append(f"aquatic {n}: {e}")
    # Portraits, mockups, graphics (moved out of aquatic-forms)
    for n in ["warm-portrait", "orange-sweater"]:
        try:
            deck._find_asset("portraits", n)
        except FileNotFoundError as e:
            issues.append(f"portrait {n}: {e}")
    for n in ["laptop-open", "phone-in-hand"]:
        try:
            deck._find_asset("mockups", n)
        except FileNotFoundError as e:
            issues.append(f"mockup {n}: {e}")
    # Logos
    from .mearra_deck import ASSETS
    for variant in ["symbol-dark", "symbol-light", "wordmark-light"]:
        p = ASSETS / "logos" / f"mearra-{variant}.png"
        if not p.exists():
            issues.append(f"logo {variant} missing at {p}")
    return issues


# ---------------------------------------------------------------------------
# Rendering — convert .pptx to PDF then to PNG
# ---------------------------------------------------------------------------

def render_pptx_to_pngs(pptx_path: Path, prefix: str) -> list[Path]:
    """Convert a .pptx to PDF via libreoffice, then to PNGs."""
    # LibreOffice writes to the outdir with the .pptx's basename.
    subprocess.run(
        ["libreoffice", "--headless", "--convert-to", "pdf",
         str(pptx_path), "--outdir", str(OUT)],
        check=True, capture_output=True,
    )
    pdf_path = OUT / pptx_path.with_suffix(".pdf").name
    import fitz  # PyMuPDF
    doc = fitz.open(str(pdf_path))
    png_paths = []
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2))
        out = PNGS / f"{prefix}-slide-{i:02d}.png"
        pix.save(str(out))
        png_paths.append(out)
    doc.close()
    return png_paths


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def write_report(
    api_pptx: Path, api_pngs: list[Path],
    all_pptx: Path, all_pngs: list[Path],
    ok_layouts: list[str], failed_layouts: list[tuple[str, str]],
    asset_issues: list[str],
) -> Path:
    report = OUT / "REPORT.md"
    lines = [
        "# Mearra PPTX — Alignment Test Report",
        "",
        "Run: `python -m scripts.run_alignment_tests`  ",
        f"Output directory: `{OUT}`",
        "",
        "## Test 1 — API tour",
        "",
        f"- File: `{api_pptx.name}` ({len(api_pngs)} slides, one per `MearraDeck.add_*` method)",
        f"- Rendered thumbnails: `{PNGS.name}/api-slide-*.png` ({len(api_pngs)} files)",
        "",
        "Slides exercised (in order):",
        "1. `add_cover(variant='indigo')` — dark cover",
        "2. `add_cover(variant='light')` — light cover",
        "3. `add_section_header` — indigo section divider",
        "4. `add_title_body` — single concept + aquatic accent",
        "5. `add_title_subtitle_body` — title + subtitle + body + aquatic accent",
        "6. `add_title_only` — statement slide",
        "7. `add_title_subtitle_only` — chapter opener",
        "8. `add_two_columns` — with icons above each column",
        "9. `add_three_columns` — Mearra Method grid with icons",
        "10. `add_four_columns` — four-phase grid with icons",
        "11. `add_big_number` — giant stat with context",
        "12. `add_metric_strip` — horizontal metric blocks",
        "13. `add_hero` — full-bleed photo with overlay title",
        "14. `add_quote` — pull quote slide",
        "15. `add_split_image_text` — portrait left, concept right",
        "16. `add_team_member` — single-person profile",
        "17. `add_team_grid` — 3×N circular avatars with names/roles",
        "18. `add_timeline` — V1 segmented colour bar with year pins",
        "19. `add_timeline_arrows` — V2 chevron arrow track",
        "20. `add_table` — zebra-striped brand table",
        "21. `add_pie_chart` — native doughnut with brand legend",
        "22. `add_pyramid` — stacked trapezoids, Blossom→Coral→Indigo",
        "23. `add_circular_lifecycle` — brand slide-41 service-offering ring (indigo gradient + numbered quadrants)",
        "24. `add_office_locations` — two-column office list + Europe map",
        "25. `add_principles_split` — narrow Mist + wide Trench panel with italic statements",
        "26. `add_reference_logos` — client-logo grid on Mist",
        "27. `add_chart_panel(visual='pyramid')` — brand slide-28 duplicate",
        "28. `add_chart_panel(visual='circles')` — brand slide-29 duplicate",
        "29. `add_chart_panel(visual='cycle')` — brand slide-30 duplicate",
        "30. `add_chart_panel(visual='donut')` — brand slide-31 duplicate",
        "31. `add_thank_you` — closing slide",
        "",
        "## Test 2 — All template layouts",
        "",
        f"- File: `{all_pptx.name}` (one slide per named layout, {len(ok_layouts) + len(failed_layouts)} total)",
        f"- Rendered thumbnails: `{PNGS.name}/all-slide-*.png` ({len(all_pngs)} files)",
        "",
        f"### Layouts that instantiated cleanly ({len(ok_layouts)})",
        "",
    ]
    for name in ok_layouts:
        lines.append(f"- `{name}`")
    lines.append("")
    if failed_layouts:
        lines.append(f"### Layouts that FAILED ({len(failed_layouts)})")
        lines.append("")
        for name, err in failed_layouts:
            lines.append(f"- `{name}` — {err}")
        lines.append("")
    else:
        lines.append("### No layout failures. \u2713")
        lines.append("")
    lines.extend([
        "## Test 3 — Asset library smoke test",
        "",
    ])
    if asset_issues:
        lines.append("Issues found:")
        for i in asset_issues:
            lines.append(f"- {i}")
    else:
        lines.append("All probed assets resolved. \u2713")
    lines.append("")
    lines.extend([
        "## How to review",
        "",
        "Open the two .pptx files to inspect fidelity in real PowerPoint / Keynote. ",
        "The rendered PNGs give a quick visual overview of every slide — useful for spotting ",
        "alignment / overflow / colour issues without opening PowerPoint.",
    ])
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def main() -> int:
    print("[1/3] Building API tour deck...")
    api_pptx = build_api_tour()
    print(f"      \u2713 {api_pptx}")

    print("[2/3] Building all-layouts deck...")
    all_pptx, ok_layouts, failed_layouts = build_all_layouts()
    print(f"      \u2713 {all_pptx}")
    print(f"      {len(ok_layouts)} layouts OK, {len(failed_layouts)} failed")

    print("[3/3] Rendering to PDF/PNG...")
    api_pngs = render_pptx_to_pngs(api_pptx, prefix="api")
    all_pngs = render_pptx_to_pngs(all_pptx, prefix="all")
    print(f"      \u2713 {len(api_pngs)} API tour pngs, {len(all_pngs)} layout pngs")

    print("Running asset smoke test...")
    asset_issues = asset_smoke_test()
    print(f"      {'no issues' if not asset_issues else f'{len(asset_issues)} issues'}")

    report = write_report(api_pptx, api_pngs, all_pptx, all_pngs,
                          ok_layouts, failed_layouts, asset_issues)
    print(f"\nReport: {report}")
    print(f"Browse: {PNGS}")
    return 0 if not (failed_layouts or asset_issues) else 1


if __name__ == "__main__":
    sys.exit(main())
