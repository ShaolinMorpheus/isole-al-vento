# Gruppo 14 — Menu iniziale v5: lettere dipinte e bordi rifiniti

La struttura del menu v4 (Gruppo 13) era giusta, ma i testi scritti dal
gioco in Fredoka sembravano «da app» e i contorni dei pezzi erano troppo
puliti e digitali rispetto alla bozza 1 «Mare dipinto». Questa consegna
rifà **tutta la grafica del menu** con l'aspetto dipinto a mano della
bozza:

- le **scritte fisse diventano immagini** con lettering dipinto (un
  unico carattere coerente: corpo pieno e tondo, riempimento ad
  acquerello con luce in alto e ombra in basso, contorno marrone scuro
  irregolare dove serve);
- **tutti i pezzi** sono ridisegnati con la stessa geometria, misure e
  margini della v4, ma con finitura dipinta: contorno marrone scuro
  `#4a3016` a tratto di pennello (spessore leggermente irregolare) su
  ogni pezzo, luce dipinta in alto, ombra morbida in basso, texture di
  acquerello (macchie e grana) al posto dei gradienti lisci;
- il **pannello** tiene la costruzione della v6 (pali sottili + legature
  diagonali grosse ripetute su tutto il perimetro, zona simbolo libera
  in alto al centro), con venature più grosse e meno ripetute e
  **legature tutte diverse** (forma e angolo variano a ogni posizione);
- lo **sfondo** è quello della v4 (mappa di gioco) ma **senza la
  sfocatura da 1 px** della consegna precedente: è nitido (vedi la
  deroga sul formato qui sotto).

Questo set **sostituisce interamente** i pezzi menu della v4
(`2026-11-23-menu-v4`) e il pannello della v6 (`2026-11-23-menu-v6`).
Ogni file è affiancato dal suo `.b64` (base64 su una sola riga):
decodificarlo per ottenere il file identico byte per byte. Ordine dei
file in `elenco.txt`. Misure a 3× rispetto ai px CSS.

## A) Lettering dipinto — PNG trasparenti

Un unico alfabeto dipinto per tutte le scritte. Le lettere sono
disegnate una a una: il titolo ha una leggera curvatura e oscillazione
vivace come nella bozza; i testi piccoli restano puliti e dritti per la
leggibilità. Prova eseguita: ogni scritta è stata ridotta alla sua
misura CSS (÷3) e riletta — **tutte le parole si leggono chiaramente**,
anche a 16 px CSS. Sfondo trasparente (alpha 0 ai vertici di ogni
tela); la colonna «testo nella tela» dà il riquadro reale delle lettere
(alpha bbox) in px a 3×, così il gioco può allineare il testo visibile
e non la tela.

| File | Testo | Tela (3×) | Testo nella tela (x0,y0–x1,y1) |
|---|---|---|---|
| `menu_titolo.png` | «Isole al Vento» | 1020×240 | 48,62 – 975,187 |
| `menu_t_gioca.png` | «Gioca contro il computer» | 900×150 | 39,43 – 862,107 |
| `menu_t_tutorial.png` | «Tutorial» | 420×120 | 22,23 – 394,97 |
| `menu_t_facile_oro.png` | «Facile» su oro | 270×120 | 55,38 – 217,82 |
| `menu_t_facile_vetro.png` | «Facile» su vetro | 270×120 | 55,38 – 217,82 |
| `menu_t_normale_oro.png` | «Normale» su oro | 270×120 | 18,39 – 254,81 |
| `menu_t_normale_vetro.png` | «Normale» su vetro | 270×120 | 18,39 – 254,81 |
| `menu_t_difficile_oro.png` | «Difficile» su oro | 270×120 | 23,38 – 249,82 |
| `menu_t_difficile_vetro.png` | «Difficile» su vetro | 270×120 | 23,38 – 249,82 |
| `menu_t_comesigioca.png` | «Come si gioca» | 700×120 | 199,35 – 500,84 |
| `menu_t_impostazioni.png` | «Impostazioni e prove grafiche» | 700×120 | 24,35 – 678,84 |

