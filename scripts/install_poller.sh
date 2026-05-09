#!/bin/bash
# =============================================================
#  📱 Mobile Trigger Poller のlaunchdインストーラ
#  Macが10分おきにGitHub Issuesをチェックし、新しいリクエストを処理
# =============================================================

set -euo pipefail

REPO_DIR="$HOME/github/research-dashboard"
LAUNCHD_DIR="$HOME/Library/LaunchAgents"
LABEL="com.yujiro.research-dashboard.poller"
PLIST_SRC="$REPO_DIR/scripts/$LABEL.plist"
PLIST_DST="$LAUNCHD_DIR/$LABEL.plist"

mkdir -p "$LAUNCHD_DIR"

# シェルスクリプトに実行権限
chmod +x "$REPO_DIR/scripts/check_and_run_trigger.sh"

# 既存のジョブをアンロード（あれば）
if launchctl list 2>/dev/null | grep -q "$LABEL"; then
  echo "🔄 既存のpollerをアンロード中..."
  launchctl unload "$PLIST_DST" 2>/dev/null || true
fi

# プリストをコピーしてロード
cp "$PLIST_SRC" "$PLIST_DST"
launchctl load "$PLIST_DST"

echo ""
echo "✅ Mobile Trigger Poller installed."
echo ""
echo "📍 Plist: $PLIST_DST"
echo "📍 10分おきに実行 → GitHub Issues（label \"trigger\"）をチェック"
echo "📍 ログ: ~/github/research-dashboard/scripts/logs/poller_*.log"
echo ""
echo "📱 スマホからの使い方："
echo "   1. GitHub アプリ（無料）を iOS/Android にインストール"
echo "   2. リポジトリ yasano1141-dot/research-dashboard を開く"
echo "   3. Issues → New Issue → 「📊 今日のレポートを生成」を選択"
echo "   4. テーマを選んでSubmit"
echo "   → 10分以内にMacが処理開始 → Vercelに反映"
echo ""
echo "🔧 管理コマンド："
echo "   launchctl list | grep $LABEL          # 状態確認"
echo "   launchctl start $LABEL                # 即時実行（テスト用）"
echo "   launchctl unload \"$PLIST_DST\"         # 停止"
echo "   tail -f /tmp/research-dashboard-poller.err.log  # エラーログ監視"
