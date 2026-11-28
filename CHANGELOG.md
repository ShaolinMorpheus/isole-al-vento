# Isole al Vento — registro modifiche

> **Versioni:** il gioco è in alpha. Il numero interno (v59, v58…) conta le uscite; in gioco si vede come «v0.5.9 alpha» (decine e unità separate: 58 → v0.5.8). Le note qui sotto continuano a essere scritte a ogni modifica ma **in gioco non sono visibili** finché non viene deciso (interruttore `SHOW_LOG` in `www/index.html`).

(Il registro è anche dentro il gioco, ma per ora è nascosto: in gioco si vede solo la versione.)

## v65 — 28 nov 2026 · Comandi davvero fuori dalla mappa, Cura a scelta
- Menu, aiuti e zoom stanno in una riga sopra la mappa, fuori dal campo
- Il messaggio nero (meteo ecc.) compare in basso nella mappa
- Cornice gialla attorno alla mappa più sottile: mappa più grande
- Il Guaritore torna come prima: cura da solo le unità vicine a inizio turno
- L'aiuto Cura della campagna lo decidi tu: tocchi l'unità ferita da curare e torna a piena vita; l'aiuto si consuma solo dopo il tocco (toccando altrove annulli)

## v64 — 28 nov 2026 · Comandi fuori dalla mappa, meno monete, Guaritore a scelta
- Menu, aiuti e zoom stanno in una fascia sopra la mappa: non coprono più le caselle
- L'obiettivo della campagna è sotto la mappa, più grande
- Le monete arrivano più piano: +1 a round (invece di +2), più le stazioni
- Livello Normale: il computer recluta e agisce meno spesso
- Il Guaritore cura quando lo decidi tu: tocca un amico ferito accanto (casella verde) per curarlo di 2

## v63 — 27 nov 2026 · Pedine in alto non più tagliate
- Sopra la mappa c'è ora un po' di spazio: le pedine della prima riga non vengono più tagliate dalla cornice a inizio partita

## v62 — 26 nov 2026 · Caricamento più sicuro
- Se un'immagine non arriva alla prima apertura (rete lenta) il gioco riprova da solo: niente più campo vuoto da riaprire

## v61 — 26 nov 2026 · Menu scorrevole, pannello stabile
- Il menu principale scorre col dito anche con le sezioni aperte (lo scorrimento restava bloccato nella lista interna)
- Il pannello informazioni in basso in partita ha altezza fissa: toccando le pedine il campo non si muove più su e giù

## v60 — 26 nov 2026 · Stagione 1: 10 mondi
- La campagna passa da 3 a 10 mondi e da 24 a 83 livelli (7–10 livelli per mondo), presentata come «Stagione 1»
- Nuovi mondi: Golfo delle Tempeste, Foresta dei Sussurri, Altopiani del Gelo, Valle dei Tuoni, Arcipelago Spezzato, Cratere Antico, Occhio del Ciclone; ognuno con colore di mappa, meteo e boss proprio
- Campi fino a 14×19 e fino a 10 unità per parte nei mondi finali; scorta anche in modalità ondate (4-2)
- Mappa: barra per saltare ai mondi, intestazione «Stagione 1» con avanzamento, cartello «Stagione 2 · Arriverà prossimamente» in fondo
- Stelle per aprire i mondi: 32, 42, 53, 65, 76, 88, 100 (mondi 4–10)
- Nuove imprese (livelli, stelle, nemici, boss, difficoltà Alta, un traguardo per mondo); «Leggenda» = tutti gli 83 livelli
- Dati dei livelli generati da `strumenti/campagna/livelli_dati.py` + `livelli_mondi4.py`; bilanciati con simulazioni IA contro IA

