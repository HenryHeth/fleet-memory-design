from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import sys
P=Path(sys.argv[1] if len(sys.argv)>1 else 'memory-scorecard-v2.png')
W,H=1940,1520
im=Image.new('RGB',(W,H),'#f7f9fc');d=ImageDraw.Draw(im)
reg='/System/Library/Fonts/Supplemental/Verdana.ttf';bold='/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n,b=False):return ImageFont.truetype(bold if b else reg,n)
def T(x,y,s,n=24,c='#22344c',b=False,anchor=None):d.text((x,y),s,font=F(n,b),fill=c,anchor=anchor)
dark='#1b2f4a';blue='#3267ab';green='#267a53';grey='#5b6b7e';red='#b5452f'
T(60,34,'WHICH MEMORY ACTUALLY SHOWS UP WHEN NEEDED?',40,dark,True)
T(62,92,'Scored on results, not features. Bob’s rating from product docs, one independent test and user reports.',21,'#5d6f85')
x0,cw=470,160
groups=[('CONTINUITY  ·  does it show up?',blue,0,4),('TRUST  ·  is it right?',green,4,3),('COST',grey,7,2)]
for name,c,i,n in groups:
    d.rounded_rectangle((x0+i*cw+4,146,x0+(i+n)*cw-4,192),radius=10,fill=c)
    T(x0+i*cw+(n*cw)//2,169,name,18,'#ffffff',True,'mm')
cols=[('Recalls','by itself'),('Saves','by itself'),('Shared by','all agents'),('Works in','other tools'),
      ('Updates','old facts'),('Shows','the source'),('Blocks','bad facts'),('Low','upkeep'),('Outside','evidence')]
for i,(a,b) in enumerate(cols):
    cx=x0+i*cw+cw//2; T(cx,218,a,18,dark,True,'mm'); T(cx,243,b,18,dark,True,'mm')
gc=[blue]*4+[green]*3+[grey]*2
rows=[
 ('Hermes today','Only a tiny note loads by itself',[1,1,0,0,1,1,2,3,None],'#fbe9e5'),
 ('Hindsight','Strong distiller; auto-save can pollute',[3,3,2,2,2,2,1,2,2],None),
 ('Honcho','Top test score; heaviest to run',[3,3,2,2,2,2,1,1,3],'#eef2f7'),
 ('Mem0','Old facts linger beside new ones',[3,3,1,2,1,1,1,2,2],None),
 ('Supermemory','Review queue; memories in its cloud',[3,3,2,3,2,2,2,2,1],'#eef2f7'),
 ('Mnemosyne','Local and simple; least evidence',[2,2,1,2,1,1,2,2,1],None),
 ('G-Brain','Docs only, not yet tested by us',[2,2,3,3,3,3,2,1,1],'#e8f1fb'),
 ('Obsidian','A notebook, not a memory engine',[0,0,1,1,2,2,3,2,None],None),
]
combo=('Proposed stack','Obsidian facts + G-Brain + Hermes skills',[3,3,3,3,3,3,3,2,1])
y0,rh=270,118
def ball(cx,cy,v,c,r=26):
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill='#ffffff',outline='#9aa8b8',width=3)
    if v>=3: d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=c,outline=c,width=3)
    elif v>0: d.pieslice((cx-r,cy-r,cx+r,cy+r),-90,-90+120*v,fill=c,outline=c)
def row(y,name,note,vals,fill=None,outline=None,dash=False):
    if fill: d.rounded_rectangle((40,y,W-40,y+rh-10),radius=16,fill=fill,outline=outline,width=4 if outline else 1)
    T(62,y+22,name,25,dark,True); T(62,y+62,note,16,'#5a6b80')
    for i,v in enumerate(vals):
        cx=x0+i*cw+cw//2; cy=y+(rh-10)//2
        if v is None: T(cx,cy,'n/a',16,'#7b8899',False,'mm')
        else: ball(cx,cy,v,gc[i])
for k,(n,note,v,fill) in enumerate(rows):
    y=y0+k*rh
    if n=='G-Brain': row(y,n,note,v,fill,'#3267ab')
    else: row(y,n,note,v,fill)
# arrow note for Hermes row
yc=y0+len(rows)*rh+22
row(yc,*combo,fill='#fff8e6',outline='#d39a2a')
T(62,yc+84,'target, not yet measured',15,'#9a6a12',True)
ly=yc+rh+28
for i,(v,lab) in enumerate([(0,'none'),(1,'limited'),(2,'good'),(3,'strong')]):
    ball(80+i*180,ly+20,v,'#5c6f86',18); T(108+i*180,ly+8,lab,19,'#40536a')
T(830,ly+8,'Hermes today scores lowest on continuity — the part you feel.',19,red,True)
T(62,ly+62,'Every engine tested sometimes repeated planted false claims. Keep the original conversation; only confirmed facts become authoritative.',18,'#40536a')
im.save(P);print(P,im.size)
