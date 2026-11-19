# Gruppo 8 — Terreno: variazioni del prato, terra, sabbia, dettagli

Pezzi per il campo a «prato unico»: chiazze di terreno da sovrapporre al prato,
prati pieni alternativi, dettagli sparsi e bordi di riva per i laghi. Tutti
visti dall'alto, stesso stile e stessa luce (alto-sinistra) del terreno v2,
colori saturi. Nessun contorno scuro, nessuna ombra disegnata, nessun bordo
di casella, nessuna cornice o vignetta in nessun file.

## NOTA DI INTERPRETAZIONE (punto B — da leggere prima di tutto)

La regola generale della consegna dice «PNG con sfondo trasparente», ma per
il punto B (prato pieno) è stata interpretata così: **tessere OPACHE a tutto
campo e ripetibili senza giunture**. Motivo: una chiazza con alpha sfumato
non può fare da prato pieno né essere ruotata/affiancata senza mostrare i
bordi, mentre la richiesta B chiede esplicitamente pezzi che «devono potersi
ruotare e sovrapporre senza che si veda dove finiscono». Se intendevi altro
(prato come chiazza trasparente come le altre), questo è il primo punto da
correggere: gli altri 30 file non cambiano.

## A) Chiazze di terreno — 512×512, RGBA, bordo sfumato a trasparente

Forma a chiazza irregolare/organica (mai cerchio o quadrato): centro pieno
(alpha ~255), bordo che sfuma dolcemente fino ad alpha 0, con margine vuoto
intorno (alpha sul perimetro = 0 in tutti i file). Maschera costruita con
raggio modulato da armoniche casuali + sfocatura; texture procedurale a
rumore morbido nella stessa tinta del terreno v2. Le tre varianti di ogni
tipo differiscono per forma della chiazza, tonalità e densità dei dettagli.

- `terreno_terra_a/b/c.png` — terra battuta marrone caldo, sassolini e zolle.
- `terreno_sabbia_a/b/c.png` — sabbia chiara dorata, ondine tenui e sassolini.
- `terreno_erbasecca_a/b/c.png` — erba secca gialla-ocra per le zone asciutte.
- `terreno_fango_a/b.png` — terra scura umida, da usare vicino ai laghi.
- `terreno_sassi_a/b/c.png` — ghiaia grigia con pietre piatte.

Verifica (misurata): perimetro alpha max = 0 e centro (200×200) alpha medio
≥ 254,9 per tutte e 14; riempimento della maschera rispetto al suo rettangolo
contenitore tra 0,61 e 0,81 (forme irregolari, non geometriche).

## B) Prato pieno — 512×512, OPACHI, ripetibili senza giunture

Texture costruite su toro (rumore periodico + ogni elemento replicato con
traslazione modulo 512): si affiancano e si ruotano senza cuciture visibili.
Densità uniforme fino ai bordi. Riferimento tinta prato v2: media
RGB ≈ (115, 122, 36).

- `terreno_prato_c.png` — più folta e scura. Media (95,6, 109,5, 29,9).
- `terreno_prato_d.png` — più chiara e rada. Media (133,8, 139,6, 49,7).
- `terreno_prato_e.png` — con gruppetti di trifoglio (verde più freddo).
  Media (114,7, 121,5, 35,4).
- `terreno_prato_f.png` — con piccole zolle di terra e fili secchi radi.
  Media (114,8, 121,9, 35,2).
- `terreno_prato_g.png` — standard, la più vicina al prato v2.
  Media (114,0, 121,4, 35,8).
- `terreno_prato_h.png` — verde più profondo/smeraldo, fili fini.
  Media (87,3, 118,0, 33,2).

Verifica (misurata): alpha minimo = 255 ovunque (opache). Discontinuità alla
cucitura (differenza media tra bordo destro/sinistro e tra bordo alto/basso)
confrontata con la discontinuità media tra colonne/righe interne: rapporto
tra 0,47 e 0,76 per tutte e 6 — la cucitura è più liscia delle normali
transizioni interne, non un outlier. Prova a vista nel foglio di controllo
(ripetizione 2×2 di prato_e e prato_h): nessuna linea di giunzione visibile.

## C) Dettagli sparsi — 256×256, RGBA, piccoli e centrati

Contenuto minuto al centro (zona ~60–196 px), angoli completamente
trasparenti (alpha max agli angoli = 0 per tutti), niente ombre: sono
accenti da sparpagliare sul prato, non oggetti.

