# Menu principale ridisegnato («Mare dipinto»)

Nuova grafica della schermata iniziale, stile della bozza 1 «Mare dipinto»
approvata da Davide: pannello teal profondo con cornice di legno e corda,
bottoni oro corposi, bottoni secondari in vetro di mare, sfondo dipinto
con isola oro e isola blu.

**NESSUNA scritta, lettera o numero in nessun file**: tutti i testi li
scrive il gioco (font Fredoka), come per il Gruppo 5. Le uniche scritte
compaiono nel foglio di controllo, che è una prova di composizione (vedi
sotto), non un asset.

Ogni PNG è affiancato dal suo `nome.png.b64` (base64 su una sola riga):
decodificarlo per ottenere il PNG identico byte per byte. Ordine dei
file in `elenco.txt`. Misure a 3× rispetto ai px CSS, come il Gruppo 5.
Pezzi UI disegnati a programma (Python/PIL, supersampling 4×): bordi e
raggi precisi al pixel e stati con maschera alpha identica.

## Palette (campionata dalla bozza 1 approvata)

- Teal pannello: alto `#1a6a80`, centro piatto `#14586b`, basso `#0e4256`
  (nella bozza il teal misura circa `#16647a`–`#1d7182`)
- Legno cornice `#6b4a2c` / venature `#7d5836`; corda `#c9a86a` / ombra
  `#a37f45`, profili `#4a3016`
- Oro bottoni: alto `#f8cd76`, centro `#f2b84b`, basso `#eda63a`, bordo
  `#b57e1e`, alone pulsante `#ffe9b0`
- Vetro di mare: alto `#57a7b5`, centro `#2e7f8f`, basso `#256b78`, bordo
  `#8fd0da`; sezione: `#256b7a` → `#1b5566`, bordo `#3d8a99`
- Campo mappa: fondo `#0b2a3a`, bordo `#2a6a7d`
- Difficoltà non selezionata: fondo `#0d3547`, bordo `#2a6a7d`
- Fondo mare (velo sullo sfondo) `#0e2433`; freccia `#f2b84b`

## File

### Sfondo — opaco

- `sfondo_menu.png` — 1236×2640. Cielo luminoso con vortici di vento in
  alto, mare dipinto in basso, isola oro con palme in basso a sinistra,
  isola rocciosa blu acciaio con pini in basso a destra, piccolo vulcano
  lontano al centro sull'orizzonte. Sulla zona dove sta il pannello
  (y 300–2350) è steso un velo morbido `#0e2433` (alpha massimo 0,48,
  rampe coseno y 300→560 e 2090→2350). Luminanza misurata nel rettangolo
  del pannello (x 48–1188, y 300–2350): media 101,1, deviazione standard
  34,4; media dell'intera immagine 111,7. Nota: i valori sono più alti
  che nel Gruppo 6 perché qui il pannello è **opaco** (lì la scheda era
  semitrasparente): il velo serve a staccare i bordi del pannello, non a
  rendere leggibile il testo sopra lo sfondo.

### Pannello — ridimensionabile a 9 parti

- `menu_pannello.png` — 1140×1680, raggio angoli 48, **margine di taglio
  9-parti 84 px su tutti i lati**. Struttura del bordo (dentro il
  margine): fascia esterna di legno caldo con venature (0–46 px), linea
  di corda canapa con striature ritorte e profili scuri (46–84 px),
  interno teal. Il gradiente verticale del teal è confinato entro i
  margini: il centro è piatto `#14586b`, quindi l'allungamento non crea
  cuciture. Prova eseguita: allungamento a 9 parti ×1,5 in larghezza e
  ×0,7 in altezza (1710×1176) → angoli pixel-identici all'originale
  (0 px diversi); gradino massimo alle cuciture 138–143, uguale a quello
  dell'originale allo stesso punto (136–141): è il bordo di disegno tra
  corda e teal, che cade esattamente sul margine, non un difetto di
  allungamento; dentro il teal il gradino è 0.

### Simbolo del titolo — trasparente

- `menu_simbolo.png` — 512×512, contenuto 464×416 centrato. Isoletta oro
  dipinta: vulcano con pennacchio di fumo, una palma per lato, cespugli
  dorati, due vortici di vento bianchi. Va sopra il titolo scritto dal
  gioco. Ritagliato a programma da disegno dipinto su fondo verde
  (chroma key con despill): sui bordi possono restare aloni chiarissimi
  di 1 px, invisibili sul pannello teal.

### Bottoni oro primari («Continua partita», «Gioca contro il computer»)

1020×252, raggio 63, bordo `#b57e1e` da 10 px, luce interna in alto.

- `menu_bottone_oro_normale.png`
- `menu_bottone_oro_premuto.png` — stessa maschera, colori scuriti ×0,75
- `menu_bottone_oro_disattivo.png` — desaturato (saturazione ~40%) e
  spento ×0,85
- `menu_bottone_oro_pulsante.png` — normale + alone morbido `#ffe9b0`
  solo dentro la forma, lungo il bordo interno

### Bottoni secondari in vetro di mare («Tutorial»)

