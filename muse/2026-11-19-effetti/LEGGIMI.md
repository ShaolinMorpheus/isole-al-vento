# Gruppo 4 — Effetti e meteo

Effetti che il gioco mostra sopra la mappa a caselle 9×13. Sono singoli
elementi: il gioco li muove, li ruota e li ripete, qui non ci sono
animazioni già montate. Tutti i PNG sono trasparenti (RGBA), disegnati
a programma nello stile del terreno v2 / oggetti / pedine: cartoon
pulito e luminoso, colori saturi, niente contorno scuro, niente scritte
(unico simbolo: il punto esclamativo nel triangolo di avviso di
`ui_casella_pericolo.png`).

Formato di consegna: ogni PNG viaggia anche come `nome.png.b64`
(base64 su una sola riga) perché il caricamento GitHub accetta solo
testo; per usare un file, decodificare il `.b64` e salvare il
risultato come `.png`. L'ordine dei 24 file è in `elenco.txt`.
La cartella `controllo/` contiene solo il foglio di prova: NON è
materiale di gioco e non è in `elenco.txt`.

## A. Meteo a tutto schermo — tessere 512×512 ripetibili

Da ripetere a tappeto sopra la mappa. Sono semitrasparenti e leggere:
la mappa resta leggibile sotto (alpha medio e copertura misurati).

| file | misura | alpha medio | copertura (alpha>10) | contenuto |
|---|---|---|---|---|
| meteo_pioggia.png | 512×512 | 3,6/255 (1,4%) | 6,4% | 155 strisce sottili inclinate 12° dalla verticale, bianco-azzurro |
| meteo_nebbia.png | 512×512 | 22,5/255 (8,8%) | 87,4% a alpha bassa | 20 banchi ellittici + 14 sbuffi morbidi, bianco caldo |
| meteo_gelo.png | 512×512 | 5,3/255 (2,1%) | 8,9% | 130 cristalli a 6 rami + brina, più fitti ai bordi (cornice periodica) |
| meteo_vento.png | 512×512 | 3,1/255 (1,2%) | 7,3% | 44 scie curve sottili, prevalentemente orizzontali |

Ripetibilità garantita per costruzione: ogni elemento è disegnato
anche traslato di ±512 px in x e in y (replica 3×3 su canvas
1536×1536, ritaglio centrale). Misura della cucitura (differenza
media assoluta tra le due colonne/righe che si toccano quando la
tessera si ripete, contro la differenza media tra colonne/righe
adiacenti interne; percentile della cucitura tra tutte le coppie
interne — sotto 100 = non è la coppia peggiore):

| file | cucitura X vs interna | cucitura Y vs interna | percentile X / Y |
|---|---|---|---|
| meteo_pioggia.png | 8,3 vs 4,6 | 1,8 vs 1,5 | 89 / 65 |
| meteo_nebbia.png | 0,3 vs 0,5 | 1,2 vs 1,0 | 8 / 60 |
| meteo_gelo.png | 14,5 vs 6,7 | 18,7 vs 6,7 | 87 / 96 |
| meteo_vento.png | 2,8 vs 1,5 | 2,3 vs 5,0 | 95 / 28 |

Per il gelo i valori grezzi di cucitura sono più alti perché la
cucitura cade nella banda di bordo, densa per progetto; confrontata
con le coppie interne della stessa banda (±31 px) la cucitura è in
linea (X 14,5 vs media banda 17,5; Y 18,7 vs 16,9): nessuna
discontinuità. Nel foglio di controllo ogni tessera è mostrata
ripetuta 2×2 sul prato: le giunture non si vedono.
Nota sul gelo: la cornice periodica fa sì che, ripetendo la tessera,
i bordi tra tessere vicine risultino più ricchi di brina (griglia
sottile agli incroci). È l'interpretazione coerente col wrap di
«più fitto ai bordi»: da valutare in gioco.
Nota sulla nebbia: la copertura è alta (87%) ma a alpha molto bassa
(medio 8,8%): è un velo, non una copertura.

## B. Elementi singoli — 256×256, centrati

Centroide del contenuto entro ±1,3 px da (128,128) in tutti i file.

