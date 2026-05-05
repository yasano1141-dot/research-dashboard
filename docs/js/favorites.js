// =============================================================
// Cross-page favorites system (single-domain on GitHub Pages,
// so localStorage is shared between all site pages — and also
// shared with individual report HTML pages because they all
// live under the same origin).
//
// Storage key: researchFavorites_v3
// Backwards compat: imports from researchFavorites_v2 if present.
// =============================================================

const FAV_KEY = "researchFavorites_v3";
const FAV_LEGACY_V2 = "researchFavorites_v2";
const FAV_LEGACY_V1 = "researchFavorites_v1";

const Favorites = (() => {

  function _read() {
    try {
      const raw = localStorage.getItem(FAV_KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) { console.warn(e); }
    // Try legacy v2
    try {
      const v2 = localStorage.getItem(FAV_LEGACY_V2);
      if (v2) {
        const arr = JSON.parse(v2);
        localStorage.setItem(FAV_KEY, JSON.stringify(arr));
        return arr;
      }
    } catch (e) {}
    // Try legacy v1
    try {
      const v1 = localStorage.getItem(FAV_LEGACY_V1);
      if (v1) {
        const arr = JSON.parse(v1).map(p => ({ ...p, rating: 0 }));
        localStorage.setItem(FAV_KEY, JSON.stringify(arr));
        return arr;
      }
    } catch (e) {}
    return [];
  }

  function _write(arr) {
    localStorage.setItem(FAV_KEY, JSON.stringify(arr));
    document.dispatchEvent(new CustomEvent("favorites:change", { detail: { count: arr.length } }));
  }

  function list() { return _read(); }

  function has(id) {
    return _read().some(p => p.id === id);
  }

  function get(id) {
    return _read().find(p => p.id === id) || null;
  }

  function add(paper) {
    if (!paper || !paper.id) return;
    const arr = _read();
    if (arr.some(p => p.id === paper.id)) return;
    arr.push({ ...paper, addedAt: new Date().toISOString(), rating: paper.rating || 0 });
    _write(arr);
  }

  function remove(id) {
    _write(_read().filter(p => p.id !== id));
  }

  function toggle(paper) {
    if (has(paper.id)) {
      remove(paper.id);
      return false;
    } else {
      add(paper);
      return true;
    }
  }

  function rate(id, rating) {
    const arr = _read();
    const idx = arr.findIndex(p => p.id === id);
    if (idx < 0) return;
    arr[idx].rating = rating;
    _write(arr);
  }

  function clear() {
    _write([]);
  }

  function exportJSON() {
    return JSON.stringify(_read(), null, 2);
  }

  function importJSON(json, merge = true) {
    let incoming;
    try { incoming = JSON.parse(json); }
    catch (e) { throw new Error("JSON parse failed: " + e.message); }
    if (!Array.isArray(incoming)) throw new Error("JSON must be an array");
    if (!merge) { _write(incoming); return incoming.length; }
    const cur = _read();
    const byId = new Map(cur.map(p => [p.id, p]));
    let added = 0;
    for (const p of incoming) {
      if (!p.id) continue;
      if (!byId.has(p.id)) {
        byId.set(p.id, p);
        added++;
      } else {
        // merge rating + any missing fields
        const existing = byId.get(p.id);
        byId.set(p.id, { ...p, ...existing, rating: Math.max(existing.rating || 0, p.rating || 0) });
      }
    }
    _write(Array.from(byId.values()));
    return added;
  }

  return { list, has, get, add, remove, toggle, rate, clear, exportJSON, importJSON };
})();

// Update fav badge across pages on change
document.addEventListener("favorites:change", () => {
  if (window.SITE && SITE.updateFavBadge) SITE.updateFavBadge();
});

// Cross-tab sync
window.addEventListener("storage", e => {
  if (e.key === FAV_KEY) {
    document.dispatchEvent(new CustomEvent("favorites:change", { detail: { count: Favorites.list().length } }));
  }
});

window.Favorites = Favorites;
