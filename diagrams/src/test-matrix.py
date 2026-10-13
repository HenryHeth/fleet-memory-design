from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys
out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('03-test-matrix.png')
x0, cw = 560, 290
W = x0 + 5 * cw + 40
im = Image.new('RGB', (W, 2400), '#f7f9fc'); d = ImageDraw.Draw(im)
reg = '/System/Library/Fonts/Supplemental/Verdana.ttf'; bold = '/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n, b=False): return ImageFont.truetype(bold if b else reg, n)
def T(x, y, s, n=22, c='#22344c', b=False, anchor=None): d.text((x, y), s, font=F(n, b), fill=c, anchor=anchor)
dark = '#1b2f4a'; blue = '#3267ab'; green = '#267a53'; orange = '#ad6a1d'; purple = '#7951a6'; grey = '#4f6075'
T(40, 30, 'TESTING EACH TYPE OF MEMORY, OVER TIME', 38, dark, True)
T(42, 86, 'Automated. Probes run in fresh sessions with no hint to look anything up. Short term on the left, medium term on the right.', 19, '#5d6f85')
cols = [('SAME SESSION', 'minutes'), ('NEW SESSION', '+10 minutes'), ('NEXT DAY', 'after nightly jobs'), ('ONE WEEK', 'after tidy-ups'), ('ONE MONTH', 'long memory')]
d.rounded_rectangle((x0 + 4, 130, x0 + 2*cw - 4, 160), radius=8, fill='#dbe6f5'); T(x0 + cw, 145, 'SHORT TERM', 16, blue, True, 'mm')
d.rounded_rectangle((x0 + 2*cw + 4, 130, x0 + 5*cw - 4, 160), radius=8, fill='#efe3d3'); T(x0 + 3.5*cw, 145, 'MEDIUM TERM', 16, orange, True, 'mm')
for i, (a, b) in enumerate(cols):
    x = x0 + i*cw
    d.rounded_rectangle((x + 6, 168, x + cw - 6, 238), radius=12, fill=dark)
    T(x + cw//2, 192, a, 19, '#ffffff', True, 'mm'); T(x + cw//2, 220, b, 15, '#cfd9e6', False, 'mm')
groups = [
 ('WORKING', blue, [
   ('Live context', 'held within a chat', ['survives compression', '', '', '', '']),
   ('Handoff note', 'resume a task', ['', 'new session resumes', 'other agent resumes', '', '']),
 ]),
 ('SEMANTIC', green, [
   ('Confirmed facts', 'known, no lookup', ['', 'golden facts', 'edit flows to card', 'old value gone', 'full golden set']),
   ('Inferred facts', 'never promoted', ['hinted canary', 'flagged as inferred', 'not in vault/card', 'confirmed wins', 'still not promoted']),
 ]),
 ('EPISODIC', orange, [
   ('Original chats', 'found + cited', ['', '', 'exact quote + link', 'exact quote + link', '"last August" query']),
   ('Distilled decisions', 'recalled unasked', ['decision captured', 'recalled unasked', 'recalled unasked', 'date question', 'recalled unasked']),
 ]),
 ('PROCEDURAL', purple, [
   ('Skills', 'right skill, unasked', ['', 'right skill loads', 'patch sticks', 'Claude finds it', '']),
 ]),
 ('ACROSS ALL', grey, [
   ('Shared', 'told one, ask another', ['', 'tell Bob, ask Henry', 'tell Bob, ask Henry', '', 'all six agents']),
   ('Other tools', 'same answer anywhere', ['', '', 'Claude = Hermes', 'Claude = Hermes', 'cloud token denied']),
   ('Failure', 'admits, never guesses', ['', '', '', '', 'engine off: says so']),
   ('Real chats', 'should-have-known', ['', '', 'nightly scan', 'rate by type', 'trend']),
 ]),
]
rh = 104; y = 254
for gname, gc, rows in groups:
    gh = rh * len(rows)
    d.rounded_rectangle((20, y + 4, 62, y + gh - 4), radius=10, fill=gc)
    gimg = Image.new('RGBA', (gh - 8, 42), (0, 0, 0, 0)); gd = ImageDraw.Draw(gimg)
    gd.text(((gh - 8)//2, 21), gname, font=F(15 if len(rows) > 1 else 12, True), fill='#ffffff', anchor='mm')
    gimg = gimg.rotate(90, expand=True); im.paste(gimg, (20, y + 4), gimg)
    for k, (name, sub, cells) in enumerate(rows):
        ry = y + k*rh
        if k % 2 == 0: d.rectangle((70, ry, W - 20, ry + rh), fill='#eef2f7')
        T(88, ry + 24, name, 23, dark, True); T(88, ry + 60, sub, 17, '#5a6b80')
        for i, s in enumerate(cells):
            if not s: continue
            x = x0 + i*cw
            d.rounded_rectangle((x + 14, ry + 22, x + cw - 14, ry + rh - 22), radius=14, fill='#ffffff', outline=gc, width=3)
            T(x + cw//2, ry + rh//2, s, 17, dark, False, 'mm')
    y += gh + 14
d.rounded_rectangle((20, y + 6, W - 20, y + 150), radius=18, fill='#1f344f')
T(55, y + 26, 'SCORES FEED THE SCORECARD', 21, '#9fcbff', True)
T(55, y + 64, 'Each row becomes a measured circle on the four-types scorecard, replacing our judgement ratings.', 20, '#ffffff')
T(55, y + 100, 'Nightly, weekly and monthly runs, plus after every update. Alert only when a score drops.', 19, '#d7e3f0')
im = im.crop((0, 0, W, y + 180)); im.save(out); print(out, im.size)
