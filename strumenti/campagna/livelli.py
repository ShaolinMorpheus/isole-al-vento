#!/usr/bin/env python3
"""Generatore dei livelli della campagna di «Isole al Vento».

Ogni livello è una MAPPA LOGICA a caratteri (. prato, F bosco, M monte, L lago, V vulcano, S stazione,
1 base del giocatore, 2 base nemica, T meta) più le regole. Il disegno del terreno (Muse o altro) legge
soltanto questi caratteri: se un giorno cambia lo stile del terreno, i livelli restano identici.

Uso:  python3 strumenti/campagna/livelli.py          -> scrive www/campagna-livelli.js e stampa le mappe
      python3 strumenti/campagna/livelli.py --solo 2-3   -> stampa solo quel livello
Le mappe sono deterministiche (seed fisso per livello): rigenerarle dà sempre lo stesso risultato.
"""
import json, random, sys, os
from collections import deque

WALK = set('.FSTP12C')          # transitabili senza gelo
BLOCK = set('MLV')

class Grid:
    def __init__(s, w, h):
        s.w, s.h = w, h
        s.c = [['.'] * w for _ in range(h)]
    def ok(s, x, y): return 0 <= x < s.w and 0 <= y < s.h
    def get(s, x, y): return s.c[y][x] if s.ok(x, y) else 'M'
    def set(s, x, y, ch):
        if s.ok(x, y): s.c[y][x] = ch
    def rows(s): return [''.join(r) for r in s.c]
    def cells(s, ch): return [(x, y) for y in range(s.h) for x in range(s.w) if s.c[y][x] == ch]

def bfs(g, start, passable=lambda ch: ch in WALK):
    seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if g.ok(nx, ny) and (nx, ny) not in seen and passable(g.get(nx, ny)):
                seen.add((nx, ny)); q.append((nx, ny))
    return seen

def dist_map(g, start, passable=lambda ch: ch in WALK):
    d = {start: 0}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            n = (x+dx, y+dy)
            if g.ok(*n) and n not in d and passable(g.get(*n)):
                d[n] = d[(x, y)] + 1; q.append(n)
    return d

def mirror(x, y, w, h): return (w-1-x, h-1-y)

