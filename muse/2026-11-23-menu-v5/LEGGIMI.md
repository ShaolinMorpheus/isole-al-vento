# Menu principale — pannello v5 (cornice come la bozza 1)

Questa cartella sostituisce **solo** `menu_pannello.png` del set
`muse/2026-11-23-menu-v4/`: stesso nome, stessa misura (1140×1680),
stesso margine di taglio a 9 parti (200 px su tutti i lati). Per Claude
è un puro scambio di file: nessun altro pezzo del set v4 cambia e
nessuna misura nel codice cambia.

## Perché

La cornice v4 (fascia di legno con un canale di corda ritorta continuo
lungo tutto il bordo) è stata bocciata da Davide: nella bozza 1
approvata la cornice è fatta in tutt'altro modo, ed è quello che qui
viene riprodotto.

## La cornice v5 (struttura della bozza 1)

- **Pali di legno sottili** centrati sulla linea del bordo del
  pannello: spessore 32 px, legno caldo con venature e luce da
  alto-sinistra, metà sul teal e metà fuori. I pali sono segmentati:
  anelli di giunto scuri ogni ~220–240 px lungo i lati.
- **La corda c'è SOLO come legatura**, mai come corda continua lungo
  il bordo (il canale di corda della v2/v4 qui NON esiste):
  - a ogni angolo, una corda ritorta tesa in diagonale che lega
    l'angolo, da un palo all'altro, con la sua ombra morbida;
  - gruppi di avvolgimento (3 giri di corda con nodo sporgente in
    fuori) attorno ai pali vicino agli angoli: sui due pali verticali
    in alto e in basso, e sul palo inferiore vicino alle estremità.
    Tutti i gruppi stanno dentro le zone di margine da 200 px, quindi
    l'allungamento a 9 parti non li deforma mai; i tratti lunghi di
    palo restano lisci, con i soli anelli di giunto.
- Interno **teal piatto #14586b** (un solo colore nella zona
  centrale), con la sola ombra morbida dei pali e delle legature
  proiettata sul teal vicino al bordo, come nella bozza.
- Fuori dalla cornice: **trasparenza piena** (alpha 0 ai vertici
  della tela e ovunque fuori dalla sagoma), niente fascia scura,
  niente alone. Angoli arrotondati puliti; il centro del bordo
  superiore è libero e retto, dove il gioco appoggia il simbolo.

Disegno a programma (Python/PIL, supersampling 3×), nessuna scritta.

## Verifiche eseguite

- Misura esatta 1140×1680; decodifica `.b64` byte-identica per
  entrambi i file in `elenco.txt`.
- Alpha ai 4 vertici della tela: 0, 0, 0, 0 (fuori cornice
  trasparente, nessuna fascia).
- **Niente viola**: scansione a piena risoluzione — 0 pixel con
  tonalità 260–345° e saturazione ≥0,08 (pixel visibili).
- Centro del pannello: un solo colore, #14586b esatto.
- Stretch a 9 parti con margini fissi 200 (×1,5 in larghezza, ×0,7
  in altezza → 1710×1176): angoli pixel-identici all'originale
  (0 px diversi), centro ancora piatto #14586b (gradino 0); le
  legature, tutte nelle zone di margine, non vengono deformate.
- Ispezione al 200%: legatura diagonale d'angolo, gruppo di
  avvolgimento laterale, tratto di palo nella zona che si allunga
  (vedi anche la striscia di confronto nel foglio di controllo).

## Controllo

`controllo/prova_pannello_v5.png` — (a) il menu completo composto
con gli asset del set v4 ma con il pannello v5 (testi di prova
scritti sopra, non fanno parte degli asset); (b) striscia di
confronto alla stessa scala (×1,373): angolo e legatura laterale
della bozza 1 a sinistra, gli stessi dettagli del pannello v5 a
destra.

## Cosa NON deve cambiare

- Misura 1140×1680 e margine di taglio a 9 parti 200 px.
- La struttura della cornice: pali sottili + legature solo agli
  angoli e dentro le zone di margine; mai una corda continua lungo
  il bordo.
- Interno teal piatto #14586b e trasparenza piena fuori dalla
  cornice.

STATO: pronto
