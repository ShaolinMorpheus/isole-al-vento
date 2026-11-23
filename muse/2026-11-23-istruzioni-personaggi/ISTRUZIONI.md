# Per Claude — Nuovi personaggi (Gruppo 10): cosa usare e cosa cambiare nel gioco

Data: 23 nov 2026. Queste istruzioni riassumono lo stato finale della grafica dei personaggi dopo le approvazioni di Davide. I LEGGIMI delle singole cartelle restano il dettaglio tecnico; qui trovi l'elenco completo e le modifiche da applicare al codice.

## 1. I file da usare (stato finale)

Cartella principale: `muse/2026-11-23-personaggi-v2/` — 36 PNG (come sempre in formato `.png.b64`, da decodificare):
9 unità × 2 squadre (oro, blu) × 2 stati (normale, stanca).

Correzione successiva: `muse/2026-11-23-personaggi-v3/` contiene SOLO `guerriero_blu_normale.png` e `guerriero_blu_stanca.png`, che SOSTITUISCONO i due file omonimi della cartella v2 (il blu del guerriero era più acceso di quello del set; ora è allineato). Tutti gli altri file restano quelli della v2.

Da NON usare più:
- `muse/2026-11-22-personaggi/` (Parte A: design superati, approvati solo come tappa intermedia).
- Le vecchie pedine del Gruppo 3 in `muse/2026-11-18-pedine/` (`pedina_<tipo>_viola_<posa>.png` ecc.): sostituite da questo set.

## 2. La novità principale: l'avversario è BLU, non più viola

Decisione di Davide: il viola è abolito («colore finto»); la squadra del computer è ora BLU acciaio naturale. Nei file la squadra avversaria si chiama `blu`:

`<nome>_<squadra>_<stato>.png` con squadra = `oro` | `blu`, stato = `normale` | `stanca`.

Corrispondenza con i vecchi nomi del Gruppo 3: `pedina_<tipo>_oro_normale` → `<tipo>_oro_normale`; `pedina_<tipo>_viola_*` → `<tipo>_blu_*` (stessa unità, nuovo colore e nuovo disegno).

## 3. Le 9 unità: file, misure, ancore

Tutti i PNG sono trasparenti, larghezza 256 px, ancora (128, altezza−24): piedi o zoccoli al centro, a 24 px dal bordo basso. Nessuna ombra e nessun anello a terra nei PNG: ombre, anelli di selezione, barre vita e numeri li disegna il gioco, come prima. Lo stato `stanca` è la stessa unità con colori più spenti, leggermente più bassa e con la testa un po' china (è già disegnata così, non serve alcun filtro a codice).

| Unità | File (esempio oro normale) | Misure | Note |
|---|---|---|---|
| Esploratore | `esploratore_oro_normale.png` | 256×264 | zaino, cannocchiale, mantella corta |
| Guerriero | `guerriero_oro_normale.png` | 256×245 | scudo piccolo, spada grande (per il blu usare la v3) |
| Arciere | `arciere_oro_normale.png` | 256×286 | cappuccio, arco grande, faretra (variante A approvata) |
| Cavaliere | `cavaliere_oro_normale.png` | 256×316 | cavaliere su cavallo baio, lancia; il più imponente (variante B approvata) |
| Sciamano | `sciamano_oro_normale.png` | 256×294 | bastone con cristallo, mantello |
| Lanciere | `lanciere_oro_normale.png` | 256×300 | NUOVO: lancia lunga, scudo piccolo, postura ferma |
| Guaritore | `guaritore_oro_normale.png` | 256×280 | NUOVO: veste chiara con finiture di squadra, ampolla/bastone con foglia |
| Balestriere | `balestriere_oro_normale.png` | 256×270 | NUOVO: balestra grande, armatura leggera |
| Alfiere | `alfiere_oro_normale.png` | 256×320 | NUOVO: stendardo alto col colore della squadra; il più alto |

Per ogni unità esistono le 4 combinazioni: `_oro_normale`, `_oro_stanca`, `_blu_normale`, `_blu_stanca`.

## 4. Le 4 unità nuove: ruoli da collegare nel codice

Le grafiche sono pronte; le regole di gioco le definisci tu nel codice (Davide le ha descritte così nella specifica):

- **Lanciere**: colpisce da vicino ma sa difendersi (attacco a portata ravvicinata, buona difesa).
- **Guaritore**: cura le unità vicine.
- **Balestriere**: tira da lontano ma lento (lunga gittata, ritmo lento).
- **Alfiere**: aiuta le unità vicine a muoversi (bonus movimento alle unità adiacenti).

Statistiche, costi e bilanciamento sono scelte di codice: i disegni non impongono valori.

## 5. Resta da allineare al blu (NON ancora ridisegnato)

I personaggi sono a posto, ma il resto dell'identità avversaria nel gioco è ancora viola. Da decidere con Davide se ritoccare a codice o con una nuova consegna grafica:

- Base viola (blocchi base del Gruppo 1/terreno v2 e relativi elementi).
- Bandiere viola (`oggetto_bandiera_viola_*` del Gruppo 2).
- Colore viola dell'interfaccia (palette Gruppo 5: viola #9a86ee usato per la squadra avversaria).
- Schermata di sconfitta del Gruppo 6 (`sfondo_sconfitta.png`: bandiera viola sull'isola vinta).

Finché non sono allineati, in gioco si vedranno pedine blu contro basi/bandiere viola: è lo stato transitorio voluto, i personaggi erano il primo passo.

## 6. Invariato

Gruppi 1–9 già consegnati restano validi (in particolare i 24 fotogrammi dell'anemometro in `muse/2026-11-20-anemometro/`). Il guerriero oro è identico in v2 e in Parte A: è il master approvato da cui è nato il nuovo stile (proporzioni adulte, disegno dettagliato) seguito da tutte le bozze approvate il 23 nov.
