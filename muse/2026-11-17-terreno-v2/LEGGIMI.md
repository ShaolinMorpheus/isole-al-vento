# Gruppo 1 — Terreno v2 (16 blocchi, correzioni dalla RISPOSTA di Claude)

Nuova consegna che sostituisce `2026-11-17-terreno` (lasciata intatta).
Stesse misure (256×256, faccia 194, fronte 62, opachi), stessi nomi file,
stesso ordine in `elenco.txt`. I fronti di terra sono quelli della v1,
innestati invariati.

## Correzioni applicate

1. **Prato e stazione a/b stessa tinta.** La «a» è stata allineata alla
   «b» per canale fino a media e saturazione coincidenti; cambia solo la
   disposizione dei ciuffi. Misure sulla faccia: prato a (110,5, 135,3,
   33,7) sat 0,754 — prato b (110,4, 135,2, 33,9) sat 0,755; stazione
   a/b (108,4, 138,4, 36,5) sat 0,739 entrambe. Niente più effetto toppe.
2. **Bosco rifatto dal prato nuovo**: stessa trama d'erba, saturazione
   ×1,18 e luce ×0,60 con spinta sul verde. Media (68, 91, 14),
   saturazione 0,85: verde medio-scuro saturo, niente tono nero-verde,
   niente foglie marroni (gli alberi restano oggetti a parte).
3. **Meno dettaglio minuto**: passata morbida (mediana 3 + sfocatura 0,7)
   sulle facce d'erba: sparisce la grana fine, restano i ciuffi grandi.
   Controllo in `controllo/prova-telefono.png` (blocchi a 45 px).
4. **Basi**: piedistallo ridisegnato grande — ellisse 172×116 sulla
   faccia (~67% della larghezza del blocco), parete laterale di 15 px
   (più spesso), anello del colore di squadra largo 11 px vicino al
   bordo, ben visibile anche a 45 px; disco interno e piccolo segno
   centrale dello stesso colore; ombra morbida sul prato. Oro e viola
   differiscono solo dentro l'area del piedistallo (5.954 pixel, bbox
   x 42–213, y 43–171: anello e segno). Sopra va la bandiera (oggetto).
5. **Cenere ricalcolata dal prato nuovo** a/b con lo stesso metodo v1
   (luminanza annerita e desaturata, chiazze di cenere chiara e scorie):
   i ciuffi restano nelle stesse posizioni del prato nuovo.
   **Lago e ghiaccio invariati** (il lago non è cambiato): i 6 file
   lago/ghiaccio/monte sono byte-identici alla v1, verificato per hash.

## Controlli
- `controllo/contatto.png` — i 16 blocchi.
- `controllo/prova-telefono.png` — mosaico a 45 px per blocco (la misura
  reale sul telefono): prato a/b e stazione a/b si alternano senza
  cuciture di tinta, il bosco stacca come tono e non come colore,
  l'anello delle basi si legge.

STATO: pronto
