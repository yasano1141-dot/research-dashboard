#!/bin/bash
# =============================================================
#  📊 Daily Research Report — Double-click launcher
#  ダブルクリックするだけで今日のレポートを生成 → GitHubに反映 → Vercel公開
#  Claude Code サブスクリプションで動作（API従量課金なし）
# =============================================================

set -uo pipefail

REPO_DIR="$HOME/github/research-dashboard"
SITE_URL="https://research-dashboard.vercel.app"  # Vercel自動URL（後でREADMEと一緒に更新）

# Color helpers
B="\033[1m"; G="\033[32m"; Y="\033[33m"; R="\033[31m"; C="\033[36m"; N="\033[0m"

cd "$REPO_DIR" || { echo "❌ Cannot cd to $REPO_DIR"; read -p "Press enter to close..."; exit 1; }

clear
echo -e "${B}${C}╔══════════════════════════════════════════════════════════════╗${N}"
echo -e "${B}${C}║      📊 Daily Research Report — $(date +%Y-%m-%d) $(LC_ALL=ja_JP.UTF-8 date +%A)${N}"
echo -e "${B}${C}╚══════════════════════════════════════════════════════════════╝${N}"
echo ""

# ---- 1. Pre-flight checks ----
if ! command -v claude >/dev/null 2>&1; then
  echo -e "${R}❌ Claude Code CLI が見つかりません。${N}"
  echo "   インストール: https://docs.claude.com/claude-code"
  read -p "Press enter to close..." _
  exit 1
fi

# ---- 2. Pull latest from remote (avoid conflicts) ----
echo -e "${B}🔄 Step 1/5: GitHubから最新を取得${N}"
git pull --ff-only origin main 2>&1 | grep -v "^$" || true
echo ""

# ---- 3. Run Claude Code skill ----
WEEKDAY_JP=$(LC_ALL=ja_JP.UTF-8 date +"%A")
TODAY=$(date +%Y-%m-%d)
PROMPT="今日（${TODAY} ${WEEKDAY_JP}）の研究論文レポートを作成してください。
.claude/skills/daily-research-report/SKILL.md の絶対遵守ルールに従って実行：
- 通常レポート1本（木曜のみPD研究特化版を追加で計2本）
- 出力: docs/reports/{YYYYMMDD}_{theme_en}.html を作成
- docs/data/papers.json と reports.json に追記
- メール送信は不要
完了したらサマリー（生成ファイル名・10論文タイトル・PD関連数）を一行ずつ報告してください。"

echo -e "${B}🤖 Step 2/5: Claude Codeで論文検索＋レポート生成${N}"
echo -e "${Y}   （5〜10分かかります。コーヒーでも飲んでお待ちください）${N}"
echo ""

if ! claude --print --permission-mode bypassPermissions "$PROMPT"; then
  echo -e "${R}❌ Claude Code 実行失敗${N}"
  read -p "Press enter to close..." _
  exit 1
fi
echo ""

# ---- 4. Update RSS ----
echo -e "${B}📡 Step 3/5: RSSフィード更新${N}"
python3 scripts/generate_rss.py 2>&1 | tail -3 || echo "  (RSS生成をスキップ)"
echo ""

# ---- 5. Commit and push ----
echo -e "${B}📤 Step 4/5: GitHub に push${N}"
if [[ -n "$(git status --porcelain docs/)" ]]; then
  git add docs/data/ docs/reports/ docs/rss.xml 2>/dev/null
  git commit -m "📚 Daily report: ${TODAY} (${WEEKDAY_JP})" 2>&1 | tail -3
  git push origin main 2>&1 | tail -5
  echo -e "${G}   ✅ 反映完了${N}"
else
  echo -e "${Y}   ⚠️  変更なし（生成失敗の可能性）${N}"
fi
echo ""

# ---- 6. Notify and open browser ----
echo -e "${B}🌐 Step 5/5: サイトを開きます${N}"
echo "   ${SITE_URL}"
osascript -e 'display notification "今日の研究レポートが反映されました" with title "Research Dashboard" sound name "Glass"' 2>/dev/null || true
sleep 2
open "$SITE_URL" 2>/dev/null || true

echo ""
echo -e "${G}${B}✅ 完了！${N}"
echo ""
echo "Vercel側の反映には1〜2分かかります（自動デプロイ中）。"
echo ""
read -p "ウィンドウを閉じるにはEnterを押してください... " _
