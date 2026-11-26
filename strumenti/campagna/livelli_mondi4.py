# -*- coding: utf-8 -*-
"""Stagione 1, mondi 4-10 (59 livelli). Stesso formato di livelli_dati.py, con qualche scorciatoia per scrivere meno.
Le posizioni sono frazioni del campo (0..1). Unità: G guerriero, A arciere, E esploratore, K cavaliere, W sciamano,
L lanciere, H guaritore, B balestriere, R alfiere. Si può scrivere 'GAEL' al posto di ['G','A','E','L'].
"""
ALL = ['G', 'A', 'E', 'L', 'W', 'K', 'H', 'B', 'R']

# regole e IA di partenza per tipo di obiettivo (si possono cambiare livello per livello)
RULES = dict(stations={}, elim=dict(eNoRec=True, eNoRf=True), survive=dict(eNoRec=True, eNoRf=True, baseFall=True),
             reach=dict(eNoRec=True, eNoRf=True), boss=dict(eNoRec=True, eNoRf=True))
AIM = dict(stations=dict(mode='stations'), elim=dict(mode='hunt'), survive=dict(mode='hunt'), reach=dict(mode='hunt'),
           boss=dict(mode='guard', wake=4))

def G(t, x, y, **k):
    """Difensore fermo che si sveglia solo se un nemico si avvicina."""
    return dict(t=t, at=(x, y), mode='guard', anchor='self', **k)

def BOSS(t, x, y, name, bh, ba=1, wake=4):
    return dict(t=t, at=(x, y), boss=True, name=name, bh=bh, ba=ba, mode='guard', anchor='self', wake=wake)

def VIP(t, name, bh):
    return dict(t=t, vip=True, name=name, bh=bh)

def WV(*rows):
    """Ondate dall'alto: (round, 'GAE', [x...])."""
    return [dict(r=r, u=list(u), at=[(x, 0.0) for x in xs]) for (r, u, xs) in rows]

def WS(*rows):
    """Ondate da punti qualsiasi: (round, 'GAE', [(x, y)...])."""
    return [dict(r=r, u=list(u), at=list(at)) for (r, u, at) in rows]

def units(v):
    return list(v) if isinstance(v, str) else v

def default_stars(sp):
    g = sp['goal']['t']; r = sp['rounds']
    if g == 'stations': return [('rounds', round(r * .8)), ('lost', 1)]
    if g == 'elim':
        n = len(sp.get('e', []))
        return [('rounds', round(r * .72)), ('lost', 1 if n <= 6 else 2)]
    if g == 'survive':
        n = sum(len(w['u']) for w in sp.get('waves', []))
        return [('lost', 2), ('kills', max(5, round(n * .6)))]
    if g == 'reach':
        if sp['goal'].get('vip'): return [('rounds', round(r * .75)), ('vipsafe', 0)]
        return [('rounds', round(r * .85)), ('lost', 1)]
    return [('rounds', round(r * .72)), ('lost', 2)]

def lv(id, name, w, h, desc, goal, **k):
    wd, n = id.split('-')
    sp = dict(id=id, name=name, w=w, h=h, desc=desc, seed=int(wd) * 100 + int(n), allow=ALL, lvl='normale', tip='',
              maxu=8 if int(wd) <= 6 else (9 if int(wd) <= 8 else 10))
    sp['goal'] = dict(goal) if isinstance(goal, dict) else dict(t=goal)
    t = sp['goal']['t']
    sp['sym'] = k.pop('sym', t in ('stations', 'elim'))
    sp['rules'] = k.pop('rules', dict(RULES[t]))
    sp['ai'] = k.pop('ai', dict(AIM[t]))
    sp['coins'] = k.pop('coins', [5, 0]) if not isinstance(k.get('coins'), int) else [k.pop('coins'), 0]
    sp['weather'] = dict(pool=k.pop('wx', ['sereno', 'vento', 'pioggia']))
    if 'seq' in k: sp['weather']['seq'] = k.pop('seq')
    for key in ('p', 'e'):
        if key in k: k[key] = units(k[key])
    sp.update(k)
    sp.setdefault('p', 'GAEL'); sp['p'] = units(sp['p'])
    sp.setdefault('e', []); sp['e'] = units(sp['e'])
    if t != 'stations' and 'mirror_st' not in sp and not sp['sym']: sp['mirror_st'] = False
    if 'stars' not in sp: sp['stars'] = default_stars(sp)
    return sp

