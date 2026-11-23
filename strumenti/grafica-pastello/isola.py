import math, asyncio
from playwright.async_api import async_playwright
def leaf(cx,cy,ang,L,wd,fill,stroke='#4f7a3a'):
    a=math.radians(ang); dx,dy=math.cos(a),math.sin(a); px,py=-dy,dx
    ex,ey=cx+dx*L,cy+dy*L+L*0.28   # le foglie ricadono
    c1=(cx+dx*L*.5+px*wd, cy+dy*L*.5+py*wd-L*0.12)
    c2=(cx+dx*L*.5-px*wd, cy+dy*L*.5-py*wd-L*0.12)
    return (f'<path d="M{cx:.1f} {cy:.1f} Q{c1[0]:.1f} {c1[1]:.1f} {ex:.1f} {ey:.1f} Q{c2[0]:.1f} {c2[1]:.1f} {cx:.1f} {cy:.1f}Z" fill="{fill}" stroke="{stroke}" stroke-opacity=".55" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<path d="M{cx:.1f} {cy:.1f} Q{(cx+ex)/2:.1f} {(cy+ey)/2-L*.1:.1f} {ex:.1f} {ey:.1f}" fill="none" stroke="#3f6a30" stroke-opacity=".45" stroke-width="1.6"/>')
def palm(x0,y0,x1,y1,bend,flip):
    cx,cy=x1,y1
    s=f'<path d="M{x0} {y0} Q{x0+bend} {(y0+y1)/2} {x1} {y1}" fill="none" stroke="#a8714a" stroke-width="19" stroke-linecap="round"/>'
    s+=f'<path d="M{x0} {y0} Q{x0+bend} {(y0+y1)/2} {x1} {y1}" fill="none" stroke="#d9a574" stroke-width="7" stroke-linecap="round" stroke-opacity=".6" transform="translate({-4*flip} 0)"/>'
    s+=f'<path d="M{x0} {y0} Q{x0+bend} {(y0+y1)/2} {x1} {y1}" fill="none" stroke="#6f4528" stroke-width="19" stroke-linecap="round" stroke-dasharray="2 13" stroke-opacity=".55"/>'
    angs=[-170,-135,-100,-60,-20,15,165,200,235] if True else []
    cols=['#8ccf72','#74c063','#9bd77a','#6cb85c','#86cb6e']
    for i,a in enumerate([-175,-140,-105,-70,-35,0,140,175,-5]):
        s+=leaf(cx,cy,a,92 if abs(a) in(175,5,0,140) else 84,20,cols[i%5])
    return s
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="440" viewBox="0 0 800 440">
<defs>
<linearGradient id="sand" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbe3a6"/><stop offset="1" stop-color="#eec378"/></linearGradient>
<linearGradient id="volc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d79a6a"/><stop offset=".55" stop-color="#bd7b52"/><stop offset="1" stop-color="#8f5a40"/></linearGradient>
<linearGradient id="wat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ae3e6"/><stop offset="1" stop-color="#5ec1d1"/></linearGradient>
<filter id="w" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="6"/></filter>
<filter id="b"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="tex"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="2" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .35 -.1"/></filter>
</defs>
<g filter="url(#w)">
 <!-- acqua -->
 <ellipse cx="400" cy="352" rx="385" ry="66" fill="#ffffff" fill-opacity=".9"/>
 <ellipse cx="400" cy="350" rx="372" ry="58" fill="url(#wat)" stroke="#3f9db4" stroke-opacity=".5" stroke-width="3"/>
 <path d="M60 352 Q120 336 190 352 M610 352 Q680 336 745 352 M180 385 Q260 372 330 388 M470 388 Q550 372 640 386" fill="none" stroke="#ffffff" stroke-opacity=".85" stroke-width="6" stroke-linecap="round"/>
 <path d="M120 372 Q170 362 230 374 M560 374 Q620 362 690 372" fill="none" stroke="#3f9db4" stroke-opacity=".45" stroke-width="4" stroke-linecap="round"/>
 <!-- isola -->
 <path d="M105 330 Q140 262 255 246 L545 246 Q662 262 697 330 Q600 372 400 374 Q200 372 105 330Z" fill="url(#sand)" stroke="#b98a4a" stroke-opacity=".55" stroke-width="3"/>
 <path d="M150 336 Q250 366 400 368 Q560 366 655 336" fill="none" stroke="#c89a56" stroke-opacity=".5" stroke-width="5" stroke-linecap="round"/>
 <path d="M190 262 Q300 236 400 240 Q520 236 612 262 Q520 282 400 282 Q290 282 190 262Z" fill="#a8d57f" stroke="#5f9446" stroke-opacity=".5" stroke-width="3"/>
 <!-- vulcano -->
 <path d="M262 258 L352 92 Q400 72 448 92 L538 258 Q400 284 262 258Z" fill="url(#volc)" stroke="#6a3f2c" stroke-opacity=".55" stroke-width="3.5" stroke-linejoin="round"/>
 <path d="M352 92 Q400 72 448 92 Q400 112 352 92Z" fill="#7a4631"/>
 <path d="M386 98 Q396 140 378 176 Q372 205 392 230 Q412 200 408 160 Q420 126 414 100Z" fill="#ff9a5c" stroke="#e0703a" stroke-opacity=".6" stroke-width="2"/>
 <path d="M392 104 Q398 140 388 170 Q404 150 406 118Z" fill="#ffd08a"/>
 <path d="M318 170 Q338 160 350 190 M452 150 Q470 170 462 210 M340 220 Q360 205 372 236 M430 226 Q450 214 468 238" fill="none" stroke="#6a3f2c" stroke-opacity=".45" stroke-width="5" stroke-linecap="round"/>
 <!-- fumo -->
 <g fill="#ffffff" fill-opacity=".92" stroke="#b8c7cf" stroke-opacity=".5" stroke-width="2.5">
  <circle cx="404" cy="62" r="19"/><circle cx="426" cy="42" r="24"/><circle cx="452" cy="26" r="21"/><circle cx="472" cy="38" r="14"/>
 </g>
 <!-- cespugli -->
 <g fill="#86bf66" stroke="#4f8a3c" stroke-opacity=".5" stroke-width="2.5">
  <ellipse cx="262" cy="258" rx="40" ry="20"/><ellipse cx="300" cy="262" rx="34" ry="18" fill="#7bb85c"/><ellipse cx="540" cy="260" rx="38" ry="19"/><ellipse cx="500" cy="264" rx="32" ry="17" fill="#7bb85c"/>
 </g>
 <!-- palme -->
 {palm(215,262,170,122,-34,1)}
 {palm(585,262,634,126,34,-1)}
</g>
<rect width="800" height="440" filter="url(#tex)" opacity=".35" style="mix-blend-mode:soft-light"/>
</svg>'''
open('isola.svg','w').write(svg)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':800,'height':440},device_scale_factor=2)
        await pg.set_content('<html><body style="margin:0;background:transparent">'+svg+'</body></html>')
        await pg.wait_for_timeout(400)
        await pg.screenshot(path='/tmp/rp/isola_nuova.png',omit_background=True)
        await b.close()
asyncio.run(main())
