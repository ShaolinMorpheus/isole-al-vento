/* Isole al Vento - cache delle immagini sul telefono: dal secondo avvio parte subito, anche senza rete.
   La versione arriva dal parametro ?v= con cui la pagina registra questo file. */
const V = 'isole-' + (new URL(self.location.href).searchParams.get('v') || '0');
self.addEventListener('install', () => { self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== V) await caches.delete(k);
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET') return;
  const u = new URL(r.url);
  if (u.origin !== self.location.origin) return;
  if (u.pathname.indexOf('/assets/') >= 0) {
    // immagini e font: prima la cache, poi la rete
    e.respondWith((async () => {
      const c = await caches.open(V);
      const m = await c.match(r);
      if (m) return m;
      const res = await fetch(r);
      if (res.ok) c.put(r, res.clone());
      return res;
    })());
    return;
  }
  // pagina e resto: prima la rete (cosi' gli aggiornamenti arrivano), cache se non c'e' rete
  e.respondWith((async () => {
    try {
      const res = await fetch(r);
      if (res.ok) { const c = await caches.open(V); c.put(r, res.clone()); }
      return res;
    } catch (err) {
      const m = await caches.match(r);
      if (m) return m;
      throw err;
    }
  })());
});