## v59 — 25 nov 2026 · Versione alpha, registro nascosto
- La versione si vede come «v0.5.9 alpha» invece di «versione 59»
- Il registro modifiche non è più leggibile in gioco (resta qui e nell'array `CHANGELOG`); si riattiva con `SHOW_LOG`

## v58 — 25 nov 2026 · Difficoltà della campagna
- Nella scheda di ogni livello: Facile / Medio / Alta (scelta salvata). Insane c'è ma è bloccata col lucchetto
- Facile: avversario più lento, nemici un po' più fragili, +1 vita alle tue unità, più monete e 2 round extra. Medio: avversario più mite del normale, qualche moneta in più. Alta: avversario normale (mai il «difficile»)
- Perle: ×0,6 Facile, ×1 Medio, ×1,5 Alta; stelle uguali; si vede la difficoltà con cui hai vinto il livello
- Nuove imprese per la difficoltà Alta
- Livelli 1-7, 2-1, 2-6 e 3-1 più alla portata
- Corretto: i messaggi brevi nei menu della campagna ora si vedono

## v57 — 25 nov 2026 · Scheda livello compatta
- La scheda di un livello sta tutta nello schermo: titolo con X per chiudere, mappa piccola accanto a obiettivo e stelle, tasto «Inizia» (o «Riprendi» / «Ricomincia») sempre visibile in basso, senza scorrere

## v56 — 25 nov 2026 · La Campagna
- Nuovo tasto «Campagna»: 3 mondi, 24 livelli (campi da 7×9 a 13×17) con mappa, meteo e obiettivo propri
- Obiettivi: tieni le stazioni, elimina tutti, resisti alle ondate, porta il messaggero alla meta, sconfiggi il boss (uno per mondo)
- 3 stelle per livello (vittoria + due sfide bonus); servono stelle per aprire i mondi 2 e 3
- Perle di ricompensa e Arsenale: 3 potenziamenti per unità, validi solo in campagna; nuove unità sbloccabili completando i livelli
- Aiuti in partita (Cielo sereno, Cura, Rinforzo), 31 Imprese, Sfida del giorno con serie di giorni
- Salvataggio della campagna separato dalla partita veloce (che resta invariata)
- Spazio pubblicitario pronto ma spento («Pubblicità (prova)» nelle impostazioni mostra striscia e finto video)
- Corretto: «Continua partita» non resta più visibile senza una partita da riprendere

## v55 — 24 nov 2026 · Terreno a caselle separate di base
- Il terreno predefinito è «a caselle separate» (la variante scelta); le altre restano nel tasto «Terreno (prova)»

## v54 — 24 nov 2026 · Vulcano ben visibile e Fine turno pulito
- Zona di danno del vulcano molto più visibile: caselle arancio piene con bordo che pulsa e numeri −3 / −1 grandi, già dal round prima (più tenui) e forti nel round dell'eruzione; cenere calda (−1) più evidente
- Tasto «Fine turno» che pulsa: alone morbido che segue la forma, senza rettangolo attorno

## v53 — 24 nov 2026 · Più spettacolo
- Montagne a colori naturali (pietra calda, un po' di muschio, niente neve bianca)
- Pedine più grandi; tasto «Dimensione pedine (prova)»: normali / grandi / molto grandi
- Combattimento più spettacolare: scintille con coda, onda d'urto, arco di taglio, scia della freccia, numeri di danno più grandi, scossone a ogni colpo
- Vulcano scenografico: fumo e bagliore che crescono verso l'eruzione; tremolio d'eruzione lento e ondeggiante (diverso da quello dei colpi), pioggia di cenere, vibrazione a onde
- Schermate di vittoria (coriandoli) e sconfitta (pioggia) animate

## v52 — 24 nov 2026 · Menu che scorrono
- Menu iniziale scorrevole con le tendine aperte; menu di gioco, registro e Recluta con cornice intera e lista scorrevole, «Chiudi» sempre visibile

## v51 — 24 nov 2026 · Mappe più ricche e pedine ferme
- Mappe con meno zone vuote (boschi, monti e laghi dove c'era solo prato), simmetriche e con le corsie libere
- Solo la pedina selezionata fa l'animazione su e giù; le altre stanno ferme

## v50 — 24 nov 2026 · Tornano le prove grafiche
- Tasti «Grafica di prova», «Oggetti 3D», «Terreno (prova)» di nuovo nelle Impostazioni e nel menu di gioco (valgono le scelte salvate)
- Mare attorno al campo: ora è una prova a parte, spenta di base (il campo torna com'era)

## v49 — 24 nov 2026 · Mare, spiaggia e onde attorno all'isola
- Campo di gioco come isola nel mare: acque basse, schiuma animata, spiaggia, onde che scorrono (col vento nella sua direzione), riflessi di sole, ombre di nuvole, colori diversi con gelo e nebbia
- Scheda meteo e monete in alto sistemate (niente testo a capo o tagliato col vento)

## v48 — 24 nov 2026 · Caricamento pulito e più veloce
- Schermata di caricamento con barra, font inclusi, immagini dei menu in WebP, cache sul telefono (service worker)

## v47 — 24 nov 2026 · Menu adattato allo schermo
- La scheda del menu iniziale si scala per stare sempre intera (cornice compresa); tolta la bandiera dietro l'isoletta

## v46 — 24 nov 2026 · Isoletta ridisegnata e sfondo naturale
- Nuova isoletta con vulcano e palme; sfondo del menu senza neve, a colori naturali

## v45 — 24 nov 2026 · Grafica pastello in tutti i menu
- Cornice a pali con corda ritorta, bottoni, campi, pannelli e schede in tavolozza pastello; nuova isoletta; sfondi schiariti; testi più leggibili

## v44 — 24 nov 2026 · Menu con lettere dipinte (set v5)
- Scritte fisse del menu come immagini dipinte di Muse; pezzi rifiniti; sfondo nitido

## v43 — 23 nov 2026 · Correzione bottoni del menu
- Altezza minima dei bottoni forzata (erano schiacciati sul telefono)

## v42 — 24 nov 2026 · Menu iniziale rifatto
- Pezzi Muse menu-v4 e cornice v6; bottoni a 9 parti

## v41 — 23 nov 2026 · Suono sui tasti dei menu
- Piccolo suono a ogni tasto dei menu

## v40 — 23 nov 2026 · Nuovo menu iniziale
- Menu iniziale con i pezzi di Muse (menu-v3), margine pannello 200 px

## v39 — 23 nov 2026 · Grafica fissa
- Grafica di prova, Oggetti 3D e Terreno sempre attivi e tolti dai menu

## v38 — 23 nov 2026 · Corsie libere e Facile più semplice
- Mappe con una corsia libera a sinistra e una a destra; Facile: rinforzi solo Guerriero, Arciere, Esploratore

## v37 — 23 nov 2026 · Normale più facile da battere
- Computer in Normale meno preciso (più errori, a volte salta un'unità); Facile più morbido; Difficile invariato

## v36 — 23 nov 2026 · Nuova icona dell'app
- Icona di Muse v3 (vulcano, bandiere oro e blu pari) per tutte le densità Android

## v35 — 23 nov 2026 · Partita più lunga
- Stazioni da tenere 3 round di fila, massimo 36 round
- Tutorial: i tuoi personaggi sono quelli color oro, evidenziati

## v34 — 23 nov 2026 · Barra vita del guerriero più alta
- Barra della vita del Guerriero più in alto, si vede l'elmo

## v33 — 23 nov 2026 · Basi, bandiere e sconfitta in blu
- Basi, bandiere e schermata di sconfitta di Muse (squadra blu); gemelli oro rifatti

## v32 — 23 nov 2026 · Barra vita sopra la pedina
- La barra della vita sta fuori dalla sagoma, sopra la testa

## v31 — 23 nov 2026 · Pedine stanche e colore blu
- Posa stanca di Muse senza filtro grigio; colore avversario dell'interfaccia blu

## v30 — 23 nov 2026 · Nuovi personaggi e squadra blu
- Pedine di Muse (9 unità, oro/blu, normale/stanca) con «Grafica di prova»; il computer è blu
- Nuove unità: Lanciere, Guaritore, Balestriere, Alfiere (rinforzi, reclutamento, computer)
- Ancora da allineare al blu: basi, bandiere, interfaccia

## v29 — 22 nov 2026 · Pedine visibili dietro agli oggetti
- Oggetti (alberi, montagne, vulcano) trasparenti quando davanti a una pedina: la pedina resta dietro

## v28 — 22 nov 2026 · Rinforzi a scelta
- Rinforzo gratuito a scelta tra 2 unità (stessa offerta per entrambi), ogni 3 round dal round 4
- Si possono attraversare le proprie unità (non fermarcisi sopra)
- Facile: niente reclutamento con le monete

## v27 — 22 nov 2026 · Nuovo scopo: le stazioni meteo
- Base nemica non fa più vincere; si vince tenendo le 2 stazioni per 2 round di fila o eliminando tutte le unità
- Allo scadere dei 28 round vince chi ha controllato di più le stazioni
- IA orientata alle stazioni; avanzamento mostrato nel pannello round

## v26 — 19 nov 2026 · Anemometro più fluido
- 24 fotogrammi di Muse (Gruppo 9) per la rotazione fluida; velocità maggiore

## v25 — 19 nov 2026 · Terreno di Muse
- Zone di terra, sabbia, erba secca, sassi, fango; rive dei laghi; dettagli sparsi (Gruppo 8 di Muse)

## v24 — 19 nov 2026 · Solo verticale e caselle su prato unico
- Orientamento bloccato in verticale (manifest Android + blocco web)
- Terreno «caselle separate su prato unico»

## v23 — 19 nov 2026 · Menu in partita
- Tasto menu sul campo: riprendi, menu principale (salvata), suoni/vibrazione/musica/grafica
- Interruttore vibrazione
- Workflow APK: verifica firma + release «ultimo» scaricabile direttamente

## v22 — 19 nov 2026 · Suono di selezione, vibrazione, menu riordinato
- Suono + micro vibrazione alla selezione di una pedina
- Vibrazione nativa nell'app Android (plugin Haptics + permesso VIBRATE; serve nuovo APK)
- Menu iniziale a tendine, contenuto dentro la cornice

## v21 — 19 nov 2026 · Più spazio al campo, vita con numero, pedine animate
- Pannelli meteo/dati più piccoli: campo più grande
- Barra vita più grossa con numero
- Unità pronte: salto + alone dorato; usate: grigie
- Pedine animate (respiro, passo, sciamano che fluttua)
- Prato gigante con chiazze variegate
- Prova «Terreno» nel menu: caselle continue, 6 aspetti; di base «tutt’uno» (erba sfumata senza bordi, laghi fusi nel prato, griglia appena accennata)

## v20 · 19 nov 2026 — Si capisce quali unità si muovono
- Anello dorato (da muovere), rosso (può attaccare), spunta (finita); conteggio nel pannello; Fine turno pulsa solo a fine azioni.

## v19 · 19 nov 2026 — Pericolo eruzione sopra agli alberi
- Segni di pericolo del vulcano disegnati sopra oggetti e unità, più marcati.

## v18 · 19 nov 2026 — Musica e suoni del meteo
- Musica di sottofondo sintetizzata (tasto «Musica»), suoni del meteo di qualche secondo a ogni round, audio in pausa in secondo piano.

## v17 · 19 nov 2026 — Grafica di prova: schermate di Muse
- Sfondo e logo del menu, sfondi vittoria/sconfitta/pareggio dietro «Grafica di prova». Icona app e caricamento non ancora attivi.

## v16 · 19 nov 2026 — Grafica di prova: interfaccia di Muse
- Pannelli a 9 parti, bottoni a 3 stati, zoom, icone meteo/unità/moneta dietro «Grafica di prova».

## v15 · 19 nov 2026 — Cenere calda, riepilogo, pedina stanca
- Cenere dell'eruzione calda per 1 round (−1), riepilogo di fine partita, pedina stanca più bassa.

## v14 · 19 nov 2026 — Grafica di prova: effetti e meteo di Muse
- Meteo a tessere, fiocchi/foglie, colpi e frecce disegnati, eruzione con lava/fumo/cenere, caselle libere/attacco/pericolo e anello di selezione.

## v13 · 19 nov 2026 — Grafica di prova: pedine di Muse
- 5 unità × oro/viola, posa normale e stanca, dietro «Grafica di prova».

## v12 · 18 nov 2026 — Percorso a passi, bandiere fluide, oggetti 3D di prova
- Le pedine camminano casella per casella. Bandiere con stoffa a strisce, ondeggiamento continuo e più rapido. Tasto «Oggetti 3D (prova)»: alberi/montagne variati e sconfinanti.

## v11 · 18 nov 2026 — Suoni, partita salvata, mappe a numero
- Suoni/vibrazione (spegnibili), «Continua partita», mappe a numero + «Rigioca questa mappa», annulla recluta, serie e vittoria più veloce nelle statistiche.

## v10 · 18 nov 2026 — Grafica di prova: oggetti di Muse
- Con «Grafica di prova» accesa: pini/boschetti, montagne, stazione meteo animata (3 fotogrammi, velocità secondo il meteo), bandiere oro/viola, vulcano a 3 stati (calmo / arde a ≤1 round / eruttato).
- Pedine ed effetti ancora vettoriali. Regole invariate.

## Versione 9 — 17 nov 2026 — Grafica di prova: terreno di Muse
- Nuovo tasto «Grafica di prova» nel menu iniziale (spento di default). Acceso, le caselle usano i disegni di Muse (consegna terreno v2): prato, stazione meteo, bosco, lago, ghiaccio, monte, cenere e basi oro/viola.
- Più semplice: niente fronte di terra marrone né strati sotto le caselle. Ogni casella è la sola faccia del disegno di Muse, con angoli arrotondati e un filo di spazio verde scuro tra le vicine.
- Spento, il gioco resta com'è; la scelta resta salvata sul telefono.
- Vulcano, oggetti alti, pedine ed effetti restano vettoriali in attesa dei disegni di Muse.
- I disegni si caricano solo quando accendi il tasto. Regole e bilanciamento invariati.

## Versione 8 — 17 nov 2026 — Versione app per Android
- Il gioco si installa come app Android (Capacitor) e si carica da GitHub Pages: gli aggiornamenti arrivano da soli.
- Schermo intero senza barre di Android; margini di sicurezza per notch e angoli arrotondati.
- Pagina «Serve internet» con tasto Riprova se manca la connessione.
- Regole, grafica e bilanciamento invariati rispetto alla versione 7.

## Versioni 1–7 (24–25 ott 2026)
Vedi il registro dentro il gioco: mappa 9×13 con zoom, vista mezzo 3D, animazioni di combattimento, tutorial, vulcano e stazioni meteo, tre livelli del computer, Cavaliere e Sciamano.
