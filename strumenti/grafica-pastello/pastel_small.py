import rope, build, numpy as np
rope.ROPE.update(mid=(236,212,164), light=(250,236,198), dark=(208,178,128), groove=(150,114,76))
rope.WOOD.update(mid=(205,158,108), light=(232,196,148), dark=(160,116,74), edge=(120,86,56))
rope.SHK = 0.5; rope.SHC = (0.10, 0.20, 0.24)
build.INT_BASE = (58, 150, 170); build.INT_VIG = 0.10
build.W = build.H = 720
specs = [dict(ref=c, turns=3.0, pitch=88, d=27, seed=20 + i, kind='corner', phase=0.35 * (i % 2)) for i, c in enumerate(build.corner_pts(54, 150))]
build.compose('/tmp/rp/pannello_piccolo.png', 'pole', 66, 54, 150, specs, joint=260, label='piccolo')
