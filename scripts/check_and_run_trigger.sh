#!/bin/bash
# =============================================================
#  📱 Mobile Trigger Poller
#  GitHub Issues（label "trigger"）を10分おきにチェック。
#  新しいリクエストがあればレポート生成→push→Issue close。
#
#  launchd（com.yujiro.research-dashboard.poller）から呼ばれる。
# =============================================================

set -uo pipefail

REPO_DIR="$HOME/github/research-dashboard"
LOG_DIR="$REPO_DIR/scripts/logs"
GH="$HOME/.local/bin/gh"
SITE_URL="https://research-dashboard-nine.vercel.app"

mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/poller_$(date +%Y%m%d).log"

cd "$REPO_DIR" || exit 1

log() { echo "[$(date '+%H:%M:%S')] $*" >> "$LOG"; }

# ---- 0. 前提チェック ----
if [[ ! -x "$GH" ]]; then
  log "❌ gh CLI not found at $GH"
  exit 1
fi

# ---- 1. 最新を pull（他PCからの変更を取り込む） ----
git pull --ff-only origin main 2>>"$LOG" || true

# ---- 2. open issues with label "trigger" を取得 ----
issues_json=$("$GH" issue list --repo yasano1141-dot/research-dashboard \
  --label trigger --state open \
  --json number,title,body,createdAt 2>>"$LOG")

count=$(echo "$issues_json" | python3 -c "import sys, json; print(len(json.load(sys.stdin)))")

if [[ "$count" == "0" ]]; then
  # 新しいトリガーなし、静かに終了
  exit 0
fi

log "📬 Found $count trigger issue(s)"

# ---- 3. 各Issueを処理 ----
echo "$issues_json" | python3 -c "
import sys, json
for issue in json.load(sys.stdin):
    print(f\"{issue['number']}|{issue['title']}|{issue['body'].replace(chr(10), '%LF%')}\")
" | while IFS='|' read -r number title body_encoded; do
  body=$(echo "$body_encoded" | sed 's/%LF%/\n/g')
  log "----- Issue #$number: $title"

  # body から theme を抽出
  # 「auto（...）」「pd（...）」「monday（...）」のような形式
  theme=$(echo "$body" | grep -oE '(auto|pd|monday|tuesday|wednesday|thursday|friday|saturday|sunday)' | head -1)
  theme="${theme:-auto}"
  log "  theme=$theme"

  # 開始コメント
  "$GH" issue comment "$number" \
    --repo yasano1141-dot/research-dashboard \
    --body "🤖 Macが受信しました。レポート生成を開始します（テーマ: \`$theme\`）..." 2>>"$LOG" || true

  TODAY=$(date +%Y%m%d)
  WEEKDAY=$(LC_ALL=ja_JP.UTF-8 date +%A)
  EXIT=0

  case "$theme" in
    auto)
      # 今日の曜日に応じて適切なジェネレータ
      case "$(date +%a)" in
        Mon) script="generate_monday_curated.py";;
        Tue) script="generate_tuesday_curated.py";;
        Wed) script="generate_wednesday_curated.py";;
        Thu) script="generate_thursday_curated.py";;
        Fri) script="generate_friday_curated.py";;
        Sat) script="generate_saturday_curated.py";;
        Sun) script="generate_sunday_curated.py";;
      esac
      if [[ -f "scripts/$script" ]]; then
        python3 "scripts/$script" --date "$TODAY" >> "$LOG" 2>&1 || EXIT=$?
      else
        # ジェネレータ未作成の曜日は Claude Code を起動
        if command -v claude >/dev/null 2>&1; then
          claude --print --permission-mode bypassPermissions \
            "今日（${TODAY} ${WEEKDAY}）の研究レポートを生成。.claude/skills/daily-research-report/SKILL.md に従う。" \
            >> "$LOG" 2>&1 || EXIT=$?
        else
          log "  ⚠️ Generator not available for today; Claude CLI not found"
          EXIT=2
        fi
      fi
      ;;
    pd)
      python3 scripts/generate_pd_curated_report.py --date "$TODAY" >> "$LOG" 2>&1 || EXIT=$?
      ;;
    friday)
      python3 scripts/generate_friday_curated.py --date "$TODAY" >> "$LOG" 2>&1 || EXIT=$?
      ;;
    saturday)
      python3 scripts/generate_saturday_curated.py --date "$TODAY" >> "$LOG" 2>&1 || EXIT=$?
      ;;
    monday|tuesday|wednesday|thursday|sunday)
      script="generate_${theme}_curated.py"
      if [[ -f "scripts/$script" ]]; then
        python3 "scripts/$script" --date "$TODAY" >> "$LOG" 2>&1 || EXIT=$?
      else
        log "  ⚠️ scripts/$script not yet created"
        EXIT=3
      fi
      ;;
    *)
      log "  ⚠️ unknown theme: $theme"
      EXIT=4
      ;;
  esac

  # ---- 4. RSS再生成 + commit + push ----
  if [[ "$EXIT" == "0" ]]; then
    python3 scripts/generate_rss.py >> "$LOG" 2>&1 || true
    if [[ -n "$(git status --porcelain docs/)" ]]; then
      git add docs/data/ docs/reports/ docs/rss.xml 2>>"$LOG"
      git commit -m "📱 Mobile trigger: $theme report ($TODAY)" >> "$LOG" 2>&1 || true
      git push origin main >> "$LOG" 2>&1 || EXIT=5
    fi
  fi

  # ---- 5. 完了通知 + Issue close ----
  if [[ "$EXIT" == "0" ]]; then
    "$GH" issue comment "$number" \
      --repo yasano1141-dot/research-dashboard \
      --body "✅ 完了しました！
レポートはこちら → ${SITE_URL}/reports/${TODAY}_${theme}.html
（または最新一覧 → ${SITE_URL}/）
Vercel自動デプロイで1〜2分後に反映されます。" 2>>"$LOG" || true

    "$GH" issue close "$number" \
      --repo yasano1141-dot/research-dashboard 2>>"$LOG" || true

    log "✅ Issue #$number completed"
  else
    "$GH" issue comment "$number" \
      --repo yasano1141-dot/research-dashboard \
      --body "❌ エラーが発生しました（exit code: $EXIT）。Macで以下を確認してください：
\`\`\`
tail -50 $LOG
\`\`\`" 2>>"$LOG" || true
    log "❌ Issue #$number failed with exit $EXIT"
  fi
done

log "===== poller cycle complete ====="
