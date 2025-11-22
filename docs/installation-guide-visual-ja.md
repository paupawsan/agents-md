<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# agents-md インストールガイド（ビジュアル版）

**シンプル。高速。効果的。** 5つの簡単なステップでagents-mdを始めましょう。

---

## ステップ1: ダウンロード 📥

どちらの方法でもリポジトリをダウンロードできます：

![ステップ1: agents-mdをダウンロード](images/installation-step-1-download.png)

**どちらかを選択：**
- GitHubからZIPをダウンロード
- または使用：`git clone https://github.com/...`

---

## ステップ2: セットアップスクリプトを実行 ⚙️

セットアップスクリプトを実行して設定を構成します：

![ステップ2: セットアップスクリプトを実行](images/installation-step-2-setup.png)

**コマンド：**
- macOS/Linux: `python3 setup.py`
- Windows: `python setup.py`

**設定：**
- 言語を選択（英語/日本語）
- メモリパスを設定

---

## ステップ3: ワークスペースに追加 📁

メモリフォルダをCursor/VS Codeワークスペースに追加します：

![ステップ3: メモリフォルダをワークスペースに追加](images/installation-step-3-workspace.png)

**簡単な方法：** ワークスペースのサイドバーにメモリフォルダをドラッグ&ドロップします。

**💡 ベストプラクティス（ワークスペースシステムが対応している場合）：** より良い組織化のために、外部の`agentic-system`フォルダ構造を使用します。これにより、メモリをプロジェクトコードから分離し、1つのフォルダですべてのプロジェクトに対応できます。詳細については、以下の[推奨フォルダ構造](#-推奨フォルダ構造)セクションを参照してください。

---

## ステップ4: 設定ファイルをコピー 📋

設定ファイルをプロジェクトにコピーします：

![ステップ4: 設定ファイルをコピー](images/installation-step-4-copy-files.png)

**両方のファイルをコピー：**
- `AGENTS.md`（Cursor用）
- `GEMINI.md`（Google Antigravity用）

---

## ステップ5: メモリを初期化 🚀

AIアシスタントでメモリを初期化します：

![ステップ5: メモリを初期化](images/installation-step-5-initialize.png)

**AIチャットに入力：**
```
initialize memory for this project
```

**完了！** AIエージェントがプロジェクトのパターン、設定、決定を記憶するようになります。

---

## ベストプラクティス

### ❌ 避けるべき: 混在構造

![以前: 混在構造](images/best-practice-before-mixed.png)

**問題：** コードとメモリファイルが混在すると、プロジェクトが乱雑になり管理が困難になります。

---

### ✅ 推奨: クリーンな分離

![以後: クリーンな分離](images/best-practice-after-separation.png)

**解決策：** 外部の`agentic-system`フォルダを使用して、メモリをコードから分離します。

**利点：**
- 🔄 **再利用可能** - 1つのフォルダがすべてのプロジェクトに対応
- 📤 **共有可能** - 任意のワークスペースに簡単に追加
- ✨ **クリーン** - コードはメモリから分離

---

### 📋 メモリ組織構造

![メモリ組織構造](images/best-practice-memory-organization.png)

各プロジェクトのメモリは次のように整理されます：
- **context/** - クイックリファレンス（概要、ステータス、アーキテクチャ、ファイル）
- **topic/** - 知識ファイル（パターン、決定、研究）
- **session/** - 作業セッションアーカイブ
- **memories.json** - 機械可読インデックス

---

### 📂 推奨フォルダ構造

![推奨フォルダ構造](images/best-practice-folder-structure.png)

```
あなたのワークスペース:
├── CurrentProject/          ← あなたのプロジェクトコード
│   ├── app.py
│   ├── README.md
│   └── ...
│
└── agentic-system/          ← 外部、共有
    ├── agent-memory/
    │   ├── common/          ← 共有パターン
    │   ├── [CurrentProject]/ ← このプロジェクトのメモリ
    │   └── [OtherProjects]/ ← 他のプロジェクトのメモリ
    │
    └── agents-md/           ← 設定テンプレート
        ├── AGENTS.md
        └── ...
```

**1つの`agentic-system`フォルダがすべてのプロジェクトに対応します！**

---

## 主な機能

### 🧠 高度なRAGサポート

![高度なRAGサポート](images/feature-rag-support.png)

インテリジェントなセマンティック検索により**80-95%のトークン削減**を実現。

---

### 💻 マルチプラットフォームサポート

![マルチプラットフォームサポート](images/feature-multi-platform.png)

**macOS、Linux、Windows**で動作します。

---

### 🔒 プライバシー重視とローカル

![プライバシー重視とローカル](images/feature-privacy.png)

- ✅ 完全な透明性
- ✅ 完全な制御
- ✅ 簡単なバックアップ
- ✅ 外部サービス不要

---

## 以上です！

準備完了です！AIエージェントがプロジェクトのパターンを自動的に記憶し、学習するようになります。

**ヘルプが必要ですか？** [完全なドキュメント](../README.ja.md)を確認してください。

