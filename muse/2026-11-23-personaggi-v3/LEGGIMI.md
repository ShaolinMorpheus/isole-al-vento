# Gruppo 10 — Personaggi v3: correzione guerriero blu

## Cosa contiene questa cartella

Correzione di **2 soli file** del set personaggi: il guerriero della squadra blu.

- `guerriero_blu_normale.png` — guerriero blu ridisegnato, palette allineata al set
- `guerriero_blu_stanca.png` — posa stanca derivata dal nuovo normale

## Perché

Nel set `2026-11-23-personaggi-v2` il guerriero blu veniva dalla bozza v7, generata prima delle altre unità: il suo blu era più acceso ed elettrico di quello del resto del set, e in fila con le altre pedine blu si vedeva che era «di un blu diverso» (segnalazione dell'utente con screenshot, 23 nov 2026). Questa cartella riallinea il guerriero al blu del set; **tutti gli altri file del set restano quelli della consegna v2 e non vanno toccati**.

## Sostituzione

Questi 2 file **sostituiscono** gli omonimi in `muse/2026-11-23-personaggi-v2/`:

- `guerriero_blu_normale.png`
- `guerriero_blu_stanca.png`

Il guerriero oro e tutte le altre 8 unità (entrambe le squadre, entrambi gli stati) restano quelli della v2.

## Misure e ancora

- Entrambi i file: PNG trasparente 256×245 px, ancora (128, 221) — piedi al centro, ultima riga opaca a y=220.
- Contenuto: bbox x 24–231 (centro 127,5), y 8–220 per il normale; la stanca è compressa del 3% ancorata ai piedi (contenuto alto 207 px contro 213).
- Niente ombra disegnata, niente anello a terra, niente contorno scuro spesso.

## Allineamento del blu — misure

Criterio unico per tutte le misure: pixel opachi (alpha ≥128) con tonalità in famiglia blu (190–240°) e saturazione ≥0,25; mediana su quella zona (stoffa/armatura di squadra).

| File | Tonalità mediana | Saturazione mediana |
|---|---|---|
| Set v2 — esploratore blu | 207,7° | 0,488 |
| Set v2 — arciere blu | 210,9° | 0,450 |
| **Set v2 — riferimento (esploratore+arciere)** | **209,3°** | **0,471** |
| Guerriero blu v2 (vecchio, da sostituire) | 212,8° | **0,976** |
| **Guerriero blu v3 (questo file)** | **210,5°** | **0,519** |

Scarti del nuovo guerriero rispetto al riferimento del set: tonalità +1,2° (tolleranza ±5°), saturazione +0,048 (tolleranza ±0,06). Il difetto del vecchio era quasi tutta saturazione: 0,976 contro 0,471 del set — da qui l'effetto «blu elettrico».

## Metodo

- Normale: disegno **nato blu**, generato da zero su sfondo magenta con il master oro approvato (bozza v2) come riferimento di design — stesso guerriero: massiccio, elmo d'acciaio con cresta blu, scudo rotondo piccolo al fianco, spada grande alzata, cinghie e borselli di cuoio marrone, pelle rosa naturale, acciaio grigio solo sul metallo vero. Nessuna ricolore a programma. Due generazioni: la prima è stata scartata perché troppo desaturata (saturazione mediana 0,327, sotto la fascia del set); la seconda è quella consegnata.
- Scontorno e normalizzazione con lo stesso script della Parte A (`normalizza_b.py`): contenuto scalato in altezza fino alla linea dell'ancora, centrato x=128.
- Stanca derivata dal nuovo normale con `deriva_stanca.py` della Parte A: saturazione ×0,55, valore ×0,92, compressione verticale 3% ancorata ai piedi, testa china morbida (zona testa 30%). Verifiche: rapporto altezza contenuto 0,972; rapporto saturazione media 0,543.

## Controllo

`controllo/confronto_blu.png`: striscia sul prato con guerriero blu vecchio (v2), guerriero blu nuovo (v3) e arciere blu del set come riferimento, a piena misura e a ~110 px. A vista, il nuovo guerriero in fila con l'arciere non si stacca più per colore; il vecchio sì.

## Cosa NON deve cambiare

- Non toccare nessun altro file del set v2: solo questi 2 file sostituiscono gli omonimi.
- Il design del guerriero (posa, scudo piccolo, spada grande, elmo con cresta) è quello approvato: non ridisegnarlo.
- La palette blu di riferimento è quella del set v2 (tonalità ~209°, saturazione ~0,47): future unità blu vanno allineate a questi valori, non al vecchio guerriero.

## Nota sui file .b64

Ogni PNG è affiancato dal suo `.png.b64`: il contenuto del PNG codificato in base64 su una sola riga (più a capo finale). Per riottenere il PNG: decodificare il base64. Verificato: la decodifica di tutti e 3 i .b64 (2 sprite + foglio di controllo) è byte-identica ai PNG.

STATO: pronto
