// Shared service worker: cache-first app shell for all languages.
// Lives at the repo root; each page registers it with '../sw.js'
// (the landing uses './sw.js').
// After changing any page or asset, bump CACHE_VERSION (see AGENTS.md).
const CACHE_VERSION = 'v7';
const CACHE_NAME = `lang-cheat-${CACHE_VERSION}`;
const APP_SHELL = [
  './',
  './index.html',
  './assets/base.css',
  './deutsch/',
  './deutsch/index.html',
  './deutsch/manifest.webmanifest',
  './deutsch/icons/favicon.svg',
  './deutsch/icons/icon-180.png',
  './deutsch/icons/icon-192.png',
  './deutsch/icons/icon-512.png',
  './deutsch/icons/icon-512-maskable.png',
  './english/',
  './english/index.html',
  './english/manifest.webmanifest',
  './english/icons/favicon.svg',
  './english/icons/icon-180.png',
  './english/icons/icon-192.png',
  './english/icons/icon-512.png',
  './english/icons/icon-512-maskable.png',
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
