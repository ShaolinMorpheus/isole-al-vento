# Isole al Vento – promemoria per Google Play

Stato: build di prova dell'AAB pronta (workflow «Crea AAB per Google Play»); mancano campagna, chiave di caricamento e scheda dello store.

## Cosa serve
- [ ] Account Google Play Console (a pagamento una tantum) con verifica dell'identità
- [ ] Chiave di caricamento (keystore) + 4 segreti nel repo: PLAY_KEYSTORE_B64, PLAY_KEYSTORE_PASS, PLAY_KEY_ALIAS, PLAY_KEY_PASS (conservare una copia della chiave fuori da GitHub)
- [ ] Test chiuso: almeno 12 tester iscritti per 14 giorni di fila (se l'account personale è stato creato dopo il 13 nov 2023), poi richiesta di accesso alla produzione
- [ ] Informativa privacy pubblicata a un indirizzo web (modello in `play/privacy.template.html`), con email di contatto
- [ ] Scheda dello store: testi (bozza in `play/store-listing.md`), icona 512, immagine 1024×500, almeno 2 screenshot verticali
- [ ] Questionario sulla classificazione dei contenuti (IARC) e modulo «Sicurezza dei dati» (al lancio: nessun dato raccolto)
- [ ] Android 16 (API 36) come target: già controllato dal workflow (la build si ferma se è più basso)
- [ ] Decisione: l'identificativo dell'app resta `it.isolealvento.game` (non si cambia più dopo il primo caricamento); chi ha l'APK di prova deve disinstallarlo una volta prima di installare quello da Play (firma diversa)

## Differenze rispetto all'APK degli amici
- Il gioco sta dentro l'app (si apre anche senza internet); gli aggiornamenti passano da Google Play invece di arrivare da soli dalla pagina web
- Nessuna pubblicità al lancio (se arriveranno: consenso UMP, AdMob con ID reale, aggiornare privacy e modulo dati)
