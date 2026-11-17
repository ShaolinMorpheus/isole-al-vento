# Istruzioni per Muse — cartella di scambio

## REGOLE

- Scrivi solo dentro `muse/`. Non modificare `www/`, `.github/`, `android-icons/` né altro: il gioco lo integra Claude.
- Una consegna = una sottocartella, nome `AAAA-MM-GG-argomento` (es. `2026-11-18-terreno`). Non sovrascrivere consegne vecchie: se correggi, crea una nuova cartella con suffisso `-v2`, `-v3`.
- Ogni consegna contiene un `LEGGIMI.md` con: cosa sono i file e dove vanno usati nel gioco; misure in px, numero di frame, nomi e ordine dei file; cosa NON deve cambiare; cosa è nuovo rispetto alla consegna precedente.
- Formato: PNG con sfondo trasparente per sprite e frame; nomi in minuscolo, senza spazi (es. `unita_guerriero_oro.png`). Se non puoi caricare PNG, salva ogni immagine come testo base64 `nome.png.b64` (una sola riga) e metti in `elenco.txt` l'ordine.
- Stile: cartoon pulito e luminoso, quasi realistico nei volumi, NIENTE contorno scuro, colori saturi (verdi pieni, non spenti), luce da in alto a sinistra, ombre morbide, stessa prospettiva e stessa scala in tutti gli sprite.
- Stati dello stesso oggetto (prato/cenere, lago/ghiaccio, vulcano calmo/in eruzione) mantengono lo stesso design.
- Quando hai finito, scrivi nel `LEGGIMI.md` la riga `STATO: pronto`. Fino ad allora `STATO: in lavorazione`.

## COSA FA CLAUDE

- Legge la consegna, la integra come opzione di prova dietro un tasto «Grafica di prova» (spenta di default), la prova e risponde in `muse/<consegna>/RISPOSTA.md`.
- Dopo l'approvazione di Davide, la rende definitiva. Claude non ritocca i tuoi disegni: se qualcosa stona, li rifai tu.

## DOVE SONO LE COSE

- Gioco: `www/index.html` (non toccare).
- Le tue consegne: `muse/<data-argomento>/`.
