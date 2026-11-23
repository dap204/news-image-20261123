#!/usr/bin/env python3
"""Draw the news-image-20261123 entry: a flat newspaper front page that sums up
the world's news of Monday 23 November 2026 in one 1024x1024 PNG.

Run:  python3 draw.py            (writes entry.png beside this file)
The competition program (main.ts) only copies entry.png to /output/entry.png;
this script is the image's source, kept in the repo so the picture is
reproducible byte for byte. No network, no external assets; fonts are the
system DejaVu faces. Every text block is auto-fitted with PIL's own text
measurement (fit_lines / fit_one), so a block can shrink but never overflow
its box or collide with the next one.
"""

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 233)
INK = (20, 22, 26)
BODY = (52, 54, 60)
GREY = (92, 92, 96)
RED = (178, 32, 44)
BLUE = (29, 78, 137)
TEAL = (14, 116, 110)
GREEN = (24, 110, 58)
PURPLE = (94, 52, 140)
ORANGE = (214, 116, 26)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, maxw):
    """Greedy word wrap; returns the lines that fit maxw."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, path, size, maxw, max_lines):
    """Largest size <= size whose wrap of text fits max_lines lines."""
    while size > 10:
        f = font(path, size)
        if len(wrap(draw, text, f, maxw)) <= max_lines:
            return f
        size -= 1
    return font(path, size)


def fit_one(draw, text, path, size, maxw):
    """Largest size <= size that fits text on one line of maxw."""
    while size > 10:
        f = font(path, size)
        if draw.textlength(text, font=f) <= maxw:
            return f
        size -= 1
    return font(path, size)


def draw_lines(draw, xy, text, fnt, fill, maxw, leading=1.12):
    """Draw the wrapped text; return the y just past the block."""
    x, y = xy
    step = int(fnt.size * leading)
    for line in wrap(draw, text, fnt, maxw):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def kicker(draw, xy, label, color):
    """Coloured tag with white bold text; return x just past the tag."""
    x, y = xy
    f = font(SANS_B, 24)
    w = draw.textlength(label, font=f) + 28
    draw.rounded_rectangle([x, y, x + w, y + 36], radius=6, fill=color)
    draw.text((x + 14, y + 5), label, font=f, fill=WHITE)
    return x + w


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 40  # page margin
RIGHT = W - M  # 984

# ---------------------------------------------------------------- masthead
d.line([M, 26, RIGHT, 26], fill=INK, width=3)
name_f = font(SERIF_B, 88)
title = "THE WORLD TODAY"
tw = d.textlength(title, font=name_f)
d.text(((W - tw) / 2, 38), title, font=name_f, fill=INK)
d.line([M, 150, RIGHT, 150], fill=INK, width=6)
d.line([M, 162, RIGHT, 162], fill=INK, width=2)
d.text((M, 176), "Monday, 23 November 2026", font=font(SANS_B, 33), fill=RED)
strap = "THE DAY'S NEWS ON ONE PAGE"
strap_f = font(SANS_B, 24)
d.text((RIGHT - d.textlength(strap, font=strap_f), 182), strap,
       font=strap_f, fill=GREY)

# ---------------------------------------------------------------- lead story
LY = 228
kicker(d, (M, LY), "CLIMATE  •  ANTALYA, TÜRKİYE", RED)
lead_f = fit_one(d, "COP31 CLIMATE TALKS", SERIF_B, 56, 630)
ly = LY + 52
for line in ("COP31 CLIMATE TALKS", "COLLAPSE — NO DEAL"):
    d.text((M, ly), line, font=lead_f, fill=INK)
    ly += int(lead_f.size * 1.12)
lead_sub = ("The UN summit ends in deadlock as the EU and its allies "
            "reject a final pact that never mentions fossil fuels — the "
            "first climate breakdown since Copenhagen in 2009.")
sub_f = fit_lines(d, lead_sub, SANS, 27, 620, 3)
draw_lines(d, (M, ly + 12), lead_sub, sub_f, BODY, 620, leading=1.28)

# lead visual (right column): globe, factory smoke, and the rejected pact
gx, gy = 692, 240
d.ellipse([gx, gy, gx + 168, gy + 168], fill=(120, 178, 224),
          outline=BLUE, width=5)
d.ellipse([gx + 24, gy + 28, gx + 76, gy + 66], fill=TEAL)
d.ellipse([gx + 88, gy + 84, gx + 142, gy + 130], fill=TEAL)
d.ellipse([gx + 38, gy + 102, gx + 78, gy + 132], fill=TEAL)
d.line([gx + 28, gy + 142, gx + 70, gy + 102, gx + 98, gy + 148],
       fill=RED, width=6)  # crack across the globe
fx = 884  # factory silhouette right of the globe: base, sawtooth roof,
# two chimneys, and a smoke trail climbing away to the upper right
d.polygon([(fx, gy + 168), (fx, gy + 128), (fx + 26, gy + 144),
           (fx + 52, gy + 128), (fx + 80, gy + 144), (fx + 80, gy + 168)],
          fill=INK)
d.rectangle([fx + 58, gy + 84, fx + 76, gy + 132], fill=INK)
d.rectangle([fx + 30, gy + 102, fx + 46, gy + 132], fill=INK)
for cx, cy, r in [(fx + 67, gy + 68, 10), (fx + 78, gy + 48, 13),
                  (fx + 92, gy + 24, 16)]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(168, 168, 172))
px, py = 692, 436  # the rejected pact: a sheet with a red cross
d.rectangle([px, py, px + 168, py + 72], fill=WHITE, outline=GREY, width=3)
for i in range(3):
    d.line([px + 16, py + 16 + i * 17, px + 152, py + 16 + i * 17],
           fill=(178, 178, 182), width=6)
d.line([px + 34, py + 10, px + 134, py + 62], fill=RED, width=11)
d.line([px + 134, py + 10, px + 34, py + 62], fill=RED, width=11)

d.line([M, 532, RIGHT, 532], fill=INK, width=3)

# ---------------------------------------------------------------- panels
def panel(x, y, w, label, color, headline, sub):
    """Story panel: colour bar, section label, <=2-line headline and sub."""
    d.rectangle([x, y, x + 8, y + 146], fill=color)
    d.text((x + 22, y), label, font=font(SANS_B, 23), fill=color)
    hf = fit_lines(d, headline, SANS_B, 34, w - 22, 2)
    hy = draw_lines(d, (x + 22, y + 32), headline, hf, INK, w - 22,
                    leading=1.1)
    sf = fit_lines(d, sub, SANS, 22, w - 22, 2)
    draw_lines(d, (x + 22, hy + 5), sub, sf, BODY, w - 22, leading=1.25)


CW = 452
panel(M, 552, CW, "WAR AT SEA  •  LIBYA", BLUE,
      "SEA DRONES SINK RUSSIAN WARSHIP",
      "Ukrainian sea drones sink the corvette Merkury at Benghazi; a "
      "cargo ship is ablaze in the Baltic.")
panel(532, 552, CW, "UKRAINE  •  DYMER, KYIV REGION", TEAL,
      "SEARCH IN THE RUBBLE NEAR KYIV",
      "Rescuers comb a collapsed block of flats in Dymer; at least 11 "
      "dead, and the missing are still sought.")
panel(M, 720, CW, "GULF  •  BAHRAIN & SAUDI ARABIA", ORANGE,
      "IRAN STRIKE WOUNDS TWO IN BAHRAIN",
      "The Houthis claim a strike on a Saudi oil refinery as missiles "
      "and drones fly across the Gulf.")
panel(532, 720, CW, "FOOTBALL  •  ANFIELD", GREEN,
      "LIVERPOOL ROUT TEN-MAN UNITED 4–0",
      "A nightmare debut for United boss Pochettino: Yoro was sent off "
      "inside eight minutes at Anfield.")

# ---------------------------------------------------------------- wide panel
WY = 894
d.line([M, WY - 10, RIGHT, WY - 10], fill=INK, width=2)
tag_end = kicker(d, (M, WY), "FOOTBALL  •  FIFA", PURPLE)
wide_head = "UK TO HOST 2035 WOMEN'S WORLD CUP"
wf = fit_one(d, wide_head, SERIF_B, 31, RIGHT - (tag_end + 24))
d.text((tag_end + 24, WY + 1), wide_head, font=wf, fill=INK)
wide_sub = ("FIFA to confirm the sole UK bid on Monday — the first World "
            "Cup in the UK since 1966.")
wsf = fit_one(d, wide_sub, SANS, 22, 944)
d.text((M, WY + 46), wide_sub, font=wsf, fill=BODY)

# ---------------------------------------------------------------- briefs band
BY = 974
d.rectangle([M, BY, RIGHT, 1016], fill=INK)
briefs = (
    "ALSO TODAY — ALCARAZ WINS FIRST ATP FINALS TITLE  •  THITIKUL'S LPGA THREE-PEAT",
    "DEMOCRATS SEAL LARGEST US HOUSE MAJORITY SINCE 1992   (REUTERS • AP • AFP • CNN • BBC)",
)
for i, line in enumerate(briefs):
    bf = fit_one(d, line, SANS_B, 19, 920)
    lw = d.textlength(line, font=bf)
    d.text((M + (944 - lw) / 2, BY + 2 + i * 21), line, font=bf, fill=WHITE)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
