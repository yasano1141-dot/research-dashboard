# セットアップ手順（10分・電源OFF対応版）

クラウド完全運用：
- **Vercel** がサイトをホスト（GitHub連携で自動デプロイ）
- **GitHub Actions** が毎朝8:00 JSTにcron実行 → 論文検索＋HTML生成 → push
- Macが電源OFFでも動きます

---

## ステップ1: GitHubリポジトリを作る（1分）

1. https://github.com/new を開く
2. **Repository name**: `research-dashboard`
3. **Public** を選択（プライバシーが必要なら別途相談）
4. オプションは **すべてOFF**（READMEなど。ローカルにすでにあります）
5. 「Create repository」

---

## ステップ2: ローカルをGitHubにpush（30秒）

```bash
cd ~/github/research-dashboard
git remote add origin https://github.com/yasano1141-dot/research-dashboard.git
git push -u origin main
```

初回はGitHubの認証画面（ブラウザ）が開きます。**Personal Access Token (PAT)** が必要：

- https://github.com/settings/tokens/new
- Note: `research-dashboard`、Expiration: `90 days`、Scope: `repo` をチェック
- Generate → トークンをコピー
- `git push` 時にユーザー名 `yasano1141-dot`、パスワードに **トークンを貼る**
- 1回認証すれば macOS Keychain に保存されて以降は自動

---

## ステップ3: Vercelで公開（2分）

1. https://vercel.com/new を開く（GitHubアカウントでログイン）
2. **Import Git Repository** で `research-dashboard` を選んで Import
3. Configure Project：
   - Framework Preset: **Other**
   - Root Directory: `./`（変更不要）
   - Build Command, Output Directory: 空欄でOK（`vercel.json` で `outputDirectory: "docs"` を指定済み）
4. **Deploy** クリック

数十秒で完了。サイトURL：

> **`https://research-dashboard-yasano1141-dot.vercel.app/`**
> （または `https://research-dashboard.vercel.app/` のような自動URL）

正確なURLはVercelのダッシュボードで確認できます。

### カスタムドメイン（任意）
Vercel Project → Settings → Domains で独自ドメイン追加可能。

---

## ステップ4: GitHub Secretsを登録（1分）

毎朝8:00自動更新でClaude APIを使うため、APIキーをGitHub Secretsに登録します。

1. https://github.com/yasano1141-dot/research-dashboard/settings/secrets/actions
2. **New repository secret** をクリック
3. 必須: **`ANTHROPIC_API_KEY`** = `sk-ant-...`（Anthropic Console から取得）
4. 任意: **`NCBI_API_KEY`** = NCBI のAPIキー（PubMed検索を高速化、無料）
5. 任意: **`USE_OPUS`** = `1`（Sonnet 4.6→Opus 4.7 に切替、コスト3〜5倍だが品質向上）

### Anthropic API キーの取得
https://console.anthropic.com/settings/keys → Create Key → コピー

### NCBI API キー（任意・推奨）
https://www.ncbi.nlm.nih.gov/account/settings/ → API Keys → Create
登録すると 3 req/sec → 10 req/sec に。無料・登録30秒。

---

## ステップ5: 自動更新の動作確認（30秒）

GitHub Actionsを手動でテスト実行できます。

1. https://github.com/yasano1141-dot/research-dashboard/actions
2. 左サイドバーの **Daily Research Report** を選択
3. **Run workflow** をクリック → デフォルト（auto）のまま **Run workflow**
4. 数分待つ → 緑のチェックマークで成功

成功すると：
- `docs/reports/` に新しいHTMLレポートが追加され
- `docs/data/papers.json` と `reports.json` が更新され
- 自動コミット → Vercelが自動デプロイ → サイトに反映

### 8:00 JSTの自動実行を確認

ワークフローには `cron: '0 23 * * *'`（23:00 UTC = 8:00 JST 翌日）が設定済み。
何もしなくても毎日この時刻に自動実行されます。

---

## トラブルシューティング

### 「git push」で認証エラー
PAT方式（上記ステップ2参照）か SSH方式：

```bash
ssh-keygen -t ed25519 -C "yujiro.asano.rs@gmail.com"
cat ~/.ssh/id_ed25519.pub
# https://github.com/settings/ssh/new に登録
git remote set-url origin git@github.com:yasano1141-dot/research-dashboard.git
```

### Vercelデプロイが失敗する
- vercel.json のJSON構文を確認: `python3 -c "import json; json.load(open('vercel.json'))"`
- Vercelダッシュボードのビルドログで具体的なエラーを確認

### GitHub Actionsで生成器が失敗
- Settings → Secrets で `ANTHROPIC_API_KEY` が登録されているか確認
- Actionsログで具体的なエラーを確認
- ローカルで dry-run テスト：
  ```bash
  cd ~/github/research-dashboard
  pip install -r scripts/requirements.txt
  ANTHROPIC_API_KEY=sk-ant-... python scripts/daily_generator.py --weekday monday --dry-run
  ```

### Vercelのfree tierを超えそう
- Deploys: 100/day まで（1日1pushなので余裕）
- Bandwidth: 100GB/month まで（個人用なら余裕）
- Build minutes: 6,000/month（静的サイトはほぼゼロ）

### コストが気になる
Claude API使用量：
- Sonnet 4.6（デフォルト）：1日約 $0.50〜$1（11本のセクション生成）
- Opus 4.7（USE_OPUS=1）：1日約 $2〜$5
- 月額: Sonnet $15〜30、Opus $60〜150

---

## 旧 launchd（ローカル）方式について

`scripts/run_daily_update.sh` `install_launchd.sh` `com.yujiro.research-dashboard.plist` は**フォールバック用**として残しています。

- 通常運用：Vercel + GitHub Actions（電源OFF対応）
- ローカルバックアップ：Macの常時起動運用＋スキル経由のリッチ生成（MCP使用可能）

両方併用も可能ですが、push競合に注意。基本はGitHub Actions単独運用を推奨。
