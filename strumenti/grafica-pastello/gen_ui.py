import numpy as np, cv2
from PIL import Image
SSU=2
def hexc(h): h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)],np.float32)/255
def noise(h,w,s,seed):
    rng=np.random.RandomState(seed); n=rng.rand(h,w).astype(np.float32)
    n=cv2.GaussianBlur(n,(0,0),s); return (n-n.mean())/(n.std()+1e-6)
def sdf(w,h,box,rt,rb):
    x0,y0,x1,y1=[v*SSU for v in box]; rt*=SSU; rb*=SSU
    yy,xx=np.mgrid[0:h*SSU,0:w*SSU].astype(np.float32)
    cx,cy=(x0+x1)/2,(y0+y1)/2; hx,hy=(x1-x0)/2,(y1-y0)/2
    r=np.where(yy<cy,rt,rb)
    qx=np.abs(xx-cx)-(hx-r); qy=np.abs(yy-cy)-(hy-r)
    return np.sqrt(np.maximum(qx,0)**2+np.maximum(qy,0)**2)+np.minimum(np.maximum(qx,qy),0)-r
def paint(w,h,box,r,top,bot,outline,ow=5,hi=0.5,rb=None,shadow=(0,9,7,.28),seed=1,inset=False,rim=None,glow=None,tex=1.0,outline2=None):
    rb=r if rb is None else rb
    H,W=h*SSU,w*SSU
    d=sdf(w,h,box,r,rb)
    body=np.clip(0.5-d,0,1)
    yy=np.mgrid[0:H,0:W][0].astype(np.float32)
    t=np.clip((yy-box[1]*SSU)/((box[3]-box[1])*SSU),0,1)[...,None]
    fill=hexc(top)*(1-t)+hexc(bot)*t
    n1=noise(H,W,22*SSU/2,seed); n2=noise(H,W,5*SSU/2,seed+1); n3=np.random.RandomState(seed+2).randn(H,W).astype(np.float32)
    var=(n1*0.018+n2*0.010+n3*0.004)*tex
    fill=fill*(1+var[...,None])
    if inset:  # campo scavato: ombra interna in alto
        sh=np.exp(np.clip(-d,0,None)/(14*SSU))
        inner=np.exp(-np.clip(-d,0,None)/(12*SSU))
        fill=fill*(1-0.22*inner[...,None]*(1-t))
    # luce morbida in alto
    inside=np.clip(-d,0,None)
    hl=np.exp(-((yy-(box[1]+16)*SSU)/(18*SSU))**2)*np.clip(inside/(6*SSU),0,1)*hi
    fill=fill+(1-fill)*hl[...,None]*0.55
    # bordo interno chiaro in basso (riflesso)
    if rim is not None:
        rm=np.exp(-((d+9*SSU)/(3.5*SSU))**2)*(t[...,0]>0.55)
        fill=fill*(1-0.5*rm[...,None])+hexc(rim)*0.5*rm[...,None]
    # contorno morbido
    ring=np.clip(0.5-(np.abs(d+ow*SSU/2)-ow*SSU/2),0,1)
    oc=hexc(outline)
    if outline2:  # sfumatura contorno alto->basso
        oc=hexc(outline)*(1-t)+hexc(outline2)*t
    rgb=fill*(1-ring[...,None]*0.9)+oc*ring[...,None]*0.9
    A=body
    # alone
    if glow:
        g=cv2.GaussianBlur(np.clip(0.5-(d-4*SSU),0,1).astype(np.float32),(0,0),9*SSU)*0.9
        gc=hexc(glow)
        a2=np.clip(g*(1-A),0,1)
        rgb=np.where(A[...,None]>0, rgb, gc)
        A=np.clip(A+a2,0,1)
    # ombra portata
    dx,dy,bl,st=shadow
    sm=cv2.warpAffine(body.astype(np.float32),np.float32([[1,0,dx*SSU],[0,1,dy*SSU],]),(W,H))
    sm=cv2.GaussianBlur(sm,(0,0),bl*SSU)*st
    sc=np.array([.12,.28,.33],np.float32)
    outA=A+sm*(1-A)
    outRGB=(rgb*A[...,None]+sc*(sm*(1-A))[...,None])/np.maximum(outA[...,None],1e-4)
    img=np.dstack([np.clip(outRGB,0,1),outA])
    img=cv2.resize(img,(w,h),interpolation=cv2.INTER_AREA)
    return Image.fromarray((img*255+.5).astype(np.uint8))
