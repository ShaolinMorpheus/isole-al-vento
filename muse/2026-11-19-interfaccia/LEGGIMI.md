# Gruppo 5 — Interfaccia (specifica aggiornata v15)

Sfondi di pannelli e bottoni e icone per l'interfaccia del gioco.
**Nessuna scritta e nessun simbolo nei PNG**: il testo (font Fredoka) e i
simboli dei bottoni zoom (+, −, mappa intera) li disegna il gioco.
Tutte le misure sono a 3× rispetto ai px CSS del telefono.
Disegno a programma (Python/PIL, supersampling 4×): bordi e raggi sono
precisi al pixel e gli stati condividono la stessa maschera.

## Palette usata (valori guida v15)

- Fondo mare `#0e2433` · pannello `#10222f` · linea `#2a4a5d`
- Mare chiaro `#15384c` · oro `#f2b84b` · viola `#9a86ee`
- Menta `#59cdb7` · corallo `#ef6a5a` · testo `#eaf3f2`

Campioni misurati sui file: centro pannelli `#10222f` esatto, bordo pannelli
e bottoni chiari `#2a4a5d` esatto, centro bottone chiaro `#15384c` esatto,
centro bottone oro `#f2b84b` esatto, bordo oro `#b57e1e`.

## Pannelli (5) — vuoti, ridimensionabili «a 9 parti»

| File | Misura PNG | Raggio | Margine di taglio 9-parti |
|---|---|---|---|
| `ui_pannello_meteo.png` | 762×312 | 42 | 48 px su tutti i lati |
| `ui_pannello_stat.png` | 354×312 | 42 | 48 px su tutti i lati |
| `ui_pannello_info.png` | 1140×234 | 42 | 48 px su tutti i lati |
| `ui_pannello_scheda.png` | 1200×900 | 60 | 66 px su tutti i lati |
| `ui_pannello_riga.png` | 1020×192 | 42 | 48 px su tutti i lati |

Costruzione: riempimento `#10222f` uniforme in tutta la zona centrale;
unica sfumatura verticale morbida (alto appena più chiaro, basso appena
più scuro) confinata entro il margine di taglio; bordo uniforme `#2a4a5d`
da 6 px, interamente interno; fuori dagli angoli trasparenza vera.
Prova eseguita: ridimensionamento 9-parti a larghezza ×1,5 e altezza ×0,75
di tutti e 5 i pannelli → zone angolari pixel-identiche agli originali
(0 px diversi) e differenza alle cuciture media e massima 0: il centro si
allunga senza giunture visibili.

## Bottoni — sfondi senza testo né simboli

Per ogni bottone, forma, raggio e maschera alpha sono **identici in tutti
gli stati** (verifica a programma: 0 px diversi tra le maschere).

- **Chiaro/mare** (Recluta, Annulla) — 327×126, raggio 36, fondo `#15384c`,
  bordo `#2a4a5d`:
  `ui_bottone_chiaro_normale.png`, `ui_bottone_chiaro_premuto.png`,
  `ui_bottone_chiaro_disattivo.png`
- **Oro** (Fine turno) — 441×126, raggio 36, fondo oro con sfumatura
  verticale (alto `#f8cd76`, centro `#f2b84b`, basso `#eda63a`), bordo
  `#b57e1e`:
  `ui_bottone_oro_normale.png`, `ui_bottone_oro_premuto.png`,
  `ui_bottone_oro_disattivo.png`, `ui_bottone_oro_pulsante.png`
- **Zoom** — 114×114, raggio 36, stile chiaro/mare, nessun simbolo:
  `ui_zoom_normale.png`, `ui_zoom_premuto.png`, `ui_zoom_disattivo.png`

Stati: **premuto** = stessa forma, fondo scurito (×~0,75) e luce interna
ridotta (effetto schiacciato solo di colore); **disattivo** = desaturato
(saturazione ~40%) e spento (×~0,85), bordo meno contrastato.
**Pulsante** (solo oro): come il normale, con in più un alone luminoso
morbido `#ffe9b0` **dentro** la forma, lungo il bordo interno e sfumato
verso il centro (centro invariato) — nessun pixel fuori dal rettangolo
arrotondato, maschera identica agli altri stati. Il gioco può animarlo
alternando normale/pulsante o modulando l'opacità del pulsante.

## Icone 96×96 — trasparenti, centrate

Nel gioco si vedono a 26 px (pannello) e a 16 px («Dopo»): forme grandi e
semplici, verificate a vista a entrambe le misure nel foglio di controllo.

- Meteo: `icona_meteo_sereno.png` (sole oro `#f2b84b`),
  `icona_meteo_vento.png` (scie curve menta `#59cdb7`),
  `icona_meteo_pioggia.png` (nuvola chiara e gocce azzurre),
  `icona_meteo_nebbia.png` (bande morbide chiare ad alpha decrescente),
  `icona_meteo_gelo.png` (fiocco bianco-azzurro)
- Unità (testa/busto, colori naturali neutri — valgono per entrambi i
  giocatori, niente oro/viola di squadra): `icona_unita_esploratore.png`
  (faccia scoperta, capelli castani, sciarpa verde), `icona_unita_guerriero.png`
  (elmo e grande scudo d'acciaio), `icona_unita_arciere.png` (cappuccio verde
  e arco), `icona_unita_cavaliere.png` (elmo con grande pennacchio corallo),
  `icona_unita_sciamano.png` (cappuccio teal e bastone con grande cristallo
  azzurro ghiaccio)
- `icona_moneta.png` (moneta oro `#f2b84b`, bordo `#c78f2d`, nessun simbolo),
  `icona_cuore.png` (cuore corallo `#ef6a5a`)

## Ordine dei file

`elenco.txt` elenca i 27 PNG nell'ordine: pannelli, bottone chiaro,
bottone oro, zoom, icone meteo, icone unità, moneta, cuore.

## Controllo

`controllo/prova_interfaccia.png` — su fondo mare `#0e2433`: ogni pannello
in originale e allungato con taglio a 9 parti, i bottoni in tutti gli
stati (chiaro ×3, oro ×4, zoom ×3), le 12 icone a 96, 26 e 16 px.

## Formato di consegna

Oltre ai PNG, ogni immagine è presente come `nome.png.b64` (base64 su una
sola riga) da decodificare in `nome.png`; anche il foglio di controllo ha
il suo `.b64`. Verificato: decodifica byte-identica per tutti i file.

## Cosa NON deve cambiare

- Misure, raggi e margini di taglio dichiarati: il gioco ritaglia i
  pannelli a 9 parti con questi margini.
- Le maschere alpha degli stati di un bottone devono restare identiche:
  se uno stato viene rifatto, vanno rifatti tutti gli stati del bottone.
- Le icone unità restano in colori neutri: la squadra si distingue dalle
  pedine e dai colori di interfaccia, non da queste icone.

## Nuovo rispetto alla consegna precedente

È la prima consegna di interfaccia (Gruppo 5), secondo la specifica
aggiornata alla v15 del gioco: misure reali a 3×, palette esatta e nomi
file definitivi sostituiscono la bozza originaria del gruppo.

STATO: pronto
