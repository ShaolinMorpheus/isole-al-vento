# Menu principale — versione dai pixel della bozza (v3)

Questo set sostituisce i pezzi del menu delle consegne
`muse/2026-11-23-menu/` (v1) e `muse/2026-11-23-menu-v2/` (solo
pannello). Dopo il verdetto di Davide («lo voglio come me l'hai fatto
vedere qui, identico»), i pezzi NON sono ridisegnati: sono **estratti e
ricostruiti dai pixel della bozza 1 «Mare dipinto» approvata**
(`bozze-menu/bozza_menu_1.png`). Forme, luci, bordi e texture sono
quelli della bozza; le scritte sono state cancellate ricostruendo il
riempimento dal gradiente e dalla grana della bozza stessa (mediana per
riga + ombreggiatura per colonna dalle bande senza testo): nessun
fantasma di lettera, verificato a vista al 200% su ogni pezzo.

**NESSUNA scritta in nessun asset**: i testi li scrive il gioco
(Fredoka). Le scritte nel foglio di controllo sono solo prova di
impaginazione. Ogni PNG ha il suo `nome.png.b64` (base64 su una riga,
decodifica byte-identica verificata). Ordine in `elenco.txt`.

## ⚠️ Margine del pannello CAMBIATO: 200 px (v1/v2: 84 px)

`menu_pannello.png` (1140×1680) va stirato a 9 parti con **margine
200 px su tutti i lati**. Il margine è più grande perché la cornice
della bozza — pali segmentati con legature di corda agli angoli — non
entra in 84 px: dentro i 200 px stanno padding trasparente (40 px, per
le legature che sporgono fuori dalla linea del palo), palo, legature
agli angoli e curva teal. Claude deve aggiornare il margine da 84 a
200: è l'unico cambio di codice richiesto da questa consegna.

## File e provenienza (dalla bozza)

### Pannello