OUT='/tmp/rp/ui/'
import os; os.makedirs(OUT,exist_ok=True)
def save(name,im): im.save(OUT+name)

# --- oro 1020x216 (corpo y 15..190)
box=(6,15,1014,190); r=74
save('menu_bottone_oro_normale.png',paint(1020,216,box,r,'#ffeeb4','#f8cf72','#c98f45',5,0.6,seed=11,outline2='#b9803c',rim='#fff6d4'))
save('menu_bottone_oro_premuto.png',paint(1020,216,(6,24,1014,194),r,'#f8d27a','#efbd5c','#b9803c',5,0.25,seed=12,shadow=(0,4,4,.2),outline2='#a8702f'))
save('menu_bottone_oro_disattivo.png',paint(1020,216,box,r,'#ece4cf','#d9cfb6','#b3a78b',5,0.3,seed=13,shadow=(0,6,5,.15)))
save('menu_bottone_oro_pulsante.png',paint(1020,216,box,r,'#fff3c4','#ffd983','#d89a3e',5,0.7,seed=14,glow='#fff0a8',outline2='#c98f45',rim='#fff6d4'))
# --- vetro 1020x180 (corpo 13..168)
box=(6,13,1014,168); r=62
save('menu_bottone_vetro_normale.png',paint(1020,180,box,r,'#b4ece8','#74cbd4','#3f9bb0',5,0.6,seed=21,outline2='#368aa0',rim='#d6f6f2'))
save('menu_bottone_vetro_premuto.png',paint(1020,180,(6,20,1014,172),r,'#69c2cd','#4fb0be','#2f84998',5,0.2,seed=22,shadow=(0,3,4,.2)) if False else paint(1020,180,(6,20,1014,172),r,'#69c2cd','#4fb0be','#2f8499',5,0.2,seed=22,shadow=(0,3,4,.2)))
save('menu_bottone_vetro_disattivo.png',paint(1020,180,box,r,'#d3e3e4','#b9cfd2','#8fa9ae',5,0.3,seed=23,shadow=(0,5,5,.15)))
# --- difficolta 318x150
box=(5,8,313,142); r=52
save('menu_difficolta_normale.png',paint(318,150,box,r,'#b4ece8','#74cbd4','#3f9bb0',4,0.55,seed=31,shadow=(0,6,5,.26)))
save('menu_difficolta_premuto.png',paint(318,150,(5,14,313,144),r,'#69c2cd','#4fb0be','#2f8499',4,0.2,seed=32,shadow=(0,3,4,.2)))
save('menu_difficolta_selezionato.png',paint(318,150,box,r,'#ffeeb4','#f8cf72','#c98f45',4,0.6,seed=33,shadow=(0,6,5,.26),outline2='#b9803c'))
# --- campo mappa e sezioni 1020x162
save('menu_campo_mappa.png',paint(1020,162,(6,6,1014,152),66,'#2a7f94','#2f8ba0','#236a7d',5,0.0,seed=41,inset=True,shadow=(0,4,3,.14),tex=0.8))
save('menu_sezione.png',paint(1020,162,(6,6,1014,152),66,'#4aa7bb','#3a93a9','#2a7a8f',5,0.35,seed=51,shadow=(0,5,4,.2)))
save('menu_sezione_aperta.png',paint(1020,162,(6,6,1014,156),66,'#4aa7bb','#3a93a9','#2a7a8f',5,0.35,rb=10,seed=52,shadow=(0,2,3,.12)))

