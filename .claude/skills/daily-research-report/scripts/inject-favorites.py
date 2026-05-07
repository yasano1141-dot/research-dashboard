#!/usr/bin/env python3
"""
お気に入り機能注入スクリプト v3
- 通常レポート HTML に data-* 属性とお気に入りチェックボックスJSを注入
- 詳細分析 HTML にも同様に注入
- 既存のセクション構造から各データを抽出して data-* 属性として埋め込む

使い方:
    python3 inject-favorites.py <regular_html_path> <detail_html_path> <date_key> <theme_name>

例:
    python3 inject-favorites.py \
        ~/Desktop/3勉強/claudeのファイル/火曜日_身体活動・運動疫学/20260428_身体活動・運動疫学.html \
        ~/Desktop/3勉強/claudeのファイル/火曜日_身体活動・運動疫学/20260428_身体活動・運動疫学_詳細分析.html \
        20260428 \
        身体活動・運動疫学
"""

import re
import html as html_lib
import sys
from pathlib import Path


def strip_tags(s: str) -> str:
    s = re.sub(r'<[^>]+>', '', s)
    s = html_lib.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def attr_escape(s: str) -> str:
    return (s.replace('&', '&amp;').replace('"', '&quot;').replace("'", '&#39;')
             .replace('<', '&lt;').replace('>', '&gt;'))


