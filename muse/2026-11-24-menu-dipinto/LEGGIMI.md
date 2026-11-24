# Menu dipinto — pezzi estratti dal dipinto intero (24 novembre 2026)

Questi pezzi NON sono ridisegnati: sono **estratti dal menu dipinto approvato**
(l'immagine intera generata il 24 novembre), con le scritte cancellate.
Sostituiscono i pezzi a programma della v4/Gruppo 14 a parità di misure e
contratti: stesse tele, stessi margini a 9 parti, stesse regole per i testi.

**Testi fissi**: restano i PNG di lettering del Gruppo 14
(`2026-11-23-menu-v5-lettering`: titolo, Gioca, Tutorial, difficoltà,
etichette sezioni). **Testi variabili**: li scrive il gioco (Continua
partita…, riga di stato, campo mappa, motto, Novità, valori impostazioni).

## Metodo (in breve)

- Ogni elemento è stato ritagliato dal dipinto con margine, la scritta è
  stata cancellata per inpainting (Telea) con maschera delle lettere; per
  le assi oro, dove l'inpainting lasciava aloni, si è usato l'incrocio tra
  le due assi (i pixel puliti dell'una riempiono le lettere dell'altra).
  Superfici ricontrollate al 200%: niente fantasmi di lettere.
- Pannello: interno ricostruito in teal dipinto (le zone coperte da
  titolo/bottoni sono state riempite con la texture teal del dipinto
  stesso), cornice = pixel originali del dipinto; sagoma = rettangolo
  arrotondato geometrico + legature dipinte che lo toccano: **nessun pixel
  di sfondo fuori sagoma** (il difetto «banda scura agli angoli» della v3
  non c'è), alfa 0 fuori, piuma 1–2 px.
- Simbolo: scontorno per chiave colore dal teal con despill dei bordi e
  scala in spazio premoltiplicato: **nessun rettangolo teal** (verificato
  su cielo e su fondo scuro al 200%).

## File

- `sfondo_menu.png` 1236×2640 — la scena dipinta attorno al pannello
  (cielo con vortici, mare, isola d'oro in basso a sinistra, rocce blu in
  basso a destra, vulcano lontano). PNG pieno, nessuna sfocatura.
  **Deroga dichiarata**: la zona coperta dal pannello dipinto
  (x 100–1139, y 559–2310) è ricostruita con inpainting a bassa
  risoluzione (continuazione plausibile di cielo e mare) + velo #0e2433
  alpha max 0,5 con rampe coseno sulla zona (48,300)–(1188,2350), come la
  v4. In gioco la zona ricostruita è coperta dal pannello: restano
  visibili solo i margini.
- `menu_pannello.png` 1140×1680, margine a 9 parti **200** su tutti i lati.
  Cornice del dipinto: pali di legno con legature di corda diagonali agli
  angoli e ai giunti, interno teal dipinto. Bbox alfa (14,33)–(1124,1646).
  Sagoma = rettangolo arrotondato puro, senza rilievi: il palo superiore
  corre **diritto su tutto il bordo**, anche al centro — dove nel dipinto
  passava dietro la cupola dell'emblema, il tratto centrale (~500 px) è
  stato prolungato con la texture dei tratti di palo rettilinei ai suoi
  lati (`lavoro/fix_panel_top.py`), e il teal interno arriva a filo sotto
  il palo. Il simbolo si monta centrato sul bordo superiore e copre il
  centro. Fuori sagoma alfa 0 (audit: nessun pixel oltre la piuma di
  2 px; prima della correzione c'erano 56 px di alone, alfa max 23, agli
  angoli).
  Agli angoli inferiori, dentro la sagoma, restano gli schizzi
  d'acquerello chiari del dipinto attorno alla cornice (sono pittura, non
  fondo estraneo).
- `menu_simbolo.png` 512×512 — l'isoletta col vulcano dell'emblema.
  **Ancora: la linea di schiuma alla base dell'isola è a y=256** (il centro
  della tela va sul bordo superiore del pannello). Contenuto: bbox
  (56,60)–(456,275); il mare sotto la linea sfuma in trasparenza.
- Bottoni oro 1020×216, margine a 9 parti 60, ombra morbida disegnata
  DENTRO la tela sotto l'asse:
  - `menu_bottone_oro_normale.png` — asse estratta dall'asse «Continua
    partita» del dipinto (la più pulita delle due; quella «Gioca» è tenuta
    come candidata in `lavoro/`), scritta cancellata.
  - `menu_bottone_oro_premuto.png` — dallo stesso normale, luminosità ×0,75.
  - `menu_bottone_oro_disattivo.png` — dallo stesso normale, saturazione
    ×0,45 circa e luminosità ×0,85.
  - `menu_bottone_oro_pulsante.png` — dallo stesso normale + bagliore
    interno caldo #ffe9b0 sul bordo interno.
  - Tutti e quattro con la **stessa maschera alfa** (0 px di differenza).
  - Parte opaca (asse + ombra piena): bbox (2,13)–(1017,204), altezza
    visibile ~192 px; **centro visivo per i testi: (509, 108)** — centrare
    le scritte sull'area visibile, non sulla tela.
- Bottoni vetro di mare 1020×180, margine 60, ombra dentro la tela:
  - `menu_bottone_vetro_normale.png` — estratto dal bottone «Tutorial».
  - `menu_bottone_vetro_premuto.png` (×0,75) e
    `menu_bottone_vetro_disattivo.png` (desaturato) derivati con la stessa
    maschera alfa (0 px di differenza).
  - Parte opaca: bbox (2,11)–(1017,172); centro visivo (509, 91).
