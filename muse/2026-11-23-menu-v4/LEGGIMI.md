# Gruppo 13 — Menu iniziale rifatto da zero (v4)

Nuova grafica della schermata iniziale, stile bozza 1 «Mare dipinto»,
ma con tutti i pezzi **disegnati nuovi e puliti alle misure esatte del
gioco** (niente ritagli dalla bozza: la v3 estratta aveva il rettangolo
teal dietro il vulcano, la fascia scura agli angoli e i bottoni col
bordo basso tagliato). Questo set **sostituisce interamente** i set
menu `2026-11-23-menu` (v1), `2026-11-23-menu-v2` e
`2026-11-23-menu-v3`.

**NESSUNA scritta, lettera o numero in nessun file**: tutti i testi li
scrive il gioco (Fredoka 600 per titoli e bottoni). Le uniche scritte
compaiono nel foglio di controllo, che è una prova di composizione.
Ogni PNG è affiancato dal suo `nome.png.b64` (base64 su una sola riga):
decodificarlo per ottenere il PNG identico byte per byte. Ordine dei
file in `elenco.txt`. Misure a 3× rispetto ai px CSS. Pezzi UI disegnati
a programma (Python/PIL, supersampling): bordi e raggi precisi al pixel
e stati con maschera alpha identica.

## Palette

- Teal pannello piatto `#14586b`; velo sullo sfondo `#0e2433`
- Legno cornice `#6b4a2c`–`#7d5836` con venature; corda `#c9a86a`,
  luce `#dec084`, ombra `#a37f45`, profili `#4a3016`
- Oro bottoni: alto `#f8cd76`, centro `#f2b84b`, basso `#eda63a`,
  bordo `#b57e1e`, alone pulsante `#ffe9b0`
- Vetro di mare: alto `#57a7b5`, centro `#2e7f8f`, basso `#256b78`,
  bordo `#8fd0da`; sezione più scura `#256b7a` → `#1b5566`, filo
  `#3d8a99`
- Campo mappa: fondo `#0b2a3a`, filo `#2a6a7d`
- Freccia `#0d3b47`

## File

### Sfondo — opaco

- `sfondo_menu.png` — 1236×2640. NUOVO soggetto: la **mappa di gioco**
  dall'alto in leggera prospettiva — campo a caselle erbose arrotondate
  e separate come il terreno del gioco, boschetti di pini, montagne
  innevate in alto, due laghetti, **due stazioni meteo** con le coppe
  dell'anemometro, il **vulcano al centro**, la **base con bandiera ORO
  in basso** e la **base con bandiera BLU ACCIAIO in alto**, qualche
  pedina in lontananza, vortici di vento e nebbia leggera ai bordi.
  Sulla zona del pannello (x 48–1188, y 300–2350) è steso un velo
  morbido `#0e2433` (alpha massimo 0,5, rampe coseno su tutti i lati).
  Luminanza misurata nella zona pannello: **media 110,0, deviazione
  standard 39,1**; media dell'intera immagine 126,7. Nota: i valori
  sono più alti che nel Gruppo 6 perché qui il pannello è **opaco**:
  il velo serve a staccare i bordi del pannello, non a rendere
  leggibile il testo sopra lo sfondo.

### Pannello — ridimensionabile a 9 parti

- `menu_pannello.png` — 1140×1680, **margine di taglio 9-parti 200 px
  su tutti i lati**. Cornice di legno con legature di corda nello stile
  della bozza (pali segmentati con giunti, corda ritorta spessa ~34 px
  lungo tutto il bordo interno della fascia, legature con nodo ai 4
  angoli e giri singoli vicino agli angoli lungo i lati). Interno
  **teal piatto `#14586b`** (nessuna sfumatura: il centro resta
  identico a qualsiasi allungamento). **Fuori dalla cornice è tutto
  trasparente** (alpha 0 ai vertici della tela, verificato): niente
  fascia scura, angoli arrotondati puliti. Il centro del bordo
  superiore è **libero e retto**: lì il gioco appoggia il simbolo.
  Nota di costruzione: per tenere tutta la cornice dentro il margine
  da 200 px, la fascia legno+corda occupa i ~110 px esterni e il resto
  del margine è teal piatto — il margine resta comunque 200 px.
  Prova eseguita: allungamento a 9 parti ×1,5 in larghezza e ×0,7 in
  altezza (1710×1176) → angoli **0 px diversi** dall'originale e centro
  con **un solo colore** (`#14586b`, gradino 0).

### Simbolo del titolo — trasparente

