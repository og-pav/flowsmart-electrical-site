#!/usr/bin/env python3
"""Generate og-share.png (1200x630) and apple-touch-icon.png with PIL."""
from PIL import Image, ImageDraw, ImageFont

INK = (16, 22, 15)
INK2 = (27, 36, 26)
VOLT = (134, 192, 73)
SPARK = (183, 227, 110)
PAPER = (231, 237, 227)
MIST = (174, 185, 168)

def font(size, bold=True):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")
    return ImageFont.truetype(path, size)

# ------------------------------------------------------------- og image ---
W, H = 1200, 630
img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# soft radial glow top-right (manual radial gradient)
glow = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(glow)
cx, cy, maxr = 950, 60, 640
for r in range(maxr, 0, -4):
    a = int(46 * (1 - r / maxr))
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=a)
img = Image.composite(Image.new("RGB", (W, H), (52, 74, 32)), img, glow)
d = ImageDraw.Draw(img)

# faint grid
for x in range(0, W, 72):
    d.line([(x, 0), (x, H)], fill=(24, 32, 23), width=1)
for y in range(0, H, 72):
    d.line([(0, y), (W, y)], fill=(24, 32, 23), width=1)

# bolt mark
bolt = [(150, 96), (96, 190), (128, 190), (124, 240), (182, 140), (148, 140), (152, 96)]
d.polygon(bolt, fill=VOLT)

# wordmark
d.text((210, 118), "flowsmart", font=font(64), fill=PAPER)
wm_w = d.textlength("flowsmart", font=font(64))
d.text((210 + wm_w + 18, 118), "electrical", font=font(64), fill=VOLT)

# headline
d.text((96, 300), "Power done properly.", font=font(76), fill=PAPER)
d.text((96, 392), "Answered the first time.", font=font(76), fill=VOLT)

# footer strip
d.line([(96, 508), (1104, 508)], fill=(52, 62, 50), width=2)
d.text((96, 532), "Electricians · Melbourne's West  ·  REC 20672  ·  0433 348 403",
       font=font(30, bold=False), fill=MIST)
img.save("assets/img/og-share.png", optimize=True)

# ---------------------------------------------------- apple touch icon ---
S = 180
icon = Image.new("RGB", (S, S), INK)
di = ImageDraw.Draw(icon)
b = [(103, 22), (42, 107), (79, 107), (74, 158), (140, 73), (101, 73), (106, 22)]
di.polygon(b, fill=VOLT)
icon.save("assets/img/apple-touch-icon.png", optimize=True)
print("assets written")