- Difficoltà 318×150, margine 60:
  - `menu_difficolta_selezionato.png` — pillola oro «Facile» estratta,
    scritta cancellata; **maschera alfa propria**.
  - `menu_difficolta_normale.png` — pillola vetro «Normale» estratta.
  - `menu_difficolta_premuto.png` — dal normale (×0,75), **stessa
    maschera** del normale (0 px di differenza).
  - Parte opaca: bbox (1,5)–(317,149); centro visivo (159, 77).
- `menu_campo_mappa.png` 1020×162, margine 60 — il campo scuro incassato
  del dipinto, **vuoto** (il segnaposto «Mappa n.…» è cancellato).
- `menu_sezione.png` 1020×162, margine 60 — una riga di sezione in vetro
  di mare, senza scritta e senza freccia.
- `menu_sezione_aperta.png` 1020×162 — come `menu_sezione` ma con gli
  angoli inferiori squadrati (la texture della riga è prolungata negli
  angoli).
- `icona_freccia_giu.png` 96×96 — la freccia delle righe di sezione,
  estratta e centrata; colore = il teal scuro dipinto dell'originale
  (mediana RGB 9,68,81). Contenuto bbox (15,26)–(80,70).
- `controllo/prova_menu_dipinto.png` — il menu ricomposto a 412×880 (×2,
  poi ridotto a 0,8 per il limite di invio: 1306×1459) **solo** con questi
  pezzi + lettering del Gruppo 14 + segnaposto semplici per i testi
  variabili, a fianco del dipinto approvato alla stessa altezza. Le
  posizioni nella ricomposizione sono quelle relative misurate sul
  dipinto; i pezzi larghi sono disegnati a proporzione nativa (il
  nine-slice nel foglio li schiaccerebbe: in gioco valgono i margini
  dichiarati sopra).

## Ritagli dal dipinto (coordinate sorgente 1040×2352)

Pannello (84,498)–(958,2058) [interno e cornice]; simbolo (388,528)–(668,712),
linea di schiuma y=662; asse «Continua partita» (120,1140)–(920,1370) e asse
«Gioca» (120,1300)–(920,1530) [incrocio anti-aloni]; «Tutorial»
(300,1610)–(740,1790); pillole: «Facile» (120,940)–(410,1110), «Normale»
(375,940)–(665,1110); campo (130,1470)–(910,1660); riga sezione 1
(105,1740)–(935,1872); freccia da (812,1805)–(866,1848). Dettagli e script
in `lavoro/` (`extract_lib.py`, `build_pieces.py`, `build_panel.py`,
`build_symbol.py`, `build_background.py`, `build_sheet.py`,
`fix_violet.py`, `fix_panel_top.py`, `finalize.py`, `verify.py`,
immagini QA).

## Verifiche (script `lavoro/verify.py`, esito TUTTO OK)

- Misure esatte di tutti i file; .b64 a riga singola con round-trip
  byte-identico per tutti i file; il .b64 più grande è lo sfondo
  (4.156.540 caratteri, sotto il limite ~4,8 MB).
- Anti-viola: **0 px** in banda 260–345° (saturazione ≥0,08, pixel
  visibili) su ogni file, foglio di controllo incluso (correzioni ruotate
  a 225°: 656+151 px nel pannello, 5 px in ciascun bottone oro
  normale/premuto, 2 nel disattivo).
- Maschere alfa identiche (0 px di differenza) nei gruppi oro ×4, vetro
  ×3, difficoltà normale/premuto; la pillola oro selezionata ha maschera
  propria (dichiarato).
- Pannello stirato a 9 parti (1710×1176, margine 200): angoli 0 px
  diversi, gradiente massimo alla cucitura centrale 3 (nessuna cucitura).
- Pulizia alfa: alfa <12 azzerato con RGB azzerato su tutti i pezzi;
  0 pixel artefatto (0,0,255) residui.
- Correzione del 24 novembre (round 2): palo superiore prolungato su
  tutto il bordo (al centro il teal arrivava fino alla sagoma e si
  leggeva come una linguetta piatta); audit alone del pannello: prima
  56 px con alfa >0 oltre 2 px dalla sagoma piena (alfa max 23, agli
  angoli), dopo **0 px** su tutti e quattro gli angoli; nel foglio di
  controllo il simbolo è ora montato come in gioco, con la linea di
  galleggiamento sul bordo superiore **visibile** del pannello reso
  (prima galleggiava 34 px sopra, sul filo della tela trasparente).
- Ogni pezzo è stato guardato al 200% (cancellature, scontorni, angoli
  del pannello) e il foglio di controllo è stato confrontato col dipinto.

## Note oneste (punti deboli)

- L'interno del pannello, dove sedevano titolo e bottoni, è teal
  ricostruito dalla texture del dipinto: restano tenui cuciture orizzontali
  morbide in alcuni punti, in gran parte coperte dagli elementi in gioco.
- Nel dipinto l'emblema siede in una cupola della cornice; il pannello di
  gioco ha il bordo superiore diritto (contratto v4) con il palo continuo:
  il tratto centrale del palo è ricostruito dalla texture del palo stesso
  (non sono i pixel originali del dipinto, dove lì c'era la cupola) ed è
  l'unico tratto di cornice non originale. Il simbolo si appoggia sul
  bordo come nel dipinto e copre il centro del palo.
- Il bottone «Tutorial» del dipinto è più bombato della tela di contratto
  1020×180: l'estrazione lo riporta alle proporzioni della v4 (parte
  visibile ~137–162 px di altezza), come gli altri pezzi.

STATO: pronto