# colori della mappa dei mondi: filtro sullo sfondo (wf) e velo (wg)
WORLDS_B = [
    dict(id=4, name='Golfo delle Tempeste', sub='Il vento non si ferma mai', need=32,
         story='Mare grosso, isole sparse e un cielo che cambia ogni minuto. Qui il vento non si subisce: si sfrutta.',
         boss='Ammiraglio Fulmine', hue=10, sat=.6, bri=.78, accent='#8fc7ff',
         wf='hue-rotate(15deg) saturate(.65) brightness(.8)', wg='linear-gradient(rgba(20,40,80,.4),rgba(70,100,150,.28))'),
    dict(id=5, name='Foresta dei Sussurri', sub='Tra gli alberi qualcuno ti osserva', need=42,
         story='Un bosco fitto dove la vista è corta e le imboscate sono la regola. Muoviti piano e scegli tu dove combattere.',
         boss='Druido Antico', hue=-30, sat=1.2, bri=.75, accent='#a6f08a',
         wf='hue-rotate(-35deg) saturate(1.25) brightness(.72)', wg='linear-gradient(rgba(8,50,26,.4),rgba(30,90,40,.25))'),
    dict(id=6, name='Altopiani del Gelo', sub='Il ghiaccio apre strade e le chiude', need=53,
         story='Laghi congelati, creste e tormente. Con il gelo si cammina sull’acqua; quando finisce, non farti trovare sul ghiaccio.',
         boss='Regina del Gelo', hue=160, sat=.45, bri=1.15, accent='#d6f3ff',
         wf='hue-rotate(160deg) saturate(.5) brightness(1.12)', wg='linear-gradient(rgba(235,246,255,.45),rgba(120,160,200,.28))'),
    dict(id=7, name='Valle dei Tuoni', sub='La pioggia non perdona i distratti', need=65,
         story='Una lunga valle battuta dalla pioggia, dove i temporali coprono ogni mossa. I balestrieri nemici fanno la differenza.',
         boss='Signore dei Tuoni', hue=-100, sat=.8, bri=.8, accent='#c9a6ff',
         wf='hue-rotate(-95deg) saturate(.85) brightness(.78)', wg='linear-gradient(rgba(40,20,70,.4),rgba(90,60,140,.25))'),
    dict(id=8, name='Arcipelago Spezzato', sub='Ogni isola è una piccola guerra', need=76,
         story='Isole divise da canali stretti e ponti di sabbia. Chi controlla i passaggi controlla tutto.',
         boss='Re delle Maree', hue=60, sat=1.3, bri=1.05, accent='#7ff0d6',
         wf='hue-rotate(55deg) saturate(1.35) brightness(1.02)', wg='linear-gradient(rgba(0,80,90,.25),rgba(255,240,170,.12))'),
    dict(id=9, name='Cratere Antico', sub='Il vulcano più grande della stagione', need=88,
         story='Un cratere gigantesco che erutta sempre più spesso. Il fuoco ferisce tutti: usalo contro il nemico.',
         boss='Titano di Magma', hue=-170, sat=1.3, bri=.7, accent='#ff7a4a',
         wf='hue-rotate(-165deg) saturate(1.3) brightness(.68)', wg='linear-gradient(rgba(60,10,0,.4),rgba(255,90,30,.25))'),
    dict(id=10, name='Occhio del Ciclone', sub='L’ultima battaglia della Stagione 1', need=100,
         story='Al centro di tutte le tempeste c’è lui. Ogni meteo, ogni terreno, ogni nemico: tutto quello che hai imparato serve ora.',
         boss='Signore dei Venti', hue=-60, sat=.95, bri=.85, accent='#ffe17a',
         wf='hue-rotate(-55deg) saturate(1.0) brightness(.82)', wg='linear-gradient(rgba(30,20,60,.42),rgba(255,200,80,.25))'),
]