| file | a cosa serve |
|---|---|
| eff_goccia.png | spruzzo di una goccia che cade (pioggia che colpisce) |
| eff_fiocco_a.png | fiocco di neve con ramificazioni (meteo gelo) |
| eff_fiocco_b.png | fiocco diverso: stella a 6 punte, nucleo esagonale |
| eff_foglia_a.png | foglia verde portata dal vento |
| eff_foglia_b.png | foglia giallo-arancio, orientamento diverso |
| eff_cenere.png | pezzetto di cenere che vola (dopo l'eruzione) |

## C. Colpi e combattimento — 256×256, centrati

| file | a cosa serve |
|---|---|
| eff_colpo.png | lampo di impatto corpo a corpo, giallo-bianco (stella r≈70 px) |
| eff_colpo_critico.png | impatto grande del colpo che uccide: stessa famiglia, r≈98 px (1,4×), anello d'urto e scintille |
| eff_taglio.png | segno di taglio da spada, arco diagonale (centroide (123,135): le estremità affusolate spostano il peso) |
| eff_freccia.png | freccia in volo ORIZZONTALE, punta a destra: il gioco la ruota. Asta spessore 9 px centrata a y=128 esatta; centroide totale (112,128) per impennaggio rosso e scia |
| eff_scintilla.png | piccola scintilla: nucleo e 4 raggi r≈30 px, glow tenue fino a ~39 px |
| eff_onda_vento.png | onda d'aria dello sciamano: 4 archi concentrici aperti verso destra, centro archi x=78, centroide (136,128) — spinta verso destra voluta |

## D. Eruzione — 256×256, centrati

| file | a cosa serve |
|---|---|
| eff_lava_a.png | schizzo di lava radiale, nucleo incandescente e glow caldo |
| eff_lava_b.png | schizzo allungato con coda e gocce separate |
| eff_fumo.png | nuvola di fumo scuro, grumi morbidi semitrasparenti ai bordi |
| eff_cenere_caduta.png | macchia di cenere da appoggiare sulla casella colpita: piatta, dall'alto, raggio ~90 px, bordi morbidi con alpha parziale (il terreno si vede sotto ai bordi), granelli e punti di brace spenta |

## E. Interfaccia sulla mappa — 256×256, sovrapposizioni sulla casella intera

Costruzione uguale per le tre caselle: velo semitrasparente su
rettangolo arrotondato (inset 6 px, raggio 28, angoli trasparenti),
alpha del velo interno 68/255 — il fondo resta visibile — più bordo
luminoso morbido ~14 px a alpha ~210 per leggersi su ogni fondo.
Nel foglio di controllo sono mostrate su prato, lago, bosco e cenere
del terreno v2: si leggono su tutti e quattro.

| file | a cosa serve |
|---|---|
| ui_casella_libera.png | casella dove la pedina può muoversi: velo verde chiaro luminoso |
| ui_casella_attacco.png | nemico attaccabile: velo rosso acceso |
| ui_casella_pericolo.png | casella a rischio eruzione: velo arancio + triangolo di avviso giallo-arancio ~88×76 px al centro con punto esclamativo scuro (alpha medio totale 103/255 per il simbolo quasi opaco) |
| ui_anello_selezione.png | anello sotto la pedina selezionata: ellisse 191×71 px, centro esatto (128,160) nella metà bassa della casella, bordo oro ~10 px con nucleo giallo-bianco e glow; interno trasparente |

## Cosa NON deve cambiare

- Le misure: tessere meteo 512×512, tutti gli altri 256×256, e la
  trasparenza reale (angoli alpha=0 nei singoli e negli overlay).
- La ripetibilità delle tessere meteo: non ritagliare né ridisegnare
  una tessera senza mantenere il wrap-around su entrambi gli assi.
- L'orientamento di eff_freccia.png (orizzontale, punta a destra) e
  di eff_onda_vento.png (apertura verso destra): il gioco li ruota.
- La posizione dell'anello di selezione (centro (128,160)) e la
  costruzione degli overlay (velo 68/255 + bordo luminoso): sono
  calibrati per leggersi sui quattro fondi.
- I nomi file in minuscolo senza spazi e l'ordine in `elenco.txt`.

## Novità rispetto alla consegna precedente

Gruppo nuovo (effetti e meteo): nessun file delle consegne
terreno/oggetti/pedine è stato toccato o sostituito. I fondi usati
nel foglio di controllo sono le caselle del terreno v2 (prato, lago,
bosco, cenere).

## Limiti dichiarati

- Resa vettoriale morbida da programma (forme pulite, glow, blur),
  non pittorica: coerente con gli altri pezzi disegnati a programma
  (stazione meteo del Gruppo 2), ma più «grafica» dei pezzi dipinti.
- eff_goccia.png a piena misura può ricordare una coroncina; a 45 px
  si legge come spruzzo d'acqua.
- eff_colpo_critico.png arriva a ~12 px dai bordi (è l'1,4× del
  colpo normale, come da specifica): nessun taglio, angoli alpha=0.
- Le tessere meteo nel foglio di controllo sono mostrate sul blocco
  prato v2 completo (faccia + fronte di terra): le fasce marroni
  nelle anteprime sono la fronte del blocco, non fanno parte del
  meteo.

STATO: pronto
