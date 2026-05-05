# Daily Research Report Skill (Claude Code 版)

老年医学・疫学・身体機能研究の最新論文を曜日テーマ別に検索し、通常レポート（10本均等解説）と詳細分析レポート（Top 3の7セクション分析）を作成、Gmailで送信するスキル。

## ✨ 主な機能

- 7曜日それぞれ異なるテーマで論文10本を選定（うち1〜2本は2026年の最新論文）
- HTML（カード型レイアウト・カラーラベル付き）+ DOCX 両形式で出力
- お気に入りチェックボックス機能 + 累積ビューア連携
- Gmail で 3 通のメールを自動下書き・送信
  - 通常レポート / 詳細分析 / ローカルファイルパス案内
- ユーザーの研究プロフィール（健康寿命・身体機能・筋質・身体活動・認知機能・遺伝子・方法論）と紐付けて研究示唆を提示

## 📁 ディレクトリ構造

```
daily-research-report/
├── SKILL.md                      ← Claude Code が読むメインファイル
├── README.md                     ← この手順書
├── references/                   ← 参照ドキュメント（必要時にRead）
│   ├── themes-by-day.md         ← 曜日別テーマ・キーワード
│   ├── priority-journals.md     ← 優先ジャーナル・検索戦略
│   ├── researcher-profile.md    ← Yujiの研究プロフィール
│   ├── output-spec-regular.md   ← 通常レポート仕様
│   ├── output-spec-detail.md    ← 詳細分析仕様
│   ├── file-naming.md           ← ファイル命名規則
│   ├── email-spec.md            ← メール送信仕様
│   └── troubleshooting.md       ← よくある問題と対処
├── templates/                    ← HTML/メールテンプレート
│   ├── regular-report.html      ← 通常レポートHTML骨格
│   ├── detail-report.html       ← 詳細分析HTML骨格
│   ├── email-regular.html       ← 通常メールHTML
│   ├── email-detail.html        ← 詳細分析メールHTML
│   └── email-paths.html         ← パス案内メールHTML
├── scripts/                      ← 再利用可能スクリプト
│   ├── inject-favorites.py      ← お気に入り機能注入
│   ├── generate-docx.js         ← 通常版DOCX生成（Node.js）
│   ├── generate-detail-docx.js  ← 詳細版DOCX生成
│   ├── get-today-context.py     ← 今日の曜日・テーマ情報取得
│   └── package.json             ← Node依存関係（docx）
├── assets/                       ← 静的ファイル
│   └── favorites-viewer.html    ← お気に入り累積ビューア
└── examples/                     ← 過去レポート例
    ├── README.md
    ├── example_monday_regular.html
    ├── example_monday_detail.html
    ├── example_tuesday_regular.html
    └── example_tuesday_detail.html
```

## 🚀 Claude Code への移植手順

### 1. スキルフォルダを Claude Code のスキルディレクトリにコピー

```bash
# パーソナル（全プロジェクトで使う）
mkdir -p ~/.claude/skills
cp -r ~/Desktop/3勉強/claudeのファイル/claude-code-skills/daily-research-report ~/.claude/skills/
```

または、特定プロジェクトで使う場合：

```bash
cd <project-root>
mkdir -p .claude/skills
cp -r ~/Desktop/3勉強/claudeのファイル/claude-code-skills/daily-research-report .claude/skills/
```

### 2. 必要な MCP サーバを設定

Claude Code の `~/.claude.json` または `.mcp.json` に以下を追加：

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
    },
    "chrome": {
      "command": "...",
      "args": ["..."]
    }
  }
}
```

または Claude Desktop の Connector を使う場合は、対応する MCP サーバを有効化する。

### 3. 必要なパッケージインストール

DOCX 生成用：
```bash
mkdir -p /tmp/npm-work && cd /tmp/npm-work
npm init -y > /dev/null 2>&1
npm install docx
```

Python は標準ライブラリのみで動くため不要。

### 4. お気に入りビューアを workspace ルートに配置

```bash
cp ~/.claude/skills/daily-research-report/assets/favorites-viewer.html \
   ~/Desktop/3勉強/claudeのファイル/お気に入りビューア.html
```

（既に存在していれば不要）

### 5. 動作確認

Claude Code を起動して、以下のコマンドを実行：

```
/skill daily-research-report
```

または自然言語で：

```
今日の研究レポートを作って
```

## 🔧 スケジュール実行（毎朝7:00 JST）

### macOS (launchd) で設定する場合

`~/Library/LaunchAgents/com.user.daily-research-report.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.daily-research-report</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/claude</string>
        <string>--skill</string>
        <string>daily-research-report</string>
        <string>--non-interactive</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>7</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>/tmp/daily-research-report.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/daily-research-report.error.log</string>
</dict>
</plist>
```

ロード：
```bash
launchctl load ~/Library/LaunchAgents/com.user.daily-research-report.plist
```

### crontab で設定する場合

```bash
crontab -e
```

```
0 7 * * * /usr/local/bin/claude --skill daily-research-report --non-interactive >> /tmp/daily-research-report.log 2>&1
```

## 📝 仕様変更履歴

### v3.0 (2026/04/28)
- 「オリジナリティ」「新発見項目」を独立セクションとして追加
- HTML カラーラベル `.section.originality`（紫系）と `.section.discovery`（緑系）
- DOCX にも独立ブロックで反映

### v2.0 (2026/04/27)
- お気に入りチェックボックス機能追加
- localStorage `researchFavorites_v2` で永続化
- お気に入り累積ビューアの実装

### v1.0
- 初版（通常版＋詳細分析版の2種類のレポート）

## 🐛 トラブルシューティング

`references/troubleshooting.md` を参照。よくある問題：
- Gmail 下書きが作れない
- DOCX 生成でフォントエラー
- お気に入りチェックボックスが表示されない
- ブラウザで `file://` が開かない

## 📜 ライセンス・注意事項

- ユーザー（浅野優次郎）の個人用スキル
- 論文の要約・解説のみで、原文の長文引用はしない
- メール送信先は本人のみ（y.asano1141@gmail.com）

## ✉️ 連絡

問題があれば、Claude Code 内で `/feedback` するか、このスキルを編集する。
