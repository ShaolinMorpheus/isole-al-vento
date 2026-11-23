# Gruppo 10 — Personaggi, PARTE A: nuovo look delle 5 unità attuali

## AVVISO PER CLAUDE — la squadra avversaria ora è BLU

La squadra avversaria **non è più viola**: per decisione di Davide (22 nov 2026) i file `_blu_` di questa consegna **sostituiscono** i vecchi `_viola_` del Gruppo 3 (`muse/2026-11-18-pedine/`). Il viola resta ancora da allineare in basi, bandiere e interfaccia: sarà una consegna successiva, non questa.

## Cosa sono questi file

Nuovo look delle 5 unità attuali del gioco, più curato e con più carattere rispetto alle pedine del Gruppo 3, nello stile cartoon colorato del terreno v2. Ogni unità ha una silhouette diversa dalle altre e la sua arma/oggetto ben riconoscibile anche a ~110 px sullo schermo.

**Metodo (importante):** ogni versione è un **disegno nato nel suo colore** — la versione oro e la versione blu di una unità sono due disegni generati separatamente, non ricolori una dell'altra. Per questo i dettagli tra oro e blu della stessa unità **non sono identici** (è voluto e approvato da Davide dopo le bozze del guerriero: le ricolori a programma lasciavano zone grigie). La pelle è sempre rosa naturale disegnata; l'acciaio è grigio solo dove è metallo vero; il cuoio è marrone caldo; nessuna zona spenta su stoffa e armatura.

| Unità | Idea | Misure PNG | Ancora |
|---|---|---|---|
| Esploratore | leggero e rapido, zaino e cannocchiale/bussola, mantella corta | 256×264 | (128, 240) |
| Guerriero | robusto, scudo piccolo al fianco e spada grande ben visibile, elmo (master approvati da Davide nelle bozze v2 oro / v7 blu) | 256×245 | (128, 221) |
| Arciere | cappuccio, arco grande dominante, faretra | 256×286 | (128, 262) |
| Cavaliere | in sella al cavallo (un solo sprite), lancia o spada, il più alto; cavallo con pelo naturale, colori di squadra su bardatura e cavaliere | 256×316 | (128, 292) |
| Sciamano | bastone con cristallo e luce magica, mantello a vento | 256×294 | (128, 270) |

Per ogni unità: `<nome>_oro_normale.png`, `<nome>_oro_stanca.png`, `<nome>_blu_normale.png`, `<nome>_blu_stanca.png` — 20 file, elencati in `elenco.txt` in ordine unità → squadra → stato.

## Posa «stanca»

Derivata a programma da ciascun normale **della stessa squadra** (mai dall'altra): stessa posa, colori più spenti e grigi (saturazione ×0,55, valore HSV ×0,92), figura un pochino più bassa (compressione verticale 3% ancorata alla linea dei piedi, che non si muovono) e testa un po' china (spostamento morbido verso il basso, max 4 px, della zona testa). Script usato: `lavoro/deriva_stanca.py`.

## Regole rispettate

- PNG con sfondo trasparente, personaggio intero, vista dall'alto-davanti, posa neutra con leggero movimento, non di profilo.
- Ancora (128, altezza−24): piedi (o zoccoli) al centro, a 24 px dal bordo basso.
- Niente ombra disegnata, niente anello a terra, niente contorno scuro spesso.
- Luce da in alto a sinistra, come il terreno.

## Cosa NON deve cambiare

- Nomi file, misure e ancore: il gioco li carica così.
- I colori di squadra: oro = giallo/ambra caldo; blu = blu acciaio naturale. Niente viola in questa consegna.

## File .b64

Ogni PNG è presente anche come `nome.png.b64` (base64 su una sola riga): è la stessa immagine, serve solo al caricamento. Il foglio `controllo/prova_personaggi_a.png` (tutte le pedine a ~110 px sul prato v2 e le normali a piena misura) non è in `elenco.txt`.

## Nota di verifica (23 nov 2026) — problema cavaliere RISOLTO

La prima verifica aveva bocciato i colori del cavaliere (oro verde, 88°; blu turchese). Le due normali del cavaliere sono state **rigenerate da zero** con lo stesso metodo «nato nel colore» e le stanche ridivate da esse con `lavoro/deriva_stanca.py` (zona testa 22%); gli altri 16 file non sono stati toccati e il foglio di controllo è stato rigenerato. Misure finali (criterio: pixel con alpha ≥128, saturazione ≥0,35, valore ≥0,25):

- `cavaliere_oro_normale`: tonalità mediana dei pixel saturi **31,3°** (fascia oro 30–58°) — armatura e bardatura ambra dominanti, cavallo baio scuro naturale (testiera e coperta ambra, baio solo su muso, orecchie, criniera e zampe).
- `cavaliere_blu_normale`: tonalità mediana **208,8°** (fascia blu acciaio 200–235°) — niente più turchese; cavallo baio come l'oro.
- Entrambe 256×316, angoli trasparenti, centro contenuto x=127,5, zoccoli con ultima riga opaca a y=291 (linea ancora 292).
- Stanche: altezza contenuto 0,968× rispetto alle normali, saturazione media ×0,55 (oro) e ×0,54 (blu).
- Verifica completa sui 20 file: formato, ancore, .b64 byte-identici dopo decodifica ed elenco passano per tutte le unità.

STATO: pronto