Colori: titolo oro dipinto `#f7c452` con luce `#ffe08a` in alto, ombra
`#9a5f14` in basso e contorno spesso irregolare `#4a3016`. Testi su
bottoni oro: marrone scuro `#3a2503` con una linea di luce chiara in
alto. Testi su vetro di mare: `#0d3b47` con riflesso chiaro in alto.
Etichette delle sezioni: chiare `#e4f4f7` con contorno sottile
`#0b2a3a` (le righe di sezione sono scure). Le tre parole di difficoltà
hanno la **stessa taglia di carattere** tra loro, e le due etichette di
sezione pure: l'aspetto è coerente anche se le tele hanno larghezze
diverse. Le versioni `_oro` delle difficoltà vanno sul pezzo
`menu_difficolta_selezionato.png`, le `_vetro` su
`menu_difficolta_normale.png` e `menu_difficolta_premuto.png`.

### Come centrare ogni scritta

Il centro del testo visibile è quasi sempre il centro della tela:
scostamenti misurati ≤ 2 px (titolo: +1,5 px in x, +4,5 px in y per via
dell'ombra sotto le lettere; tutorial: −2 px in x). Regole pratiche:

- **Titolo**: centrare la tela (340×80 px CSS) in orizzontale sul
  pannello; il testo risulta centrato da sé.
- **Gioca / Tutorial / difficoltà**: centrare la tela della scritta sul
  centro dell'**area visibile** del bottone (non della sua tela
  intera, che include l'ombra sotto). Aree visibili misurate sui nuovi
  pezzi (fascia pienamente opaca, coordinate nella tela del bottone):
  - bottone oro 1020×216: righe **16–181**, altezza visibile **166 px**,
    centro a **y = 98,5** (9,5 px sopra il centro tela);
  - bottone vetro 1020×180: righe **14–151**, altezza visibile
    **138 px**, centro a **y = 82,5** (7,5 px sopra il centro tela);
  - difficoltà 318×150: righe **8–133**, altezza visibile **126 px**,
    centro a **y = 70,5** (4,5 px sopra il centro tela).
  In orizzontale l'area visibile è centrata nella tela: basta centrare
  anche la scritta.
- **Etichette di sezione**: la riga `menu_sezione.png` è alta 162 px
  senza ombra esterna: centrare la tela della scritta (700×120) in
  verticale sulla riga. In orizzontale il testo del gioco parte a
  18 px CSS dal bordo sinistro della riga: per allineare lì il testo
  visibile, posizionare la tela in modo che il suo «testo nella tela»
  (colonna x0, divisa per 3) cada a 18 px CSS — cioè tela di
  «Come si gioca» con il bordo sinistro **48,3 px CSS a sinistra**
  dell'inizio riga (il testo è centrato nella sua tela), tela di
  «Impostazioni e prove grafiche» con il bordo sinistro **10 px CSS a
  destra** dell'inizio riga. In alternativa, centrare la tela nella
  riga: il testo resta comunque dentro la riga in entrambi i casi.

### Testi che restano al gioco (NON sono in questa consegna)

«Continua partita · round N · mappa N», il segnaposto del campo mappa
(«Mappa n. (vuoto = a caso)»), i testi lunghi del «Come si gioca», i
valori delle impostazioni (Suoni: accesi, ecc.), il motto sotto il
titolo, la riga di stato («Nessuna partita a questo livello.») e il
link «Novità e registro modifiche». Nel foglio di controllo sono resi
in un carattere semplice come segnaposto di impaginazione.

## B) Pezzi rifiniti — stesse misure e margini della v4

Geometria, raggi, margini 9-parti e maschere sono quelli della v4;
cambia solo la finitura (contorno `#4a3016` irregolare su tutti i
pezzi, texture acquerello, luce/ombra dipinte). Il bordo basso resta
intero: l'ombra è disegnata dentro la tela.

- `menu_pannello.png` — 1140×1680, **margine 9-parti 200 px**. Cornice
  della v6 (pali sottili sul filo del teal, legature diagonali grosse
  su tutto il perimetro, incroci con nodo agli angoli, centro del lato
  superiore libero per il simbolo) con finitura dipinta: venature più
  grosse, legature mai uguali tra loro, contorno scuro irregolare
  attorno alla sagoma. Interno teal con una **leggerissima texture
  acquerello** (colore medio misurato `#14586b`, deviazione standard
  sotto 1 livello: a occhio resta il teal piatto della v4/v6). Fuori
  dalla cornice tutto trasparente (alpha 0 ai vertici, verificato).
  Prova di allungamento a 9 parti (×1,5 larghezza, ×0,7 altezza):
  angoli **0 px diversi** e **nessun gradino al centro** — il gradiente
  misurato a cavallo delle cuciture (2 livelli) è uguale al gradiente
  interno della texture: la texture è continua, non c'è una cucitura.
  Nota: allungando il pannello, la distanza tra le legature centrali
  dei lati si allarga come nella v6.
- `menu_simbolo.png` — 512×512. Stesso soggetto della v4 (arco di legno
  e corda con legature, vulcano in eruzione sull'isoletta oro, mare che
  sfuma in basso, **nessun rettangolo dietro**) con finitura dipinta:
  texture dentro la sagoma e contorno scuro morbido sotto arco e
  isola, che sfuma insieme al mare. **Ancora invariata: y = 256 sul
  bordo superiore del pannello** (linea di galleggiamento a y = 256,
  verificata).
- Bottoni oro 1020×216, raggio 54, **9 parti margine 60**:
  `menu_bottone_oro_normale.png`, `_premuto.png` (colori ×0,75),
  `_disattivo.png` (desaturato ~40%, ×0,85), `_pulsante.png` (alone
  `#ffe9b0` interno). Visibile 166 px (vedi sopra).
- Bottoni vetro 1020×180, raggio 45, **9 parti margine 60**:
  `menu_bottone_vetro_normale.png`, `_premuto.png`, `_disattivo.png`.
  Visibile 138 px.
- Difficoltà 318×150, raggio 45: `menu_difficolta_selezionato.png`
  (oro), `menu_difficolta_normale.png` (vetro),
  `menu_difficolta_premuto.png` (normale ×0,75). Visibile 126 px.
- `menu_campo_mappa.png` — 1020×162, raggio 40: fondo incassato
  `#0b2a3a` con ombra interna in alto, filo `#2a6a7d`, contorno dipinto.
- `menu_sezione.png` — 1020×162, raggio 40: vetro di mare più scuro,
  filo `#3d8a99`, contorno dipinto. Nessuna freccia disegnata.
- `menu_sezione_aperta.png` — come la sezione ma con gli **angoli
  bassi dritti** (raggio 0 in basso): è l'unico pezzo con maschera
  diversa, come nella v4.
- `icona_freccia_giu.png` — 96×96: chevron `#0d3b47` con vertici
  leggermente irregolari e filo di contorno dipinto; il gioco la ruota
  di 180° con la sezione aperta.

### Sfondo — DEROGA dichiarata sul formato

- `sfondo_menu.webp` — 1236×2640, **WebP senza perdita (lossless)**.
  Stessa immagine della v4 (mappa di gioco dall'alto: caselle erbose,
  pini, montagne innevate, laghetti, due stazioni meteo, vulcano al
  centro, base oro in basso e base blu acciaio in alto, velo `#0e2433`
  alpha max 0,5 sulla zona pannello x 48–1188, y 300–2350; luminanza
  zona pannello: media 110,0, deviazione 39,2), ma **senza la sfocatura
  da 1 px** che la consegna v4 aveva applicato per stare nei limiti di
  invio: questa è nitida. Il PNG senza perdita dell'immagine nitida
  peserebbe 5.624.368 caratteri in base64, sopra il limite pratico di
  invio (~4,8 MB); il WebP lossless pesa 4.148.776 caratteri in base64
  ed è **identico pixel per pixel** al PNG (verificato: 0 pixel diversi
  tra la decodifica del WebP e l'immagine sorgente). Android legge il
  WebP nativamente; in alternativa il gioco può decodificarlo in PNG
  senza perdere nulla. Correzione anti-viola applicata sull'immagine
  nitida: 4.940 pixel ruotati alla famiglia del blu acciaio (225°),
  scansione finale 0 pixel di banda.

## Verifiche eseguite

- Misure esatte di tutti i 28 asset + foglio di controllo; decodifica
  `.b64` byte-identica per tutti i 29 file in `elenco.txt`.
- **Maschere alpha degli stati: 0 px diversi** in ogni gruppo
  (oro ×4, vetro ×3, difficoltà ×3) — gli stati derivano dallo stesso
  disegno base con trasformazioni che non toccano l'alpha.
- **Niente viola**: scansione a piena risoluzione di ogni file —
  0 pixel con tonalità 260–345° e saturazione ≥0,08 (pixel con
  alpha ≥128; sfondo: tutti). Anche il foglio di controllo è a 0
  (163+256 pixel da ricampionamento corretti allo stesso modo).
- Lettering: alpha 0 ai vertici di ogni tela; riquadro delle lettere
  con almeno 16 px di margine dalla tela in ogni file (nessuna lettera
  tagliata); prova di leggibilità a misura CSS (÷3) superata per tutte
  le scritte.
- Pannello: stretch 9-parti con angoli a 0 px e nessun gradino centrale
  (vedi sopra); alpha 0 fuori dalla cornice.
- Simbolo: composto su fondo cielo chiaro e su fondo scuro al 200% —
  nessun rettangolo, nessun alone; la linea di galleggiamento è a
  y = 256.
- **Controllo al 200% di ogni pezzo**: angoli e legature del pannello,
  bordi bassi di bottoni oro/vetro/difficoltà (interi, ombra dentro la
  tela), angolo basso della sezione aperta, campo, freccia, simbolo —
  niente bordi tagliati, rettangoli o fantasmi.

## Istruzioni per Claude

- Questo set sostituisce **solo la schermata iniziale**: pezzi v4 e
  pannello v6 sono superati. Pannelli/bottoni di gioco (Gruppo 5) e
  altri sfondi (Gruppo 6) restano in uso.
- Margini 9-parti: **pannello 200 px**, **bottoni oro e vetro 60 px**,
  come nella v4. Simbolo centrato sul bordo superiore del pannello con
  **y = 256 sulla linea del bordo**.
- Le scritte fisse NON vanno più scritte dal gioco: usare i file
  `menu_t_*.png` come immagini, centrati come descritto nella sezione
  A (sul centro dell'area visibile dei bottoni). I testi variabili
  elencati sopra restano scritti dal gioco.
- Corrispondenze invariate dalla v4: «Continua partita» e «Gioca
  contro il computer» → bottoni oro; «Tutorial» e pulsanti delle
  Impostazioni → bottoni vetro (Tutorial largo il 62%, taglio 9-parti);
  campo → `menu_campo_mappa.png`; sezioni → `menu_sezione.png` da
  chiuse e `menu_sezione_aperta.png` da aperte, con
  `icona_freccia_giu.png` a destra ruotata di 180° da aperta; le parole
  di difficoltà sono immagini: `_oro` sul selezionato, `_vetro` sugli
  altri due stati.
- Lo sfondo è `sfondo_menu.webp` (lossless, identico al PNG): se il
  pipeline richiede PNG, decodificarlo una volta e usare il PNG
  risultante.
- Per l'animazione «pulsante» alternare normale/pulsante o modulare
  l'opacità, come nella v4.

## Controllo

`controllo/prova_menu_v5.png` — menu composto a 412×880 CSS ingrandito
2× con **solo** gli asset di questa consegna: pezzi rifiniti e
lettering dipinto al posto dei testi fissi; i testi variabili sono
segnaposto in carattere semplice (non fanno parte degli asset).
Accanto, alla stessa altezza, la **bozza 1 «Mare dipinto»** per il
confronto diretto dell'aspetto dipinto. Il foglio è stato ridotto a
1500 px di larghezza per stare nei limiti di invio della sua `.b64`.

## Cosa NON deve cambiare

- Misure, raggi e margini 9-parti dichiarati (pannello 200 px,
  bottoni 60 px); le maschere alpha degli stati di un bottone restano
  identiche tra loro (unica eccezione dichiarata: `menu_sezione_aperta`).
- L'ancora del simbolo (y = 256) e la trasparenza fuori dalla cornice
  del pannello.
- Le scritte fisse sono immagini (`menu_t_*.png`): non riscriverle con
  un font e non ritagliare le tele (gli spazi trasparenti fanno parte
  del posizionamento descritto).
- Niente viola/magenta in nessun pezzo: la squadra avversaria è blu
  acciaio.

## Nuovo rispetto alle consegne precedenti

Menu alla quinta versione: lettering dipinto per tutte le scritte
fisse (novità assoluta: nella v4 le scriveva il gioco in Fredoka),
finitura dipinta a mano su tutti i pezzi (contorno `#4a3016`
irregolare, texture acquerello), pannello con la cornice della v6
rifinita (legature tutte diverse, venature più grosse), sfondo nitido
senza sfocatura consegnato in WebP lossless per i limiti di invio.

STATO: pronto
