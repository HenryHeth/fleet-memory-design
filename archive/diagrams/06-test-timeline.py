from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('memory-test-timeline.png')
W, H = 2000, 1600
im = Image.new('RGB', (W, H), '#f7f9fc'); d = ImageDraw.Draw(im)
reg = '/System/Library/Fonts/Supplemental/Verdana.ttf'; bold = '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n, b=False): return ImageFont.truetype(bold if b else reg, n)
def T(x, y, s, n=22, c='#22344c', b=False, anchor=None): d.text((x, y), s, font=F(n, b), fill=c, anchor=anchor)
dark = '#1b2f4a'
T(60, 34, 'AUTOMATED MEMORY TEST  ·  WHAT IS CHECKED, AND WHEN', 38, dark, True)
T(62, 90, 'A test harness plants harmless "canary" facts through normal conversation, then probes in fresh sessions.', 21, '#5d6f85')
x0, cw = 560, 284
cols = [('SAME HOUR', '+10 min', '#3267ab'), ('NEXT DAY', 'after nightly jobs', '#1f7f86'),
        ('ONE WEEK', 'after tidy-ups', '#7951a6'), ('ONE MONTH', 'long memory', '#ad6a1d'), ]
for i, (a, b, c) in enumerate(cols):
    x = x0 + i*cw
    d.rounded_rectangle((x+6, 140, x+cw-6, 222), radius=12, fill=c)
    T(x+cw//2, 166, a, 21, '#ffffff', True, 'mm'); T(x+cw//2, 198, b, 16, '#e8eef6', False, 'mm')
rows = [
 ('L1  Core card', 'basic facts, no lookup', '#267a53', ['golden facts', 'card rebuilt OK', 'golden facts', 'full golden set']),
 ('L2  Auto recall', 'arrives before reply', '#7951a6', ['canary recalled', 'canary recalled', 'canary recalled', 'canary recalled']),
 ('L3  Deep search', 'finds + cites source', '#ad6a1d', ['', 'cites exact chat', 'cites exact chat', 'old decision found']),
 ('Capture', 'decision saved as said', '#3267ab', ['decision indexed', 'Claude Code log in', '', '']),
 ('Updates', 'old value disappears', '#1f7f86', ['', 'changed fact', 'no old value', 'no old value']),
 ('Bad facts', 'never promoted', '#b5452f', ['planted claim', 'not in vault', 'not in card', 'not in card']),
 ('Handoff', 'pick up mid-task', '#5a4fb0', ['new session', 'other agent', '', '']),
 ('Skills', 'right skill, unasked', '#7951a6', ['', 'skill loads', 'patch sticks', 'Claude finds it']),
 ('Cross-tool', 'same answer everywhere', '#4f6075', ['', 'Hermes = Claude', 'Hermes = Claude', 'all 6 agents']),
 ('Guardrails', 'access + failure', '#4f6075', ['', '', 'cloud token denied', 'engine down: says so']),
]
y0, rh = 240, 118
for k, (name, sub, c, cells) in enumerate(rows):
    y = y0 + k*rh
    if k % 2 == 0: d.rectangle((40, y, W-40, y+rh), fill='#eef2f7')
    d.rectangle((40, y+14, 52, y+rh-14), fill=c)
    T(72, y+26, name, 24, dark, True); T(72, y+64, sub, 18, '#5a6b80')
    for i, s in enumerate(cells):
        if not s: continue
        x = x0 + i*cw
        d.rounded_rectangle((x+18, y+24, x+cw-18, y+rh-24), radius=14, fill='#ffffff', outline=c, width=3)
        T(x+cw//2, y+rh//2, s, 18, dark, False, 'mm')
fy = y0 + len(rows)*rh + 30
d.rounded_rectangle((40, fy, W-40, fy+150), radius=18, fill='#1f344f')
T(75, fy+22, 'RUNS BY ITSELF', 21, '#9fcbff', True)
T(75, fy+60, 'Nightly: plant + same-hour + next-day checks.  Weekly and monthly: older canaries + full sweep.', 20, '#ffffff')
T(75, fy+98, 'Also after every Hermes or memory update.  Results to the dashboard; alert only when a score drops.', 20, '#d7e3f0')
im = im.crop((0, 0, W, fy+190)); im.save(out); print(out, im.size)
