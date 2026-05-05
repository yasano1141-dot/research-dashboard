# セットアップ手順（5分）

ローカルの全ファイルは準備済み。以下のコマンドをコピペで実行するだけ。

---

## ステップ1: GitHubリポジトリを作る（ブラウザで1分）

1. https://github.com/new を開く
2. **Repository name**: `research-dashboard`
3. **Public** を選択（GitHub Pages無料運用のため。プライバシーが必要なら別途相談）
4. **Add a README** などのオプションは **すべてOFF**（ローカルにすでにあるため）
5. 「Create repository」をクリック

---

## ステップ2: ターミナルでpush（30秒）

GitHub上に表示される `<your-username>` を埋めて、以下を実行：

```bash
cd ~/github/research-dashboard
git remote add origin https://github.com/<your-username>/research-dashboard.git
git push -u origin main
```

初回はGitHubの認証画面（ブラウザ）が開きます。認証情報はmacOSキーチェーンに保存されるので以降は自動。

---

## ステップ3: GitHub Pages を有効化（ブラウザで1分）

1. リポジトリページの **Settings** タブを開く
2. 左サイドバー **Pages** をクリック
3. **Source**: 「Deploy from a branch」
4. **Branch**: `main` / `/docs` を選択 → **Save**
5. 数分待つ

サイトURL：

> **`https://<your-username>.github.io/research-dashboard/`**

---

## ステップ4: 毎朝8:00自動更新を有効化（10秒）

```bash
bash ~/github/research-dashboard/scripts/install_launchd.sh
```

これで毎朝8:00に自動で：
- 今日の曜日テーマで最新論文10本を検索
- HTMLレポート生成
- データJSON更新
- GitHubに自動push
- GitHub Pagesが自動デプロイ → サイトに反映

---

## 動作確認

```bash
# launchdジョブが登録されているか
launchctl list | grep com.yujiro.research-dashboard

# 手動で1回テスト実行（夜中とかにやらず、忙しくないタイミングで）
launchctl start com.yujiro.research-dashboard

# ログを見る
tail -f ~/github/research-dashboard/scripts/logs/$(date +%Y%m%d).log
```

---

## トラブルシューティング

### 「git push」で認証エラー

GitHubは2021年8月からパスワード認証廃止。Personal Access Token (PAT) または SSH鍵が必要：

**PAT方式（簡単）**:
1. https://github.com/settings/tokens/new
2. Note: `research-dashboard`、Expiration: 90 days、Scope: `repo` をチェック
3. Generate → トークンをコピー
4. `git push` 時にユーザー名は GitHub ID、パスワードに **トークン** を貼り付け
5. 1回認証すれば macOS Keychain に保存される

**SSH方式（推奨・長期）**:
```bash
# 鍵生成
ssh-keygen -t ed25519 -C "yujiro.asano.rs@gmail.com"
# 公開鍵を https://github.com/settings/ssh/new に登録
cat ~/.ssh/id_ed25519.pub
# リモートをSSHに変更
git remote set-url origin git@github.com:<your-username>/research-dashboard.git
```

### launchdが8:00に動かない

- Macが完全電源OFFだと skip される（スリープなら起動後にcatch upする）
- 確認: `launchctl print gui/$(id -u)/com.yujiro.research-dashboard | head -50`
- 代替: Anthropicの`scheduled-tasks` MCPを使うクラウド方式もあります（要相談）

### サイトが404になる

GitHub Pages反映まで5〜10分かかることがあります。`Settings → Pages` で「Your site is live at...」と表示されるまで待機。
