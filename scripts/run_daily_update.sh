#!/bin/bash
# =============================================================
#  毎朝8:00 JSTにlaunchdから呼ばれるエントリポイント
#  - daily-research-report スキルを起動
#  - 生成完了後、自動で git add / commit / push
#  - GitHub Pagesが自動デプロイ → https://<username>.github.io/research-dashboard/
# =============================================================

set -euo pipefail

REPO_DIR="$HOME/github/research-dashboard"
LOG_DIR="$REPO_DIR/scripts/logs"
mkdir -p "$LOG_DIR"
LOG="$LOG_DIR/$(date +%Y%m%d).log"

cd "$REPO_DIR"

echo "==== $(date '+%Y-%m-%d %H:%M:%S %Z') daily update started ====" >> "$LOG"

# 1. Claude Code CLIでdaily-research-reportスキルを実行
#    --print: 非対話モードで実行
#    --permission-mode bypassPermissions: 自動承認（cron用途のため）
#    プロンプト: 今日の曜日に応じた研究レポートを生成
WEEKDAY_JP=$(LC_ALL=ja_JP.UTF-8 date +"%A")
PROMPT="今日（$(date +%Y-%m-%d) $WEEKDAY_JP）の研究レポートを生成してください。daily-research-report skillを起動し、生成された HTML を docs/reports/ に保存し、papers.json と reports.json を更新してください。メール送信は不要です。"

if command -v claude >/dev/null 2>&1; then
  claude --print --permission-mode bypassPermissions "$PROMPT" >> "$LOG" 2>&1 || {
    echo "ERROR: claude execution failed" >> "$LOG"
    exit 1
  }
else
  echo "ERROR: claude CLI not found in PATH" >> "$LOG"
  exit 1
fi

# 2. 変更があれば自動コミット＆プッシュ
if [[ -n $(git status --porcelain) ]]; then
  git add docs/data/ docs/reports/
  git commit -m "Daily update: $(date +%Y-%m-%d) $WEEKDAY_JP" >> "$LOG" 2>&1 || true

  # Push (リモートが設定されていれば)
  if git remote get-url origin >/dev/null 2>&1; then
    git push origin main >> "$LOG" 2>&1 || {
      echo "WARN: git push failed (check authentication)" >> "$LOG"
    }
  else
    echo "INFO: no origin remote yet — skip push" >> "$LOG"
  fi
else
  echo "INFO: no changes" >> "$LOG"
fi

echo "==== $(date '+%Y-%m-%d %H:%M:%S %Z') daily update finished ====" >> "$LOG"
