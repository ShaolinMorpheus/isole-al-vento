# Gruppo 11 — Squadra BLU: basi, bandiere, schermata di sconfitta

## Cosa sono i file e dove vanno nel gioco

Il viola è abolito: la squadra del computer è ora BLU acciaio, lo stesso blu dei
personaggi del Gruppo 10. Questa consegna sostituisce gli ultimi elementi di
gioco ancora viola (basi, bandiere, schermata di sconfitta) e, per coerenza,
include anche i gemelli ORO rifatti in coppia con lo stesso identico disegno,
così le due squadre restano una coppia pulita e sostituibile senza spostare
nulla nel gioco.

Riferimento di tinta vincolante: `guerriero_blu_normale.png` della consegna
`2026-11-23-personaggi-v3` — zona squadra: tonalità mediana 210,5°, saturazione
mediana 0,519 (blu acciaio naturale, NON elettrico).

## File (7, nell'ordine di `elenco.txt`)

1. `terreno_base_blu.png` — 256×256, blocco base del computer.
   Sostituisce `terreno_base_viola.png` (Gruppo 1, `2026-11-17-terreno`).
2. `terreno_base_oro.png` — 256×256, blocco base del giocatore, gemello della blu.
   Sostituisce `terreno_base_oro.png` (Gruppo 1).
3. `bandiera_blu_1.png`, `bandiera_blu_2.png` — 256×344 trasparente, 2 fotogrammi
   di sventolio. Sostituiscono `oggetto_bandiera_viola_1/2.png` (Gruppo 2,
   `2026-11-18-oggetti`).
4. `bandiera_oro_1.png`, `bandiera_oro_2.png` — 256×344 trasparente, gemelle.
   Sostituiscono `oggetto_bandiera_oro_1/2.png` (Gruppo 2).
5. `sfondo_sconfitta.webp` — 824×1760 verticale, WebP. Sostituisce
   `sfondo_sconfitta.png` (Gruppo 6, `2026-11-19-schermate`, che era
   1236×2640 PNG): stessa scena e stessa composizione, ricampionata a 2/3,
   con la bandiera sull'isola in blu acciaio invece che viola.

## Misure, ancore, ingombri (identici ai file sostituiti)

- Basi: blocchi interi 256×256 OPACHI (RGB), come i blocchi terreno del
  Gruppo 1: faccia superiore righe 0–193, fronte righe 194–255. Nota: i file
  attuali sono blocchi opachi, non sprite trasparenti; le nuove basi li
  rispecchiano esattamente per poter essere sostituite 1:1. Stesso piedistallo
  in pietra, stessa inclinazione, nessuna ombra aggiunta (non ce n'erano).
  Le due basi differiscono SOLO nel segno sul piedistallo: 1.466 pixel diversi,
  tutti in x 100–155, y 79–113 — esattamente come la coppia oro/viola attuale.
- Bandiere: 256×344, ancora (128, 320) come le attuali; ingombro del contenuto
  identico (x 65–239, y 16–338 in tutti e 4 i file). Palo di legno e base sono
  identici tra le due squadre: fuori dal drappo, blu e oro non differiscono in
  nessun pixel. I 2 fotogrammi di ciascuna coppia differiscono SOLO per le
  pieghe del drappo (differenze tutte in x 128–241, y 30–118; fuori da lì: 0).
- Schermata: 824×1760 WebP lossless (536.660 byte). Composizione, atmosfera e
  spazio libero per testo e tasti invariati rispetto alla PNG attuale.

## Il blu, misurato (mediane sulla zona squadra)

| File | Tonalità | Saturazione | Scarto dal riferimento |
|---|---|---|---|
| guerriero_blu_normale (riferimento) | 210,5° | 0,519 | — |
| bandiera_blu_1 (drappo) | 210,6° | 0,519 | +0,1° / ±0,000 |
| bandiera_blu_2 (drappo) | 210,6° | 0,519 | +0,1° / ±0,000 |
| terreno_base_blu (segno) | 210,4° | 0,519 | −0,1° / ±0,000 |
| sfondo_sconfitta (bandiera) | 210,5° | 0,540 | 0,0° / +0,021 |

Tolleranze richieste: ±6° e ±0,08 — ampiamente rispettate.

## Nessun viola/magenta

Verifica numerica su tutti e 7 i file: pixel opachi con tonalità in fascia
viola/magenta 260–345° = **0**, sia con saturazione ≥0,15 sia con ≥0,08.
Per ottenerla anche nella schermata, oltre alla bandiera sono stati ritoccati
i triangoli magenta dei festoni sull'isola (spostati a un rosa caldo, 355°:
restano festoni rosa, non più magenta) e, nelle basi, 6 pixel di fiori rosa
del prato (tonalità portata da ~340° a 355°). La WebP è codificata lossless
proprio per non reintrodurre tinte viola di compressione ai bordi.

## Come sono stati prodotti

Disegni di base invariati rispetto alle consegne approvate (stesso
piedistallo, stesso palo, stessa scena): è cambiato solo il colore delle
parti di squadra, con ricolore in HSV che conserva ombreggiatura e luminanza
(tonalità portata a ~210° con compressione della dispersione, saturazione
riscalata sulla mediana del riferimento). La base oro è il disegno attuale
con la sola micro-correzione dei 6 pixel di fiori; le bandiere oro sono i
file attuali. Così ingombri, prospettive e ancore combaciano per costruzione.

## Cosa NON deve cambiare

- Misure e ancore: basi 256×256 con faccia 194 px e fronte 62 px; bandiere
  256×344 con ancora (128, 320); schermata 824×1760.
- Palo e base delle bandiere uguali per le due squadre; tra i 2 fotogrammi
  cambiano solo le pieghe del drappo.
- Il blu di squadra è quello dei personaggi del Gruppo 10 (210,5° / 0,519):
  non usare tinte più accese (il vecchio guerriero v2, saturazione 0,98,
  era l'errore da non ripetere).
- Niente viola o magenta in nessun elemento di squadra.

## Note sui `.b64`

Per ogni file c'è il gemello `nome.b64`: il file codificato in base64 su una
sola riga (il canale GitHub accetta solo testo). Per usarli: decodificare il
`.b64` e salvare il risultato col nome originale (per la schermata:
`sfondo_sconfitta.webp.b64` → `sfondo_sconfitta.webp`). Tutti i `.b64` sono
stati verificati byte-identici dopo decodifica (7/7, più il foglio di
controllo). La cartella `controllo/` contiene solo il foglio di prova
`prova_squadra_blu.png` (base+bandiera+pedina delle due squadre sul prato e
ritagli della schermata): NON è materiale di gioco e non è in `elenco.txt`.

STATO: pronto