- `menu_simbolo.png` — 512×512. Arco di legno e corda con legature,
  vulcano in eruzione sull'isoletta oro con una palma per lato, base di
  mare con archi di spuma il cui bordo inferiore **sfuma** in
  trasparenza. **Ancora: il centro verticale della tela (y = 256) sta
  sul bordo superiore del pannello** (la linea di galleggiamento
  dell'isola è a y = 256); nel gioco è largo 150 px CSS. Sagoma pulita:
  tutto ciò che non è arco/isola/mare è trasparente — **nessun
  rettangolo e nessun alone dietro**, verificato componendo il simbolo
  su fondo cielo chiaro e su fondo scuro al 200%. Disegno dipinto
  generato su fondo croma verde e scontornato a programma con
  de-spill (ricostruzione del colore del soggetto sui pixel
  semi-trasparenti): residui 26 pixel semi-trasparenti vicini al verde
  chiave sui bordi delle foglie, invisibili nelle prove su cielo e su
  scuro.

### Bottoni oro primari («Continua partita», «Gioca contro il computer»)

1020×216, raggio 54, **anche a 9 parti con margine 60 px**. Bordo
`#b57e1e`, luce in alto, **ombra morbida sotto il bottone disegnata
dentro il file**: il bottone visibile è alto **166 px** (fascia
pienamente opaca misurata 165 px, y 17–181), con ~16 px di margine
sopra e ~34 px sotto per l'ombra — **il bordo basso è intero, niente è
tagliato dalla tela**. Il testo del gioco (Fredoka 600, 21 px,
`#3a2503`, anche su due righe per «Continua partita · round N · mappa
NNNNNNNNN») sta dentro i 166 px.

- `menu_bottone_oro_normale.png`
- `menu_bottone_oro_premuto.png` — stessa maschera, colori scuriti ×0,75
- `menu_bottone_oro_disattivo.png` — desaturato (saturazione ~40%) e
  spento ×0,85
- `menu_bottone_oro_pulsante.png` — normale + alone morbido `#ffe9b0`
  solo dentro la forma, lungo il bordo interno

### Bottoni in vetro di mare («Tutorial», pulsanti delle Impostazioni)

1020×180, raggio 45, **a 9 parti con margine 60 px** (il Tutorial nel
gioco è largo il 62% — 210 px CSS — e si allunga senza deformare i
bordi). Bordo `#8fd0da`, stessa cura per l'ombra interna alla tela:
bottone visibile alto **138 px** (fascia opaca misurata 137 px).

- `menu_bottone_vetro_normale.png`, `menu_bottone_vetro_premuto.png`,
  `menu_bottone_vetro_disattivo.png` (stesse regole di stato degli oro)

### Selettore di difficoltà

318×150, raggio 45, bordo basso intero (bottone visibile 126 px,
fascia opaca misurata 125 px). Testo del gioco: Fredoka 600, 16 px;
`#3a2503` sul selezionato, `#0d3b47` sugli altri.

- `menu_difficolta_selezionato.png` — oro, stessa ricetta dei primari
- `menu_difficolta_normale.png` — vetro di mare
- `menu_difficolta_premuto.png` — il normale premuto (×0,75)

### Campo e sezioni

- `menu_campo_mappa.png` — 1020×162, raggio 40. Campo di testo vuoto:
  fondo incassato `#0b2a3a`, ombra interna in alto, filo `#2a6a7d`.
  Testo del gioco (segnaposto e numeri): Fredoka 600, 16 px,
  `#d9eef2`, centrato.
- `menu_sezione.png` — 1020×162, raggio 40. Riga di sezione
  espandibile: vetro di mare più scuro, filo `#3d8a99`. **Nessuna
  freccia disegnata**: la mette il gioco con il file qui sotto. Testo
  del gioco: Fredoka 600, 16 px, `#0d3b47`, allineato a sinistra con
  18 px CSS di margine.
- `menu_sezione_aperta.png` — **nuovo**: la stessa riga con i due
  **angoli bassi dritti** (raggio 0 in basso, 40 in alto), per quando
  la sezione è aperta e sotto compare il riquadro scuro dei contenuti.
  Differisce da `menu_sezione.png` solo negli angoli bassi (1.184 px,
  righe 117–158): è l'unico pezzo con maschera diversa, dichiarata.
- `icona_freccia_giu.png` — 96×96 trasparente. Chevron ▼ pieno, teal
  scuro `#0d3b47`. Il gioco la posiziona a destra nella riga e la
  **ruota di 180°** quando la sezione è aperta.

## Testi che scrive il gioco (riferimento colori/misure)

Titolo «Isole al Vento»: Fredoka 600, 40 px CSS, oro `#f7c452` con
ombra `#9a5f14`. Motto: 14 px, `#d9eef2`, due righe centrate. Riga di
stato: 13 px, `#b4dbe2`. Link «Novità e registro modifiche»: 14 px,
oro chiaro `#f4cf7a`, sottolineato. Bottoni oro: Fredoka 600, 21 px,
`#3a2503`. Vetro di mare: Fredoka 600, 19 px, `#0d3b47`.

## Verifiche eseguite

- Misure esatte di tutti i 17 asset (tabella sopra) e decodifica
  `.b64` byte-identica per tutti i 18 file in `elenco.txt`.
- Maschere alpha degli stati: **0 px diversi** in ogni gruppo
  (oro ×4, vetro ×3, difficoltà ×3).
- **Niente viola**: scansione di ogni file — 0 pixel con tonalità
  260–345° e saturazione ≥0,08 (pixel visibili, alpha ≥128). Lo sfondo
  generato conteneva 3.555 pixel di banda nelle ombre mauve delle
  montagne: corretti ruotando la tonalità a 225° (famiglia del blu
  acciaio) a parità di saturazione e luminanza, residui 0. Nota di
  consegna: per stare nei limiti di dimensione dell'invio, il file
  `sfondo_menu.png` consegnato ha una sfocatura leggera (raggio 1 px,
  invisibile alla scala del telefono: l'immagine è a 3×) e la
  correzione anti-viola è stata riapplicata dopo (1.058 pixel),
  scansione finale a piena risoluzione: 0 pixel di banda. Nel foglio
  di controllo 43 pixel da ricampionamento sono stati corretti allo
  stesso modo. L'avversario è blu acciaio ovunque (bandiera in alto).
- Stretch a 9 parti del pannello: vedi sopra (angoli 0 px, centro
  piatto). Pannello: alpha 0 fuori dalla cornice, nessun alone scuro.
- **Controllo al 200% di ogni pezzo** (script e tavole in `lavoro/`):
  angolo e corda del pannello, simbolo su cielo e su scuro, bordo
  basso dei bottoni oro e vetro, angolo basso della sezione aperta,
  difficoltà e campo — niente fasce, rettangoli, bordi tagliati o
  fantasmi di lettere.

## Istruzioni per Claude

- Questo set (v4) sostituisce **solo la schermata iniziale** e
  rimpiazza per intero i set menu v1, v2 e v3. I pannelli e i bottoni
  di gioco del Gruppo 5 e gli altri sfondi del Gruppo 6 restano in uso.
- Tutti i testi li scrive il gioco in Fredoka: negli asset non c'è
  nulla da ritagliare.
- Corrispondenze: simbolo → `menu_simbolo.png` centrato sul bordo
  superiore del pannello con **y = 256 (metà tela) sulla linea del
  bordo**; Facile/Normale/Difficile → `menu_difficolta_*`;
  «Continua partita» e «Gioca contro il computer» →
  `menu_bottone_oro_*`; campo «Mappa n.» → `menu_campo_mappa.png`;
  «Tutorial» e i pulsanti delle Impostazioni (Suoni, Vibrazione,
  Musica) → `menu_bottone_vetro_*`; sezioni → `menu_sezione.png` da
  chiuse e `menu_sezione_aperta.png` da aperte, con
  `icona_freccia_giu.png` a destra (rotazione 180° da aperta).
- Margini di taglio a 9 parti: **pannello 200 px**, **bottoni oro e
  vetro 60 px**. Non usare margini diversi: cornice, ombre e raggi
  stanno dentro questi margini.
- Per l'animazione «pulsante» alternare normale/pulsante o modulare
  l'opacità del pulsante, come nel Gruppo 5.

## Controllo

`controllo/prova_menu_v4.png` — menu completo composto **solo** con
gli asset di questa consegna sullo sfondo nuovo, a 412×880 CSS
ingrandito 2× (824×1760), con i testi abituali scritti sopra come
prova di impaginazione (resi in DejaVu Sans, il Fredoka non è
disponibile a Muse; **non fanno parte degli asset**). Sotto, striscia
di dettagli ingranditi: simbolo su cielo, angolo del pannello 1:1,
bordi bassi di bottone oro e vetro e angolo della sezione aperta 1:1.

## Cosa NON deve cambiare

- Misure, raggi e margini 9-parti dichiarati (pannello 200 px,
  bottoni 60 px).
- Le maschere alpha degli stati di un bottone devono restare
  identiche: se uno stato viene rifatto, vanno rifatti tutti gli
  stati del gruppo (unica eccezione dichiarata: `menu_sezione_aperta`,
  che ha gli angoli bassi dritti per costruzione).
- L'ancora del simbolo (y = 256 sul bordo superiore del pannello) e la
  trasparenza fuori dalla cornice del pannello.
- Nessuna scritta dentro i PNG: i testi restano scritti dal gioco.
- Niente viola/magenta in nessun pezzo: la squadra avversaria è blu
  acciaio.

## Nuovo rispetto alle consegne precedenti

Set menu alla quarta versione, ridisegnato da zero dopo i difetti
della v3 in gioco: pezzi puliti alle misure reali della versione 38 e
oltre (bottoni oro 1020×216 con ombra interna alla tela, vetro
1020×180, difficoltà 318×150, campo e sezioni 1020×162, nuovo pezzo
`menu_sezione_aperta`), simbolo senza rettangolo dietro e sfondo nuovo
con la mappa di gioco al posto della veduta mare/cielo.

STATO: pronto
