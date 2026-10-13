from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math, sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('memory-recall-levels.png')
W, H = 1900, 2200
im = Image.new('RGB', (W, H), '#f7f9fc'); d = ImageDraw.Draw(im)
reg = '/System/Library/Fonts/Supplemental/Verdana.ttf'; bold = '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n, b=False): return ImageFont.truetype(bold if b else reg, n)
def T(x, y, s, n=22, c='#22344c', b=False, anchor=None): d.text((x, y), s, font=F(n, b), fill=c, anchor=anchor)
def wrap(x, y, s, maxw, n=20, c='#33465c', b=False, lh=None):
    f = F(n, b); lh = lh or int(n * 1.45); line = ''
    for w in s.split():
        t = (line + ' ' + w).strip()
        if d.textlength(t, font=f) > maxw and line:
            d.text((x, y), line, font=f, fill=c); y += lh; line = w
        else: line = t
    if line: d.text((x, y), line, font=f, fill=c); y += lh
    return y
def B(box, fill, stroke=None, r=20, w=3): d.rounded_rectangle(box, radius=r, fill=fill, outline=stroke, width=w)
def A(p, q, c, w=6):
    d.line([p, q], fill=c, width=w); a = math.atan2(q[1]-p[1], q[0]-p[0]); L = 20
    d.polygon([q, (q[0]-L*math.cos(a-.5), q[1]-L*math.sin(a-.5)), (q[0]-L*math.cos(a+.5), q[1]-L*math.sin(a+.5))], fill=c)
dark = '#1b2f4a'; blue = '#3267ab'; green = '#267a53'; purple = '#7951a6'; orange = '#ad6a1d'; teal = '#1f7f86'
T(60, 34, 'THREE LEVELS OF RECALL  ·  TWO OPTIONS TO VET', 40, dark, True)
T(62, 92, 'Goal: agents already know the basics. Nobody should have to say "go look it up."', 22, '#5d6f85')
# agent bar
B((60, 150, W-60, 250), '#e7eefb', blue)
T(95, 172, 'EVERY NEW REPLY', 20, blue, True)
T(95, 206, 'Hermes agents · Claude Code · Codex  (cloud apps: read-only)', 22, dark)
levels = [
 ('1', 'ALWAYS KNOWN', 'Core card', green, '#e5f4ea',
  'Loaded at the start of every conversation. No search, no AI step, so it cannot be missed.',
  'Address, family, standing rules, active projects. Built nightly from the Obsidian vault.'),
 ('2', 'RECALLED AUTOMATICALLY', 'Before every reply', purple, '#f0e9fa',
  'The memory engine is queried by the system before the model answers, not when the agent remembers to look.',
  'Recent decisions, related past conversations, people and projects mentioned.'),
 ('3', 'SEARCHED ON DEMAND', 'Deep lookup', orange, '#fff0de',
  'The agent calls a search tool for older or detailed history, with links to the exact conversation.',
  '"What did we decide about the boat battery in August?"'),
]
y = 300; lh = 250
for n, cap, name, c, fill, how, ex in levels:
    B((60, y, W-60, y+lh-30), fill, c)
    d.ellipse((90, y+30, 170, y+110), fill=c); T(130, y+70, n, 40, '#ffffff', True, 'mm')
    T(200, y+28, cap, 20, c, True); T(200, y+62, name, 30, dark, True)
    wrap(200, y+112, how, 760, 20, '#33465c')
    B((1010, y+24, W-90, y+lh-54), '#ffffff', c, 14, 2)
    T(1032, y+38, 'EXAMPLE', 16, c, True)
    wrap(1032, y+66, ex, W-90-1032-30, 20, dark)
    y += lh
# source of truth band
B((60, y, W-60, y+170), '#1f5a3d', None)
T(95, y+22, 'SOURCE OF TRUTH  ·  OBSIDIAN VAULT', 22, '#b9f0cf', True)
wrap(95, y+62, 'Confirmed facts in plain Markdown, edited by people, kept in git. Feeds the level 1 core card nightly and is indexed by G-Brain for levels 2 and 3. Engines may propose facts; only a confirmed edit lands here.', W-220, 21, '#ffffff', False, 31)
for x in (500, 950, 1400):
    A((x, y-22), (x, y-4), '#1f5a3d', 5)
y += 190
# options
oy = y + 20
T(60, oy, 'WHO FILLS LEVEL 2?  VET BOTH IN THE PILOT', 28, dark, True)
cw = (W-60*2-40)//2
opts = [
 ('OPTION A', 'G-Brain only', teal,
  ['One shared index of Obsidian + chats for all', 'G-Brain plugs into the Hermes pre-reply hook', 'Fewer moving parts, nothing can disagree'],
  'Risk: G-Brain\'s Hermes hookup is unverified; may need a small plugin.'),
 ('OPTION B', 'Mnemosyne + G-Brain', purple,
  ['Mnemosyne: fast local recall per agent', 'G-Brain: indexes Obsidian + deep search', 'Mnemosyne ranks below confirmed facts'],
  'Risk: two memories can disagree; weakest published evidence.'),
]
for i, (tag, name, c, pts, risk) in enumerate(opts):
    x = 60 + i*(cw+40); yy = oy + 60
    B((x, yy, x+cw, yy+420), '#ffffff', c, 20, 4)
    T(x+30, yy+24, tag, 20, c, True); T(x+30, yy+58, name, 30, dark, True)
    py = yy + 124
    for s in pts:
        d.ellipse((x+32, py+8, x+46, py+22), fill=c); py = wrap(x+62, py, s, cw-100, 21, dark) + 12
    B((x+24, yy+300, x+cw-24, yy+396), '#fbeee9', None, 12)
    wrap(x+44, yy+316, risk, cw-90, 19, '#7a3b1d')
fy = oy + 510
B((60, fy, W-60, fy+190), '#1f344f', None)
T(95, fy+24, 'PASS / FAIL TEST (same for both options)', 22, '#9fcbff', True)
wrap(95, fy+66, 'Same automated suite for both options: every level, tested minutes, a day, a week and a month after a fact is planted. Any "let me check" on a basic fact is a fail. See docs/07-test-methodology.md.', W-220, 21, '#ffffff', False, 32)
im = im.crop((0, 0, W, fy+230))
im.save(out); print(out, im.size)
