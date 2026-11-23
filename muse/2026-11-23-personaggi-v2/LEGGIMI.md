# Gruppo 10 — Personaggi v2 (set completo, design approvati dall'utente)

**Questa consegna SOSTITUISCE i design della Parte A** (`2026-11-22-personaggi`) per le 8 unità rifatte su bozze approvate: esploratore, arciere, cavaliere, sciamano, lanciere, guaritore, balestriere, alfiere.
Le bozze sono state approvate da Davide il 23 nov 2026, con varianti scelte: **arciere = variante A** (cappuccio, arco lungo verticale), **cavaliere = variante B** (lancia in resta, posa da carica).
Il **guerriero è invariato**: i suoi 4 file sono copiati tali e quali dalla Parte A (master già approvati in precedenza).

**Avviso per Claude:** la squadra avversaria è **BLU** (blu acciaio naturale), non viola. I file si chiamano `<unita>_blu_<stato>.png`. Il viola resta da allineare in basi/bandiere/interfaccia in una consegna successiva.

## Contenuto

36 PNG con sfondo trasparente (in questa cartella anche come `nome.png.b64`, base64 su una sola riga): 9 unità × 2 squadre (oro, blu) × 2 stati (normale, stanca). Ordine in `elenco.txt`.

| Unità | Misura (px) | Segno distintivo |
|---|---|---|
| esploratore | 256×264 | cappello a tesa larga, zaino con mappe, cannocchiale |
| guerriero | 256×245 | scudo piccolo e spada grande (dalla Parte A, invariato) |
| arciere | 256×286 | cappuccio, arco lungo verticale, faretra |
| cavaliere | 256×316 | in sella al cavallo baio, lancia in resta; il più imponente |
| sciamano | 256×294 | bastone con sfera di cristallo ciano, mantello ampio |
| lanciere | 256×300 | lancia lunga verticale, scudo piccolo, postura ferma |
| guaritore | 256×280 | veste chiara crema, finiture del colore squadra, ampolla verde |
| balestriere | 256×270 | balestra grande davanti, passo basso accovacciato |
| alfiere | 256×320 | stendardo alto quasi tutto del colore squadra; il più alto |

Per tutte: larghezza 256, ancora (128, altezza−24), piedi/zoccoli al centro a 24 px dal bordo basso. Niente ombra disegnata, niente anello a terra, niente contorno scuro spesso.

## Metodo

- **Oro normale** = le bozze approvate da Davide, tali e quali (guerriero: i file della Parte A).
- **Blu normale** = disegno **nato blu**, generato da zero usando la bozza oro come riferimento di composizione e design (stesso metodo del guerriero blu v7 approvato): stesso personaggio, stessa posa e stessi oggetti, palette blu acciaio naturale sulle parti squadra. **Nessuna ricolore a programma.** Pelle sempre rosa naturale; acciaio grigio solo dove è metallo vero; cuoio marrone caldo; il cavallo del cavaliere resta baio naturale (blu solo bardatura e armatura); la veste del guaritore resta chiara (blu solo le finiture); il cristallo dello sciamano resta ciano in entrambe le squadre.
- **Stanca** = derivata a programma dal normale della stessa squadra: saturazione ×0,55, valore HSV ×0,92, compressione verticale 3% ancorata alla linea dei piedi (i piedi non si muovono), testa china con spostamento morbido (max 4 px) sulla zona testa (30% del contenuto, 22% per il cavaliere).

## Cosa NON deve cambiare

- Nomi file, misure e ancore: il gioco li carica così.
- Il guerriero di questa cartella è identico a quello della Parte A: non sostituirlo con altre versioni.
- Le due squadre si distinguono dal colore (oro ambra / blu acciaio); pelle, acciaio, cuoio e manto del cavallo sono naturali in entrambe.

## Verifica

Foglio di controllo in `controllo/prova_personaggi_v2.png`: tutte le 36 pedine a ~110 px sul prato e le 18 normali ingrandite.
Verifiche numeriche superate su tutti i file: misure esatte, angoli trasparenti, centro del contenuto entro 128±2, piedi sulla linea dell'ancora entro 1 px; oro normale byte-identici alle bozze approvate (guerriero: ai file della Parte A); stanche con altezza ~0,97 e saturazione ~0,55 rispetto al loro normale; `.b64` tutti byte-identici dopo decodifica.

## Note oneste (scostamenti dei disegni nati blu rispetto alle bozze oro)

I blu sono disegni nuovi, non copie: dettagli e tratti dei volti non sono identici agli oro (è il metodo approvato). In particolare:

- **Cavaliere blu**: posa più frontale della bozza B (cavallo che carica più verso lo spettatore, testa più alta; in 3 tentativi il generatore ha dato sempre questa lettura). Composizione, lancia in resta e identità conservate; cavallo rimasto baio. Contenuto un po' più largo dell'oro (251 contro 240 px).
- **Balestriere blu**: posa più eretta/in affondo invece dell'accovacciata bassa della bozza (in tutti i 4 tentativi); blu squadra però molto leggibile (34% dei pixel saturi in fascia blu, mediana fuori-cuoio 212°). Nel blu sono blu anche pantaloni e copricapo, marroni nell'oro.
- **Sciamano blu**: sprite scalato per larghezza, quindi in gioco appare leggermente più grande/largo dell'oro.
- **Misure di tonalità**: per arciere, sciamano, cavaliere e balestriere la mediana calcolata su *tutti* i pixel saturi resta in fascia calda, perché cuoio, legno, pelle e (per il cavaliere) manto baio — parti che per specifica restano naturali in entrambe le squadre — pesano più della stoffa. La componente squadra è in fascia blu acciaio in tutte: esploratore 205°, arciere 211°, cavaliere 38% dei saturi in fascia 200–235° (oro: 0%), sciamano 204° sulla stoffa, lanciere 208°, guaritore 210° sulle finiture, balestriere 212° fuori-cuoio, alfiere 208° con telo al 77% in fascia blu. Nessun pixel in fascia turchese/verde-acqua dove non deve stare.

STATO: pronto
