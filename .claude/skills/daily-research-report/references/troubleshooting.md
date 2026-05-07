# トラブルシューティング

## Gmail 関連

### Q: 下書き作成 API が "scope error" で失敗する
A: Gmail MCP の OAuth スコープに `gmail.compose` または `gmail.modify` が必要。Claude Code の `~/.claude/mcp.json` で MCP サーバ設定を確認。

### Q: 送信ボタンを押しても下書きが残る
A: ブラウザのコンポーズウィンドウが最小化されている可能性。スクリーンショットで確認し、最小化アイコン（画面右下）をクリックして展開してから「送信」ボタンを押す。

### Q: file:// リンクが本文から消える
A: Gmail は `file://` プロトコルをセキュリティ上の理由で削除する。`<code>` + `user-select:all` でパスをコピー可能な「テキスト」として表示する。

## DOCX 生成

### Q: `docx` パッケージが見つからない
```
Error: Cannot find module 'docx'
```
A:
```bash
mkdir -p /tmp/npm-work && cd /tmp/npm-work
npm init -y > /dev/null 2>&1
npm install docx
```
そして node スクリプトでは `require('/tmp/npm-work/node_modules/docx')` で参照する。

### Q: 日本語が文字化けする
A: `Document` の `styles.default.document.run.font` を `Yu Gothic`（macOS）または `Yu Mincho`（明朝体が欲しい場合）に設定。Windowsの場合は `Yu Gothic` のまま動く。

### Q: ハイパーリンクが青くならない
A: `ExternalHyperlink` の `children` に `TextRun` を入れる際、`style: "Hyperlink"` を指定。色は `color: "2B6CB0"` を併用。

### Q: ページサイズがおかしい
A: `properties: { page: { size: { orientation: PageOrientation.PORTRAIT } } }` を `sections` に追加。デフォルトはA4縦。

## HTML / お気に入り機能

### Q: チェックボックスが表示されない
A: 以下を確認：
1. `<body data-source-date="..." data-source-theme="...">` が設定されているか
2. 各論文カードに `data-paper-id="..."` 属性があるか
3. `</body>` 直前にお気に入り機能JSが入っているか
4. ブラウザのコンソールでJSエラーが出ていないか
5. CSSで `.paper { position: relative }` になっているか（チェックボックスは absolute 配置）

### Q: お気に入りビューアでカードが見えない
A: localStorage は `file://` プロトコルでファイルごとに分離される（Chrome）。レポートHTMLの「📤 お気に入りビューアを開く」ボタンを使うと URL hash 経由でデータが転送される。Firefox なら自動で共有される。

### Q: ビューアパスが見つからない
A: お気に入りビューアは `~/Desktop/3勉強/claudeのファイル/お気に入りビューア.html` にある必要がある。レポートHTMLからの相対パスは `../お気に入りビューア.html`。

## ブラウザ・MCP

### Q: Chrome MCP のタブが見つからない
A: `tabs_context_mcp({ createIfEmpty: true })` で MCP タブグループを作成してから他の操作をする。

### Q: file:// URLに `https://` が前置される
A: `mcp__Claude_in_Chrome__navigate` の URL バリデーションが file:// を拒否する場合がある。代わりに：
1. 既存のブラウザで Finder からファイルを開く
2. または `mcp__Claude_in_Chrome__javascript_tool` で `window.location.href = "file://..."` を実行

### Q: WebSearch が古い結果を返す
A: クエリに「2026」や具体的な月を含める。例：`physical activity meta-analysis 2026 January Lancet`。WebSearch は学術データベース API ではないので、PubMed検索や Google Scholar のような厳密性は期待できない。

## 日付・タイムゾーン

### Q: 曜日が想定と違う
A: 日本時間（JST）で取得する：
```python
from datetime import datetime, timezone, timedelta
jst = timezone(timedelta(hours=9))
today = datetime.now(jst)
```
スケジュールタスクが UTC で動いている場合、夜中に実行すると前日扱いになることがある。

### Q: 既存ファイルを上書きしてしまった
A: バックアップが必要なら、生成前に既存ファイルを `_backup_HHMMSS` 付きでリネーム：
```bash
if [ -f "target.html" ]; then
  cp target.html "target_backup_$(date +%H%M%S).html"
fi
```

## ファイル系

### Q: 日本語フォルダ名でエラー
A: ファイルパスを必ずダブルクォートで囲む。bash 内で `unicode normalization` の問題が起きることがあるので、`LANG=ja_JP.UTF-8` を設定：
```bash
export LANG=ja_JP.UTF-8
export LC_ALL=ja_JP.UTF-8
```

### Q: パーミッションエラー
A: ワークスペースフォルダ全体の owner と permissions を確認：
```bash
ls -la ~/Desktop/3勉強/claudeのファイル/
chmod -R u+rw ~/Desktop/3勉強/claudeのファイル/
```

## ユーザー側で確認すべきこと

### MCP サーバが接続されているか
- Gmail MCP（`@modelcontextprotocol/server-gmail` または相当）
- Chrome MCP（`@modelcontextprotocol/server-chrome` または `claude-in-chrome` 拡張）
- WebSearch（Anthropic 標準）

### 必要な権限
- macOS のフルディスクアクセス（Finder/Terminal）
- Chrome の拡張機能インストール
- Gmail OAuth の同意（compose スコープ）

### ライセンス・注意
- 論文 URL は元論文へのリンクなので著作権問題なし
- 抽出する内容は要約・解説のみで、原文の長文引用は避ける
- メール送信先は本人のみ（y.asano1141@gmail.com）
