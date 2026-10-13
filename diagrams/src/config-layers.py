from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
import sys
P=Path(sys.argv[1] if len(sys.argv)>1 else 'memory-config-layers.png')
W,H=1900,2120
im=Image.new('RGB',(W,H),'#f7f9fc');d=ImageDraw.Draw(im)
reg='/System/Library/Fonts/Supplemental/Verdana.ttf';bold='/System/Library/Fonts/Supplemental/Verdana Bold.ttf'
def F(n,b=False):return ImageFont.truetype(bold if b else reg,n)
def T(x,y,s,n=22,c='#22344c',b=False,anchor=None):d.text((x,y),s,font=F(n,b),fill=c,anchor=anchor)
def wrap(x,y,s,maxw,n=20,c='#33465c',b=False,lh=None):
    f=F(n,b);lh=lh or int(n*1.45);line=''
    for w in s.split():
        t=(line+' '+w).strip()
        if d.textlength(t,font=f)>maxw and line:
            d.text((x,y),line,font=f,fill=c);y+=lh;line=w
        else: line=t
    if line: d.text((x,y),line,font=f,fill=c);y+=lh
    return y
def B(box,fill,stroke=None,r=20,w=3):d.rounded_rectangle(box,radius=r,fill=fill,outline=stroke,width=w)
def A(pts,c,w=6):
    d.line(pts,fill=c,width=w); p,q=pts[-2:]
    a=math.atan2(q[1]-p[1],q[0]-p[0]);L=20
    d.polygon([q,(q[0]-L*math.cos(a-.5),q[1]-L*math.sin(a-.5)),(q[0]-L*math.cos(a+.5),q[1]-L*math.sin(a+.5))],fill=c)
dark='#1b2f4a'
T(60,34,'RECOMMENDED MEMORY STACK  ·  CONFIG LAYERS',40,dark,True)
T(62,92,'Design for the pilot. G-Brain details come from its docs; nothing installed or tested yet.',21,'#5d6f85')
# column headers
LX,LW=60,430; CX,CW=520,640; RX,RW=1190,560
for x,s in [(LX+24,'LAYER'),(CX+10,'CONFIGURATION'),(RX+10,'RECOMMENDATION')]:
    T(x,150,s,18,'#6a7a8e',True)
layers=[
 ('1','WHO CONNECTS','Clients','#3267ab','#e7eefb',
  ['Hermes: 6 agents (Bob + Henry first)','Claude Code, Codex','Cloud apps: Sesame, Grok bot, Muse'],
  'Start with Bob, Henry and Claude Code. Add cloud apps last, read-only.'),
 ('2','HOW THEY REACH IT','Network + login','#1f7f86','#e3f3f3',
  ['Tailscale Serve: private, full access','Cloudflare Tunnel + Access: public, with login','One scoped token per agent'],
  'Do not use Tailscale Funnel for personal facts: it has no login.'),
 ('3','FRONT DOOR','G-Brain MCP server','#5a4fb0','#ecebfa',
  ['One HTTP MCP endpoint on Homebase','Sensitive facts tagged private','Cloud apps: read-only scope'],
  'Facts and recall share one door, so every tool gets the same answer.'),
 ('4','RECALL ENGINE','G-Brain index','#7951a6','#f0e9fa',
  ['Start: keyword search, no AI keys','Then: local embeddings (Ollama)','Later: synthesis, overnight tidy-up'],
  'Turn features on one at a time, only after the 20-question test passes.'),
 ('5','CAPTURE','As-you-go indexing','#ad6a1d','#fff0de',
  ['Pull out decisions + facts each turn','Each one links to the exact chat','Claude Code / Codex logs: nightly'],
  'Signposts only. Never replace the original conversation.'),
 ('6','SOURCES OF TRUTH','Owned files','#267a53','#e5f4ea',
  ['Obsidian vault: confirmed facts','Hermes skills: how-to','Hermes chats + Toodledo: evidence'],
  'Plain files in git, backed up nightly to the NAS. Survive any engine swap.'),
]
y=190;lh=262
tops=[]
for n,cap,name,c,fill,cfg,rec in layers:
    B((LX,y,W-60,y+lh-22),fill,c)
    d.ellipse((LX+22,y+28,LX+92,y+98),fill=c); T(LX+57,y+63,n,34,'#ffffff',True,'mm')
    T(LX+112,y+30,cap,18,c,True)
    wrap(LX+112,y+62,name,LW-130,26,dark,True,34)
    yy=y+34
    for s in cfg:
        d.ellipse((CX+12,yy+8,CX+24,yy+20),fill=c); yy=wrap(CX+36,yy,s,CW-60,21,'#22344c')+12
    B((RX,y+22,RX+RW,y+lh-44),'#ffffff',c,16,2)
    T(RX+20,y+38,'DO THIS',16,c,True)
    wrap(RX+20,y+66,rec,RW-40,21,dark,False,30)
    tops.append(y);y+=lh
# authority bar on far right
ax=W-34
# flows: captured -> engine, truth -> engine (left margin arrows)
# ops band
oy=y+10
B((60,oy,W-60,oy+300),'#1f344f',None)
T(95,oy+26,'RULES THAT KEEP IT TRUSTWORTHY',24,'#9fcbff',True)
rules=[('Who wins','Confirmed fact  >  skill  >  original chat  >  recalled summary'),
       ('New facts','Engine proposes; Paul confirms in a weekly 5-minute review'),
       ('Checks','20-question test monthly, from Hermes and Claude Code; alert only on a drop'),
       ('Swap rule','Only layers 3–4 are replaceable (Hindsight is the backup engine)')]
ry=oy+78
for k,v in rules:
    T(95,ry,k,21,'#ffd27a',True); T(330,ry,v,21,'#ffffff'); ry+=50
im.save(P);print(P,im.size,'bottom',oy+300)
