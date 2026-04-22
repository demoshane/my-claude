"""
Worked example: build a short, on-brand pitch deck using the MearraDeck builder.

Run:  python -m scripts.build_example
Output: $COWORK_OUTPUTS/mearra-example.pptx (defaults to the active session's
        /sessions/*/mnt/outputs folder)
"""
import os
from pathlib import Path

from .mearra_deck import MearraDeck
from .colors import INDIGO, BLOSSOM, CORAL, LAGOON, TRENCH, MIST, WHITE, CURRENT


def build() -> Path:
    deck = MearraDeck()

    # 1. Cover
    deck.add_cover(
        title="Making media better, across the board",
        subtitle="A Mearra concept for Sanoma",
        presenter_line="Maija Helminen & Vesa Palmu — 20.4.2026",
        variant="indigo",
    )

    # 2. Agenda (section divider)
    deck.add_section_header("Agenda")

    # 3. Who we are
    deck.add_title_body(
        title="We know media business",
        body="From processes to concepts to technology — for 15+ years. We've built "
             "AI audio ads, dynamic pricing, self-service sales, and inventory "
             "optimisation for operators across the Nordics.",
        eyebrow="Introduction",
    )

    # 4. Our approach — 3 columns
    deck.add_three_columns(
        title="How we tackle the hard stuff",
        eyebrow="The Mearra Method",
        columns=[
            {
                "title": "IDEA",
                "body":  "A working proof-of-direction in days, not months. "
                         "Sketch the concept, align on the sharp corners early.",
            },
            {
                "title": "VISION",
                "body":  "Workshop-driven KPIs, a roadmap everyone signs up to, "
                         "and an honest view of what's worth building.",
            },
            {
                "title": "IMPLEMENT",
                "body":  "Agentic AI development with a human in the loop. "
                         "Every phase ends with a stop/continue decision.",
            },
        ],
    )

    # 5. Section divider
    deck.add_section_header("Next-level AI planning", eyebrow="Concept case study")

    # 6. The concept — title + subtitle + body
    deck.add_title_subtitle_body(
        title="Sales process for the AI era",
        subtitle="A live-listening assistant that turns meetings into media plans.",
        body="AI listens to the sales meeting with full background data on the "
             "client. It generates a prompt for MCP, which writes a candidate plan "
             "directly into the planner. The seller tweaks, the client agrees, the "
             "plan ships. Faster hit rate, less double work, shorter learning curve.",
        eyebrow="The concept",
    )

    # 7. Two columns — benefits
    deck.add_two_columns(
        title="Why it works",
        eyebrow="Outcomes that matter",
        left_title="For the seller",
        left_body="Real-time plan during the meeting. No post-call scramble. "
                  "Every client conversation compounds into better AI for the next one.",
        right_title="For the business",
        right_body="Higher hit rate, lower time-to-plan, portable process. "
                   "No vendor lock-in — your own people can continue the work.",
    )

    # 8. Close
    deck.add_thank_you(subtitle="mearra.com")

    out = _resolve_output_path("mearra-example.pptx")
    deck.save(out)
    return out


def _resolve_output_path(filename: str) -> Path:
    """Find the active Cowork session's outputs folder, or fall back to cwd."""
    override = os.environ.get("COWORK_OUTPUTS")
    if override:
        base = Path(override)
    else:
        # Any /sessions/<id>/mnt/outputs that exists right now
        candidates = sorted(Path("/sessions").glob("*/mnt/outputs"))
        base = candidates[0] if candidates else Path.cwd()
    base.mkdir(parents=True, exist_ok=True)
    return base / filename


if __name__ == "__main__":
    path = build()
    print(f"Saved: {path}")
