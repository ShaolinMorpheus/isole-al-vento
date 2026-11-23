import numpy as np, cv2, math, sys, time
from rope import *

INT_BASE = (20, 88, 107)
INT_VIG = 0.22
W, H = 1224, 2499          # card 408x833 css @3x
PW = 66                    # palo
INS = 54
R = 150

def nearest_s(path, pt):
    P, s, T, N = resample(path, 1.0)
    i = np.argmin(np.linalg.norm(P - np.array(pt, np.float32), axis=1))
    return s[i], P[i], T[i], N[i]

def fray(cv, tip, dirv, n=7, length=13, seed=0, palette=ROPE):
    rng = np.random.RandomState(seed)
    m = int(length * SS * 2 + 10)
    cx, cy = int(tip[0] * SS), int(tip[1] * SS)
    size = 2 * m
    rgb = np.zeros((size, size, 3), np.float32); a = np.zeros((size, size), np.float32)
    ang0 = math.atan2(dirv[1], dirv[0])
    cols = [np.array(palette[k], np.float32) for k in ('mid', 'light', 'dark')]
    for i in range(n):
        ang = ang0 + rng.uniform(-0.55, 0.55)
        L = length * SS * rng.uniform(0.6, 1.1)
        bend = rng.uniform(-0.35, 0.35)
        pts = []
        for u in np.linspace(0, 1, 8):
            aa = ang + bend * u
            pts.append((m + math.cos(aa) * L * u, m + math.sin(aa) * L * u))
        col = cols[rng.randint(3)] / 255.0 * rng.uniform(0.75, 1.05)
        tmp = np.zeros((size, size), np.uint8)
        cv2.polylines(tmp, [np.array(pts, np.int32)], False, 255, thickness=max(1, int(SS * 1.1)), lineType=cv2.LINE_AA)
        t = tmp.astype(np.float32) / 255.0
        rgb = rgb * (1 - t[..., None]) + col[None, None, :] * t[..., None]
        a = a + t * (1 - a)
    rgb = rgb * a[..., None]
    cv._blend(rgb, a, cx - m, cy - m)

def tail(cv, p0, dir0, length, bend, d=22, seed=0, pitch=None, shadow=True):
    """Coda di corda che pende: curva da p0, direzione dir0, piega 'bend' (px laterali)."""
    dir0 = np.array(dir0, np.float32); dir0 /= np.linalg.norm(dir0)
    perp = np.array([-dir0[1], dir0[0]], np.float32)
    g = np.array([0.25, 1.0], np.float32)  # gravita'
    pts = []
    for u in np.linspace(0, 1, 40):
        base = p0 + dir0 * length * u * (1 - 0.35 * u) + perp * bend * u * u + g * length * 0.28 * u * u
        pts.append(base)
    pts = np.array(pts, np.float32)
    layer = render_rope(pts, d, pitch=pitch or d * 2.3, seed=seed, cap_start=False, cap_end=False)
    cv.add(layer, shadow=(3 * SS, 4 * SS, 3.2, 0.5) if shadow else None)
    # sfilacciatura
    tip = pts[-1]; dv = pts[-1] - pts[-4]; dv /= np.linalg.norm(dv)
    fray(cv, tip, dv, seed=seed + 5, length=d * 0.55)
    return pts

def knot(cv, c, axis, inward, d=26, seed=0):
    """Nodo pulito: un grumo di corda in diagonale sul bordo interno del palo."""
    axis = np.array(axis, np.float32); axis /= np.linalg.norm(axis)
    inward = np.array(inward, np.float32); inward /= np.linalg.norm(inward)
    a0 = c - inward * PW * 0.30 - axis * 14
    a1 = c + inward * PW * 0.30 + axis * 14
    pts = np.array([a0 + (a1 - a0) * u for u in np.linspace(0, 1, 16)], np.float32)
    cv.add(render_rope(pts, d * 1.30, pitch=d * 1.9, seed=seed), shadow=(3 * SS, 4 * SS, 3.2, 0.6))