- `menu_pannello.png` — 1140×1680, 9 parti, margine 200.
  Cornice assemblata dai ritagli della cornice vera della bozza:
  i 4 angoli con le loro legature a croce; le bande verticali dai
  fianchi della bozza, **con le legature laterali al loro posto**
  (sono dentro le bande, nella zona che si allunga: con allungamenti
  moderati si stirano appena, dichiarato qui perché non possono stare
  altrove); la banda superiore dai segmenti laterali della banda
  superiore della bozza, specchiati (al centro, nella bozza, c'è
  l'arco col simbolo: lo copre il pezzo simbolo qui sotto); la banda
  inferiore dalla banda inferiore della bozza, con il nodo in basso.
  Interno: campo teal ricostruito dal profilo colore campionato dalle
  colonne interne libere della bozza (x=126 e x=880), con ombra morbida
  verso la cornice. La grana fine è sintetica (statistica, senza
  dettagli): la grana originale della bozza porta un *watermark
  fantasma* del generatore d'immagini — frammenti di lettere appena
  percettibili nelle zone piatte, parte dell'immagine approvata — e
  ricampionarla a tasselli lo avrebbe reso leggibile.

### Simbolo (pezzo a parte, copre l'arco)

- `menu_simbolo.png` — 512×512 trasparente. È il ritaglio della bozza
  con arco in corda, vulcano con pennacchio, isola e palme; cielo e
  nuvole sono resi trasparenti, il teal alla base sfuma nel pannello.
  **Ancoraggio: il centro verticale della tela (y=256) è la linea del
  bordo superiore del pannello** — Claude lo centra su quel bordo, in
  orizzontale al centro, e la composizione è quella della bozza.
  Sostituisce il `menu_simbolo.png` di v1 (che era un disegno a parte).

### Bottoni e pezzi (sagome estratte dalla bozza)

Misure = contratto v1 (sono le misure reali del gioco; le proporzioni
dei pezzi seguono il gioco, superfici e bordi sono della bozza).

- Oro grandi, da «Continua partita»: `menu_bottone_oro_normale.png`
  1020×252; `menu_bottone_oro_premuto.png` (×0,75),
  `menu_bottone_oro_disattivo.png` (desaturato ~40%, ×0,85),
  `menu_bottone_oro_pulsante.png` (alone interno morbido) derivati a
  programma dal normale: **maschere alpha identiche, 0 px diversi**.
- Vetro di mare, da «Tutorial»: `menu_bottone_vetro_normale.png`
  1020×216 + premuto/disattivo derivati (maschere identiche).
- Difficoltà: `menu_difficolta_selezionato.png` 330×156 da «Facile»;
  `menu_difficolta_normale.png` 330×156 da «Normale» (nella bozza le
  difficoltà non selezionate sono vetro di mare, non teal scuro come
  in v1); `menu_difficolta_premuto.png` derivato dal normale.
- `menu_campo_mappa.png` — 1020×192, dal campo della bozza, testo
  segnaposto cancellato.
- `menu_sezione.png` — 1020×192, dalla riga «Come si gioca», senza
  testo e senza freccia.
- `icona_freccia_giu.png` — 96×96 trasparente: lo chevron **teal
  scuro** estratto dalla riga della bozza. **Cambia rispetto a v1**
  (era oro #f2b84b): ora è del colore della bozza. Il gioco la mette a
  destra nella riga e la ruota di 180° con la sezione aperta.

## Cosa resta invariato

- `sfondo_menu.png` di `muse/2026-11-23-menu/` (v1) **resta quello**:
  è della stessa generazione della bozza, non va sostituito.
- Pannelli e bottoni di gioco del Gruppo 5 e gli altri sfondi del
  Gruppo 6 restano in uso.

## Verifiche eseguite

- Misure esatte di tutti i 15 asset; round-trip `.b64` byte-identico
  per tutti i 16 file in elenco.
- Maschere alpha degli stati: **0 px diversi** (oro ×4, vetro ×3,
  difficoltà normale/premuto).
- **Niente viola**: 0 pixel con tonalità 260–345° e saturazione ≥0,08
  in ogni file. Le ombre mauve della bozza (198 px nel pannello, 23 nel
  simbolo) sono state desaturate verso la loro luminanza, ombreggiatura
  conservata, come nel Gruppo 11.
- Stretch 9-parti del pannello (×1,5 larghezza, ×0,7 altezza →
  1710×1176): angoli **0 px diversi** nei pixel visibili; gradino alle
  cuciture dentro il teal 3–5 (su 255), nessun gradino nuovo.
- Controllo fantasmi di testo: ogni pezzo estratto è stato guardato
  ingrandito (200%) dopo la cancellazione — nessun contorno di lettera
  leggibile. Residui onesti: nel bottone oro si intravede una sottile
  linea verticale di giuntura del riempimento e nel campo una piccola
  sbavatura sul bordo alto a sinistra; a misura di menu non si notano.

## Controllo

`controllo/prova_menu_v3.png` — a sinistra la bozza 1 approvata, a
destra la composizione fatta **solo** con gli asset di questa consegna
sullo sfondo v1 (pannello stirato a 9 parti alla misura della scheda,
simbolo ancorato sul bordo superiore, tutti i pezzi al loro posto) con
i testi abituali scritti sopra in DejaVu Sans come prova di
impaginazione: **i testi non fanno parte degli asset**. Sotto, il
dettaglio dell'angolo superiore sinistro del pannello in scala 100%.
Giudizio di chi ha composto il foglio: a parità di impaginazione la
composizione è sovrapponibile alla bozza per cornice, simbolo e
superfici dei pezzi; le differenze visibili sono le proporzioni dei
bottoni (seguono le misure reali del gioco, più alti che nella bozza)
e l'interno del pannello più calmo (senza la grana-watermark).

## Cosa NON deve cambiare

- Il margine 9-parti del pannello: **200 px** (non tornare a 84).
- L'ancoraggio del simbolo: centro della tela sulla linea del bordo
  superiore del pannello.
- Le maschere alpha degli stati: se si rifà uno stato, si rifanno
  tutti gli stati del gruppo.
- Nessuna scritta dentro i PNG; niente viola/magenta.

STATO: pronto
