# Menu principale — pannello v6 (legatura d'angolo della bozza su tutto il giro)

Questa cartella sostituisce **solo** `menu_pannello.png` del set
`muse/2026-11-23-menu-v4/`: stesso nome, stessa misura (1140×1680),
stesso margine di taglio a 9 parti (200 px su tutti i lati). Per Claude
è un puro scambio di file: nessun altro pezzo del set v4 cambia e
nessuna misura nel codice cambia. Anche il pannello v5
(`muse/2026-11-23-menu-v5/`) è superato da questa versione.

## Perché

Davide, guardando il confronto della v5, ha chiesto la **legatura
d'angolo della bozza 1 ripetuta su tutto il perimetro**: nella bozza,
all'angolo, una corda grossa e ritorta si avvolge in diagonale sui due
pali, attraversa l'angolo sopra il teal e sporge fuori dalla linea dei
pali. La v5 aveva solo piccole legature vicino agli angoli; qui quel
trattamento diventa l'ornamento di tutta la cornice.

## La cornice v6

- **Pali di legno sottili** centrati sulla linea del bordo del
  pannello: spessore 32 px, legno caldo con venature e luce da
  alto-sinistra, metà sul teal e metà fuori; segmentati con anelli di
  giunto scuri lungo i lati. Tra una legatura e l'altra il palo resta
  nudo, come nella bozza.
- **Legature diagonali grosse** (fascia 96×58 px: 3 giri spessi di
  corda ritorta, passo ~31 px lungo il palo, canapa #c9a86a con solchi
  #6e5326 e profilo scuro), avvolte sul palo in diagonale e sporgenti
  ~13 px da entrambi i lati, ripetute lungo **tutti** i lati con passo
  ~290 px: 5 per lato verticale, 3 sul lato inferiore, 2 sul lato
  superiore (vedi sotto), con l'inclinazione specchiata ai lati opposti.
- **A ogni angolo la legatura piena della bozza**: un fascio di corda
  grossa (190×30 px) teso in diagonale sulla bisettrice, che avvolge i
  due pali e attraversa l'angolo sopra il teal, con un giro
  perpendicolare (nodo) al centro.
- **Niente corda continua** lungo il bordo: il canale di corda della
  v2/v4 qui non esiste, come già nella v5.
- **Bordo superiore**: al centro resta una zona libera da legature di
  ~340 px (x 400–740), dove il gioco appoggia il simbolo; il centro del
  bordo è retto e il palo lì è nudo.
- Interno **teal piatto #14586b** (un solo colore nella zona
  centrale), con la sola ombra morbida di pali e legature proiettata
  sul teal vicino al bordo. Fuori dalla cornice: **trasparenza piena**
  (alpha 0 ai vertici e ovunque fuori dalla sagoma), niente fascia
  scura, niente alone; angoli arrotondati puliti.
- Nota sull'allungamento: le legature stanno anche nelle zone di
  bordo che il taglio a 9 parti allunga, quindi quando il gioco stira
  il pannello la loro **distanza** cambia con l'altezza/larghezza
  scelta (è inevitabile per un ornamento ripetuto lungo il lato); le
  proporzioni dichiarate sono quelle del file 1140×1680. Le legature
  stesse non si deformano in altezza/larghezza più dello stiramento
  applicato al lato, e gli angoli restano intatti.

Disegno a programma (Python/PIL, supersampling 3×), nessuna scritta.
Pulizia di consegna: nei pixel quasi trasparenti del bordo sono stati
azzerati eventuali RGB spuri saturi da ridimensionamento (artefatto
presente anche in v4/v5): nel file finale i pixel «arcobaleno»
(rosso/giallo puri a bassa alpha) sono 0.

## Verifiche eseguite

- Misura esatta 1140×1680; decodifica `.b64` byte-identica per
  entrambi i file in `elenco.txt`.
- Alpha ai 4 vertici della tela: 0, 0, 0, 0; sagoma contenuta nella
  tela (nessuno sbavo fuori dai bordi).
- **Niente viola**: scansione a piena risoluzione — 0 pixel con
  tonalità 260–345° e saturazione ≥0,08 (pixel visibili).
- Centro del pannello: un solo colore, #14586b esatto.
- Zona simbolo: nella fascia del bordo superiore, x 400–740, nessun
  pixel di legatura (solo il palo nudo).
- Stretch a 9 parti con margini fissi 200 (×1,5 in larghezza, ×0,7
  in altezza → 1710×1176): angoli pixel-identici all'originale
  (0 px diversi), centro ancora piatto #14586b (gradino 0).
- Ispezione al 200%: legatura d'angolo contro l'angolo della bozza,
  una legatura laterale, la zona libera in alto al centro (vedi anche
  la striscia di confronto nel foglio di controllo).

## Controllo

`controllo/prova_pannello_v6.png` — (a) il menu completo composto
con gli asset del set v4 ma con il pannello v6 (testi di prova
scritti sopra, non fanno parte degli asset); (b) striscia di
confronto alla stessa scala (×1,373): angolo e legatura laterale
della bozza 1 a sinistra, gli stessi dettagli del pannello v6 a
destra.

## Cosa NON deve cambiare

- Misura 1140×1680 e margine di taglio a 9 parti 200 px.
- La struttura della cornice: pali sottili + legature diagonali
  grosse ripetute su tutto il perimetro e legatura piena agli
  angoli; mai una corda continua lungo il bordo.
- La zona libera da legature in alto al centro (~340 px) per il
  simbolo.
- Interno teal piatto #14586b e trasparenza piena fuori dalla
  cornice.

STATO: pronto
