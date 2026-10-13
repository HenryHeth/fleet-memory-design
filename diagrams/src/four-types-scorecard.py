from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('memory-four-types-scorecard.png')
x0, cw = 470, 136
W = x0 + 13 * cw + 50
H = 1600
im = Image.new('RGB', (W, H), '#f7f9fc'); d = ImageDraw.Draw(im)
reg = '/System/Library/Fonts/Supplemental/Verdana.ttf'; bold = '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n, b=False): return ImageFont.truetype(bold if b else reg, n)
def T(x, y, s, n=24, c='#22344c', b=False, anchor=None): d.text((x, y), s, font=F(n, b), fill=c, anchor=anchor)
blue = '#3267ab'; green = '#267a53'; orange = '#ad6a1d'; purple = '#7951a6'; grey = '#4f6075'; dark = '#1b2f4a'; red = '#9a3b1d'
T(40, 30, 'FOUR TYPES OF MEMORY  ·  WHO COVERS WHAT', 40, dark, True)
T(42, 88, 'Columns = the four memory types (CoALA) split into parts, plus the requirements added later. Rows = tools, then the two designs we are vetting.', 19, '#5d6f85')
T(42, 116, "Bob's rating from vendor docs, one independent Hermes test and user reports. Option rows are targets, not measurements.", 19, '#5d6f85')
groups = [('WORKING', blue, 0, 2), ('SEMANTIC', green, 2, 2), ('EPISODIC', orange, 4, 2), ('PROCEDURAL', purple, 6, 1), ('REQUIREMENTS', grey, 7, 6)]
for name, c, i, n in groups:
    d.rounded_rectangle((x0 + i*cw + 4, 160, x0 + (i+n)*cw - 4, 204), radius=10, fill=c)
    T(x0 + i*cw + (n*cw)//2, 182, name, 18 if n > 1 else 13, '#ffffff', True, 'mm')
cols = [('Live', 'context'), ('Handoff', 'note'), ('Confirmed', 'facts'), ('Inferred', 'facts'), ('Original', 'chats'), ('Distilled', 'decisions'),
        ('Skills', ''), ('Shows up', 'unasked'), ('Shared by', 'all agents'), ('Other', 'tools'), ('Blocks', 'bad facts'), ('Low', 'upkeep'), ('Outside', 'evidence')]
for i, (a, b) in enumerate(cols):
    cx = x0 + i*cw + cw//2; T(cx, 228, a, 17, dark, True, 'mm'); T(cx, 252, b, 17, dark, True, 'mm')
gc = [blue, blue, green, green, orange, orange, purple] + [grey]*6
N = None
rows = [
 ('Hermes (today)', 'Strong live context; tiny per-agent facts', [3,1,1,1,2,0,3, 1,0,0,2,3,N], '#fbe9e5'),
 ('Hindsight', 'Best distiller; auto-save can pollute', [1,0,1,3,1,3,0, 3,2,2,1,2,2], None),
 ('Honcho', 'Best conversation record; heaviest', [2,1,1,3,3,2,0, 3,2,2,1,1,3], '#eef2f7'),
 ('Mem0', 'Preferences; old facts linger', [1,0,1,2,0,1,0, 3,1,2,1,2,2], None),
 ('Supermemory', 'Review queue for guesses; cloud MCP', [1,0,2,2,2,1,0, 3,2,3,2,2,1], '#eef2f7'),
 ('Mnemosyne', 'Fast local working memory; least evidence', [2,1,1,1,1,2,0, 2,1,2,2,2,1], None),
 ('G-Brain', 'Sourced, correctable, shared; docs only', [1,1,3,2,2,2,2, 2,3,3,2,1,1], '#e8f1fb'),
 ('Obsidian', 'Human-edited notebook; recalls nothing', [0,1,3,0,1,0,1, 0,1,1,3,2,N], None),
]
opts = [
 ('Option A', 'Obsidian + G-Brain + Hermes', [3,2,3,2,3,2,3, 3,3,3,3,1,1]),
 ('Option B', 'Option A + Mnemosyne per agent', [3,2,3,2,3,3,3, 3,3,3,2,1,1]),
]
def ball(cx, cy, v, c, r=25):
    d.ellipse((cx-r, cy-r, cx+r, cy+r), fill='#ffffff', outline='#9aa8b8', width=3)
    if v >= 3: d.ellipse((cx-r, cy-r, cx+r, cy+r), fill=c, outline=c, width=3)
    elif v > 0: d.pieslice((cx-r, cy-r, cx+r, cy+r), -90, -90 + 120*v, fill=c, outline=c)
rh = 100
def row(y, name, note, vals, fill=None, outline=None):
    if fill: d.rounded_rectangle((20, y, W-20, y+rh-8), radius=16, fill=fill, outline=outline, width=4 if outline else 1)
    T(40, y+20, name, 24, dark, True); T(40, y+58, note, 15, '#5a6b80')
    for i, v in enumerate(vals):
        cx = x0 + i*cw + cw//2; cy = y + (rh-8)//2
        if v is None: T(cx, cy, 'n/a', 15, '#7b8899', False, 'mm')
        else: ball(cx, cy, v, gc[i])
y = 280
for name, note, vals, fill in rows:
    row(y, name, note, vals, fill, '#3267ab' if name == 'G-Brain' else None); y += rh
y += 14
T(40, y, 'DESIGNS WE ARE VETTING  (targets, not measured yet)', 18, '#9a6a12', True); y += 34
for name, note, vals in opts:
    row(y, name, note, vals, '#fff8e6', '#d39a2a'); y += rh + 6
y += 16
for i, (v, lab) in enumerate([(0, 'none'), (1, 'limited'), (2, 'good'), (3, 'strong')]):
    ball(60 + i*170, y+20, v, '#5c6f86', 17); T(88 + i*170, y+8, lab, 18, '#40536a')
T(780, y+8, 'No single tool fills its row. Hermes today fails "shared" and "shows up unasked", the gap users feel.', 18, red, True)
y += 50
T(40, y, 'Why each score: docs/02-scorecard-evidence.md', 17, '#40536a')
im = im.crop((0, 0, W, y + 50)); im.save(out); print(out, im.size)
