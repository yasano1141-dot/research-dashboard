#!/bin/bash
# =============================================================
#  launchdに毎朝8:00 JSTのジョブを登録するインストーラ
# =============================================================

set -euo pipefail

REPO_DIR="$HOME/github/research-dashboard"
LAUNCHD_DIR="$HOME/Library/LaunchAgents"
LABEL="com.yujiro.research-dashboard"
PLIST_SRC="$REPO_DIR/scripts/$LABEL.plist"
PLIST_DST="$LAUNCHD_DIR/$LABEL.plist"

mkdir -p "$LAUNCHD_DIR"

# シェルスクリプトに実行権限
chmod +x "$REPO_DIR/scripts/run_daily_update.sh"

# 既存のジョブをアンロード（あれば）
if launchctl list | grep -q "$LABEL"; then
  launchctl unload "$PLIST_DST" 2>/dev/null || true
fi

# プリストをコピーしてロード
cp "$PLIST_SRC" "$PLIST_DST"
launchctl load "$PLIST_DST"

echo "✅ launchd job installed: $LABEL"
echo "   Plist: $PLIST_DST"
echo "   毎朝 8:00 JST に \$REPO_DIR/scripts/run_daily_update.sh が実行されます"
echo
echo "確認: launchctl list | grep $LABEL"
echo "テスト実行: launchctl start $LABEL"
echo "アンインストール: launchctl unload \"$PLIST_DST\" && rm \"$PLIST_DST\""
