# Gruppo 1 — Terreno (16 blocchi)

## Cosa sono i file e dove vanno nel gioco

Sono le caselle della mappa 9×13 di «Isole al Vento». Ogni file è un blocco completo
(faccia superiore + fronte laterale) da disegnare al posto della casella vettoriale
attuale, dietro il tasto «Grafica di prova». L'anemometro della stazione meteo è un
oggetto separato (Gruppo 2): qui la casella stazione è solo prato con area centrale
più libera e piana dove appoggiarlo. Gli alberi del bosco e la montagna alta sono
oggetti a parte: qui non sono disegnati.

## Misure (impostale così nel gioco)

- Ogni blocco: **256×256 px**.
- **Faccia superiore: righe 0–193, alta 194 px.**
- **Fronte laterale: righe 194–255, alta 62 px.**
- I blocchi sono opachi (RGB, niente trasparenza): il disegno riempie tutto il
  256×256, quindi non serve canale alfa.
- Bordi sinistro/destro raccordati in orizzontale: le superfici sono state rese
  tileabili con sfumatura della cucitura (roll di metà larghezza e blend), così
  due blocchi vicini combaciano senza fessure. Il raccordo è a livello di
  continuità della texture, non pixel-identico tra tipi diversi di casella.

## File (16, nell'ordine di `elenco.txt`)

1. `terreno_prato_a.png`, `terreno_prato_b.png` — prato, 2 varianti.
2. `terreno_stazione_a.png`, `terreno_stazione_b.png` — prato base stazione meteo, centro più libero/piano.
3. `terreno_bosco_a.png`, `terreno_bosco_b.png` — prato scuro di sottobosco, senza alberi.
4. `terreno_lago_a.png`, `terreno_lago_b.png` — lago incavato con sponda di terra.
5. `terreno_ghiaccio_a.png`, `terreno_ghiaccio_b.png` — lo stesso lago ghiacciato (stato gelo).
6. `terreno_monte_a.png`, `terreno_monte_b.png` — superficie rocciosa, senza montagna alta.
7. `terreno_cenere_a.png`, `terreno_cenere_b.png` — lo stesso prato a/b bruciato (effetto eruzione).
8. `terreno_base_oro.png`, `terreno_base_viola.png` — prato con piedistallo in pietra e segno anello/stemma oro o viola, senza testo.

Per ogni PNG c'è il gemello `nome.png.b64`: il PNG codificato in base64 su una
sola riga (il canale GitHub accetta solo testo). Per usarli: decodificare il
`.b64` e salvare il risultato come `.png`. La cartella `controllo/` contiene solo
il foglio di contatto per la verifica visiva: NON è materiale di gioco e non è
in `elenco.txt`.

## Come sono garantite le coerenze tra stati

- **Lago/ghiaccio**: il ghiaccio è derivato dal lago con la stessa maschera di
  sponda (stessa sagoma, stessa posizione). Fuori dalla superficie dell'acqua i
  pixel di lago e ghiaccio sono identici (verificato: differenza massima 0 su
  ~21.800 pixel per variante); cambia solo l'interno, che diventa lastra chiara
  con crepe, a livello del prato.
- **Prato/cenere**: la cenere è una trasformazione del blocco prato
  corrispondente (desaturazione e annerimento sulla stessa luminanza, più
  chiazze di cenere e scorie morbide): ciuffi e dettagli restano nella stessa
  posizione (correlazione di luminanza prato/cenere: 0,95 variante a, 0,92 b).
- **Basi oro/viola**: disegno identico; differisce solo il segno sul piedistallo
  (verificato: 1.231 pixel diversi su 65.536, tutti dentro l'area del segno,
  x 102–154, y 80–112).
- Luce da in alto a sinistra in tutti i blocchi; ombra morbida di raccordo
  (gradiente) tra faccia superiore e fronte, nessuna linea di contorno scura.

## Cosa NON deve cambiare

- Le misure: 256×256, faccia 194 px, fronte 62 px.
- La sagoma di sponda condivisa tra lago e ghiaccio a/b e la derivazione
  prato→cenere a/b: se un disegno stona, lo rifà Muse in una nuova consegna,
  non va ritoccato qui.
- I nomi file in minuscolo senza spazi e l'ordine in `elenco.txt`.

STATO: pronto