1020×216, raggio 54, bordo `#8fd0da` da 8 px.

- `menu_bottone_vetro_normale.png`, `menu_bottone_vetro_premuto.png`,
  `menu_bottone_vetro_disattivo.png` (stesse regole di stato degli oro)

### Selettore di difficoltà

330×156, raggio 48. In riga: un pezzo selezionato + due normali.

- `menu_difficolta_selezionato.png` — oro, stessa ricetta dei primari
- `menu_difficolta_normale.png` — teal scuro `#0d3547` con filo
  `#2a6a7d` e leggera ombra interna in alto
- `menu_difficolta_premuto.png` — il normale premuto (×0,75)

### Campo e sezioni

- `menu_campo_mappa.png` — 1020×192, raggio 48. Campo di testo vuoto:
  fondo incassato `#0b2a3a`, ombra interna in alto, filo `#2a6a7d`.
- `menu_sezione.png` — 1020×192, raggio 48. Riga di sezione espandibile
  («Come si gioca», «Impostazioni e prove grafiche»): vetro di mare più
  scuro del bottone Tutorial, filo `#3d8a99`. **Nessuna freccia
  disegnata**: la mette il gioco con il file qui sotto.
- `icona_freccia_giu.png` — 96×96 trasparente. Chevron ▼ pieno, oro
  `#f2b84b` (scelto perché si legge meglio sul fondo della sezione
  rispetto al crema). Il gioco la posiziona a destra nella riga e la
  **ruota di 180°** quando la sezione è aperta.

## Verifiche eseguite

- Misure esatte di tutti i 16 asset (tabella sopra) e decodifica `.b64`
  byte-identica per tutti i 17 file in `elenco.txt`.
- Maschere alpha degli stati: **0 px diversi** in ogni gruppo (oro ×4,
  vetro ×3, difficoltà ×3, selezionato incluso).
- **Niente viola**: scansione di ogni file — 0 pixel con tonalità
  260–345° e saturazione ≥0,08 (pixel visibili, alpha ≥128). Lo sfondo
  generato conteneva 47 pixel di banda nelle ombre del vulcano lontano:
  corretti a programma desaturandoli verso la loro luminanza, residui 0.
  L'avversario è blu acciaio, come nei Gruppi 10 e 11.
- Stretch a 9 parti del pannello: vedi sopra (angoli 0 px, cuciture
  senza gradini nuovi).

## Istruzioni per Claude

- Questo set sostituisce **solo la schermata iniziale**: sfondo menu e
  pezzi del menu. I pannelli e i bottoni di gioco del Gruppo 5 e gli
  altri sfondi del Gruppo 6 restano in uso invariati.
- Tutti i testi li scrive il gioco in Fredoka: titolo, motto, etichette
  dei bottoni e delle sezioni, testo del campo mappa, riga di stato e
  collegamento in basso. Negli asset non c'è nulla da ritagliare.
- Corrispondenza con il menu attuale: simbolo → `menu_simbolo.png`
  sopra il titolo; Facile/Normale/Difficile → i tre pezzi
  `menu_difficolta_*` (selezionato = livello attivo); «Continua
  partita» e «Gioca contro il computer» → `menu_bottone_oro_*`;
  campo «Mappa n.» → `menu_campo_mappa.png`; «Tutorial» →
  `menu_bottone_vetro_*`; «Come si gioca» e «Impostazioni e prove
  grafiche» → `menu_sezione.png` + `icona_freccia_giu.png` a destra
  (rotazione 180° da aperta).
- Il pannello va stirato a 9 parti con margine 84 px: non ritagliarlo
  con margini diversi, il bordo legno+corda sta tutto dentro il margine.
- Per l'animazione «pulsante» alternare normale/pulsante o modulare
  l'opacità del pulsante, come nel Gruppo 5.

## Controllo

`controllo/prova_menu.png` — menu completo composto **solo** con gli
asset di questa consegna (sfondo, pannello allungato a 9 parti alla
misura reale della scheda, simbolo, tutti i pezzi) con i testi abituali
scritti sopra come prova di impaginazione: i testi sono resi in DejaVu
Sans (il Fredoka non è disponibile a Muse) e **non fanno parte degli
asset**. A destra: i bottoni oro e vetro in tutti gli stati, la freccia
su fondo sezione e la miniatura del pannello allungato della prova
9-parti.

## Cosa NON deve cambiare

- Misure, raggi e margine 9-parti (84 px) del pannello.
- Le maschere alpha degli stati di un bottone devono restare identiche:
  se uno stato viene rifatto, vanno rifatti tutti gli stati del gruppo.
- Nessuna scritta dentro i PNG: i testi restano scritti dal gioco.
- Niente viola/magenta in nessun pezzo: la squadra avversaria è blu
  acciaio.

## Nuovo rispetto alle consegne precedenti

È la prima consegna dedicata alla sola schermata iniziale: sostituisce
lo sfondo menu del Gruppo 6 e, per la home, i bottoni/pannelli generici
del Gruppo 5, con pezzi disegnati apposta nelle misure reali del menu
attuale (versione 38) e lo stile «Mare dipinto» approvato da Davide.

STATO: pronto
