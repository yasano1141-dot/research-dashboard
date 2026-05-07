// =============================================================
// Site-wide helpers — themes, data loading, toasts, fav badge
// =============================================================

const THEME = {
  monday:    { jp: "老年医学・健康寿命",    short: "老年医学",   color: "var(--t-monday)" },
  tuesday:   { jp: "身体活動・運動疫学",    short: "運動疫学",   color: "var(--t-tuesday)" },
  wednesday: { jp: "筋質・体組成",          short: "筋質",       color: "var(--t-wednesday)" },
  thursday:  { jp: "脳・認知",              short: "脳・認知",   color: "var(--t-thursday)" },
  friday:    { jp: "疫学方法論",            short: "疫学方法",   color: "var(--t-friday)" },
  saturday:  { jp: "AI・データ科学",        short: "AI",         color: "var(--t-saturday)" },
  sunday:    { jp: "遺伝子・オミクス",      short: "オミクス",   color: "var(--t-sunday)" },
  pd:        { jp: "PD研究",                short: "PD研究",     color: "var(--t-pd)" },
};

const THEME_BY_EN = {
  "geriatrics-healthspan":         "monday",
  "physical-activity-epidemiology":"tuesday",
  "muscle-body-composition":       "wednesday",
  "brain-cognition":               "thursday",
  "brain-cognition-pd":            "thursday",
  "epidemiology-methods":          "friday",
  "ai-data-science":               "saturday",
  "genetics-omics":                "sunday",
  "pd-research":                   "pd",
};

const WEEKDAY_JP = ["日", "月", "火", "水", "木", "金", "土"];
const WEEKDAY_ORDER = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"];
// 8番目の独立テーマ「PD研究」を含む完全リスト（曜日カレンダーには使わない）
const THEME_ORDER = [...WEEKDAY_ORDER, "pd"];

// ---- Data loading ----------------------------------------------------------

let _papersCache = null;
let _reportsCache = null;

async function loadPapers() {
  if (_papersCache) return _papersCache;
  // Resolve data path relative to /docs
  const url = resolveDataUrl("data/papers.json");
  try {
    const r = await fetch(url, { cache: "no-cache" });
    if (!r.ok) throw new Error(r.status);
    _papersCache = await r.json();
  } catch (e) {
    console.warn("papers.json load failed", e);
    _papersCache = [];
  }
  return _papersCache;
}

async function loadReports() {
  if (_reportsCache) return _reportsCache;
  const url = resolveDataUrl("data/reports.json");
  try {
    const r = await fetch(url, { cache: "no-cache" });
    if (!r.ok) throw new Error(r.status);
    _reportsCache = await r.json();
  } catch (e) {
    console.warn("reports.json load failed", e);
    _reportsCache = [];
  }
  return _reportsCache;
}

// Resolves a path like "data/papers.json" or "index.html" from any page,
// based on the depth of the current document under /docs.
function resolveDataUrl(rel) {
  // Document path examples (under GitHub Pages):
  //   /<repo>/index.html         depth=0 from docs root
  //   /<repo>/papers.html        depth=0
  //   /<repo>/reports/X.html     depth=1
  // We detect depth by counting path segments after the repo root.
  const path = window.location.pathname;
  // Remove trailing filename
  const segs = path.split("/").filter(Boolean);
  // Drop trailing filename (anything with a dot)
  if (segs.length && segs[segs.length - 1].includes(".")) segs.pop();
  // The site is rooted at the second-to-last "docs" or repo segment.
  // Heuristic: count segments after a known root. We assume docs root is
  // the directory containing index.html. Easiest: look for "reports/" in path.
  let depth = 0;
  if (path.includes("/reports/")) depth = 1;
  else if (path.includes("/themes/")) depth = 1;
  const prefix = depth === 0 ? "" : "../".repeat(depth);
  return prefix + rel;
}

// ---- Date helpers ----------------------------------------------------------

function parseYMD(s) {
  // Accepts "YYYY-MM-DD" or "YYYYMMDD"
  if (!s) return null;
  if (/^\d{8}$/.test(s)) {
    return new Date(+s.slice(0,4), +s.slice(4,6)-1, +s.slice(6,8));
  }
  const m = s.match(/^(\d{4})-(\d{2})-(\d{2})/);
  if (!m) return null;
  return new Date(+m[1], +m[2]-1, +m[3]);
}

function fmtDateJP(s) {
  const d = parseYMD(s);
  if (!d) return s;
  return `${d.getFullYear()}年${d.getMonth()+1}月${d.getDate()}日（${WEEKDAY_JP[d.getDay()]}）`;
}

function fmtDateShort(s) {
  const d = parseYMD(s);
  if (!d) return s;
  return `${d.getMonth()+1}/${d.getDate()}`;
}

// ---- Toast -----------------------------------------------------------------

let _toastTimer;
function toast(msg) {
  let el = document.querySelector(".toast");
  if (!el) {
    el = document.createElement("div");
    el.className = "toast";
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.classList.add("show");
  clearTimeout(_toastTimer);
  _toastTimer = setTimeout(() => el.classList.remove("show"), 1800);
}

// ---- Favorite count badge -------------------------------------------------

function updateFavBadge() {
  const el = document.querySelector(".fav-pill .count");
  if (!el) return;
  el.textContent = String(Favorites.list().length);
}

// ---- Active nav link ------------------------------------------------------

function highlightActiveNav() {
  const path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav a").forEach(a => {
    const href = a.getAttribute("href").split("/").pop();
    if (href === path) a.classList.add("active");
  });
}

document.addEventListener("DOMContentLoaded", () => {
  highlightActiveNav();
  updateFavBadge();
});

// Expose
window.SITE = { THEME, THEME_BY_EN, WEEKDAY_ORDER, THEME_ORDER, loadPapers, loadReports,
                parseYMD, fmtDateJP, fmtDateShort, toast, updateFavBadge };
