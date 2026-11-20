# Gruppo 9 — Anemometro: 24 fotogrammi di rotazione della stazione meteo

## Cosa sono e dove vanno

24 fotogrammi `stazione_f00.png` … `stazione_f23.png` che sostituiscono i 3 fotogrammi
`oggetto_stazione_0/40/80.png` del Gruppo 2 (`muse/2026-11-18-oggetti/`): stessa stazione
meteo, stesso disegno, ma l'anemometro a 3 coppe ruota in passi di 5° invece di 40°,
così in gioco la rotazione è fluida. Il ciclo si ripete ogni 120° (3 coppe):
f00 = 0°, f01 = 5°, …, f23 = 115°; il fotogramma dopo f23 è di nuovo f00.

- Misure: 256 × 320 px, PNG trasparenti, per tutti i 24 file.
- Ancora: (128, 296), identica alla stazione del Gruppo 2.
- Ordine: quello di `elenco.txt` (f00 → f23, da ripetere in ciclo).
- Senso di rotazione: orario nel piano dell'immagine, lo stesso degli originali
  0° → 40° → 80° del Gruppo 2, costante da un fotogramma al successivo.
- f00 coincide con `oggetto_stazione_0`, f08 (40°) con `oggetto_stazione_40` e
  f16 (80°) con `oggetto_stazione_80`: vedi «Verifiche» per gli scarti misurati.

## Come sono fatti (metodo)

- Centro di rotazione misurato dai 9 centroidi delle coppe dei 3 originali:
  (127,41; 71,48), raggio coppe 46,1 px, residuo massimo del fit 0,10 px.
- **Base statica unica**: palo, base, piedistallo e perno centrale sono gli stessi
  pixel in tutti i 24 fotogrammi, copiati da `oggetto_stazione_0` e mai ridisegnati.
  Il perno è tenuto fermo in modo forzato per un disco di 13 px di raggio attorno
  al centro.
- **Gruppo rotante**: bracci + coppe separati dalla base nel fotogramma a 0° e ruotati
  di k×5° attorno al centro, in spazio premoltiplicato (niente aloni), poi ricomposti
  sulla base statica con compositing «over».
  Nota: il gruppo rotante è quello originale, **non** risimmetrizzato. Misurando si
  vede che il gruppo del Gruppo 2 non è perfettamente simmetrico a 120° e che i suoi
  fotogrammi a 40°/80° derivano dalla rotazione rigida del gruppo a 0° (i centroidi
  delle coppe ruotate coincidono con gli originali entro 0,2 px): risimmetrizzare
  avrebbe allontanato f08/f16 dagli originali.
- **Nitidezza coppe**: leggero unsharp (raggio 1,2, intensità 30%) applicato solo
  alle coppe/bracci del master, come chiesto («coppe leggermente più nitide»);
  in f00 lo scarto dall'originale resta sotto la soglia di misura (0 px con
  differenza premoltiplicata > 16 nel disco rotante, differenza media 0,29).
- **Ombra a terra**: i fotogrammi del Gruppo 2 avevano un'ellisse scura
  semitrasparente sotto la base (4.608 px, y ≥ 284, alpha < 200). In questa consegna
  l'utente la vieta: è stata rimossa dalla base statica. Base e piedistallo restano
  pixel-identici all'originale (opachi fino a y = 299). Nei pixel quasi trasparenti
  (alpha < 8) l'RGB è azzerato, così il motore non crea sbavature di colore quando
  scala gli sprite.

## Verifiche (i 3 controlli chiesti, con i numeri)

1. **Sequenza senza salti** — Differenza premoltiplicata nel disco rotante tra
   fotogrammi consecutivi (pixel con scarto > 16): i 23 passi tra fotogrammi
   ricampionati stanno tra 2.807 e 2.884 (media 2.859, ±1,4%). Spostamento medio
   dei centroidi delle coppe a ogni passo: 3,93–4,12 px (atteso ≈ 4,0 px a
   raggio 46,1 per 5°), regolare anche nel passo di chiusura.
2. **Chiusura del ciclo** — Il passo f23 → f00 misura 3.344 pixel > 16, lo stesso
   ordine degli altri passi (+17% sulla media): è l'unico passo che coinvolge f00,
   che è il master non ricampionato (tutti gli altri fotogrammi sono rotazioni
   ricampionate allo stesso modo). Nessun salto di posizione: lo spostamento dei
   centroidi nel passo di chiusura è nella stessa banda 3,93–4,12 px.
3. **Palo fermo** — Fuori dal disco rotante (r > 80 px dal centro) i 24 fotogrammi
   sono pixel-identici alla base statica: **0 pixel diversi** in tutti i 24.
   Il perno (r < 10 px) è pixel-identico in tutti i 24 fotogrammi: **0 diversi**.
   La zona statica di f00 coincide con quella di `oggetto_stazione_0`:
   **0 pixel diversi** (esclusa l'ellisse d'ombra rimossa, vedi sopra).

Altre misure:

- Confronto con gli originali (differenza premoltiplicata, zona del disco rotante):
  f08 vs `oggetto_stazione_40`: 456 px con scarto > 16, 150 con scarto > 40,
  media 1,27. f16 vs `oggetto_stazione_80`: 515 px > 16, 175 px > 40, media 1,38.
  Sono residui di ricampionamento confinati ai bordi di coppe e bracci (fuori dal
  disco gli scarti sono 0 per costruzione).
- Colore delle coppe stabile: colore medio delle coppe per fotogramma
  R 24,7–25,2, G 200,5–200,9, B 172,9–173,3 (scarto massimo ≈ 0,5 su 255):
  nessun lampeggio.
- Formato: 24/24 file a 256 × 320, angoli trasparenti.
- `.png.b64`: 24/24 decodificano byte-identici ai PNG (stessa cosa per il foglio
  di controllo).

## File

- `stazione_f00.png` … `stazione_f23.png` (+ `.png.b64` su una sola riga, da
  decodificare per ottenere i PNG omonimi).
- `elenco.txt`: ordine dei 24 fotogrammi.
- `controllo/prova_anemometro.png` (+ `.b64`): griglia 6×4 dei 24 fotogrammi su
  fondo mare scuro e striscia di confronto originale vs nuovo per 0°/40°/80°
  (negli originali si vede l'ombra a terra, rimossa nei nuovi fotogrammi).

## Cosa NON deve cambiare

- Misure (256 × 320) e ancora (128, 296).
- La base statica (palo, base, perno) deve restare quella unica usata qui: se in
  futuro servono correzioni ai fotogrammi, si rigenera la serie dal master, non si
  ritocca un singolo fotogramma.
- Niente ombra a terra aggiunta nei PNG: se il gioco vuole l'ombra, la disegna lui.

STATO: pronto
