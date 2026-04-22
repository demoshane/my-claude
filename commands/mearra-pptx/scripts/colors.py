"""
Mearra brand color palette — the ONLY colors allowed in any Mearra deck.
All values are from the Mearra Brand Identity 2026 document.
"""
from pptx.dml.color import RGBColor


# ---- Warm tones (visual signature) ----
BLOSSOM = RGBColor(0xFF, 0xA5, 0xD2)   # #ffa5d2 — pink, primary warm accent
CORAL   = RGBColor(0xFF, 0x5C, 0x5F)   # #ff5c5f — coral red

# ---- Cool tones ----
INDIGO  = RGBColor(0x44, 0x00, 0xF0)   # #4400f0 — section/cover background
TRENCH  = RGBColor(0x1E, 0x00, 0x50)   # #1e0050 — heading color, deep navy
LAGOON  = RGBColor(0x00, 0xBE, 0xBE)   # #00bebe — teal
CURRENT = RGBColor(0x00, 0xF0, 0x87)   # #00f087 — bright green

# ---- Neutrals ----
MIST    = RGBColor(0xEB, 0xE6, 0xE0)   # #ebe6e0 — primary light background
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
BLACK   = RGBColor(0x00, 0x00, 0x00)


# ---- Approved 3-color gradients (from brand guide) ----
APPROVED_GRADIENTS = [
    ("BLOSSOM", "CORAL"),
    ("INDIGO",  "BLOSSOM"),
    ("BLOSSOM", "TRENCH"),
    ("INDIGO",  "TRENCH"),
    ("INDIGO",  "LAGOON"),
    ("LAGOON",  "TRENCH"),
    ("BLOSSOM", "CORAL",  "CURRENT"),
]


# ---- Tint opacities permitted ----
TINT_OPACITIES = [5, 25, 50, 75, 95]


# ---- Typography constants ----
FONT_HEADING = "Sofia Sans Extra Condensed"   # Bold / ExtraBold / Black — often italic
FONT_BODY    = "Sofia Sans"                   # Regular / Medium


# ---- Brand text constants ----
SLOGAN   = "Business. People. Tech. Together."
URL      = "mearra.com"
COMPANY  = "Mearra"


# ---- Color usage proportions (from brand guide §4) ----
# 80% neutral / 15% warm / 5% cool as a loose guide
# Warm (Blossom, Coral) carry the visual signature.
# Cool (Indigo, Trench, Lagoon, Current) provide depth.

def hex_to_rgb(h: str) -> RGBColor:
    """Convert a hex string like '#4400f0' to RGBColor."""
    h = h.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


ALL_BRAND_COLORS = {
    "BLOSSOM": BLOSSOM, "CORAL":   CORAL,
    "INDIGO":  INDIGO,  "TRENCH":  TRENCH,
    "LAGOON":  LAGOON,  "CURRENT": CURRENT,
    "MIST":    MIST,    "WHITE":   WHITE, "BLACK": BLACK,
}
