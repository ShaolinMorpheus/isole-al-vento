# Gruppo 6 — Schermate e icona dell'app

Consegna di Muse, 19 nov 2026. Sfondi a tutto schermo, logo del titolo e
icona Android di «Isole al Vento». Nessuna scritta nei PNG, tranne il logo
del titolo (unico posto dove è richiesta): il testo lo scrive il gioco.
Ogni PNG è affiancato dal suo `nome.png.b64` (base64 su una sola riga):
decodificarlo per ottenere il PNG identico byte per byte.
Ordine dei file in `elenco.txt`. Foglio di verifica in
`controllo/prova_schermate.png`.

## A. Sfondi a tutto schermo — PNG opachi 1236 × 2640

Vanno DIETRO la scheda centrata del gioco (larga al massimo 400 px CSS).
Zona centrale calma e scura, dettagli in alto e in basso; il soggetto è al
centro perché i bordi laterali possono essere tagliati un po'.

- `sfondo_menu.png` — Schermata iniziale: nuvole e scie di vento in alto,
  in basso l'isola oro (sinistra) e l'isola viola (destra) nel mare, con il
  vulcano in lontananza al centro tra le due.
- `sfondo_vittoria.png` — Raggi di luce e cielo luminoso in alto, in basso
  l'isola oro in festa con festoni e grande bandiera oro su pennone.
- `sfondo_sconfitta.png` — La STESSA scena della vittoria, derivata a
  programma dal file `sfondo_vittoria.png` finale (stessa composizione,
  pixel per pixel di base): cielo desaturato (S ×0,55) e scurito (V ×0,74)
  con nuvole scure morbide aggiunte in alto, bandiera ricolorata da oro a
  viola (tonalità portata a 258°, famiglia del viola #9a86ee, ombreggiatura
  conservata), mare increspato con archi bianchi nella fascia bassa,
  grading globale leggero (V ×0,97, S ×0,93). Resta un pomeriggio
  nuvoloso, non una scena cupa.
- `sfondo_pareggio.png` — Cielo diviso in verticale: sereno a sinistra,
  nuvoloso a destra; in basso un'isola con due bandiere, oro e viola, alla
  stessa altezza.

Come è garantita la zona centrale leggibile: gli sfondi sono stati
ricomposti a programma con i dettagli confinati nelle fasce alta e bassa e
un velo scuro morbido (colore fondo mare #0e2433, alpha massimo 0,38,
rampe coseno y 380→630 e 2010→2260). Luminanza misurata nel rettangolo
della scheda (x 18–1218, y 630–2010, scala 0–255):

| File | Centro: media / std | Media resto immagine |
|---|---|---|
| sfondo_menu.png | 33,6 / 12,1 | 88,4 (intera) |
| sfondo_vittoria.png | 35,6 / 10,0 | 86,9 (intera) |
| sfondo_sconfitta.png | 33,3 / 7,1 | 67,2 (intera) |
| sfondo_pareggio.png | 35,3 / 17,7 | 78,7 (intera) |

Il centro è quindi molto più scuro e uniforme del resto in tutti e quattro.

## B. Logo del titolo — PNG trasparenti

- `logo_titolo.png` — 1080 × 360. Testo «Isole al Vento» con il simbolo
  (isoletta con vulcano e soffio di vento) sopra le lettere. Il testo è
  composto a programma con il font Fredoka (lo stesso dei titoli del
  gioco; peso 620, riempimento sfumato chiaro→oro #f2b84b, ombra morbida,
  nessun contorno scuro) e l'ortografia è stata verificata lettera per
  lettera sul file finale: «Isole al Vento», I e V maiuscole, resto
  minuscolo.
- `logo_titolo_solo_simbolo.png` — 512 × 512. Solo il simbolo, senza
  scritte: è lo stesso disegno del logo e dell'icona.

## C. Icona dell'app (Android)

Il simbolo (isola con vulcano e vento) è lo stesso del logo, disegnato una
sola volta come master e riadattato alle misure.

- `icona_primo_piano.png` — 432 × 432, trasparente, solo il disegno.
  Cerchio sicuro: il contenuto ha bbox x 108–324, y 128–304 e la distanza
  massima dal centro (216,216) dei pixel del simbolo è 127,3 px, dentro il
  cerchio centrale di 264 px di diametro (raggio 132). Fuori dal simbolo
  solo trasparenza: Android può tagliare i bordi senza perdere nulla.
- `icona_sfondo.png` — 432 × 432, opaco. Solo il fondo: sfumatura
  verticale del mare, da #15384c in alto a #0e2433 in basso.
- `icona_play_store.png` — 512 × 512, opaco, angoli quadrati: fondo +
  simbolo composto sopra, con la stessa zona sicura in scala (distanza
  massima dal centro 152,2 px su un limite di 156,5).

## D. Schermata di caricamento

- `sfondo_caricamento.png` — 1236 × 2640, opaco. Mare calmo (sfumatura
  #15384c → #0e2433) con il simbolo al centro (640 px di larghezza,
  centrato a metà schermo) e molto spazio vuoto sopra e sotto: il gioco ci
  scrive sopra «Caricamento». Il mare attorno al simbolo è una sfumatura
  uniforme: nelle fasce sopra e sotto il simbolo la deviazione standard
  della luminanza è 0,6–1,2 (media 43,1 sopra, 36,5 sotto).

## Controllo

`controllo/prova_schermate.png` mostra: i quattro sfondi A e il
caricamento ridotti a 412 px di larghezza con un rettangolo semitrasparente
400 × 460 (la scheda simulata) al centro; il logo a piena misura su fondo
mare e su fondo chiaro; l'icona composta (sfondo + primo piano) a 48, 96 e
192 px dentro un cerchio e dentro un quadrato arrotondato, le due forme
che usa Android. A 48 px si riconoscono il cono del vulcano con il
pennacchio, la base verde dell'isola e le scie di vento.

## Cosa NON deve cambiare

- Le misure e l'opacità/trasparenza indicate: gli sfondi e
  `sfondo_caricamento.png` sono opachi; logo e `icona_primo_piano.png`
  sono trasparenti.
- La zona centrale scura e calma degli sfondi: nuovi dettagli non vanno
  messi dove sta la scheda (y 630–2010 circa).
- `sfondo_sconfitta.png` deve restare la stessa scena di
  `sfondo_vittoria.png`: se cambia la vittoria, la sconfitta va riderivata
  da essa, non ridisegnata.
- Il testo del logo: «Isole al Vento» con questa ortografia esatta.
- Il simbolo dell'icona deve restare dentro il cerchio centrale di
  264 px di diametro in `icona_primo_piano.png`.

## Novità rispetto alla consegna precedente

Gruppo nuovo (schermate e icona): nessuna consegna precedente conteneva
sfondi a tutto schermo, logo o icona dell'app.

STATO: pronto
