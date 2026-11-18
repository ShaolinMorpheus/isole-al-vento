# Gruppo 3 — Pedine

Le 20 pedine delle unità dei due giocatori (oro = giocatore, viola = computer),
da disegnare sopra le caselle della mappa dietro il tasto «Grafica di prova».
Vista dall'alto-davanti come gli oggetti del Gruppo 2, unità in piedi sulla casella.
Stile: cartoon pulito e luminoso, volumi quasi realistici, niente contorno scuro,
colori saturi, luce da in alto a sinistra, ombra morbida sotto i piedi inclusa nel PNG.

NON sono disegnati (li fa il gioco): barra della vita, numeri, anelli di selezione,
colpi e frecce. Nessuna scritta nei PNG.

## File, misure e ancore

Tutti i PNG sono trasparenti, larghezza 256 px. Ancora (punto di appoggio al
centro in basso) = (128, altezza−24) per ogni file. Margini del contenuto
(personaggio + ombra): ≥12 px sopra e ai lati, 8 px sotto, in tutti i file.

| file | misura | ancora |
|---|---|---|
| pedina_esploratore_oro_normale.png | 256×264 | (128, 240) |
| pedina_esploratore_oro_stanca.png | 256×264 | (128, 240) |
| pedina_esploratore_viola_normale.png | 256×264 | (128, 240) |
| pedina_esploratore_viola_stanca.png | 256×264 | (128, 240) |
| pedina_guerriero_oro_normale.png | 256×245 | (128, 221) |
| pedina_guerriero_oro_stanca.png | 256×245 | (128, 221) |
| pedina_guerriero_viola_normale.png | 256×245 | (128, 221) |
| pedina_guerriero_viola_stanca.png | 256×245 | (128, 221) |
| pedina_arciere_oro_normale.png | 256×286 | (128, 262) |
| pedina_arciere_oro_stanca.png | 256×286 | (128, 262) |
| pedina_arciere_viola_normale.png | 256×286 | (128, 262) |
| pedina_arciere_viola_stanca.png | 256×286 | (128, 262) |
| pedina_cavaliere_oro_normale.png | 256×316 | (128, 292) |
| pedina_cavaliere_oro_stanca.png | 256×316 | (128, 292) |
| pedina_cavaliere_viola_normale.png | 256×316 | (128, 292) |
| pedina_cavaliere_viola_stanca.png | 256×316 | (128, 292) |
| pedina_sciamano_oro_normale.png | 256×294 | (128, 270) |
| pedina_sciamano_oro_stanca.png | 256×294 | (128, 270) |
| pedina_sciamano_viola_normale.png | 256×294 | (128, 270) |
| pedina_sciamano_viola_stanca.png | 256×294 | (128, 270) |

L'ordine è quello di `elenco.txt`: per tipo (esploratore, guerriero, arciere,
cavaliere, sciamano) → oro normale, oro stanca, viola normale, viola stanca.

Scala relativa: il cavaliere è la pedina più grande (contenuto ~282 px di
altezza, cavallo largo 228 px); l'esploratore la più piccola e leggera
(~230 px); guerriero il più largo tra le unità a piedi (232 px, per lo scudo).

Silhouette: esploratore snello con mantello corto e zaino; guerriero massiccio
con grande scudo rotondo e spada corta; arciere con grande arco e faretra
visibile di lato; cavaliere su cavallo con pennacchio; sciamano con vesti
lunghe e bastone con grosso cristallo azzurro pallido in cima.

## Come sono garantite le coerenze

- **Stesso disegno per colore e posa**: ogni tipo nasce da un unico master
  (oro, normale). Le altre tre versioni sono derivate a programma.
  La maschera alpha è IDENTICA nelle 4 versioni di ogni tipo
  (verifica: 0 pixel diversi su tutti i confronti).
- **Viola**: ricolorazione a programma delle sole zone in tinta squadra
  (vesti, mantello, scudo, armatura, pennacchio, gualdrappa: tonalità
  oro/giallo saturate, HSV H 33–74°, S ≥90, V ≥110) con rotazione di tinta
  di +225° verso il viola, mantenendo saturazione e valore invariati.
  Pixel ricolorati per tipo: esploratore 4.594, guerriero 15.822,
  arciere 7.542, cavaliere 10.090, sciamano 8.356. Fuori da queste zone
  i pixel sono identici all'oro (0 differenze): pelle, capelli, cuoio,
  legno, metalli neutri, manto del cavallo e cristallo non cambiano.
  Luminanza media (V) delle zone squadra: oro = viola (esploratore 220,5,
  guerriero 213,2, arciere 209,2, cavaliere 218,8, sciamano 211,7 su 255):
  il viola è una tinta piena e satura, NON un oro scurito.
- **Stanca**: stessa immagine, trasformazione di colore globale e uniforme
  in HSV (saturazione ×0,55, valore ×0,85, tinta e alpha invariati).
  L'impressione di abbassamento è data solo dal colore, come richiesto:
  silhouette e posizione non cambiano.
- **Ombra**: ellisse morbida semitrasparente sotto i piedi, disegnata a
  programma in modo identico nelle 4 versioni, centrata sull'ancora.

## Controllo

`controllo/prova_45px.png`: tutte e 20 le pedine a 45 px su casella di prato
del terreno v2 (griglia 5 tipi × 4 versioni), con la stessa scena ingrandita
×4 (ricampionata e in nearest-neighbour). A 45 px i cinque tipi si distinguono
dalla silhouette e oro/viola si distinguono a colpo d'occhio.

## Limiti dichiarati

- L'angolo di vista è «dall'alto-davanti» per tutti, ma guerriero e sciamano
  sono visti un po' più dall'alto degli altri tre.
- Nell'arciere la punta bassa dell'arco arriva alla linea del terreno
  (arco appoggiato a terra): è il punto più basso del disegno insieme ai piedi.
- Il primo master dell'esploratore (posa in salto, mantello lungo) è stato
  scartato e rifatto in piedi con mantello corto, come da specifica.

## Formato di viaggio

I PNG viaggiano come `nome.png.b64` (base64 su una sola riga), da decodificare
salvando il risultato come `.png`. Verificato: i 20 `.b64` decodificano
byte-identici ai PNG, come quello del foglio di controllo.

## Cosa NON deve cambiare

Nomi file, misure, ancore e maschere alpha; le quattro versioni di un tipo
devono restare lo stesso disegno. Se un disegno stona, lo rifà Muse in una
nuova consegna (-v2), non va ritoccato qui.

STATO: pronto
