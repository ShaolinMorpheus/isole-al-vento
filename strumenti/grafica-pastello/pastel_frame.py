import rope, build, numpy as np
from build import *
rope.ROPE.update(mid=(236,212,164), light=(250,236,198), dark=(208,178,128), groove=(150,114,76))
rope.WOOD.update(mid=(205,158,108), light=(232,196,148), dark=(160,116,74), edge=(120,86,56))
rope.SHK = 0.5
rope.SHC = (0.10, 0.20, 0.24)
build.INT_BASE = (58, 150, 170)
build.INT_VIG = 0.10
rng = np.random.RandomState(9)
specs = [dict(ref=c, turns=3.0, pitch=88, d=27, seed=20 + i, kind='corner', phase=0.35 * (i % 2)) for i, c in enumerate(corner_pts(54, 150))]
for k, (x, y) in enumerate([(54, H * .5), (W - 54, H * .5), (W * .3, H - 54), (W * .7, H - 54), (W * .3, 54), (W * .7, 54)]):
    specs.append(dict(ref=(x, y), turns=5, pitch=22, d=24, seed=40 + k, kind='lash', phase=rng.uniform(-.2, .2)))
compose('/tmp/rp/pannello_pastello.png', 'pole', 66, 54, 150, specs, full_spiral=dict(s0=340, s1=340, pitch=92, d=17, seed=88), joint=300, label='C-pastello')