# ======== interfaccia in-game (assets/interfaccia) ========
OUT='/tmp/rp/ui2/'; os.makedirs(OUT,exist_ok=True)
def save2(n,im): im.save(OUT+n)
PA=('#4aa7bb','#3790a6','#d9c08c')   # pannello: alto, basso, contorno sabbia
save2('ui_pannello_meteo.png',paint(762,312,(8,8,754,296),44,PA[0],PA[1],PA[2],5,0.3,seed=61,tex=0.7,shadow=(0,5,4,.2)))
save2('ui_pannello_stat.png',paint(354,312,(8,8,346,296),44,PA[0],PA[1],PA[2],5,0.3,seed=62,tex=0.7,shadow=(0,5,4,.2)))
save2('ui_pannello_info.png',paint(1140,234,(8,8,1132,222),44,PA[0],PA[1],PA[2],5,0.3,seed=63,tex=0.7,shadow=(0,5,4,.2)))
save2('ui_pannello_riga.png',paint(1020,192,(8,8,1012,180),44,'#58b2c4','#46a0b5','#d9c08c',5,0.3,seed=64,tex=0.7,shadow=(0,4,3,.18)))
save2('ui_pannello_scheda.png',paint(1200,900,(10,10,1190,884),60,PA[0],PA[1],PA[2],6,0.3,seed=65,tex=0.7,shadow=(0,6,5,.22)))
bx=(4,8,437,112)
save2('ui_bottone_oro_normale.png',paint(441,126,bx,46,'#ffeeb4','#f8cf72','#c98f45',4,0.6,seed=71,outline2='#b9803c',rim='#fff6d4',shadow=(0,5,4,.26)))
save2('ui_bottone_oro_premuto.png',paint(441,126,(4,14,437,116),46,'#f8d27a','#efbd5c','#b9803c',4,0.25,seed=72,shadow=(0,2,3,.2)))
save2('ui_bottone_oro_disattivo.png',paint(441,126,bx,46,'#ece4cf','#d9cfb6','#b3a78b',4,0.3,seed=73,shadow=(0,4,4,.15)))
save2('ui_bottone_oro_pulsante.png',paint(441,126,bx,46,'#fff3c4','#ffd983','#d89a3e',4,0.7,seed=74,glow='#fff0a8',outline2='#c98f45',rim='#fff6d4',shadow=(0,5,4,.26)))
bx=(4,8,323,112)
save2('ui_bottone_chiaro_normale.png',paint(327,126,bx,46,'#b4ece8','#74cbd4','#3f9bb0',4,0.6,seed=81,outline2='#368aa0',rim='#d6f6f2',shadow=(0,5,4,.26)))
save2('ui_bottone_chiaro_premuto.png',paint(327,126,(4,14,323,116),46,'#69c2cd','#4fb0be','#2f8499',4,0.2,seed=82,shadow=(0,2,3,.2)))
save2('ui_bottone_chiaro_disattivo.png',paint(327,126,bx,46,'#d3e3e4','#b9cfd2','#8fa9ae',4,0.3,seed=83,shadow=(0,4,4,.15)))
bz=(6,8,106,104)
save2('ui_zoom_normale.png',paint(114,114,bz,34,'#b4ece8','#74cbd4','#3f9bb0',4,0.6,seed=91,outline2='#368aa0',shadow=(0,4,3,.26)))
save2('ui_zoom_premuto.png',paint(114,114,(6,12,106,108),34,'#69c2cd','#4fb0be','#2f8499',4,0.2,seed=92,shadow=(0,2,3,.2)))
save2('ui_zoom_disattivo.png',paint(114,114,bz,34,'#d3e3e4','#b9cfd2','#8fa9ae',4,0.3,seed=93,shadow=(0,3,3,.15)))
