import numpy as np, cv2, subprocess
from PIL import Image
subprocess.run('cd /home/claude/repo-isole && git show 84b20a8:www/assets/menu/sfondo_menu.webp > /tmp/rp/bg_orig.webp',shell=True)
im=np.array(Image.open('/tmp/rp/bg_orig.webp').convert('RGB'))
H,W=im.shape[:2]
hsv=cv2.cvtColor(im,cv2.COLOR_RGB2HSV).astype(np.float32); S=hsv[...,1]/255; V=hsv[...,2]/255
def sm(x,a,b): t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)
w=sm(V,0.60,0.80)*(1-sm(S,0.14,0.30))
w=cv2.GaussianBlur(w,(0,0),2)
# regione montagne (alto) e angoli alti
yy=np.mgrid[0:H,0:W][0].astype(np.float32)/H
mount=1-sm(yy,0.15,0.22)
rock=np.array([172,164,148],np.float32)/255   # roccia calda
ground=np.array([178,210,130],np.float32)/255 # prato
tgt=rock*mount[...,None]+ground*(1-mount[...,None])
lum=np.clip(V/0.88,0.72,1.2)[...,None]
nat=np.clip(tgt*lum,0,1)
f=im.astype(np.float32)/255
out=f*(1-w[...,None])+nat*w[...,None]
# schiarisci leggermente il tutto (pastello) senza sbiancare
out=1-(1-out)*(1-0.06)
Image.fromarray((np.clip(out,0,1)*255+.5).astype(np.uint8)).save('/tmp/rp/bg_nat.png')
Image.fromarray((np.clip(out,0,1)*255+.5).astype(np.uint8)).resize((412,880)).save('/tmp/rp/bg_nat_s.png')
