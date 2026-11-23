# Pannello del menu — cornice rifatta (v2)

Questa cartella sostituisce **solo** `menu_pannello.png` della consegna
`muse/2026-11-23-menu/`. Stesso nome, stessa misura, stesso margine:
per Claude è un puro scambio di file, **non cambia nient'altro** —
nessun altro asset del menu è toccato.

Motivo: nella v1 la cornice era venuta come fasce marroni piatte con
una striscia sottile a rombi, diversa dalla bozza 1 «Mare dipinto»
approvata da Davide. Qui la cornice è ridisegnata come nella bozza.

## Il file

- `menu_pannello.png` — 1140×1680, raggio angoli 48, **margine di
  taglio 9-parti 84 px su tutti i lati** (invariato). Maschera alpha
  **identica al pixel** a quella della v1 (0 px diversi): la sagoma
  non cambia di un pixel.
- Interno teal invariato rispetto alla v1: gradiente verticale
  confinato ai margini (`#1a6a80` → centro piatto `#14586b` →
  `#0e4256`), così l'allungamento a 9 parti non crea cuciture.

## La nuova cornice (tutta dentro il margine di 84 px)

Disegno a programma (Python/PIL, supersampling 3×), pensato per
leggersi come la cornice dipinta della bozza:

- **Legno dipinto, non tinta unita**: base multi-tono (marroni caldi
  `#7d5836` / `#6b4a2c` / `#5a3d22` / `#86643f` con variazione a bassa
  frequenza), ~1160 venature lungo la fascia (scure e chiare, alpha
  basso), scanalature longitudinali a doghe, **giunti di segmento**
  attraverso la fascia (a x = 285, 570, 855 e y = 420, 840, 1260, come
  i pali della bozza), nodi del legno negli angoli, bisello chiaro sul
  filo esterno e profili scuri `#4a3016`–`#2e1c0c`.
- **Corda spessa che corre lungo tutta la cornice**: cordone da
  ~34 px centrato a 42 px dal bordo, reso con segmenti ritorti
  (striscia diagonale, solco scuro, luce da alto-sinistra e ombra da
  basso-destra su ogni segmento) e **ombra portata morbida sul legno**
  sotto la corda. Il legno resta visibile su entrambi i lati del
  cordone (fascia esterna e fascia interna).
- **Legature agli angoli**: a ogni angolo, 3 giri di corda
  perpendicolari alla bisettrice attraversano la cornice e collegano
  i due cordoni laterali, più un nodo sul vertice — come le legature
  della bozza. Stanno dentro i margini di 84 px (zone che non si
  stirano); la parte centrale dei bordi, che si allunga, è solo legno
  con venature e cordone continuo, quindi lo stretch non deforma
  nessun elemento disegnato.

Nessuna scritta in nessun file. **Niente viola**: scansione del
pannello e del foglio di controllo — 0 pixel con tonalità 260–345° e
saturazione ≥0,08.

## Verifiche eseguite

- Misura esatta 1140×1680; decodifica `.b64` byte-identica per
  entrambi i file in `elenco.txt`.
- Maschera alpha contro la v1: **0 px diversi**.
- Stretch a 9 parti ×1,5 in larghezza e ×0,7 in altezza
  (1710×1176): angoli **0 px diversi**; gradino dentro il teal piatto
  alle cuciture **0**; il gradino massimo sul bordo di disegno
  cornice/teal è 100 (nella v1 era 138–143 allo stesso punto): è il
  bordo stesso della cornice, non un difetto di allungamento.
- Anti-viola: 0 pixel in banda 260–345° (sat ≥0,08, alpha ≥128) in
  entrambi i file.

## Controllo

`controllo/prova_pannello_v2.png` — a sinistra il pannello nuovo in
grande sullo `sfondo_menu.png` consegnato con il menu; a destra i
dettagli al 100% di un angolo e di un bordo, **prima** (v1) e
**dopo** (v2) a confronto: la differenza tra fascia piatta e
legno+corda si vede a colpo d'occhio.

## Cosa NON deve cambiare

- Nome, misura, raggio e margine 9-parti (84 px): sono quelli della
  v1, il codice di Claude li usa già.
- La maschera alpha: se la cornice viene ritoccata, la sagoma resta
  questa.

## Per Claude

Sostituisci il file `menu_pannello.png` del menu con quello di
questa cartella (decodifica il `.b64`). Tutto il resto della
consegna `2026-11-23-menu/` resta valido e invariato, compreso il
suo LEGGIMI per misure, palette e corrispondenze dei pezzi.

STATO: pronto