# === 注入されるJS ===
INJECT_JS = '''
<!-- favorites-injected-start -->
<script>
(function() {
  const STORAGE_KEY = 'researchFavorites_v2';
  const VIEWER_PATH = '../お気に入りビューア.html';

  function loadFavs() { try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); } catch (e) { return {}; } }
  function saveFavs(f) { localStorage.setItem(STORAGE_KEY, JSON.stringify(f)); }

  const sourceDate = document.body.dataset.sourceDate || '';
  const sourceTheme = document.body.dataset.sourceTheme || '';
  const cards = document.querySelectorAll('[data-paper-id]');
  if (cards.length === 0) return;

  function buildPaperData(card) {
    return {
      id: card.dataset.paperId,
      title: card.dataset.title || '', authors: card.dataset.authors || '',
      journal: card.dataset.journal || '', design: card.dataset.design || '',
      url: card.dataset.url || '', summary: card.dataset.summary || '',
      overview: card.dataset.overview || '', importance: card.dataset.importance || '',
      originality: card.dataset.originality || '', discovery: card.dataset.discovery || '',
      methodology: card.dataset.methodology || '', limitation: card.dataset.limitation || '',
      implication: card.dataset.implication || '', idea: card.dataset.idea || '',
      novelty: card.dataset.novelty || '', background: card.dataset.background || '',
      result: card.dataset.result || '', impact: card.dataset.impact || '',
      keywords: card.dataset.keywords || '',
      tags: (card.dataset.tags || '').split('|').filter(Boolean),
      sourceDate, sourceTheme,
    };
  }

  cards.forEach(card => {
    const id = card.dataset.paperId;
    const checkContainer = document.createElement('div');
    checkContainer.style.cssText = 'position:absolute;top:14px;right:14px;z-index:10';
    checkContainer.innerHTML = '<label style="display:flex;align-items:center;gap:6px;cursor:pointer;background:rgba(255,255,255,0.95);padding:6px 10px;border-radius:8px;border:1px solid #cbd5e1;font-size:12px;font-weight:600;color:#475569;user-select:none"><input type="checkbox" class="paper-fav-check" style="width:16px;height:16px;cursor:pointer" /><span class="fav-label">お気に入り</span></label>';
    card.style.position = 'relative';
    card.appendChild(checkContainer);

    const cb = checkContainer.querySelector('input');
    const label = checkContainer.querySelector('.fav-label');
    const favs = loadFavs();
    if (favs[id]) { cb.checked = true; label.textContent = '保存済み'; label.style.color = '#be185d'; }

    cb.addEventListener('change', () => {
      const favs = loadFavs();
      if (cb.checked) {
        const existing = favs[id] || {};
        favs[id] = { ...buildPaperData(card), rating: existing.rating || 0, addedAt: existing.addedAt || new Date().toISOString(), updatedAt: new Date().toISOString() };
        label.textContent = '保存済み'; label.style.color = '#be185d';
      } else {
        delete favs[id];
        label.textContent = 'お気に入り'; label.style.color = '#475569';
      }
      saveFavs(favs); updateBar();
    });
  });

  const header = document.querySelector('header.main') || document.querySelector('header');
  const bar = document.createElement('div');
  bar.style.cssText = 'background:white;border-radius:12px;padding:12px 18px;margin-bottom:20px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;box-shadow:0 2px 6px rgba(0,0,0,0.05)';
  bar.innerHTML = '<div style="font-size:14px;color:#0f172a;font-weight:600">📌 このページの選択：<span id="page-count" style="color:#be185d;font-size:18px">0</span> / ' + cards.length + ' 件</div><div style="font-size:13px;color:#64748b">全体保存：<span id="total-count" style="font-weight:700;color:#be185d">0</span> 件</div><button id="open-viewer" style="margin-left:auto;padding:8px 14px;background:#be185d;color:white;border:none;border-radius:6px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer">📤 お気に入りビューアを開く</button><button id="select-all" style="padding:8px 14px;background:#e0e7ff;color:#3730a3;border:none;border-radius:6px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer">全選択</button><button id="select-none" style="padding:8px 14px;background:#fee2e2;color:#991b1b;border:none;border-radius:6px;font-family:inherit;font-size:13px;font-weight:500;cursor:pointer">全解除</button>';
  if (header && header.parentNode) header.parentNode.insertBefore(bar, header.nextSibling);

  function updateBar() {
    const checks = document.querySelectorAll('.paper-fav-check');
    const checkedCount = [...checks].filter(c => c.checked).length;
    const pc = document.getElementById('page-count'); if (pc) pc.textContent = checkedCount;
    const tc = document.getElementById('total-count'); if (tc) tc.textContent = Object.keys(loadFavs()).length;
  }

  const sa = document.getElementById('select-all');
  if (sa) sa.addEventListener('click', () => { document.querySelectorAll('.paper-fav-check').forEach(c => { if (!c.checked) { c.checked = true; c.dispatchEvent(new Event('change')); } }); });
  const sn = document.getElementById('select-none');
  if (sn) sn.addEventListener('click', () => { document.querySelectorAll('.paper-fav-check').forEach(c => { if (c.checked) { c.checked = false; c.dispatchEvent(new Event('change')); } }); });
  const ov = document.getElementById('open-viewer');
  if (ov) ov.addEventListener('click', () => {
    const checks = document.querySelectorAll('.paper-fav-check');
    const selected = {};
    checks.forEach(cb => {
      if (cb.checked) {
        const card = cb.closest('[data-paper-id]');
        selected[card.dataset.paperId] = { ...buildPaperData(card), rating: 0, addedAt: new Date().toISOString() };
      }
    });
    const hash = Object.keys(selected).length > 0 ? '#add=' + btoa(encodeURIComponent(JSON.stringify(selected))) : '';
    window.open(VIEWER_PATH + hash, '_blank');
  });

  updateBar();
})();
</script>
<!-- favorites-injected-end -->
'''