def interior(cv, loop):
    mask = np.zeros((cv.H, cv.W), np.uint8)
    cv2.fillPoly(mask, [(loop * SS).astype(np.int32)], 255)
    m = cv2.GaussianBlur(mask.astype(np.float32) / 255, (0, 0), 1.2)
    h, w = cv.H, cv.W
    big = noise2(h // 8, w // 8, 14, 14, 3); big = cv2.resize(big, (w, h), interpolation=cv2.INTER_CUBIC)
    mid = noise2(h // 3, w // 3, 6, 6, 5); mid = cv2.resize(mid, (w, h), interpolation=cv2.INTER_CUBIC)
    fine = np.random.RandomState(8).rand(h // 2, w // 2).astype(np.float32); fine = cv2.resize(fine, (w, h))
    base = np.array(INT_BASE, np.float32)
    var = (big - .5) * 14 + (mid - .5) * 8 + (fine - .5) * 4
    # vignetta verso i bordi
    dist = cv2.distanceTransform((mask > 0).astype(np.uint8), cv2.DIST_L2, 5)
    vig = 1 - INT_VIG * np.exp(-dist / (60 * SS))
    rgb = (base[None, None, :] + var[..., None]) * vig[..., None]
    rgb = np.clip(rgb, 0, 255) / 255.0
    cv._blend(rgb * m[..., None], m, 0, 0)

def finalize(cv, out):
    P = cv2.resize(cv.P, (W, cv.H // SS), interpolation=cv2.INTER_AREA) if False else cv2.resize(cv.P, (cv.W // SS, cv.H // SS), interpolation=cv2.INTER_AREA)
    A = cv2.resize(cv.A, (cv.W // SS, cv.H // SS), interpolation=cv2.INTER_AREA)
    rgb = np.where(A[..., None] > 1e-4, P / np.maximum(A[..., None], 1e-4), 0)
    img = np.dstack([np.clip(rgb, 0, 1), np.clip(A, 0, 1)])
    img = (img * 255 + .5).astype(np.uint8)
    cv2.imwrite(out, img[:, :, [2, 1, 0, 3]])

# ======================================================================

def compose(out, main='pole', pw=66, ins=54, R_=150, specs=None, seed=3, joint=260, main_pitch=None, full_spiral=None, label='X'):
    global PW
    PW = pw
    t0 = time.time()
    cv = Canvas(W * SS, H * SS)
    loop = rrect_path(ins, ins, W - ins, H - ins, R_)
    interior(cv, loop)
    rng = np.random.RandomState(4)
    parts = []
    for sp in specs:
        r = pw / 2 + sp['d'] * 0.34
        s_c, Pc, Tc, Nc = nearest_s(loop, sp['ref'])
        length = sp['turns'] * sp['pitch']
        s0 = s_c - length / 2
        fr, bk = spiral_parts(loop, s0, s0 + length, sp['pitch'], r, phase=math.pi + sp.get('phase', 0))
        parts.append((sp, fr, bk, Pc, Tc, Nc))
    if full_spiral:
        Pl, sl, _, _ = resample(loop, 1.0)
        fp = full_spiral
        r = pw / 2 + fp['d'] * 0.34
        fr, bk = spiral_parts(loop, fp['s0'], sl[-1] - fp['s1'], fp['pitch'], r, phase=math.pi)
        parts.append((dict(d=fp['d'], seed=fp['seed'], kind='lash', pitch=fp['pitch'], turns=1), fr, bk, None, None, None))
    for sp, fr, bk, *_ in parts:
        for b in bk:
            cv.add(render_rope(b, sp['d'], pitch=sp['d'] * 2.3 * (1.5 if sp.get('kind') == 'corner' else 1), seed=sp["seed"] + 1, dark=0.66))
    if main == 'pole':
        cv.add(render_pole(loop, pw, seed=seed, joint_every=joint), shadow=(7 * SS, 10 * SS, 8, 0.55))
    else:
        cv.add(render_rope(loop, pw, pitch=main_pitch or pw * 2.4, seed=seed, cap_start=False, cap_end=False), shadow=(7 * SS, 10 * SS, 8, 0.55))
    for sp, fr, bk, *_ in parts:
        for f in fr:
            cv.add(render_rope(f, sp['d'], pitch=sp['d'] * 2.3 * (1.5 if sp.get('kind') == 'corner' else 1), seed=sp['seed']), shadow=(3 * SS, 4 * SS, 3.2, 0.6))
    for sp, fr, bk, Pc, Tc, Nc in parts:
        if Pc is None:
            continue
        sgn = 1 if sp['seed'] % 2 == 0 else -1
        c = Pc + Nc * (pw * 0.16)
        down = np.array([0, 1], np.float32)
        if abs(Tc[1]) > 0.35:
            tdir = Tc * (1 if Tc[1] > 0 else -1)
        else:
            tdir = Tc * sgn
        knot(cv, c, Tc, Nc, d=sp['d'], seed=sp['seed'] + 90)
        L1 = rng.uniform(78, 105) if sp.get('kind') == 'lash' else rng.uniform(100, 140)
        tail(cv, c + tdir * 6, tdir * 0.95 + Nc * 0.22, L1, bend=rng.uniform(6, 16) * (1 if rng.rand() < .5 else -1), d=sp['d'] * 0.82, seed=sp['seed'] + 200)
        tail(cv, c - tdir * 2 + Nc * 3, tdir * 0.7 + Nc * 0.35, L1 * 0.5, bend=rng.uniform(4, 12) * (1 if rng.rand() < .5 else -1), d=sp['d'] * 0.78, seed=sp['seed'] + 300)
    finalize(cv, out)
    print(label, round(time.time() - t0, 1), 's')

def corner_pts(ins, R_):
    k = R_ * (1 - .7071)
    return [(W - ins - k, ins + k), (W - ins - k, H - ins - k), (ins + k, H - ins - k), (ins + k, ins + k)]

def side_specs(rng, fy=(0.20, 0.50, 0.80), top=(0.22, 0.78), bot=(0.22, 0.5, 0.78), ins=54, turns=(4, 5, 4), d=24, base=40):
    out = []; j = 0
    for k, f in enumerate(fy):
        for x in (ins, W - ins):
            out.append(dict(ref=(x, H * f * (1.0 + 0.02 * (x > W / 2))), turns=turns[k], pitch=rng.uniform(21, 25), d=d, seed=base + j, kind='lash', phase=rng.uniform(-.2, .2))); j += 1
    for f in top:
        out.append(dict(ref=(W * f, ins), turns=4, pitch=rng.uniform(21, 25), d=d, seed=base + j, kind='lash', phase=rng.uniform(-.2, .2))); j += 1
    for f in bot:
        out.append(dict(ref=(W * f, H - ins), turns=4, pitch=rng.uniform(21, 25), d=d, seed=base + j, kind='lash', phase=rng.uniform(-.2, .2))); j += 1
    return out

def variant_A(out):
    rng = np.random.RandomState(4)
    specs = [dict(ref=c, turns=3.0, pitch=88, d=27, seed=20 + i, kind='corner', phase=0.35 * (i % 2)) for i, c in enumerate(corner_pts(54, 150))]
    specs += side_specs(rng)
    compose(out, 'pole', 66, 54, 150, specs, label='A')

def variant_B(out):
    rng = np.random.RandomState(7)
    ins = 50
    specs = []
    for i, c in enumerate(corner_pts(ins, 150)):
        specs.append(dict(ref=c, turns=5, pitch=17, d=17, seed=60 + i, kind='lash', phase=0.3 * i))
    for k, (x, y) in enumerate([(ins, H * .33), (W - ins, H * .33), (ins, H * .67), (W - ins, H * .67), (W * .25, H - ins), (W * .75, H - ins), (W * .22, ins), (W * .78, ins)]):
        specs.append(dict(ref=(x, y), turns=5, pitch=17, d=17, seed=70 + k, kind='lash', phase=rng.uniform(-.2, .2)))
    compose(out, 'rope', 58, ins, 150, specs, main_pitch=140, seed=11, label='B')

def variant_C(out):
    rng = np.random.RandomState(9)
    specs = [dict(ref=c, turns=3.0, pitch=88, d=27, seed=20 + i, kind='corner', phase=0.35 * (i % 2)) for i, c in enumerate(corner_pts(54, 150))]
    for k, (x, y) in enumerate([(54, H * .5), (W - 54, H * .5), (W * .3, H - 54), (W * .7, H - 54), (W * .3, 54), (W * .7, 54)]):
        specs.append(dict(ref=(x, y), turns=5, pitch=22, d=24, seed=40 + k, kind='lash', phase=rng.uniform(-.2, .2)))
    compose('/tmp/rp/frameC.png', 'pole', 66, 54, 150, specs, full_spiral=dict(s0=340, s1=340, pitch=92, d=17, seed=88), joint=300, label='C')

if __name__ == '__main__':
    which = sys.argv[1:] or ['A', 'B', 'C']
    for w in which:
        {'A': variant_A, 'B': variant_B, 'C': variant_C}[w]('/tmp/rp/frame%s.png' % w)
