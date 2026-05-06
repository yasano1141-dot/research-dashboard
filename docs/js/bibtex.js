// =============================================================
// BibTeX export — 論文配列を BibTeX 形式の文字列に変換
// =============================================================

const BibTeX = (() => {

  function _slugifyAuthor(authors) {
    if (!authors) return "Anon";
    // First author last name only
    const first = authors.split(/[,;]/)[0].trim();
    const parts = first.split(/\s+/);
    const last = parts[0] || "Anon";  // PubMed 形式 "Smith J" → "Smith"
    return last.replace(/[^a-zA-Z]/g, "") || "Anon";
  }

  function _extractYear(journal, fallbackDate) {
    const m = (journal || "").match(/\b(20\d{2}|19\d{2})\b/);
    if (m) return m[1];
    if (fallbackDate) {
      const m2 = fallbackDate.match(/(20\d{2})/);
      if (m2) return m2[1];
    }
    return "n.d.";
  }

  function _slugifyTitle(title) {
    return (title || "untitled").split(/\s+/).slice(0, 2).join("").replace(/[^a-zA-Z0-9]/g, "").slice(0, 20) || "untitled";
  }

  function _escapeBibTeX(s) {
    if (!s) return "";
    return s.replace(/[&%$#_{}~^\\]/g, c => "\\" + c)
            .replace(/[“”]/g, '"')
            .replace(/[‘’]/g, "'");
  }

  function paperToEntry(paper) {
    const author = _slugifyAuthor(paper.authors);
    const year = _extractYear(paper.journal, paper.first_seen_date);
    const titleSlug = _slugifyTitle(paper.title);
    const key = `${author}${year}${titleSlug}`;

    // Detect if preprint
    const isPreprint = /preprint|biorxiv|medrxiv/i.test(paper.journal || "");
    const entryType = isPreprint ? "@misc" : "@article";

    const journalClean = (paper.journal || "").replace(/,\s*\d{4}$/, "").trim();

    const fields = [
      ["title",   _escapeBibTeX(paper.title)],
      ["author",  _escapeBibTeX(paper.authors)],
      ["journal", _escapeBibTeX(journalClean)],
      ["year",    year],
      ["url",     paper.url],
      ["note",    _escapeBibTeX((paper.summary || "").slice(0, 250))],
    ].filter(([_, v]) => v);

    const fieldStr = fields.map(([k, v]) => `  ${k} = {${v}}`).join(",\n");

    return `${entryType}{${key},\n${fieldStr}\n}`;
  }

  function generate(papers) {
    if (!Array.isArray(papers)) return "";
    return papers.map(paperToEntry).join("\n\n") + "\n";
  }

  function download(papers, filename) {
    const bib = generate(papers);
    const blob = new Blob([bib], { type: "application/x-bibtex" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename || `papers_${new Date().toISOString().slice(0,10)}.bib`;
    a.click();
    URL.revokeObjectURL(url);
  }

  return { generate, paperToEntry, download };
})();

window.BibTeX = BibTeX;