SPECS_B = [
    # ================================================================ MONDO 4 · Golfo delle Tempeste (7)
    lv('4-1', 'Mare mosso', 11, 15, 'Il vento spinge forte e i laghi tagliano il campo. Tieni le stazioni e lascia che siano gli alberi a ripararti.',
       dict(t='stations', hold=2), terrain=dict(F=.11, M=.05, L=.06), stations=[(0.2, 0.3)], rounds=24, coins=5,
       p='GAEL', e='GAL', wx=['vento', 'vento', 'pioggia', 'sereno']),
    lv('4-2', 'Il faro nella tempesta', 11, 15, 'Il Guardiano del Faro deve resistere fino alla fine del round 11. Le ondate nemiche lo cercano: proteggilo.',
       'survive', terrain=dict(F=.12, M=.05, L=.05), stations=[(0.5, 0.5)], rounds=11, coins=7,
       p=[VIP('L', 'Il Guardiano', 10), 'G', 'A', 'A', 'E'],
       waves=WV((2, 'GE', [.5]), (4, 'GAE', [.2, .8]), (6, 'KGA', [.15, .5, .85]), (8, 'LGA', [.3, .7])),
       wx=['pioggia', 'vento', 'vento', 'sereno'], stars=[('rounds', 11), ('vipsafe', 0)]),
    lv('4-3', 'Isole gemelle', 11, 15, 'Due isole unite da due soli guadi. Il nemico è schierato su entrambe: elimina tutti.',
       'elim', terrain=dict(F=.11, M=.05), bands=[dict(ch='L', fy=0.5, th=2, gaps=[0.25, 0.75], gw=0)], stations=[(0.2, 0.3)],
       rounds=22, coins=5, p='GAELK', e='GGAKL', wx=['vento', 'pioggia', 'sereno']),
    lv('4-4', 'Controvento', 11, 15, 'La Staffetta deve portare un messaggio sull’altra riva, con il vento in faccia e i nemici dietro ogni roccia.',
       dict(t='reach', vip=True), terrain=dict(F=.11, M=.06, L=.05), stations=[(0.3, 0.5)], targets=[(0.85, 0.04)],
       rounds=15, coins=3, p=[VIP('E', 'La Staffetta', 5), 'G', 'A', 'L', 'K'], e='GAEL', wx=['vento', 'vento', 'sereno', 'pioggia']),
    lv('4-5', 'Il porto', 12, 16, 'Tre stazioni meteo sparse tra i moli. Tienile tutte per 2 round, ma il nemico vuole il porto quanto te.',
       dict(t='stations', hold=2), terrain=dict(F=.10, M=.05, L=.07), stations=[(0.18, 0.3), (0.5, 0.5)], rounds=26, coins=5,
       p='GAELK', e='GAELK', wx=['sereno', 'vento', 'pioggia', 'nebbia']),
    lv('4-6', 'Marea montante', 11, 15, 'Il nemico sbarca dai lati, a ondate. Resisti fino alla fine del round 12 e non perdere la base.',
       'survive', terrain=dict(F=.12, M=.05, L=.05), stations=[(0.5, 0.5)], rounds=12, coins=8, p='GGAAEH',
       waves=WS((2, 'GE', [(0.0, 0.5)]), (4, 'GA', [(1.0, 0.5)]), (6, 'KGA', [(0.0, 0.5), (1.0, 0.5)]),
                (8, 'LGAW', [(0.5, 0.16)]), (10, 'KGGW', [(0.0, 0.45), (1.0, 0.45)])),
       wx=['pioggia', 'pioggia', 'vento', 'sereno']),
    lv('4-7', 'Ammiraglio Fulmine', 12, 16, 'L’Ammiraglio Fulmine guida la flotta del golfo. È un cavaliere velocissimo: colpiscilo prima che colpisca te.',
       'boss', terrain=dict(F=.11, M=.06, L=.04), stations=[(0.5, 0.5)], rounds=26, coins=9, p='GAELKW',
       e=[BOSS('K', 0.5, 0.1, 'Ammiraglio Fulmine', 15, 2), G('L', 0.3, 0.17), G('L', 0.7, 0.17), G('B', 0.4, 0.06), G('B', 0.6, 0.06),
          G('A', 0.22, 0.1)],
       wx=['vento', 'pioggia', 'sereno', 'nebbia'], stars=[('rounds', 19), ('lost', 2)], reward=dict(bonus=100)),

    # ================================================================ MONDO 5 · Foresta dei Sussurri (8)
    lv('5-1', 'Sentiero nel bosco', 11, 15, 'Alberi ovunque e poca visuale. Le stazioni sono nelle radure: raggiungile e tienile per 2 round.',
       dict(t='stations', hold=2), terrain=dict(F=.27, M=.05), stations=[(0.2, 0.3)], rounds=24, coins=5,
       p='GAEL', e='GAL', wx=['sereno', 'nebbia', 'sereno', 'pioggia']),
    lv('5-2', 'Occhi tra le foglie', 11, 15, 'I difensori restano nascosti finché non ti avvicini troppo. Scegli tu quando far partire lo scontro.',
       'elim', terrain=dict(F=.28, M=.05), stations=[(0.2, 0.3)], rounds=22, coins=8, sym=True, p='GAELH',
       e=[G('G', 0.3, 0.3), G('G', 0.7, 0.3), G('A', 0.5, 0.22), G('A', 0.4, 0.12), G('L', 0.6, 0.14), G('W', 0.5, 0.06)],
       ai=dict(mode='guard', wake=3), wx=['sereno', 'nebbia', 'pioggia']),
    lv('5-3', 'Il cacciatore', 11, 15, 'Il Cacciatore conosce la scorciatoia, ma i nemici gli stanno dietro. Scortalo fino alla radura sul fondo.',
       dict(t='reach', vip=True), terrain=dict(F=.26, M=.05, L=.03), stations=[(0.3, 0.5)], targets=[(0.15, 0.04)], rounds=16, coins=3,
       p=[VIP('A', 'Il Cacciatore', 3), 'G', 'G', 'L', 'E'], e='GAEKL', wx=['sereno', 'nebbia', 'nebbia']),
    lv('5-4', 'Radura assediata', 11, 15, 'Una piccola radura e nemici che sbucano da ogni lato. Resisti fino al round 11.',
       'survive', terrain=dict(F=.22, M=.05), stations=[(0.5, 0.5)], rounds=11, coins=8, p='GGAAEH',
       waves=WS((2, 'GE', [(0.0, 0.5)]), (4, 'GA', [(1.0, 0.5)]), (6, 'KGA', [(0.0, 0.45), (1.0, 0.45)]),
                (8, 'LGAW', [(0.5, 0.16)]), (10, 'KGGW', [(0.15, 0.16), (0.85, 0.16)])),
       wx=['nebbia', 'sereno', 'pioggia', 'nebbia']),
    lv('5-5', 'Ladri di vento', 12, 16, 'Tre stazioni nel cuore del bosco e un nemico svelto che le vuole. Tienile per 2 round.',
       dict(t='stations', hold=2), terrain=dict(F=.24, M=.06), stations=[(0.2, 0.3), (0.5, 0.5)], rounds=26, coins=5,
       p='GAELK', e='GAELK', wx=['sereno', 'vento', 'nebbia', 'pioggia']),
    lv('5-6', 'Il sentiero segreto', 12, 16, 'Un solo sentiero porta alla meta, oltre un torrente. Gli esploratori sono i più veloci, ma il bosco è pieno di guardie.',
       'reach', terrain=dict(F=.24, M=.06), bands=[dict(ch='L', fy=0.5, th=2, gaps=[0.1], gw=0)], stations=[(0.5, 0.5)], targets=[(0.88, 0.04)],
       rounds=17, coins=5, p='EEKGA', e=[G('G', 0.8, 0.14), G('A', 0.62, 0.1), G('L', 0.92, 0.2), G('W', 0.7, 0.2), G('B', 0.5, 0.08)],
       ai=dict(mode='guard', wake=4), wx=['sereno', 'nebbia', 'sereno', 'vento']),
    lv('5-7', 'La grande caccia', 12, 16, 'Un branco di cavalieri e guerrieri ti dà la caccia nel bosco. Fai muro tra gli alberi e resisti.',
       'elim', terrain=dict(F=.26, M=.05), stations=[(0.2, 0.3)], rounds=24, coins=8, sym=True, p='GALHW', e='KKGAEW',
       wx=['sereno', 'pioggia', 'nebbia', 'sereno']),
    lv('5-8', 'Druido Antico', 12, 17, 'Il Druido Antico veglia sul bosco con i suoi guardiani. Spingerà indietro chi si avvicina: colpisci in tanti.',
       'boss', terrain=dict(F=.24, M=.06, L=.03), stations=[(0.5, 0.5)], rounds=28, coins=9, p='GAELKW',
       e=[BOSS('W', 0.5, 0.1, 'Druido Antico', 22, 2), G('K', 0.25, 0.2), G('K', 0.75, 0.2), G('W', 0.38, 0.14), G('W', 0.62, 0.14),
          G('H', 0.5, 0.04), G('A', 0.3, 0.08), G('A', 0.7, 0.08)],
       wx=['nebbia', 'sereno', 'pioggia'], stars=[('rounds', 20), ('lost', 2)], reward=dict(bonus=110)),

    # ================================================================ MONDO 6 · Altopiani del Gelo (9)
    lv('6-1', 'Primo gelo', 11, 15, 'Il gelo arriva e i laghi diventano strade. Ma se finisce mentre sei sull’acqua, torni a riva.',
       dict(t='stations', hold=2), terrain=dict(F=.10, M=.07), blobs=[(0.5, 0.5, 2.2, 1.6, 'L')], stations=[(0.2, 0.3)], rounds=24, coins=5,
       p='GAEL', e='GAL', wx=['gelo', 'gelo', 'sereno', 'nebbia']),
    lv('6-2', 'Il lago ghiacciato', 11, 15, 'Il Pattinatore deve passare sul lago ghiacciato: aspetta il gelo e corri. Oppure aggira il lago a sinistra.',
       dict(t='reach', vip=True), terrain=dict(F=.10, M=.06), bands=[dict(ch='L', fy=0.45, th=3, gaps=[0.0], gw=0)], stations=[(0.3, 0.72)],
       targets=[(0.85, 0.04)], rounds=18, coins=4, stars=[('rounds', 14), ('lost', 1)], p=[VIP('E', 'Il Pattinatore', 8), 'E', 'G', 'A', 'K'],
       e=[G('G', 0.75, 0.12), G('A', 0.6, 0.1), G('L', 0.9, 0.2)], ai=dict(mode='guard', wake=4),
       seq=['sereno', 'gelo', 'gelo', 'gelo', 'nebbia', 'sereno', 'gelo', 'gelo', 'vento:S'], wx=['sereno', 'gelo', 'nebbia']),
    lv('6-3', 'Valanga', 11, 15, 'Dalle creste scendono ondate di nemici. Resisti fino al round 11 tra rocce e ghiaccio.',
       'survive', terrain=dict(F=.08, M=.12, L=.04), stations=[(0.5, 0.5)], rounds=11, coins=8, p='GGALEH',
       waves=WV((2, 'GE', [.5]), (4, 'GAL', [.2, .8]), (6, 'KGAW', [.15, .5, .85]), (8, 'LGBK', [.3, .7]), (10, 'KGGW', [.2, .8])),
       wx=['gelo', 'gelo', 'nebbia', 'sereno']),
    lv('6-4', 'Passo ghiacciato', 12, 16, 'Una cresta con un solo passaggio, presidiato da sei difensori. Elimina tutti e passa.',
       'elim', terrain=dict(F=.08, M=.07), bands=[dict(ch='M', fy=0.45, th=2, gaps=[0.5], gw=1)], stations=[(0.2, 0.3)],
       rounds=24, coins=8, sym=True, p='GAELK',
       e=[G('G', 0.45, 0.32), G('G', 0.55, 0.32), G('A', 0.35, 0.2), G('B', 0.5, 0.12), G('L', 0.65, 0.2), G('W', 0.5, 0.06)],
       ai=dict(mode='guard', wake=4), wx=['gelo', 'nebbia', 'sereno']),
    lv('6-5', 'Carovana di sale', 12, 16, 'Scorta Maestro Brina e la sua carovana fino al valico. Il gelo rallenta tutti, anche i banditi.',
       dict(t='reach', vip=True), terrain=dict(F=.08, M=.08, L=.04), stations=[(0.3, 0.55), (0.7, 0.4)], targets=[(0.85, 0.04)],
       rounds=19, coins=4, p=[VIP('H', 'Maestro Brina', 4), 'G', 'G', 'L', 'A', 'K'], e='GAEKLW', wx=['nebbia', 'gelo', 'vento', 'sereno']),
    lv('6-6', 'Tormenta', 12, 16, 'Tre stazioni, un campo coperto di neve e un meteo che cambia ogni turno. Tienile per 2 round.',
       dict(t='stations', hold=2), terrain=dict(F=.08, M=.08, L=.05), stations=[(0.2, 0.3), (0.5, 0.5)], rounds=26, coins=5,
       p='GAELK', e='GAELK', wx=['nebbia', 'gelo', 'vento', 'sereno']),
    lv('6-7', 'Il tempio di cristallo', 12, 16, 'Un tempio custodito da balestrieri e guaritori. Servono pazienza e arcieri per rompere la difesa.',
       'elim', terrain=dict(F=.06, M=.09), stations=[(0.2, 0.3)], rounds=26, coins=9, sym=True, p='GAELKW',
       e=[G('G', 0.35, 0.3), G('G', 0.65, 0.3), G('B', 0.3, 0.18), G('B', 0.7, 0.18), G('H', 0.5, 0.1), G('L', 0.5, 0.22), G('W', 0.42, 0.05)],
       ai=dict(mode='guard', wake=4), wx=['gelo', 'nebbia', 'sereno', 'vento']),
    lv('6-8', 'Assalto alla cresta', 12, 17, 'Il nemico attacca la tua cresta con tutto quello che ha. Resisti fino al round 13.',
       'survive', terrain=dict(F=.07, M=.14, L=.03), stations=[(0.25, 0.7), (0.75, 0.68)], rounds=13, coins=9, p='GGAALH',
       waves=WV((2, 'GEA', [.5]), (4, 'GALK', [.15, .85]), (6, 'KGAWG', [.15, .5, .85]), (8, 'LGBKH', [.3, .7]), (10, 'KKGWBL', [.15, .5, .85]),
                (12, 'KGGLWK', [.2, .8])),
       wx=['gelo', 'nebbia', 'vento', 'sereno'], lvl='difficile'),
    lv('6-9', 'Regina del Gelo', 12, 17, 'La Regina del Gelo regna sugli altopiani. Il suo bastone spinge e ferisce: tienila sotto pressione.',
       'boss', terrain=dict(F=.07, M=.09, L=.04), stations=[(0.3, 0.55), (0.7, 0.45)], rounds=28, coins=9, p='GAELKW',
       e=[BOSS('W', 0.5, 0.1, 'Regina del Gelo', 22, 2), G('K', 0.27, 0.2), G('K', 0.73, 0.2), G('B', 0.38, 0.14), G('B', 0.62, 0.14),
          G('H', 0.5, 0.04), G('G', 0.42, 0.22), G('G', 0.58, 0.22)],
       wx=['gelo', 'nebbia', 'sereno'], stars=[('rounds', 20), ('lost', 2)], reward=dict(bonus=120)),

    # ================================================================ MONDO 7 · Valle dei Tuoni (8)
    lv('7-1', 'Prime gocce', 11, 15, 'La valle si riempie di pioggia: archi più deboli e passi ridotti. Tieni le stazioni.',
       dict(t='stations', hold=2), terrain=dict(F=.12, M=.06, L=.04), stations=[(0.2, 0.3)], rounds=24, coins=5,
       p='GAEL', e='GAL', wx=['pioggia', 'pioggia', 'pioggia', 'sereno']),
    lv('7-2', 'Fulmini a ciel sereno', 11, 15, 'Cavalieri ed esploratori attaccano veloci come fulmini. Tieni una linea compatta e abbatti tutti.',
       'elim', terrain=dict(F=.13, M=.06), stations=[(0.2, 0.3)], rounds=20, coins=8, sym=True, p='GALAH', e='KEKGAG',
       wx=['pioggia', 'sereno', 'pioggia', 'nebbia']),
    lv('7-3', 'Il ponte crollato', 11, 15, 'Il fiume è in piena e resta un solo ponte. Il Corriere deve passarlo e arrivare alla meta.',
       dict(t='reach', vip=True), terrain=dict(F=.12, M=.06), bands=[dict(ch='L', fy=0.5, th=2, gaps=[0.5], gw=0)], stations=[(0.3, 0.6)],
       targets=[(0.8, 0.04)], rounds=17, coins=3, p=[VIP('K', 'Il Corriere', 5), 'G', 'A', 'L', 'E'], e='GAELK',
       wx=['pioggia', 'pioggia', 'sereno', 'nebbia']),
    lv('7-4', 'Muro d’acqua', 12, 16, 'Un temporale senza fine e nemici a ondate. Resisti fino al round 12.',
       'survive', terrain=dict(F=.12, M=.06, L=.04), stations=[(0.5, 0.5)], rounds=12, coins=8, p='GGAALH',
       waves=WV((2, 'GE', [.5]), (4, 'GAL', [.15, .85]), (6, 'KGAW', [.15, .5, .85]), (8, 'LGBK', [.3, .7]), (10, 'KGGWB', [.15, .5, .85])),
       wx=['pioggia', 'pioggia', 'nebbia', 'pioggia']),
    lv('7-5', 'Cecchini', 12, 16, 'I balestrieri nemici colpiscono da 3 caselle. Avvicinati sotto la pioggia, quando mirano peggio.',
       dict(t='stations', hold=2), terrain=dict(F=.11, M=.07, L=.03), stations=[(0.2, 0.3)], rounds=26, coins=6, p='GALKH', e='BBGAL',
       wx=['pioggia', 'pioggia', 'nebbia', 'sereno']),
    lv('7-6', 'La corte del tuono', 12, 16, 'Otto difensori, guaritori compresi, aspettano dentro il forte. Rompi la cura prima di tutto.',
       'elim', terrain=dict(F=.10, M=.08), stations=[(0.2, 0.3)], rounds=26, coins=9, sym=True, p='GAELKWH',
       e=[G('G', 0.3, 0.3), G('G', 0.7, 0.3), G('K', 0.2, 0.18), G('K', 0.8, 0.18), G('H', 0.5, 0.1), G('B', 0.4, 0.14), G('B', 0.6, 0.14), G('L', 0.5, 0.24)],
       ai=dict(mode='guard', wake=4), wx=['pioggia', 'nebbia', 'sereno']),
    lv('7-7', 'Tempesta perfetta', 13, 17, 'Il cielo si scatena e il nemico con lui. Resisti fino al round 14: ogni unità conta.',
       'survive', terrain=dict(F=.11, M=.07, L=.03), stations=[(0.25, 0.7), (0.75, 0.68)], rounds=14, coins=9, p='GGAALHK',
       waves=WV((2, 'GEA', [.5]), (4, 'GALK', [.15, .85]), (6, 'KGAWG', [.15, .5, .85]), (8, 'LGBKH', [.3, .7]), (10, 'KKGWBL', [.15, .5, .85]),
                (12, 'KGGLWK', [.2, .8])),
       wx=['pioggia', 'pioggia', 'nebbia', 'vento'], lvl='difficile'),
    lv('7-8', 'Signore dei Tuoni', 13, 17, 'Il Signore dei Tuoni non si muove, ma il suo balestro colpisce da lontano e fortissimo. Non farti cogliere in fila.',
       'boss', terrain=dict(F=.11, M=.07, L=.03), stations=[(0.3, 0.6), (0.7, 0.45)], rounds=30, coins=10, p='GAELKW',
       e=[BOSS('B', 0.5, 0.1, 'Signore dei Tuoni', 16, 1), G('K', 0.3, 0.2), G('K', 0.7, 0.2), G('L', 0.4, 0.15), G('L', 0.6, 0.15),
          G('H', 0.5, 0.04), G('B', 0.25, 0.08)],
       wx=['pioggia', 'nebbia', 'pioggia', 'sereno'], stars=[('rounds', 22), ('lost', 3)], reward=dict(bonus=130)),

    # ================================================================ MONDO 8 · Arcipelago Spezzato (9)
    lv('8-1', 'Ponti di sabbia', 11, 15, 'Canali stretti tagliano l’isola e restano pochi ponti. Tieni i passaggi e prendi le stazioni.',
       dict(t='stations', hold=2), terrain=dict(F=.10, M=.04),
       bands=[dict(ch='L', fy=0.36, th=1, gaps=[0.3, 0.7], gw=0), dict(ch='L', fy=0.62, th=1, gaps=[0.3, 0.7], gw=0)],
       stations=[(0.2, 0.22)], rounds=24, coins=5, p='GAEL', e='GAL', wx=['sereno', 'vento', 'pioggia']),
    lv('8-2', 'Isola per isola', 12, 16, 'Un arcipelago di laghi e isolotti. Il nemico è sparso ovunque: dagli la caccia isola per isola.',
       'elim', terrain=dict(F=.10, M=.04), blobs=[(0.3, 0.38, 1.8, 1.2, 'L'), (0.7, 0.62, 1.8, 1.2, 'L'), (0.5, 0.5, 1.4, 1.0, 'L')],
       stations=[(0.2, 0.25)], rounds=24, coins=7, sym=True, p='GAELK', e='GGAKLE', wx=['sereno', 'vento', 'nebbia']),
    lv('8-3', 'La traversata', 12, 16, 'Un canale largo separa le due rive. Con il gelo lo attraversi in un attimo; senza, devi fare il giro.',
       'reach', terrain=dict(F=.10, M=.05), bands=[dict(ch='L', fy=0.5, th=3, gaps=[1.0], gw=0)], stations=[(0.5, 0.5)], targets=[(0.14, 0.04)],
       rounds=17, coins=5, p='EEKKGA', e=[G('G', 0.2, 0.12), G('A', 0.38, 0.1), G('L', 0.1, 0.2), G('W', 0.3, 0.2), G('B', 0.5, 0.08)],
       ai=dict(mode='guard', wake=4), seq=['sereno', 'vento:O', 'gelo', 'gelo', 'sereno', 'pioggia', 'gelo', 'gelo', 'nebbia'],
       wx=['sereno', 'gelo', 'nebbia', 'vento']),
    lv('8-4', 'Pirati!', 12, 16, 'I pirati sbarcano da ogni lato. Resisti fino al round 12 e non lasciargli la base.',
       'survive', terrain=dict(F=.10, M=.04, L=.04), stations=[(0.5, 0.5)], rounds=12, coins=9, p='GGAAEH',
       waves=WS((2, 'GE', [(0.0, 0.5)]), (4, 'GA', [(1.0, 0.5)]), (6, 'KGA', [(0.0, 0.45), (1.0, 0.45)]),
                (8, 'LGAW', [(0.15, 0.16), (0.85, 0.16)]), (10, 'KGGWB', [(0.0, 0.45), (1.0, 0.45), (0.5, 0.16)])),
       wx=['vento', 'sereno', 'pioggia', 'vento']),
    lv('8-5', 'Tre isole', 12, 16, 'Tre stazioni su tre isolotti, collegati da guadi. Tienile per 2 round.',
       dict(t='stations', hold=2), terrain=dict(F=.10, M=.04),
       bands=[dict(ch='L', fy=0.4, th=1, gaps=[0.25, 0.75], gw=0), dict(ch='L', fy=0.58, th=1, gaps=[0.25, 0.75], gw=0)],
       stations=[(0.2, 0.25), (0.5, 0.5)], rounds=26, coins=5, p='GAELK', e='GAELK', wx=['sereno', 'vento', 'pioggia', 'nebbia']),
    lv('8-6', 'Il traghettatore', 12, 16, 'Il Traghettatore, con l’Alfiere, aiuta le unità vicine a muoversi più veloci. Portalo sull’isola più lontana.',
       dict(t='reach', vip=True), terrain=dict(F=.10, M=.05), bands=[dict(ch='L', fy=0.45, th=2, gaps=[0.2, 0.8], gw=0)],
       stations=[(0.3, 0.6), (0.7, 0.35)], targets=[(0.3, 0.06)], rounds=19, coins=4,
       p=[VIP('R', 'Il Traghettatore', 4), 'G', 'G', 'A', 'K', 'L'], e='GAELKA', wx=['sereno', 'vento', 'nebbia', 'pioggia']),
    lv('8-7', 'Flotta nemica', 12, 17, 'Nove avversari all’attacco su più isole. Fai fronte comune, cura i feriti e colpisci insieme.',
       'elim', terrain=dict(F=.09, M=.05), blobs=[(0.3, 0.4, 1.6, 1.2, 'L'), (0.7, 0.6, 1.6, 1.2, 'L')], stations=[(0.2, 0.25)],
       rounds=26, coins=10, sym=True, p='GAELKWH', e='GGAAKLWBE', wx=['sereno', 'vento', 'pioggia', 'nebbia']),
    lv('8-8', 'Marea nera', 13, 17, 'Un’ondata dopo l’altra, dai lati e dall’alto. Resisti fino al round 14.',
       'survive', terrain=dict(F=.10, M=.05, L=.04), stations=[(0.25, 0.7), (0.75, 0.68)], rounds=14, coins=9, p='GGAALHK',
       waves=WS((2, 'GEA', [(0.5, 0.16)]), (4, 'GALK', [(0.0, 0.5), (1.0, 0.5)]), (6, 'KGAWG', [(0.15, 0.16), (0.5, 0.16), (0.85, 0.16)]),
                (8, 'LGBKH', [(0.0, 0.45), (1.0, 0.45)]), (10, 'KKGWBL', [(0.15, 0.16), (0.5, 0.16), (0.85, 0.16)]),
                (12, 'KGGLWK', [(0.0, 0.5), (1.0, 0.5)])),
       wx=['vento', 'pioggia', 'nebbia', 'sereno'], lvl='difficile'),
    lv('8-9', 'Re delle Maree', 13, 17, 'Il Re delle Maree comanda l’arcipelago dall’isola più alta. I suoi cavalieri tagliano la strada.',
       'boss', terrain=dict(F=.09, M=.05, L=.04), stations=[(0.3, 0.6), (0.7, 0.45)], rounds=28, coins=10, p='GAELKW',
       e=[BOSS('R', 0.5, 0.1, 'Re delle Maree', 26, 3), G('K', 0.28, 0.2), G('K', 0.72, 0.2), G('H', 0.42, 0.06), G('H', 0.58, 0.06),
          G('B', 0.3, 0.12), G('B', 0.7, 0.12), G('W', 0.5, 0.2), G('L', 0.5, 0.28)],
       wx=['vento', 'pioggia', 'sereno', 'nebbia'], stars=[('rounds', 20), ('lost', 3)], reward=dict(bonus=140)),

    # ================================================================ MONDO 9 · Cratere Antico (8)
    lv('9-1', 'Fumarole', 11, 15, 'Un vulcano immenso al centro e fumarole ovunque. Erutta ogni 3 round: stai lontano dal cratere.',
       dict(t='stations', hold=2), terrain=dict(F=.09, M=.07), vol=(0.5, 0.5), stations=[(0.2, 0.28)], rounds=24, coins=5, erupt=3,
       p='GAEL', e='GAL', wx=['sereno', 'vento', 'pioggia']),
    lv('9-2', 'Colata di lava', 11, 15, 'Il vulcano erutta ogni 2 round: il campo brucia e il nemico attacca. Combatti dove il fuoco non arriva.',
       'elim', terrain=dict(F=.09, M=.06), vol=(0.5, 0.5), stations=[(0.2, 0.28)], rounds=22, coins=8, erupt=2, sym=True, p='GAELKH', e='GGLAKW',
       wx=['sereno', 'vento', 'pioggia']),
    lv('9-3', 'Fuga dal cratere', 12, 16, 'La Sacerdotessa del fuoco deve fuggire dal cratere in eruzione. Studia i turni e passa quando il fuoco è passato.',
       dict(t='reach', vip=True), terrain=dict(F=.09, M=.06, L=.03), vol=(0.5, 0.5), stations=[(0.25, 0.4), (0.75, 0.6)], targets=[(0.1, 0.04)],
       rounds=19, coins=4, erupt=3, p=[VIP('H', 'La Sacerdotessa', 5), 'G', 'G', 'A', 'K', 'E'], e='GAELK', wx=['sereno', 'vento', 'gelo', 'pioggia']),
    lv('9-4', 'Pioggia di cenere', 12, 16, 'Cenere e nemici dal cielo. Resisti fino al round 12 sfruttando le eruzioni.',
       'survive', terrain=dict(F=.10, M=.06, L=.03), vol=(0.5, 0.5), stations=[(0.25, 0.7), (0.75, 0.3)], rounds=12, coins=9, erupt=3, p='GGAALH',
       waves=WV((2, 'GE', [.5]), (4, 'GAL', [.15, .85]), (6, 'KGAW', [.15, .5, .85]), (8, 'LGBK', [.3, .7]), (10, 'KGGWB', [.15, .5, .85])),
       wx=['sereno', 'pioggia', 'vento']),
    lv('9-5', 'Il tempio del fuoco', 12, 16, 'Tre stazioni attorno al cratere e un nemico che le conosce a memoria. Tienile per 2 round.',
       dict(t='stations', hold=2), terrain=dict(F=.08, M=.08), vol=(0.5, 0.5), stations=[(0.22, 0.34), (0.78, 0.66), (0.78, 0.34)],
       rounds=26, coins=6, erupt=3, sym=False, mirror_st=False, p='GAELK', e='GAELKA', wx=['sereno', 'vento', 'pioggia', 'gelo']),
    lv('9-6', 'La forgia', 13, 17, 'Otto fabbri di guerra difendono la forgia. Il vulcano è dalla tua parte, se sai quando farti da parte.',
       'elim', terrain=dict(F=.08, M=.09), vol=(0.5, 0.5), stations=[(0.2, 0.26)], rounds=28, coins=10, erupt=3, sym=True, p='GAELKWH',
       e='GGLAKWBK', wx=['sereno', 'vento', 'pioggia', 'gelo']),
    lv('9-7', 'L’ultima risalita', 13, 17, 'L’ultima risalita verso il cratere, con il nemico che non si ferma mai. Resisti fino al round 14.',
       'survive', terrain=dict(F=.09, M=.08, L=.03), vol=(0.5, 0.5), stations=[(0.25, 0.7), (0.75, 0.3)], rounds=14, coins=9, erupt=3, p='GGAALHK',
       waves=WV((2, 'GEA', [.5]), (4, 'GALK', [.15, .85]), (6, 'KGAWG', [.15, .5, .85]), (8, 'LGBKH', [.3, .7]), (10, 'KKGWBL', [.15, .5, .85]),
                (12, 'KGGLWK', [.2, .8])),
       wx=['sereno', 'pioggia', 'vento', 'nebbia'], lvl='difficile'),
    lv('9-8', 'Titano di Magma', 13, 17, 'Il Titano di Magma dorme nel cratere. Più è vicino all’eruzione, più è vulnerabile: scegli il momento.',
       'boss', terrain=dict(F=.08, M=.08, L=.03), vol=(0.5, 0.5), stations=[(0.25, 0.65), (0.75, 0.5)], rounds=28, coins=10, erupt=3, p='GAELKW',
       e=[BOSS('G', 0.5, 0.28, 'Titano di Magma', 30, 2, 3), G('K', 0.28, 0.16), G('K', 0.72, 0.16), G('B', 0.4, 0.08), G('B', 0.6, 0.08),
          G('W', 0.3, 0.07), G('W', 0.7, 0.07)],
       wx=['sereno', 'vento', 'pioggia'], stars=[('rounds', 20), ('lost', 3)], reward=dict(bonus=150)),

    # ================================================================ MONDO 10 · Occhio del Ciclone (10)
    lv('10-1', 'Il vento cambia', 11, 15, 'Da qui il meteo non ha più regole: sereno, vento, pioggia, nebbia e gelo si alternano. Ripassa le basi.',
       dict(t='stations', hold=2), terrain=dict(F=.10, M=.06, L=.04), stations=[(0.2, 0.3)], rounds=24, coins=5, p='GAEL', e='GAL',
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo']),
    lv('10-2', 'Quattro stagioni', 12, 16, 'Sette avversari e un cielo che cambia a ogni round. Adatta la tua formazione al meteo.',
       'elim', terrain=dict(F=.10, M=.06, L=.04), stations=[(0.2, 0.3)], rounds=24, coins=9, sym=True, p='GAELKH', e='GGLAKWE',
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo']),
    lv('10-3', 'La staffetta del ciclone', 13, 17, 'La Messaggera deve attraversare un campo di laghi e rocce. Il nemico la cerca in ogni angolo.',
       dict(t='reach', vip=True), terrain=dict(F=.09, M=.07, L=.05), bands=[dict(ch='L', fy=0.5, th=2, gaps=[0.15, 0.85], gw=0)],
       stations=[(0.3, 0.6), (0.7, 0.4)], targets=[(0.2, 0.05)], rounds=20, coins=4, p=[VIP('E', 'La Messaggera', 4), 'G', 'G', 'A', 'K', 'H'],
       e='GAELKWA', wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo']),
    lv('10-4', 'Assedio finale', 12, 16, 'Il nemico lancia l’offensiva generale. Resisti fino al round 13.',
       'survive', terrain=dict(F=.10, M=.07, L=.03), stations=[(0.25, 0.7), (0.75, 0.68)], rounds=13, coins=10, p='GGAALHK',
       waves=WV((2, 'GEA', [.5]), (4, 'GALK', [.15, .85]), (6, 'KGAWG', [.15, .5, .85]), (8, 'LGBKH', [.3, .7]), (10, 'KKGWBL', [.15, .5, .85]),
                (12, 'KGGLWK', [.2, .8])),
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo'], lvl='difficile'),
    lv('10-5', 'Generale Bora', 12, 17, 'Il Generale Bora, braccio destro del Signore dei Venti, ti sbarra la strada con la sua guardia.',
       'boss', terrain=dict(F=.10, M=.07, L=.03), stations=[(0.3, 0.6), (0.7, 0.45)], rounds=28, coins=10, p='GAELKW',
       e=[BOSS('K', 0.5, 0.1, 'Generale Bora', 18, 2), G('L', 0.3, 0.17), G('L', 0.7, 0.17), G('B', 0.4, 0.06), G('B', 0.6, 0.06),
          G('W', 0.25, 0.1), G('W', 0.75, 0.1), G('H', 0.5, 0.04)],
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo'], stars=[('rounds', 20), ('lost', 3)], reward=dict(bonus=100)),
    lv('10-6', 'Quattro stendardi', 13, 17, 'Quattro stazioni sparse e un nemico che non perdona. Tienile tutte per 2 round.',
       dict(t='stations', hold=2), terrain=dict(F=.09, M=.08, L=.04), stations=[(0.2, 0.26), (0.8, 0.4)], rounds=28, coins=6, p='GAELK', e='GAELK',
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo'], lvl='difficile'),
    lv('10-7', 'Il ponte del ciclone', 13, 17, 'Il Custode deve portare l’ultimo sigillo oltre il fiume e oltre il vulcano. Un solo ponte, un solo tentativo.',
       dict(t='reach', vip=True), terrain=dict(F=.08, M=.07, L=.03), vol=(0.5, 0.5), bands=[dict(ch='L', fy=0.62, th=2, gaps=[0.5], gw=0)],
       stations=[(0.25, 0.4), (0.75, 0.75)], targets=[(0.9, 0.04)], rounds=22, coins=4, erupt=3,
       p=[VIP('G', 'Il Custode', 7), 'G', 'K', 'A', 'H', 'L'], e='GAELK', wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo']),
    lv('10-8', 'Tempesta di cenere', 13, 17, 'Eruzioni, vento e ondate nemiche: resisti fino al round 15.',
       'survive', terrain=dict(F=.09, M=.08, L=.03), vol=(0.5, 0.5), stations=[(0.25, 0.7), (0.75, 0.3)], rounds=15, coins=10, erupt=3, p='GGAALHK',
       waves=WS((2, 'GEA', [(0.5, 0.16)]), (4, 'GALK', [(0.0, 0.5), (1.0, 0.5)]), (6, 'KGAWG', [(0.15, 0.16), (0.5, 0.16), (0.85, 0.16)]),
                (8, 'LGBKH', [(0.0, 0.45), (1.0, 0.45)]), (10, 'KKGWBL', [(0.15, 0.16), (0.5, 0.16), (0.85, 0.16)]),
                (12, 'KGGLWK', [(0.0, 0.5), (1.0, 0.5)]), (14, 'KKGWBH', [(0.2, 0.16), (0.8, 0.16)])),
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo'], lvl='difficile'),
    lv('10-9', 'La soglia', 13, 17, 'Dieci difensori davanti alla fortezza del Signore dei Venti. L’ultima prova prima del boss.',
       'elim', terrain=dict(F=.08, M=.08, L=.03), stations=[(0.2, 0.26)], rounds=30, coins=10, sym=True, p='GAELKWH',
       e=[G('G', 0.3, 0.3), G('G', 0.7, 0.3), G('K', 0.2, 0.2), G('K', 0.8, 0.2), G('L', 0.5, 0.26), G('B', 0.35, 0.14), G('B', 0.65, 0.14),
          G('W', 0.3, 0.08), G('W', 0.7, 0.08), G('H', 0.5, 0.05)],
       ai=dict(mode='guard', wake=4), wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo'], lvl='difficile'),
    lv('10-10', 'Signore dei Venti', 14, 19, 'Il Signore dei Venti ti aspetta al centro dell’occhio del ciclone, con tutta la sua corte. La battaglia finale della Stagione 1.',
       'boss', terrain=dict(F=.08, M=.08, L=.03), stations=[(0.3, 0.65), (0.7, 0.5)], rounds=34, coins=11, p='GAELKWH',
       e=[BOSS('K', 0.5, 0.08, 'Signore dei Venti', 22, 2), G('K', 0.28, 0.18), G('K', 0.72, 0.18), G('G', 0.4, 0.2), G('G', 0.6, 0.2),
          G('W', 0.35, 0.1), G('W', 0.65, 0.1), G('B', 0.2, 0.1), G('B', 0.8, 0.1), G('H', 0.45, 0.04), G('H', 0.55, 0.04)],
       wx=['sereno', 'vento', 'pioggia', 'nebbia', 'gelo'], lvl='difficile', stars=[('rounds', 24), ('lost', 3)], reward=dict(bonus=250)),
]
