# Proposte di miglioramento per «Isole al Vento»

Scritte da Muse il 18 nov 2026 e approvate dall'utente, che le passa a Claude
per valutarle. Non sono specifiche vincolanti: sono idee da discutere.
Per ognuna è indicato cosa serve: solo codice, grafica già consegnata,
oppure grafica ancora da fare (Gruppo 5 interfaccia, Gruppo 6 schermate/icona).

## Gioco

1. **Previsione meteo** — Mostrare il meteo del round successivo accanto a
   quello corrente. Sapere in anticipo che arriva gelo o nebbia cambia le
   mosse del turno presente e aggiunge strategia a costo basso.
   Serve: solo codice + icone meteo (Gruppo 5, già previste).

2. **Direzione del vento con effetto vero** — Col vento: le frecce
   dell'arciere deviano di una casella sottovento; l'onda d'aria dello
   sciamano spinge più lontano nella direzione del vento. Il vento diventa
   una meccanica, non solo un'icona.
   Serve: solo codice. La freccia e l'onda sono già consegnate (Gruppo 4).

3. **Nebbia = nascondiglio** — Con la nebbia, le unità sui boschi non sono
   attaccabili a distanza. Valorizza il terreno bosco e l'esploratore,
   l'unità più fragile.
   Serve: solo codice.

4. **Colata dopo l'eruzione** — Le caselle di cenere restano pericolose per
   1 round (chi ci sta sopra perde vita), poi tornano normali. L'eruzione
   pesa anche dopo il botto.
   Serve: solo codice. L'overlay pericolo è già consegnato (Gruppo 4).

5. **Doppia stazione** — Chi controlla entrambe le stazioni meteo vede la
   previsione a 2 round invece di 1. Le stazioni diventano un obiettivo
   conteso, non solo una rendita in monete.
   Serve: solo codice (si appoggia alla proposta 1).

## Grafica e sensazione

6. **Micro-animazioni con i frame già consegnati** — Bandiere che sventolano
   (2 frame, Gruppo 2), coppe della stazione che ruotano (3 frame,
   Gruppo 2), foglie e cenere che volano quando c'è vento (singoli,
   Gruppo 4). Costo quasi zero, mappa molto più viva.
   Serve: solo codice; la grafica c'è già.

7. **Tinta del turno per meteo** — Una velatura leggera su tutta la mappa
   (fredda col gelo, calda col sereno) usando le tessere meteo del Gruppo 4.
   Il meteo si capisce senza guardare l'icona.
   Serve: solo codice; la grafica c'è già.

8. **Pedina «stanca» abbassata di 1–2 px a codice** — La posa stanca è solo
   colore (specifica dell'utente: silhouette identica). Se il gioco abbassa
   la pedina stanca di un paio di pixel in fase di disegno, si legge ancora
   meglio senza ridisegnare nulla.
   Serve: solo codice (offset di disegno, non un nuovo sprite).

## Partita e interfaccia

9. **Riepilogo fine partita** — Turni giocati, unità perse, eruzioni subite:
   una schermata semplice che invoglia a rigiocare.
   Serve: codice + sfondi vittoria/sconfitta (Gruppo 6, già previsti).

10. **Tre livelli di difficoltà del computer** — Cambia solo quanto il
    computer «vede» la previsione meteo (nessuna / 1 round / 2 round).
    Facile da bilanciare, allunga la vita del gioco.
    Serve: solo codice (si appoggia alle proposte 1 e 5).

11. **Prima partita guidata** — 3–4 suggerimenti sulle prime mosse
    («Muovi il guerriero», «Attenzione: tra 2 round erutta il vulcano»)
    in pannelli vuoti con testo composto dal gioco.
    Serve: codice + pannelli interfaccia (Gruppo 5, già previsti).

## Stato delle consegne grafiche al 18 nov 2026

- Gruppo 1 terreno v2: consegnato.
- Gruppo 2 oggetti: consegnato, approvato dall'utente.
- Gruppo 3 pedine: consegnato, in attesa di verdetto.
- Gruppo 4 effetti e meteo: consegnato, in attesa di verdetto.
- Gruppo 5 interfaccia e Gruppo 6 schermate/icona: non ancora commissionati.