def extract_regular_data(card_html: str) -> dict:
    """通常版の各セクションから抽出"""
    data = {}
    m = re.search(r'<h2>(.*?)</h2>', card_html, re.DOTALL)
    data['title'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<strong>著者:</strong>\s*([^<]+)</div>', card_html)
    data['authors'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<strong>ジャーナル・年:</strong>\s*([^<]+)</div>', card_html)
    data['journal'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<strong>研究デザイン:</strong>\s*([^<]+)</div>', card_html)
    data['design'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<a href="(http[^"]+)"', card_html)
    data['url'] = m.group(1) if m else ''

    def section(label):
        pattern = rf'<span class="label">{re.escape(label)}</span><br>\s*(.*?)\s*</div>'
        m = re.search(pattern, card_html, re.DOTALL)
        return strip_tags(m.group(1)) if m else ''

    data['summary'] = section('一言要約')
    data['overview'] = section('研究概要')
    data['importance'] = section('重要な点')
    data['originality'] = section('オリジナリティ')
    data['discovery'] = section('新発見項目')
    data['methodology'] = section('方法論評価')
    data['limitation'] = section('限界')
    data['implication'] = section('研究への示唆')
    data['idea'] = section('研究アイデア')

    tag_matches = re.findall(r'<span class="tag[^"]*">([^<]+)</span>', card_html)
    data['tags'] = '|'.join(tag_matches)

    data['novelty'] = data['background'] = data['result'] = data['impact'] = data['keywords'] = ''
    return data


def extract_detail_data(card_html: str, rank: int, theme: str) -> dict:
    """詳細版の各セクションから抽出"""
    data = {}
    m = re.search(r'<h2>(.*?)</h2>', card_html, re.DOTALL)
    data['title'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<strong>著者:</strong>\s*([^<]+)</div>', card_html)
    data['authors'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<strong>ジャーナル:</strong>\s*([^<]+)</div>', card_html)
    data['journal'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<strong>研究デザイン:</strong>\s*([^<]+)</div>', card_html)
    data['design'] = strip_tags(m.group(1)) if m else ''
    m = re.search(r'<a href="(http[^"]+)"', card_html)
    data['url'] = m.group(1) if m else ''

    sections = re.findall(
        r'<div class="section-block">\s*<h3>([^<]+)</h3>(.*?)</div>\s*(?=<div class="section-block">|<!--|</div>\s*<!--\s*TOP)',
        card_html, re.DOTALL
    )
    sec_map = {}
    for head, body in sections:
        head_clean = strip_tags(head)
        m_p = re.search(r'<p>(.*?)</p>', body, re.DOTALL)
        if m_p:
            sec_map[head_clean] = strip_tags(m_p.group(1))
        else:
            kws = re.findall(r'<div class="kw-item"><strong>([^<]+)</strong>\s*—\s*([^<]+)</div>', body)
            if kws:
                sec_map[head_clean] = ' / '.join(f"{k}: {v}" for k, v in kws)

    data['keywords'] = ''
    data['summary'] = data['novelty'] = data['background'] = data['methodology'] = ''
    data['result'] = data['impact'] = ''

    for head, val in sec_map.items():
        if '核心' in head or 'キーワード' in head:
            data['keywords'] = val
        elif '要旨' in head:
            data['summary'] = val
        elif '革新性' in head or '新規性' in head:
            data['novelty'] = val
        elif '研究背景' in head:
            data['background'] = val
        elif '研究手法' in head:
            data['methodology'] = val
        elif '研究成果' in head:
            data['result'] = val
        elif '社会的インパクト' in head:
            data['impact'] = val

    data['overview'] = data['background']
    data['importance'] = data['novelty']
    data['originality'] = data['novelty']
    data['discovery'] = data['result']
    data['limitation'] = ''
    data['implication'] = data['impact']
    data['idea'] = ''
    data['tags'] = f"詳細分析|TOP{rank}|{theme}"
    return data


def build_attrs(data: dict, paper_id: str) -> str:
    return (
        f' data-paper-id="{paper_id}"'
        f' data-title="{attr_escape(data.get("title", ""))}"'
        f' data-authors="{attr_escape(data.get("authors", ""))}"'
        f' data-journal="{attr_escape(data.get("journal", ""))}"'
        f' data-design="{attr_escape(data.get("design", ""))}"'
        f' data-url="{attr_escape(data.get("url", ""))}"'
        f' data-summary="{attr_escape(data.get("summary", ""))}"'
        f' data-overview="{attr_escape(data.get("overview", ""))}"'
        f' data-importance="{attr_escape(data.get("importance", ""))}"'
        f' data-originality="{attr_escape(data.get("originality", ""))}"'
        f' data-discovery="{attr_escape(data.get("discovery", ""))}"'
        f' data-methodology="{attr_escape(data.get("methodology", ""))}"'
        f' data-limitation="{attr_escape(data.get("limitation", ""))}"'
        f' data-implication="{attr_escape(data.get("implication", ""))}"'
        f' data-idea="{attr_escape(data.get("idea", ""))}"'
        f' data-novelty="{attr_escape(data.get("novelty", ""))}"'
        f' data-background="{attr_escape(data.get("background", ""))}"'
        f' data-result="{attr_escape(data.get("result", ""))}"'
        f' data-impact="{attr_escape(data.get("impact", ""))}"'
        f' data-keywords="{attr_escape(data.get("keywords", ""))}"'
        f' data-tags="{attr_escape(data.get("tags", ""))}"'
    )


def process_regular(html_path: Path, date_key: str, theme: str):
    text = html_path.read_text(encoding='utf-8')

    paper_starts = list(re.finditer(r'<div class="paper(?:\s+(top\d))?"\s*>', text))
    new_text = text
    offset = 0

    for idx, m in enumerate(paper_starts, start=1):
        start = m.start() + offset
        rest = new_text[start:]
        end_match = re.search(r'\n\s*<!--\s*(Paper|Summary)', rest[1:])
        block_end = start + 1 + end_match.start() if end_match else start + len(rest)
        block = new_text[start:block_end]
        data = extract_regular_data(block)
        attrs = build_attrs(data, f"{date_key}_{idx:02d}")

        old_open = m.group(0)
        new_open = old_open[:-1] + attrs + '>'
        new_text = new_text[:start] + new_open + new_text[start + len(old_open):]
        offset += len(new_open) - len(old_open)

    new_text = re.sub(r'<body>', f'<body data-source-date="{date_key}" data-source-theme="{theme}">', new_text)
    if 'favorites-injected-start' not in new_text:
        new_text = new_text.replace('</body>', INJECT_JS + '\n</body>')

    html_path.write_text(new_text, encoding='utf-8')
    print(f"通常版: {len(paper_starts)} paper を処理 → {html_path}")


def process_detail(html_path: Path, date_key: str, theme: str):
    text = html_path.read_text(encoding='utf-8')
    paper_starts = list(re.finditer(r'<div class="paper(?:\s+r\d)?"\s*>', text))
    new_text = text
    offset = 0

    for idx, m in enumerate(paper_starts, start=1):
        start = m.start() + offset
        rest = new_text[start:]
        end_match = re.search(r'\n\s*<!--\s*(TOP|Summary|footer|<footer)', rest[1:])
        block_end = start + 1 + end_match.start() if end_match else start + len(rest)
        block = new_text[start:block_end]
        data = extract_detail_data(block, idx, theme)
        attrs = build_attrs(data, f"{date_key}D_{idx:02d}")

        old_open = m.group(0)
        new_open = old_open[:-1] + attrs + '>'
        new_text = new_text[:start] + new_open + new_text[start + len(old_open):]
        offset += len(new_open) - len(old_open)

    new_text = re.sub(r'<body>', f'<body data-source-date="{date_key}" data-source-theme="{theme}（詳細）">', new_text)
    if 'favorites-injected-start' not in new_text:
        new_text = new_text.replace('</body>', INJECT_JS + '\n</body>')

    html_path.write_text(new_text, encoding='utf-8')
    print(f"詳細版: {len(paper_starts)} paper を処理 → {html_path}")


def main():
    if len(sys.argv) < 5:
        print("Usage: inject-favorites.py <regular_html> <detail_html> <date_key> <theme_name>")
        sys.exit(1)

    regular = Path(sys.argv[1])
    detail = Path(sys.argv[2])
    date_key = sys.argv[3]
    theme = sys.argv[4]

    process_regular(regular, date_key, theme)
    process_detail(detail, date_key, theme)
    print("✅ 完了")


if __name__ == '__main__':
    main()
