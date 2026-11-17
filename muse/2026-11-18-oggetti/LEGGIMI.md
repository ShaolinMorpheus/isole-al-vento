# Gruppo 2 — Oggetti alti

Oggetti che stanno SOPRA le caselle del terreno v2 (la casella nel gioco è la sola
faccia superiore, circa 45 px sul telefono, senza fronte di terra). Gli oggetti
possono sporgere in alto oltre la casella. Il vulcano fa eccezione: è una casella
intera a sé.

## Come si usano nel gioco

- Disegnare l'oggetto con il punto d'appoggio (ancora) allineato al centro della
  casella su cui sta: ancora a x=128, y=altezza−24 in OGNI oggetto alto.
- Sotto ogni oggetto c'è solo un'ombra morbida semitrasparente a terra, già
  disegnata nella parte inferiore del PNG: niente terra marrone e niente basi di
  roccia, l'oggetto poggia direttamente sull'erba della casella.
- Stazione meteo: ciclare i 3 fotogrammi (0°, 40°, 80°) per far girare
  l'anemometro.
- Bandiere: fotogrammi 1 e 2 da alternare per la stoffa mossa; oro = base del
  giocatore, viola = base del computer.
- Vulcano: casella opaca 256×256 che sostituisce la casella di terreno, con i 3
  stati da scambiare secondo il turno (calmo / arde prima dell'eruzione /
  eruttato appena dopo).

## File e misure (ordine in elenco.txt)

| File | Misura (px) | Ancora | Uso |
|---|---|---|---|
| oggetto_pino_a.png | 256×380 | (128, 356) | pino singolo, variante classica |
| oggetto_pino_b.png | 256×320 | (128, 296) | pino singolo, basso e pieno |
| oggetto_pino_c.png | 256×364 | (128, 340) | pino singolo, alto e slanciato |
| oggetto_boschetto_a.png | 256×340 | (128, 316) | boschetto di 3 pini composto |
| oggetto_boschetto_b.png | 256×336 | (128, 312) | boschetto di 3 pini composto |
| oggetto_montagna_a.png | 256×280 | (128, 256) | montagna innevata, cima singola; base larga ~230 px, sta sulla casella monte |
| oggetto_montagna_b.png | 256×255 | (128, 231) | montagna innevata, doppia cima; base larga ~230 px |
| oggetto_stazione_0.png | 256×320 | (128, 296) | stazione meteo, anemometro a 0° |
| oggetto_stazione_40.png | 256×320 | (128, 296) | stazione meteo, anemometro a 40° |
| oggetto_stazione_80.png | 256×320 | (128, 296) | stazione meteo, anemometro a 80° |
| oggetto_bandiera_oro_1.png | 256×344 | (128, 320) | bandiera base giocatore, fotogramma 1 |
| oggetto_bandiera_oro_2.png | 256×344 | (128, 320) | bandiera base giocatore, fotogramma 2 |
| oggetto_bandiera_viola_1.png | 256×344 | (128, 320) | bandiera base nemica, fotogramma 1 |
| oggetto_bandiera_viola_2.png | 256×344 | (128, 320) | bandiera base nemica, fotogramma 2 |
| terreno_vulcano_calmo.png | 256×256 opaco | non applicabile (casella intera) | vulcano calmo |
| terreno_vulcano_arde.png | 256×256 opaco | non applicabile (casella intera) | vulcano, bocca che arde (eruzione vicina) |
| terreno_vulcano_eruttato.png | 256×256 opaco | non applicabile (casella intera) | vulcano appena eruttato (fumo e braci) |

Per gli oggetti alti l'ancora è il centro della base: la base dell'oggetto è
centrata su x=128 e il piede sta a y=altezza−24; l'ombra a terra può estendersi
pochi px sotto l'ancora.

## Coerenze garantite (verificate a programma)

- Stazione: base e asta sono un unico master identico nei 3 frame. Pixel
  diversi tra frame fuori dall'area delle coppe (rettangolo x 40–216,
  y 0–160): 0 per tutte le coppie. Cambia solo il gruppo coppe ruotato attorno
  al mozzo; coppe color verde acqua.
- Bandiere: asta pixel-identica nei 4 file (0 pixel diversi fuori dall'area dei
  teli). A parità di fotogramma, il telo oro e il telo viola hanno la stessa
  sagoma (0 pixel alpha diversi): stesso disegno ricolorato. Tra fotogramma 1 e
  2 cambia solo l'ondulazione del telo.
- Vulcano: i 3 stati derivano dallo stesso master «calmo». Calmo→arde: 1.073
  pixel diversi, tutti dentro il disco della bocca (centro 128,128, raggio 19).
  Calmo→eruttato: 13.493 pixel diversi, tutti nelle aree dichiarate di fumo
  (rettangolo x 76–180, y 0–134) e cono/bocca/braci (disco centro 128,128,
  raggio 76); 0 pixel diversi fuori da queste aree.
- Boschetti: composti a programma dai pini singoli (stessa famiglia), con una
  sola ombra a terra condivisa.
- Tutti gli oggetti alti: larghezza 256, altezza ≤384, sfondo trasparente
  (alpha=0 ai 4 angoli), nessun elemento di terra o roccia sotto l'oggetto.

## Controllo

`controllo/prova_45px.png`: tutti gli oggetti ridotti alla dimensione reale di
gioco (casella 45 px, oggetti in proporzione) sopra le caselle prato, bosco e
monte del terreno v2, con accanto la stessa scena ingrandita ×4 in
nearest-neighbour ed etichette. A 45 px ogni oggetto si riconosce: pini e
boschetti sul verde, montagna innevata sul monte, stazione con le coppe verde
acqua, bandiere oro/viola, vulcano nei 3 stati. Non è materiale di gioco e non
è in elenco.txt.

## Cosa NON deve cambiare

- Ancora e misure di ogni file: sono il contratto di posizionamento nel gioco.
- Le sagome condivise: base/asta della stazione, asta delle bandiere, sagoma
  del telo a parità di fotogramma, disegno di base del vulcano nei 3 stati.
- Niente ritocchi ai disegni da parte di chi integra: se un pezzo stona, va
  rifatto da Muse in una nuova consegna.

## Formato di viaggio

Ogni PNG è presente anche come `nome.png.b64` (base64 su una sola riga): per
ottenere il PNG va decodificato il contenuto del .b64 e salvato come `.png`.
Vale anche per `controllo/prova_45px.png.b64`. Verificato: i 17 .b64
decodificano byte-identici ai PNG.

STATO: pronto
