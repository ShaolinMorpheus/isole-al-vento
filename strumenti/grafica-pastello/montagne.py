# Ricolora le montagne di gioco con colori naturali (pietra calda al posto del grigio freddo e della neve), mantenendo luci e ombre del disegno.
import numpy as np, cv2, sys
from PIL import Image
def smooth(x,a,b):
    t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)
STOPS=[(0.00,(52,44,40)),(0.30,(98,84,72)),(0.52,(138,121,103)),(0.70,(168,150,126)),(0.85,(190,174,148))]
def ramp(L):
    xs=[s[0] for s in STOPS]; out=np.zeros(L.shape+(3,),np.float32)
    for c in range(3):
        out[...,c]=np.interp(L,xs,[s[1][c] for s in STOPS])
    return out/255
def recolor(path_in,path_out,moss=True):
    im=np.array(Image.open(path_in).convert('RGBA')).astype(np.float32)/255
    rgb=im[...,:3]; a=im[...,3]
    H,W=a.shape
    mx=rgb.max(-1); mn=rgb.min(-1); sat=(mx-mn)/(mx+1e-6)
    lum=rgb@np.array([.299,.587,.114],np.float32)
    snow=smooth(lum,.78,.90)*(1-smooth(sat,.18,.32))
    blu=np.clip((rgb[...,2]-rgb[...,0]-.02)/.10,0,1)
    snow=np.maximum(snow,smooth(lum,.62,.76)*blu*(1-smooth(sat,.30,.46)))
    snow=cv2.GaussianBlur(snow,(0,0),1.2)
    # roccia: scala la luminanza sul gradiente caldo
    Lr=np.clip((lum-.12)/.78,0,1)*.88
    rock=ramp(Lr)
    # ex neve: calcare chiaro, con le ombre del disegno
    t=np.clip((lum-.58)/.40,0,1)[...,None]
    cap=np.array([132,116,96],np.float32)/255*(1-t)+np.array([198,181,152],np.float32)/255*t
    out=rock*(1-snow[...,None])+cap*snow[...,None]
    if moss: # un po' di muschio verde sulle rocce in basso e nelle zone d'ombra
        yy=(np.arange(H)[:,None]/H)*np.ones((1,W))
        rng=np.random.RandomState(5); n=cv2.GaussianBlur(rng.rand(H,W).astype(np.float32),(0,0),9); n=(n-n.min())/(n.max()-n.min())
        m=smooth(yy,.55,.95)*smooth(n,.45,.75)*(1-snow)*smooth(.75-lum,0,.25)
        m=(m*.55)[...,None]
        gcol=ramp(Lr)*np.array([.62,.92,.45],np.float32)+np.array([.02,.05,.0],np.float32)
        out=out*(1-m)+gcol*m
    res=np.concatenate([np.clip(out,0,1),a[...,None]],-1)
    Image.fromarray((res*255+.5).astype(np.uint8),'RGBA').save(path_out)
if __name__=='__main__':
    src=sys.argv[1] if len(sys.argv)>1 else '/home/claude/repo-isole/www/assets/oggetti'
    dst=sys.argv[2] if len(sys.argv)>2 else '/tmp/rp'
    for n in ('a','b'):
        recolor(f'{src}/montagna_{n}.png',f'{dst}/mont_nat_{n}.png')
    ims=[Image.open(f'{dst}/mont_nat_{n}.png') for n in ('a','b')]
    w=Image.new('RGBA',(sum(i.width for i in ims)+20,300),(80,130,60,255)); x=0
    for i in ims: w.alpha_composite(i,(x,0)); x+=i.width+20
    w.save(f'{dst}/mont_new.png')