- `dettaglio_fiori_a/b/c.png` — ciuffetti di fiorellini: a bianchi (centro
  giallo), b gialli (centro arancio), c viola (centro chiaro).
- `dettaglio_ciuffi_a/b/c.png` — ciuffi d'erba alta, forme e densità diverse.
- `dettaglio_sassi_a/b/c.png` — 2–3 sassolini grigi.
- `dettaglio_funghi_a.png` — funghetti rossi a puntini bianchi;
  `dettaglio_funghi_b.png` — funghetti marroni/crema.
- `dettaglio_foglie_a/b.png` — foglie cadute e un rametto.
- `dettaglio_impronte_a.png` — eccezione alla regola «centrato»: sentierino
  di terra battuta stretto (~52 px) e curvo a S che attraversa il riquadro
  toccando i bordi SINISTRO e DESTRO (così si può affiancare), bordi della
  striscia sfumati, impronte ellittiche leggere in coppie alternate lungo il
  percorso; angoli e resto del riquadro trasparenti.

Verifica (misurata): bounding box del contenuto (alpha>10) dei 13 dettagli
puntuali tutti dentro x 61–185, y 74–163; impronte: bbox (0,39)–(255,216)
per la striscia passante, angoli a 0.

## D) Bordi delle zone — 512×512, RGBA

- `bordo_sabbia_lago_a.png`, `bordo_sabbia_lago_b.png` — anello di riva da
  mettere intorno a un lago: centro trasparente (alpha = 0 nel disco r=100:
  ci sta l'acqua), fascia ad anello di sabbia dorata che vira al fango verso
  l'esterno (alpha max 255 nella fascia), bordo interno sfumato leggermente
  verso il centro, bordo esterno che sfuma gradualmente fino ad alpha 0 al
  perimetro (misurato: 0). Forma dell'anello irregolare/organica, non un
  cerchio perfetto. Le due varianti differiscono per forma del foro e
  proporzione sabbia/fango.

## Foglio di controllo

`controllo/prova_terreno.png` (1100×8610): scena composta su prato pieno
(prato_g) con lago + bordo_sabbia_lago_a, chiazze terra/erba secca/fango/
sassi/sabbia, sentierino e dettagli sparsi; striscia di ripetizione 2×2 di
prato_e e prato_h; griglia di tutti i 36 pezzi a misura intera con etichette
(le chiazze su fondo verde scuro per leggere la sfumatura alpha).

## Formato di consegna

Ogni PNG ha accanto il suo `nome.png.b64` (base64 su una sola riga, da
decodificare per riottenere il PNG identico byte per byte — verificato su
tutti i 37 file, controllo incluso). `elenco.txt` contiene i 36 nomi in
ordine A→D. Dimensioni .b64: totale consegna ~6,6 MB (il più grande è
terreno_prato_h.png.b64, ~495 KB); il foglio di controllo da solo è
~6,8 MB in .b64 e può viaggiare separato.

## Cosa NON deve cambiare

- Nomi file e misure (512×512 per A/B/D, 256×256 per C).
- Le maschere alpha: chiazze e bordi lago devono mantenere perimetro a 0 e
  sfumature morbide; i prati B devono restare opachi e toroidali (ogni
  ritocco a un prato B va fatto replicando gli elementi traslati di ±512,
  altrimenti tornano le giunture).
- La tinta di famiglia del prato v2 per i prati B (medie dichiarate sopra).

## Limiti onesti

- Le texture sono procedurali (rumore morbido e tratti): a piena risoluzione
  sono un po' meno «a pennellata» del prato v2 dipinto, pur restando nella
  stessa tinta satura e senza contorni; alla scala di gioco la differenza
  si attenua molto.
- I ciuffi d'erba alta (dettaglio_ciuffi_*) sono i pezzi più stilizzati:
  fili vettoriali regolari, si leggono bene come accenti piccoli ma sono
  meno morbidi del resto.
- Le ondine sulla sabbia sono molto tenui (scelta prudente per non creare
  contorni); a dimensione di casella quasi non si vedranno.
- `terreno_terra_a` ha una silhouette un po' «stellata» e `terreno_fango_a`
  un po' triangolare: restano organiche e si mescolano bene sul prato, ma
  sono le due forme meno tondeggianti del set.
- Rotazione dei prati B: l'affiancamento a pari orientamento è continuo
  pixel per pixel; tra copie ruotate diversamente non si vede alcuna linea
  (densità e tono uniformi fino al bordo), ma i singoli fili non proseguono
  pixel-esatti attraverso una giunzione ruotata.

STATO: pronto