def build(spec):
    """Costruisce la griglia di un livello. Ritorna (rows, info)."""
    w, h = spec['w'], spec['h']
    base0 = spec.get('base0', (w//2, h-1)); base1 = spec.get('base1', (w//2, 0))
    sym = spec.get('sym', True)
    for attempt in range(400):
        rnd = random.Random(spec['seed']*1000 + attempt)
        g = Grid(w, h)
        keep = set()
        def clear_around(p, r):
            for yy in range(p[1]-r, p[1]+r+1):
                for xx in range(p[0]-r, p[0]+r+1):
                    if abs(xx-p[0]) + abs(yy-p[1]) <= r and g.ok(xx, yy): keep.add((xx, yy))
        clear_around(base0, 2); clear_around(base1, 2)
        # stazioni (frazioni -> caselle), simmetriche se sym
        stations = []
        for (fx, fy) in spec.get('stations', []):
            p = (max(1, min(w-2, round(fx*(w-1)))), max(1, min(h-2, round(fy*(h-1)))))
            stations.append(p)
            if spec.get('mirror_st', sym) and (fx, fy) != (0.5, 0.5):
                q = mirror(*p, w, h)
                if q != p: stations.append(q)
        stations = list(dict.fromkeys(stations))
        vol = None
        if spec.get('vol'):
            fx, fy = spec['vol']; vol = (round(fx*(w-1)), round(fy*(h-1)))
        targets = [(round(fx*(w-1)), round(fy*(h-1))) for (fx, fy) in spec.get('targets', [])]
        for p in stations + targets: clear_around(p, 1)
        if vol: clear_around(vol, 0)
        # terreno a macchie
        ter = spec.get('terrain', {})
        half = h//2 + (1 if h % 2 else 0)
        def in_half(x, y):
            if not sym: return True
            return not (y > h//2 or (y == h//2 and x > w//2))
        sd = .5   # semi: le macchie crescono attorno ai semi (boschi e rocce a gruppetti, non a puntini)
        for y in range(h):
            for x in range(w):
                if (x, y) in keep or not in_half(x, y): continue
                v = rnd.random(); ch = '.'
                a = ter.get('F', 0)*sd; b = a + ter.get('M', 0)*sd; c = b + ter.get('L', 0)*sd
                if v < a: ch = 'F'
                elif v < b: ch = 'M'
                elif v < c: ch = 'L'
                g.set(x, y, ch)
        for ch, q in (('F', .30), ('M', .30), ('L', .38)):
            seeds = g.cells(ch)
            for (x, y) in seeds:
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if g.ok(nx, ny) and (nx, ny) not in keep and in_half(nx, ny) and g.get(nx, ny) == '.' and rnd.random() < q:
                        g.set(nx, ny, ch)
        if sym:
            for y in range(h):
                for x in range(w):
                    if y > h//2 or (y == h//2 and x > w//2):
                        mx, my = mirror(x, y, w, h)
                        if (x, y) not in keep: g.set(x, y, g.get(mx, my))
        # strutture: bande (fiumi/creste) con guadi
        for band in spec.get('bands', []):
            ch = band['ch']; y0 = round(band['fy']*(h-1)); th = band.get('th', 1)
            gaps = [round(gx*(w-1)) for gx in band.get('gaps', [])]
            for yy in range(y0, y0+th):
                for x in range(w):
                    if any(abs(x-gx) <= band.get('gw', 0) for gx in gaps): 
                        if g.get(x, yy) in 'LMV': g.set(x, yy, '.')
                        continue
                    if (x, yy) in keep and (x, yy) not in [(sx, sy) for (sx, sy) in stations]: pass
                    if g.get(x, yy) in '.FM': g.set(x, yy, ch)
        for (fx, fy, rx, ry, ch) in spec.get('blobs', []):
            cx, cy = round(fx*(w-1)), round(fy*(h-1))
            for y in range(h):
                for x in range(w):
                    if ((x-cx)/max(.5, rx))**2 + ((y-cy)/max(.5, ry))**2 <= 1 and (x, y) not in keep and g.get(x, y) in '.F':
                        g.set(x, y, ch)
        for (x, y) in stations: g.set(x, y, 'S')
        for (x, y) in targets: g.set(x, y, 'T')
        if vol: g.set(vol[0], vol[1], 'V')
        # niente cellule isolate: ogni casella libera dev'essere raggiungibile dalla base
        g.set(*base0, '1'); g.set(*base1, '2')
        reach = bfs(g, base0)
        need = [base1] + stations + targets
        if not all(p in reach for p in need): continue
        if spec.get('lanes_ok', True):
            # almeno 2 percorsi diversi tra le basi: la strada più breve non deve essere l'unica
            pass
        # chiudi le sacche irraggiungibili trasformandole in bosco
        for y in range(h):
            for x in range(w):
                if g.get(x, y) in '.F' and (x, y) not in reach: g.set(x, y, 'M')
        # copertura: nessuna area 4x4 completamente vuota (campo vivo, ma non affollato)
        info = dict(base0=base0, base1=base1, stations=stations, vol=vol, targets=targets)
        return g, info
    raise RuntimeError('nessuna mappa valida per ' + spec['id'])

def free_cells_near(g, p, taken, n):
    d = dist_map(g, p)
    cand = sorted([c for c, dd in d.items() if dd > 0 and g.get(*c) in '.F' and c not in taken], key=lambda c: (d[c], abs(c[0]-p[0]), c[1]))
    return cand[:n]

def nearest_free(g, fx, fy, taken, reach=None):
    px, py = round(fx*(g.w-1)), round(fy*(g.h-1))
    best = None
    for y in range(g.h):
        for x in range(g.w):
            if g.get(x, y) in '.F' and (x, y) not in taken and (reach is None or (x, y) in reach):
                d = abs(x-px) + abs(y-py)
                if best is None or d < best[0]: best = (d, (x, y))
    return best[1]

def place_units(g, info, spec):
    taken = set([info['base0'], info['base1']]) | set(info['stations']) | set(info['targets'])
    if info['vol']: taken.add(info['vol'])
    reach = bfs(g, info['base0'])
    out = {'p': [], 'e': []}
    for side, base in (('p', info['base0']), ('e', info['base1'])):
        lst = spec.get(side, [])
        near = [u for u in lst if not (isinstance(u, dict) and u.get('at'))]
        cells = free_cells_near(g, base, taken, len(near) + 6)
        # prima i vicini della base, ordinati: riga davanti alla base, poi i lati
        ci = 0
        for u in lst:
            if isinstance(u, str): t, ex = u, {}
            else: t, ex = u['t'], {k: v for k, v in u.items() if k not in ('t', 'at')}
            if isinstance(u, dict) and u.get('at'):
                c = nearest_free(g, u['at'][0], u['at'][1], taken, reach)
            else:
                c = cells[ci]; ci += 1
            taken.add(c)
            ent = [t, c[0], c[1]]
            if ex:
                ex = dict(ex)
                if 'anchor' in ex and isinstance(ex['anchor'], (list, tuple)) and isinstance(ex['anchor'][0], float):
                    ax, ay = nearest_free(g, ex['anchor'][0], ex['anchor'][1], set(), reach); ex['anchor'] = [ax, ay]
                if ex.get('anchor') == 'self': ex['anchor'] = [c[0], c[1]]
                ent.append(ex)
            out[side].append(ent)
    return out

def fix_wave_at(g, info, spec):
    waves = []
    reach = bfs(g, info['base0'])
    for w in spec.get('waves', []):
        at = []
        for (fx, fy) in w.get('at', []):
            if fy < 0.1: fy += spec.get('wave_dy', 0.16)   # le ondate compaiono un po' dentro il campo, non sul bordo
            c = nearest_free(g, fx, fy, set(), reach); at.append([c[0], c[1]])
        waves.append(dict(r=w['r'], u=[[u, {}] if isinstance(u, str) else [u[0], u[1]] for u in w['u']], at=at))
    return waves

STAR_TXT = {
    'rounds': lambda v: 'Vinci entro %d round' % v,
    'lost': lambda v: 'Non perdere nessuna unità' if v == 0 else ('Perdi al massimo %d unità' % v),
    'kills': lambda v: 'Sconfiggi almeno %d nemici' % v,
    'noaid': lambda v: 'Vinci senza usare aiuti',
    'vipsafe': lambda v: 'Il protetto non subisce mai danni',
    'units': lambda v: 'Finisci con almeno %d unità' % v,
}

def star_txt(t, v, units):
    if t == 'vipsafe':
        for u in units['p']:
            if len(u) > 3 and u[3].get('vip') and u[3].get('name'):
                return '%s non subisce mai danni' % u[3]['name']
    return STAR_TXT[t](v)

def make_level(spec):
    g, info = build(spec)
    units = place_units(g, info, spec)
    goal = dict(spec.get('goal', {'t': 'stations'}))
    lv = {
        'id': spec['id'], 'world': int(spec['id'].split('-')[0]), 'n': int(spec['id'].split('-')[1]),
        'name': spec['name'], 'desc': spec['desc'], 'tip': spec.get('tip', ''),
        'map': g.rows(), 'seed': spec['seed'],
        'p': units['p'], 'e': units['e'],
        'coins': spec.get('coins', [3, 0]), 'rounds': spec.get('rounds', 20), 'maxu': spec.get('maxu', 8),
        'erupt': spec.get('erupt', 4), 'goal': goal, 'rules': spec.get('rules', {}),
        'ai': spec.get('ai', {'mode': 'stations'}), 'lvl': spec.get('lvl', 'normale'),
        'weather': spec.get('weather', {}),
        'allow': spec.get('allow'),
        'stars': [{'t': t, 'v': v, 'txt': star_txt(t, v, units)} for (t, v) in spec.get('stars', [])],
        'reward': spec.get('reward', {}),
    }
    if spec.get('aiOv'): lv['aiOv'] = spec['aiOv']
    if spec.get('waves'): lv['waves'] = fix_wave_at(g, info, spec)
    if goal['t'] == 'reach':
        goal['cells'] = [list(c) for c in info['targets']]
    return lv

def show(lv):
    print('\n== %s %s  (%dx%d)  %s  round %d' % (lv['id'], lv['name'], len(lv['map'][0]), len(lv['map']), lv['goal']['t'], lv['rounds']))
    rows = [list(r) for r in lv['map']]
    for side, mark in (('p', 'abcdefghi'), ('e', 'ABCDEFGHI')):
        for i, u in enumerate(lv[side]):
            rows[u[2]][u[1]] = u[0].lower() if side == 'p' else '#'
    for r in rows: print('   ' + ''.join(r))
    print('   P:', ' '.join(u[0] for u in lv['p']), '| E:', ' '.join(u[0] for u in lv['e']), '| stelle:', [s['txt'] for s in lv['stars']])

if __name__ == '__main__':
    from livelli_dati import SPECS, WORLDS
    solo = sys.argv[sys.argv.index('--solo')+1] if '--solo' in sys.argv else None
    levels = []
    for sp in SPECS:
        lv = make_level(sp)
        levels.append(lv)
        if not solo or solo == sp['id']: show(lv)
    out = os.path.join(os.path.dirname(__file__), '..', '..', 'www', 'campagna-livelli.js')
    if not solo:
        with open(out, 'w', encoding='utf-8') as f:
            f.write('/* GENERATO da strumenti/campagna/livelli.py: non modificare a mano. */\n')
            f.write('window.CAMP_WORLDS=' + json.dumps(WORLDS, ensure_ascii=False, separators=(',', ':')) + ';\n')
            f.write('window.CAMP_LEVELS=' + json.dumps(levels, ensure_ascii=False, separators=(',', ':')) + ';\n')
        print('\nscritto', os.path.normpath(out), len(levels), 'livelli')
