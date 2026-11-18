import html, sys
C='../images/canva/cutout/'; K='../images/canva/class/'
def img(src,h,rot=0,flip=False): return ('img',src,h,rot,flip)
def t(s,size=30,rot=0): return ('t',s,size,rot)
def tip(name,q,line,flavor,rot=0): return ('tip',name,q,line,flavor,rot)
def chat(ch,who,msg,rot=0): return ('chat',ch,who,msg,rot)
Q={'p':'#a335ee','b':'#0070dd','o':'#ff8000','g':'#1eff00','w':'#ffffff','gr':'#9d9d9d'}
CH={'1':'#ffc0c0','2':'#ffc0c0','w':'#ff80ff','g':'#40ff40','s':'#ffffff','y':'#ff4040','r':'#ff7f00'}
def render(it):
  k=it[0]
  if k=='img':
    _,src,h,rot,flip=it
    tf=f"rotate({rot}deg)"+(" scaleX(-1)" if flip else "")
    return f'<img class="cut" src="{src}" style="height:{h}px;transform:{tf}">'
  if k=='t':
    _,s,size,rot=it
    return f'<div class="t" style="font-size:{size}px;transform:rotate({rot}deg)">{s}</div>'
  if k=='tip':
    _,name,q,line,flavor,rot=it
    return (f'<div class="tip" style="transform:rotate({rot}deg)"><b style="color:{Q[q]}">{name}</b>'
            f'<span class="w">{line}</span><i>"{flavor}"</i></div>')
  if k=='chat':
    _,ch,who,msg,rot=it
    col=CH[ch[0]]; lab={'1':'[1. General] ','2':'[2. Trade] ','w':'','g':'[Guild] ','s':'','y':'','r':'[Raid] '}[ch[0]]
    pre = f'[{who}] whispers: ' if ch[0]=='w' else (f'[{who}] yells: ' if ch[0]=='y' else f'{lab}[{who}]: ')
    return f'<div class="chat" style="color:{col};transform:rotate({rot}deg)">{pre}{msg}</div>'
CSS='''
@font-face{font-family:Goodmountain;src:url(../brand/Goodmountain-Regular.woff2)}
body{margin:0;background:#888}
section{position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff;font-family:Inter,sans-serif;color:#000;margin-bottom:20px}
h1{position:absolute;top:50px;left:0;right:0;text-align:center;margin:0;font:900 104px/1 Inter;letter-spacing:-3px}
.pill{position:absolute;top:24px;right:24px;background:#7a7a7a;color:#fff;font:500 26px Inter;padding:8px 18px;border-radius:40px}
.cols{position:absolute;top:176px;left:0;right:0;bottom:64px;display:grid;grid-template-columns:1fr 1fr}
.cols:after{content:"";position:absolute;left:538px;top:20px;bottom:10px;width:5px;background:#000}
.col{position:relative;display:flex;flex-direction:column;padding:0 18px}
.col h2{margin:0 0 10px;text-align:center;font:900 64px/1.05 Inter;letter-spacing:-1.5px}
.bag{flex:1;display:flex;flex-wrap:wrap;align-content:space-evenly;justify-content:space-evenly;align-items:center;gap:6px 10px}
.t{font-weight:700;line-height:1.08;text-align:center;max-width:250px;letter-spacing:-.3px}
.cut{display:block;filter:drop-shadow(0 6px 8px rgba(0,0,0,.25))}
.tip{width:236px;background:linear-gradient(#0d1430f2,#050817f2);border:3px solid #b9b9c4;border-radius:9px;padding:10px 13px 12px;font:500 19px/1.25 Inter;color:#fff;box-shadow:0 6px 14px rgba(0,0,0,.35);text-align:left}
.tip b{display:block;font-size:23px;font-weight:700;margin-bottom:3px}
.tip .w{display:block;color:#fff}
.tip i{display:block;color:#ffd100;font-style:normal;margin-top:4px}
.chat{background:rgba(0,0,0,.82);padding:8px 13px;border-radius:6px;font:600 19px/1.3 Inter;max-width:470px;text-shadow:1px 1px 0 #000}
.handle{position:absolute;bottom:18px;left:0;right:0;text-align:center;font:600 26px Inter;color:#555}
.me .cols:after{display:none}
'''
def slide(n,total,title,L,R,lh,rh):
  return (f'<section><h1>{title}</h1><div class="pill">{n}/{total}</div><div class="cols">'
    f'<div class="col"><h2>{lh}</h2><div class="bag">{"".join(map(render,L))}</div></div>'
    f'<div class="col"><h2>{rh}</h2><div class="bag">{"".join(map(render,R))}</div></div>'
    f'</div><div class="handle">@wowforeverguide</div></section>')
exec(open(sys.argv[1]).read())
