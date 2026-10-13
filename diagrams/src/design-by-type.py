from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('02-design-by-type.png')
cols = [('PART', 330), ('STORED IN', 360), ('REACHES THE AGENT', 380), ('OPTION A', 330), ('OPTION B ADDS', 330)]
W = 80 + sum(w for _, w in cols) + 30
im = Image.new('RGB', (W, 2200), '#f7f9fc'); d = ImageDraw.Draw(im)
reg = '/System/Library/Fonts/Supplemental/Verdana.ttf'; bold = '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n, b=False): return ImageFont.truetype(bold if b else reg, n)
def T(x, y, s, n=22, c='#22344c', b=False, anchor=None): d.text((x, y), s, font=F(n, b), fill=c, anchor=anchor)
def wrap(x, y, s, maxw, n=19, c='#22344c', b=False):
    f = F(n, b); lh = int(n * 1.4); line = ''
    for w in s.split():
        t = (line + ' ' + w).strip()
        if d.textlength(t, font=f) > maxw and line: d.text((x, y), line, font=f, fill=c); y += lh; line = w
        else: line = t
    if line: d.text((x, y), line, font=f, fill=c); y += lh
    return y
dark = '#1b2f4a'; blue = '#3267ab'; green = '#267a53'; orange = '#ad6a1d'; purple = '#7951a6'
T(40, 30, 'THE DESIGN, BY TYPE OF MEMORY', 38, dark, True)
T(42, 86, 'Where each part lives, how it reaches the agent, and what fills it in each option. Option B = Option A plus Mnemosyne.', 19, '#5d6f85')
xs = []; x = 80
for name, w in cols: xs.append(x); x += w
y = 136
d.rounded_rectangle((70, y, W - 20, y + 50), radius=10, fill=dark)
for (name, w), x in zip(cols, xs): T(x + 14, y + 14, name, 17, '#ffffff', True)
y += 62
groups = [
 ('WORKING', blue, '#e7eefb', [
   ('Live context', 'Hermes conversation', 'It is the conversation', 'Hermes', 'Short-term store per agent'),
   ('Handoff note', 'Toodledo task note, owned by the agent on the task', 'Loaded when a task is active', 'Hermes; G-Brain indexes it', 'Scratchpad per agent'),
 ]),
 ('SEMANTIC', green, '#e5f4ea', [
   ('Confirmed facts', 'Obsidian vault, in git', 'Core card at every session start', 'Core card + G-Brain recall', '—'),
   ('Inferred facts', 'G-Brain, tagged "inferred"', 'Recalled, ranked below confirmed', 'G-Brain; Paul confirms weekly', 'Also tagged "inferred"'),
 ]),
 ('EPISODIC', orange, '#fff0de', [
   ('Original chats', 'Hermes chats, Claude Code and Codex logs', 'Searched on demand, cited', 'G-Brain index', '—'),
   ('Distilled decisions', 'G-Brain, linked back to the chat', 'Automatically, before each reply', 'G-Brain pre-reply lookup', 'Faster per-agent recall'),
 ]),
 ('PROCEDURAL', purple, '#f0e9fa', [
   ('Skills', 'Hermes skills, in git', 'Index every session; full skill on use', 'Hermes; G-Brain shares to other tools', '—'),
 ]),
]
for gname, gc, fill, rows in groups:
    gy = y; rh = 128
    for k, cells in enumerate(rows):
        ry = y + k*rh
        d.rounded_rectangle((70, ry + 4, W - 20, ry + rh - 4), radius=14, fill=fill)
        for i, (s, x) in enumerate(zip(cells, xs)):
            if i == 0: wrap(x + 14, ry + 22, s, cols[i][1] - 30, 24, dark, True)
            else: wrap(x + 14, ry + 22, s, cols[i][1] - 30, 19, '#7b8899' if s == '—' else dark)
    gh = rh * len(rows)
    d.rounded_rectangle((20, gy + 4, 62, gy + gh - 4), radius=10, fill=gc)
    gimg = Image.new('RGBA', (gh - 8, 42), (0, 0, 0, 0)); gd = ImageDraw.Draw(gimg)
    gd.text(((gh - 8)//2, 21), gname, font=F(15 if len(rows) > 1 else 11, True), fill='#ffffff', anchor='mm')
    gimg = gimg.rotate(90, expand=True); im.paste(gimg, (20, gy + 4), gimg)
    y += gh + 12
y += 8
d.rounded_rectangle((20, y, W - 20, y + 236), radius=18, fill='#1f344f')
T(55, y + 24, 'RULES THAT HOLD IT TOGETHER', 21, '#9fcbff', True)
rules = [('Who wins', 'Confirmed fact  >  skill  >  original chat  >  recalled summary'),
         ('New facts', 'Engines propose; Paul confirms in a weekly 5-minute review'),
         ('Access', 'Tailscale (private) for our tools; Cloudflare + login, read-only, for cloud apps'),
         ('Swap rule', 'Only the engine is replaceable (Hindsight is the backup); owned files stay')]
ry = y + 66
for k, v in rules:
    T(55, ry, k, 19, '#ffd27a', True); T(250, ry, v, 19, '#ffffff'); ry += 40
im = im.crop((0, 0, W, y + 260)); im.save(out); print(out, im.size)
