// Shared service worker: cache-first app shell for all languages.
// Lives at the repo root; deck pages register it with '../../sw.js'
// (the landing uses './sw.js').
// After changing any page or asset, bump CACHE_VERSION (see AGENTS.md).
const CACHE_VERSION = 'v12';
const CACHE_NAME = `lang-cheat-${CACHE_VERSION}`;
const APP_SHELL = [
  './',
  './index.html',
  './assets/base.css',
  './de/ru/',
  './de/ru/index.html',
  './de/ru/manifest.webmanifest',
  './de/ru/icons/favicon.svg',
  './de/ru/icons/icon-180.png',
  './de/ru/icons/icon-192.png',
  './de/ru/icons/icon-512.png',
  './de/ru/icons/icon-512-maskable.png',
  './en/ru/',
  './en/ru/index.html',
  './en/ru/manifest.webmanifest',
  './en/ru/icons/favicon.svg',
  './en/ru/icons/icon-180.png',
  './en/ru/icons/icon-192.png',
  './en/ru/icons/icon-512.png',
  './en/ru/icons/icon-512-maskable.png',
  // Redirect stubs for pre-restructure URLs (deutsch/, english/) and the
  // /de/ default: cached so old bookmarks and installed PWAs resolve offline.
  './deutsch/',
  './english/',
  './de/',
  './icons/favicon.svg',
  './icons/icon-32.png',
  './icons/icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(APP_SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  if (request.method !== 'GET' || new URL(request.url).origin !== self.location.origin) return;

  // Navigations: network first (fresh HTML), offline fallback to the cached page.
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request).then((cached) => cached || caches.match('./index.html')))
    );
    return;
  }

  // Static assets: cache first, then network (and cache the result).
  event.respondWith(
    caches.match(request).then((cached) => cached || fetch(request).then((response) => {
      if (response.ok) {
        const copy = response.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(request, copy));
      }
      return response;
    }))
  );
});
