# セットアップ手順

毎日Macを開いて **📊 Daily Report** をダブルクリックするだけの運用。
**API課金なし**（Claude Codeサブスクリプション枠で動作）。

---

## ✅ 完了済み

- ✅ GitHubリポジトリ作成・初回push
  → https://github.com/yasano1141-dot/research-dashboard
- ✅ `gh` CLI 認証＆git credential helper 設定（以降のpushは認証不要）
- ✅ Desktopに **📊 Daily Report.command** エイリアス配置（ダブルクリックで起動）
- ✅ `.claude/skills/daily-research-report/` にスキル本体配置（プロジェクトスコープ）

---

## 🔵 残り作業：Vercel連携（3分）

[https://vercel.com/new](https://vercel.com/new) を開く

1. **Continue with GitHub** → `yasano1141-dot` でログイン → Authorize Vercel
2. **Import Git Repository** 一覧から `research-dashboard` を選んで **Import**
3. Configure Project：
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build / Output Directory: 空欄（`vercel.json`で指定済み）
4. **Deploy** クリック

数十秒で完了。Vercelダッシュボード上部に表示される **ライブURL** を控えておいてください
（`https://research-dashboard-xxxx.vercel.app/` のような形式）。

---

## 🟢 動作確認：毎日の運用テスト

1. Finder でデスクトップを開く
2. **📊 Daily Report.command** をダブルクリック
3. ターミナルが自動で開き、進捗が表示される：
   ```
   ╔══════════════════════════════════════════════════════════════╗
   ║      📊 Daily Research Report — 2026-05-07 木曜日
   ╚══════════════════════════════════════════════════════════════╝
   🔄 Step 1/5: GitHubから最新を取得
   🤖 Step 2/5: Claude Codeで論文検索＋レポート生成
      （5〜10分かかります...）
   ...
   ✅ 完了！
   ```
4. 完了するとmacOS通知＋ブラウザでサイト自動オープン
5. Vercel側の反映には1〜2分かかります（自動デプロイ中）

---

## トラブルシューティング

### ダブルクリックしてもターミナルが開かない
- Finderで右クリック → **このアプリケーションで開く** → **ターミナル.app** を選択
- もしくは：システム設定 → セキュリティとプライバシー → 「.command ファイルの実行を許可」

### Claude CLIが見つからないエラー
- `claude --version` をターミナルで叩いて確認
- なければ [https://docs.claude.com/claude-code](https://docs.claude.com/claude-code) からインストール

### Vercelデプロイが失敗する
- vercel.json の構文確認: `python3 -c "import json; json.load(open('vercel.json'))"`
- Vercelダッシュボードのビルドログで具体的なエラーを確認

### git push で認証エラー
gh CLIで再認証：
```bash
~/.local/bin/gh auth refresh
```

---

## オプション設定

### NCBI APIキー（PubMed検索を3req/sec→10req/secに加速）

[https://www.ncbi.nlm.nih.gov/account/settings/](https://www.ncbi.nlm.nih.gov/account/settings/) → API Keys → Create

取得した値を `~/.zshrc` に追加：
```bash
export NCBI_API_KEY="your_key_here"
```

スキルが自動で利用します。

### カスタムドメイン

Vercel Project → Settings → Domains で独自ドメイン追加可能。

---

## 🟡 万一のフォールバック：API版に切替（電源OFFが続く時）

長期出張・電源OFF期間中だけ自動化したい場合：

1. https://console.anthropic.com/settings/keys でAPIキー取得
2. https://github.com/yasano1141-dot/research-dashboard/settings/secrets/actions/new で `ANTHROPIC_API_KEY` 登録
3. `.github/workflows/daily-update.yml` の `# - cron: '0 23 * * *'` のコメントを外して push

戻す時は cron をコメントアウトしてsecretを削除すればOK。

---

## 🔧 メンテナンス

### 検索式・優先ジャーナルを変更したい
`scripts/themes.json` を編集 → 次回 daily.command 実行時から反映。

### スキルの絶対遵守ルールを更新したい
`.claude/skills/daily-research-report/SKILL.md` を編集 → 次回実行から反映。

### Macを買い替えた時
```bash
git clone https://github.com/yasano1141-dot/research-dashboard.git ~/github/research-dashboard
cd ~/github/research-dashboard
~/.local/bin/gh auth login   # gh CLIインストール後
chmod +x daily.command
ln -s "$HOME/github/research-dashboard/daily.command" "$HOME/Desktop/📊 Daily Report.command"
```

---

## 📊 ライブサイト

**`https://research-dashboard.vercel.app/`**（Vercelデプロイ後に確定）

GitHub: https://github.com/yasano1141-dot/research-dashboard
