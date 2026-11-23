"""Generatore procedurale di corde ritorte, pali di legno e legature (bozze menu).
Tutte le misure sono in px finali (3x CSS) e vengono moltiplicate per SS internamente.
"""
import numpy as np, cv2, math

SS = 2  # supersampling interno
SHK = 1.0
SHC = (0.03, 0.02, 0.01)

ROPE = dict(mid=(201, 168, 106), light=(226, 197, 138), dark=(160, 124, 68), groove=(70, 44, 20))
WOOD = dict(mid=(139, 92, 48), light=(190, 134, 72), dark=(88, 54, 27), edge=(42, 24, 12))

LIGHT = np.array([-0.55, -0.75], np.float32)
LIGHT /= np.linalg.norm(LIGHT)


def smooth(x, a, b):
    t = np.clip((x - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)


def noise2(h, w, sx, sy, seed):
    rng = np.random.RandomState(seed)
    n = rng.rand(h, w).astype(np.float32)
    n = cv2.GaussianBlur(n, (0, 0), sigmaX=sx, sigmaY=sy)
    n = (n - n.min()) / (n.max() - n.min() + 1e-6)
    return n


# ------------------------------------------------------------------ percorsi
def resample(pts, step):
    pts = np.asarray(pts, np.float32)
    seg = np.linalg.norm(np.diff(pts, axis=0), axis=1)
    s = np.concatenate([[0], np.cumsum(seg)])
    L = s[-1]
    n = max(2, int(L / step) + 1)
    ss = np.linspace(0, L, n)
    x = np.interp(ss, s, pts[:, 0])
    y = np.interp(ss, s, pts[:, 1])
    P = np.stack([x, y], 1)
    # leggera lisciatura per tangenti pulite
    k = 5
    Ps = P.copy()
    if n > 2 * k:
        for c in range(2):
            Ps[:, c] = np.convolve(np.pad(P[:, c], (k, k), mode='edge'), np.ones(2 * k + 1) / (2 * k + 1), mode='valid')
        Ps[:k] = P[:k]
        Ps[-k:] = P[-k:]
    T = np.gradient(Ps, axis=0)
    T /= (np.linalg.norm(T, axis=1, keepdims=True) + 1e-6)
    N = np.stack([-T[:, 1], T[:, 0]], 1)
    return Ps, ss, T, N


def rrect_path(x0, y0, x1, y1, R, step=1.0, start='top'):
    """Anello chiuso (rettangolo arrotondato), in senso orario, parte dal centro del lato alto."""
    pts = []
    def arc(cx, cy, a0, a1):
        n = max(8, int(abs(a1 - a0) * R / step))
        for i in range(n):
            a = a0 + (a1 - a0) * i / n
            pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    xm = (x0 + x1) / 2
    pts.append((xm, y0))
    pts.append((x1 - R, y0))
    arc(x1 - R, y0 + R, -math.pi / 2, 0)
    pts.append((x1, y1 - R))
    arc(x1 - R, y1 - R, 0, math.pi / 2)
    pts.append((x0 + R, y1))
    arc(x0 + R, y1 - R, math.pi / 2, math.pi)
    pts.append((x0, y0 + R))
    arc(x0 + R, y0 + R, math.pi, 1.5 * math.pi)
    pts.append((xm, y0))
    return np.array(pts, np.float32)


# ------------------------------------------------------------------ canvas
class Canvas:
    def __init__(self, W, H):
        self.W, self.H = W, H
        self.P = np.zeros((H, W, 3), np.float32)
        self.A = np.zeros((H, W), np.float32)

    def _blend(self, rgb, a, x0, y0):
        h, w = a.shape
        xa, ya = max(0, x0), max(0, y0)
        xb, yb = min(self.W, x0 + w), min(self.H, y0 + h)
        if xa >= xb or ya >= yb:
            return
        sl = (slice(ya - y0, yb - y0), slice(xa - x0, xb - x0))
        dl = (slice(ya, yb), slice(xa, xb))
        al = a[sl]
        self.P[dl] = rgb[sl] + self.P[dl] * (1 - al[..., None])
        self.A[dl] = al + self.A[dl] * (1 - al)

    def shadow(self, a, x0, y0, dx, dy, blur, strength, color=None):
        import rope as _r
        strength = strength * _r.SHK
        color = color or _r.SHC
        m = int(blur * 3 + max(abs(dx), abs(dy)) + 2)
        h, w = a.shape
        pad = np.zeros((h + 2 * m, w + 2 * m), np.float32)
        pad[m:m + h, m:m + w] = a
        M = np.float32([[1, 0, dx], [0, 1, dy]])
        pad = cv2.warpAffine(pad, M, (pad.shape[1], pad.shape[0]))
        pad = cv2.GaussianBlur(pad, (0, 0), blur) * strength
        col = np.array(color, np.float32)
        rgb = pad[..., None] * col
        self._blend(rgb, pad, x0 - m, y0 - m)

    def add(self, layer, shadow=None):
        rgb, a, x0, y0 = layer
        if shadow:
            self.shadow(a, x0, y0, *shadow)
        self._blend(rgb, a, x0, y0)


# ------------------------------------------------------------------ rendering di un "tubo" texturizzato
def _splat(P, N, d, tex_rgb, tex_a):
    nt, ns = tex_a.shape
    t = np.linspace(-1, 1, nt, dtype=np.float32)
    pos = P[None, :, :] + N[None, :, :] * (t * d / 2)[:, None, None]
    ix = np.rint(pos[..., 0]).astype(np.int32)
    iy = np.rint(pos[..., 1]).astype(np.int32)
    valid = tex_a > 0
    x0, y0 = ix[valid].min() - 2, iy[valid].min() - 2
    x1, y1 = ix[valid].max() + 3, iy[valid].max() + 3
    h, w = y1 - y0, x1 - x0
    rgb = np.zeros((h, w, 3), np.float32)
    a = np.zeros((h, w), np.float32)
    # ordina: scrive in ordine di s crescente; i duplicati vincono gli ultimi
    rgb[iy[valid] - y0, ix[valid] - x0] = tex_rgb[valid]
    a[iy[valid] - y0, ix[valid] - x0] = tex_a[valid]
    # chiude eventuali buchi di 1 px
    k = np.ones((3, 3), np.uint8)
    am = (a > 0).astype(np.uint8)
    closed = cv2.morphologyEx(am, cv2.MORPH_CLOSE, k)
    holes = (closed > 0) & (am == 0)
    if holes.any():
        blur_rgb = cv2.blur(rgb, (3, 3)) / np.maximum(cv2.blur(am.astype(np.float32), (3, 3)), 1e-3)[..., None]
        rgb[holes] = blur_rgb[holes]
        a[holes] = 1.0
    return rgb, a, int(x0), int(y0)


def _shade(H, albedo, d_px, Lt, Ln, ds, dt, spec=0.12, amb=0.40, gain=0.85):
    """H: (nt, ns) altezza normalizzata; Lt/Ln: componenti luce locali per colonna."""
    Hpx = H * d_px * 0.5
    dHds = np.gradient(Hpx, ds, axis=1)
    dHdt = np.gradient(Hpx, dt, axis=0)
    nz = 1.0 / np.sqrt(1 + dHds ** 2 + dHdt ** 2)
    nx, ny = -dHds * nz, -dHdt * nz
    Lz = 0.62
    ln = np.sqrt(Lt ** 2 + Ln ** 2 + Lz ** 2)
    lx, ly, lz = (Lt / ln)[None, :], (Ln / ln)[None, :], Lz / ln
    diff = np.clip(nx * lx + ny * ly + nz * lz, 0, 1)
    # vettore a meta' (vista dall'alto)
    hx, hy, hz = lx, ly, lz + 1
    hn = np.sqrt(hx ** 2 + hy ** 2 + hz ** 2)
    sp = np.clip((nx * hx + ny * hy + nz * hz) / hn, 0, 1) ** 22
    shade = amb + gain * diff
    rgb = albedo * shade[..., None] + spec * 255 * sp[..., None] * np.array([1, .96, .84], np.float32)
    return np.clip(rgb, 0, 255)


def render_rope(pts, d, pitch=None, seed=0, palette=ROPE, twist=1, cap_start=True, cap_end=True,
                dark=1.0, light=LIGHT, fray_end=False):
    """pts: percorso (px finali). d: diametro. Restituisce (premult rgb 0-1, alpha, x0, y0) a scala SS."""
    pts = np.asarray(pts, np.float32) * SS
    d = d * SS
    pitch = (pitch or d * 2.3) if pitch is None else pitch * SS
    step = 0.5
    P, s, T, N = resample(pts, step)
    ns = len(s)
    nt = int(d / 0.5) | 1
    t = np.linspace(-1, 1, nt, dtype=np.float32)[:, None]
    sm = s[None, :].astype(np.float32)
    phi = np.arcsin(np.clip(t, -0.999, 0.999))
    q = (twist * phi - 2 * np.pi * sm / pitch) / (2 * np.pi / 3)
    f = q - np.floor(q)
    prof = np.sin(np.pi * f)
    cyl = np.sqrt(np.clip(1 - t ** 2, 0, 1))
    H = cyl * (0.55 + 0.45 * prof ** 0.7)
    # fibre
    q2 = (twist * phi + 2 * np.pi * sm / (pitch * 1.5)) / (2 * np.pi / 3) * 6.0
    f2 = q2 - np.floor(q2)
    fib = np.sin(np.pi * f2) ** 2
    nz1 = noise2(nt, ns, 2.2, 0.8, seed + 1)
    nz2 = noise2(nt, ns, 0.7, 0.7, seed + 2)
    H = H + 0.045 * fib * cyl + 0.03 * (nz1 - .5)
    ao = smooth(prof, 0.02, 0.55)
    mid, lig, drk, grv = [np.array(palette[k], np.float32) for k in ('mid', 'light', 'dark', 'groove')]
    base = mid[None, None, :] * np.ones((nt, ns, 1), np.float32)
    mix = np.clip(0.55 * fib + 0.55 * (nz1 - .5) * 2 + 0.3 * (nz2 - .5), -1, 1)[..., None]
    base = np.where(mix > 0, base + (lig - base) * mix, base + (drk - base) * (-mix))
    albedo = grv[None, None, :] + (base - grv[None, None, :]) * (0.25 + 0.75 * ao[..., None])
    # luce locale per colonna
    Lt = (T @ light).astype(np.float32)
    Ln = (N @ light).astype(np.float32)
    rgb = _shade(H, albedo, d, Lt, Ln, step, d / (nt - 1))
    edge = smooth(np.abs(t), 0.80, 1.0)
    rgb = rgb * (1 - 0.6 * edge[..., None]) * dark
    # alpha con capi arrotondati
    alpha = np.ones((nt, ns), np.float32)
    cap = d * 0.5
    if cap_start:
        u = np.clip(sm / cap, 0, 1)
        alpha = alpha * (np.abs(t) <= np.sqrt(np.clip(1 - (1 - u) ** 2, 0, 1)) + 0.0)
        rgb = rgb * (0.65 + 0.35 * u[..., None] ** 0.5)
    if cap_end:
        u = np.clip((s[-1] - sm) / cap, 0, 1)
        alpha = alpha * (np.abs(t) <= np.sqrt(np.clip(1 - (1 - u) ** 2, 0, 1)) + 0.0)
        rgb = rgb * (0.65 + 0.35 * u[..., None] ** 0.5)
    r, a, x0, y0 = _splat(P, N, d, rgb, alpha.astype(np.float32))
    return r / 255.0 * a[..., None], a, x0, y0


# ------------------------------------------------------------------ palo di legno
def render_pole(path, pw, seed=3, palette=WOOD, joint_every=None, light=LIGHT, closed=False):
    pts = np.asarray(path, np.float32) * SS
    d = pw * SS
    step = 0.5
    P, s, T, N = resample(pts, step)
    ns = len(s)
    nt = int(d / 0.5) | 1
    t = np.linspace(-1, 1, nt, dtype=np.float32)[:, None]
    sm = s[None, :].astype(np.float32)
    cyl = np.sqrt(np.clip(1 - t ** 2, 0, 1))
    # venature
    g1 = noise2(nt, ns, 60 * SS / 2, 1.6 * SS / 2, seed)
    g2 = noise2(nt, ns, 18 * SS / 2, 0.9 * SS / 2, seed + 7)
    g3 = noise2(nt, ns, 3.0, 3.0, seed + 11)
    rings = 0.5 + 0.5 * np.sin((t * 9 + g1 * 7) * np.pi)
    H = cyl * 0.95 + 0.03 * (g2 - .5) + 0.012 * (g3 - .5)
    Jh = np.zeros_like(H)
    jmask = np.zeros_like(H)
    jl = np.zeros_like(H)
    if joint_every:
        je = joint_every * SS
        rng = np.random.RandomState(seed + 21)
        k = 0
        pos = je * 0.55
        while pos < s[-1] - je * 0.3:
            w = 2.6 * SS
            gb = np.exp(-((sm - pos) / (w * 2.4)) ** 2)
            Jh += 0.085 * gb * cyl
            jmask = np.maximum(jmask, np.exp(-((sm - pos) / w) ** 2))
            jl = np.maximum(jl, np.exp(-((sm - pos - 4.5 * SS) / (1.6 * SS)) ** 2))
            pos += je * (0.85 + 0.3 * rng.rand())
        H = H + Jh
    mid, lig, drk, edg = [np.array(palette[k], np.float32) for k in ('mid', 'light', 'dark', 'edge')]
    mix = np.clip((g1 - .5) * 1.5 + (rings - .5) * 0.7 + (g2 - .5) * 0.6, -1, 1)[..., None]
    base = mid[None, None, :] * np.ones((nt, ns, 1), np.float32)
    base = np.where(mix > 0, base + (lig - base) * mix * 0.9, base + (drk - base) * (-mix) * 0.9)
    base = base * (1 - 0.5 * jmask[..., None]) + lig * 0.35 * jl[..., None]
    Lt = (T @ light).astype(np.float32)
    Ln = (N @ light).astype(np.float32)
    rgb = _shade(H, base, d, Lt, Ln, step, d / (nt - 1), spec=0.10, amb=0.46, gain=0.80)
    edge = smooth(np.abs(t), 0.88, 1.0)
    rgb = rgb * (1 - edge[..., None]) + edg[None, None, :] * edge[..., None]
    alpha = np.ones((nt, ns), np.float32)
    r, a, x0, y0 = _splat(P, N, d, rgb, alpha)
    return r / 255.0 * a[..., None], a, x0, y0


# ------------------------------------------------------------------ avvolgimento a spirale attorno a un palo
def spiral_parts(path, s0, s1, pitch, r, phase=0.0, step=1.0):
    """Ritorna (fronte, retro): liste di percorsi (px finali) della corda che si avvolge attorno al palo.
    path: polilinea del palo (px finali). s0, s1: tratto in px di lunghezza d'arco. r: raggio della spirale."""
    P, s, T, N = resample(path, step)
    mask = (s >= s0) & (s <= s1)
    idx = np.where(mask)[0]
    pts = []
    for i in idx:
        th = 2 * np.pi * (s[i] - s0) / pitch + phase
        lat = r * np.sin(th)
        pts.append((P[i] + N[i] * lat, math.cos(th)))
    pts = [(p, c) for p, c in pts]
    front, back = [], []
    cur, cur_front = [], None
    for p, c in pts:
        fr = c >= 0
        if cur_front is None:
            cur_front = fr
        if fr != cur_front:
            (front if cur_front else back).append(np.array(cur, np.float32))
            cur = [cur[-1]] if cur else []
            cur_front = fr
        cur.append(p)
    if cur:
        (front if cur_front else back).append(np.array(cur, np.float32))
    return [f for f in front if len(f) > 3], [b for b in back if len(b) > 3]
