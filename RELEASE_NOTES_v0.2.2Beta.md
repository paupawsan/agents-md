# Release Notes: v0.2.2Beta (Prerelease)

<details>
<summary><strong>🇺🇸 English</strong></summary>

## 🎉 What's New in v0.2.2Beta

This prerelease adds **Google Antigravity support**, refactors the setup script with comprehensive localization, and significantly improves the setup experience with better cross-platform compatibility.

### ✨ Major Features

#### 🚀 Google Antigravity Support
- **Dual Editor Support**: Automatic creation and synchronization of both `AGENTS.md` (for Cursor) and `GEMINI.md` (for Google Antigravity)
- **Seamless Integration**: Both files are kept in sync when switching languages or updating memory paths
- **Zero Manual Work**: No need to manually manage multiple configuration files
- **Editor Flexibility**: Use Cursor, Antigravity, or both - the system handles everything automatically

#### 🌐 Comprehensive CLI Localization
- **CLI Language Parameter**: Use `--lang en` or `--lang ja` for direct language selection
- **Beautiful Code Structure**: All user-facing strings centralized in a clean localization table
- **Easy Maintenance**: Adding new languages is as simple as extending the localization dictionary
- **Windows UTF-8 Support**: Proper Japanese character display on Windows console

#### 🔧 Improved Setup Script
- **Simplified Name**: `setup_memory_dir.py` → `setup.py` (more intuitive)
- **Integrated Workflow**: Language selection and memory configuration in one unified script
- **Flexible Flow**: Switch language only, or continue to configure memory path
- **Better UX**: Clear prompts, progress indicators, and helpful error messages
- **Cross-Platform**: Full support for Windows, macOS, and Linux

#### 🛡️ Enhanced Safety & Usability
- **Language Preservation**: Automatically preserves `MEMORY_PATH` when switching languages
- **Quit Option**: Exit after language switching without configuring memory (useful for language-only changes)
- **Error Handling**: Graceful fallbacks and helpful error messages
- **Path Validation**: Robust path handling with automatic normalization

### 🔧 Improvements

#### Setup Experience
- **Automated Setup**: New automated setup option for non-technical users
- **Interactive Prompts**: Clear, step-by-step guidance throughout the process
- **Progress Feedback**: Visual indicators showing what's happening at each step
- **Error Recovery**: Helpful suggestions when something goes wrong

#### Script Architecture
- **Clean Separation**: Business logic separated from localization strings
- **Maintainable Code**: Easy to understand and extend
- **Well Documented**: Comprehensive docstrings and comments
- **Type Safety**: Proper error handling and validation

#### Documentation
- **Updated Guides**: All setup guides updated with new script instructions
- **Bilingual Coverage**: Both English and Japanese documentation synchronized
- **Non-Technical Friendly**: Simple setup guide includes automated option
- **Cross-Platform Notes**: Windows-specific instructions included

### 📝 Files Changed

**13 files changed**: 1,080 insertions(+), 505 deletions(-)

#### New Files
- `setup.py` - Comprehensive setup script with localization and Antigravity support
- `GEMINI.md` - Configuration file for Google Antigravity (auto-created by setup script)
- `PR_DESCRIPTION.md` - Pull request description template

#### Updated Files
- `AGENTS.md`, `AGENTS.md.en`, `AGENTS.md.ja` - Updated references to `setup.py`
- `README.md`, `README.ja.md` - Added setup script instructions and Antigravity support
- `docs/simple-setup.md`, `docs/simple-setup.ja.md` - Added automated setup option
- `docs/setup-guide.md`, `docs/setup-guide.ja.md` - Updated with new features and `--lang` parameter

#### Removed Files
- `setup_memory_dir.py` - Renamed to `setup.py`
- `switch_agents_lang.py` - Functionality integrated into `setup.py`

### 🚨 Breaking Changes

None. This is a backward-compatible release.

### ⚠️ Important Notes

- **Template Repository**: This entire repository is a configuration template. Agents will NOT automatically create or copy any part of the agents-md structure.
- **Configuration Required**: You must configure `MEMORY_PATH` in `AGENTS.md` before using the Memory System.
- **Dual Editor Support**: Both `AGENTS.md` and `GEMINI.md` are created automatically - copy both to your project if using multiple editors.

### 📖 Migration Guide

If you're upgrading from v0.2.1Beta:

1. **Run New Setup Script**: Execute `python setup.py` (Windows) or `python3 setup.py` (macOS/Linux)
2. **Select Language**: Choose your preferred language (English/Japanese)
3. **Update Configuration**: The script will automatically create `GEMINI.md` and update both files
4. **Copy Files**: Copy both `AGENTS.md` and `GEMINI.md` to your project (or add agents-md folder to workspace)

**For existing users of `setup_memory_dir.py`**:
- The new `setup.py` script will detect and preserve your existing `MEMORY_PATH` configuration
- Simply run the new script to update your setup

**For users of `switch_agents_lang.py`**:
- Language switching is now integrated into `setup.py`
- Run `python3 setup.py` and select your language, or use `python3 setup.py --lang en` / `python3 setup.py --lang ja`

### 🎯 What's Next

- More editor integrations planned
- Additional language support
- Enhanced setup automation
- Community feedback integration

### 📚 Documentation

- **[README](README.md)** - Main project overview and quick start
- **[Setup Guide](docs/setup-guide.md)** - Complete technical setup instructions
- **[Simple Setup Guide](docs/simple-setup.md)** - Plain language guide for non-technical users
- **[Usage Guide](docs/usage-guide.md)** - How to use the memory system effectively

---

</details>

<details>
<summary><strong>🇯🇵 日本語</strong></summary>

## 🎉 v0.2.2Beta の新機能

このプレリリースでは、**Google Antigravityサポート**の追加、包括的なローカライゼーションによるセットアップスクリプトのリファクタリング、そしてより良いクロスプラットフォーム互換性によるセットアップ体験の大幅な改善を提供します。

### ✨ 主要機能

#### 🚀 Google Antigravityサポート
- **デュアルエディタサポート**: `AGENTS.md`（Cursor用）と`GEMINI.md`（Google Antigravity用）の両方の自動作成と同期
- **シームレスな統合**: 言語の切り替えやメモリパスの更新時に両方のファイルが同期されます
- **手動作業不要**: 複数の設定ファイルを手動で管理する必要がありません
- **エディタの柔軟性**: Cursor、Antigravity、または両方を使用できます - システムがすべて自動的に処理します

#### 🌐 包括的なCLIローカライゼーション
- **CLI言語パラメータ**: 直接言語選択に`--lang en`または`--lang ja`を使用
- **美しいコード構造**: すべてのユーザー向け文字列をクリーンなローカライゼーションテーブルに集約
- **簡単なメンテナンス**: 新しい言語の追加はローカライゼーション辞書を拡張するだけ
- **Windows UTF-8サポート**: Windowsコンソールでの適切な日本語文字表示

#### 🔧 改善されたセットアップスクリプト
- **簡略化された名前**: `setup_memory_dir.py` → `setup.py`（より直感的）
- **統合ワークフロー**: 言語選択とメモリ設定を1つの統一されたスクリプトに統合
- **柔軟なフロー**: 言語のみを切り替えるか、メモリパスの設定を続けるか選択可能
- **より良いUX**: 明確なプロンプト、進捗インジケーター、役立つエラーメッセージ
- **クロスプラットフォーム**: Windows、macOS、Linuxの完全なサポート

#### 🛡️ 強化された安全性と使いやすさ
- **言語の保持**: 言語を切り替える際に`MEMORY_PATH`を自動的に保持
- **終了オプション**: メモリを設定せずに言語切り替え後に終了（言語のみの変更に便利）
- **エラーハンドリング**: 優雅なフォールバックと役立つエラーメッセージ
- **パス検証**: 自動正規化による堅牢なパス処理

### 🔧 改善点

#### セットアップ体験
- **自動セットアップ**: 非技術者向けの新しい自動セットアップオプション
- **インタラクティブプロンプト**: プロセス全体を通じて明確なステップバイステップガイダンス
- **進捗フィードバック**: 各ステップで何が起こっているかを示す視覚的インジケーター
- **エラー回復**: 問題が発生した場合の役立つ提案

#### スクリプトアーキテクチャ
- **クリーンな分離**: ビジネスロジックとローカライゼーション文字列の分離
- **保守可能なコード**: 理解と拡張が容易
- **十分なドキュメント**: 包括的なdocstringとコメント
- **型安全性**: 適切なエラーハンドリングと検証

#### ドキュメント
- **更新されたガイド**: 新しいスクリプト手順ですべてのセットアップガイドを更新
- **バイリンガルカバレッジ**: 英語と日本語の両方のドキュメントを同期
- **非技術者向け**: シンプルセットアップガイドに自動オプションを含む
- **クロスプラットフォーム注記**: Windows固有の手順を含む

### 📝 変更されたファイル

**13ファイル変更**: 1,080行追加(+)、505行削除(-)

#### 新規ファイル
- `setup.py` - ローカライゼーションとAntigravityサポートを含む包括的なセットアップスクリプト
- `GEMINI.md` - Google Antigravity用の設定ファイル（セットアップスクリプトで自動作成）
- `PR_DESCRIPTION.md` - プルリクエスト説明テンプレート

#### 更新されたファイル
- `AGENTS.md`, `AGENTS.md.en`, `AGENTS.md.ja` - `setup.py`への参照を更新
- `README.md`, `README.ja.md` - セットアップスクリプト手順とAntigravityサポートを追加
- `docs/simple-setup.md`, `docs/simple-setup.ja.md` - 自動セットアップオプションを追加
- `docs/setup-guide.md`, `docs/setup-guide.ja.md` - 新機能と`--lang`パラメータで更新

#### 削除されたファイル
- `setup_memory_dir.py` - `setup.py`に名前変更
- `switch_agents_lang.py` - 機能を`setup.py`に統合

### 🚨 破壊的変更

なし。これは後方互換性のあるリリースです。

### ⚠️ 重要な注意事項

- **テンプレートリポジトリ**: このリポジトリ全体は設定テンプレートです。エージェントはagents-md構造の一部を自動的に作成またはコピーしません。
- **設定が必要**: メモリシステムを使用する前に、`AGENTS.md`で`MEMORY_PATH`を設定する必要があります。
- **デュアルエディタサポート**: `AGENTS.md`と`GEMINI.md`の両方が自動的に作成されます - 複数のエディタを使用する場合は、両方をプロジェクトにコピーしてください。

### 📖 移行ガイド

v0.2.1Betaからアップグレードする場合:

1. **新しいセットアップスクリプトを実行**: `python setup.py`（Windows）または`python3 setup.py`（macOS/Linux）を実行
2. **言語を選択**: 希望する言語（英語/日本語）を選択
3. **設定を更新**: スクリプトが自動的に`GEMINI.md`を作成し、両方のファイルを更新します
4. **ファイルをコピー**: `AGENTS.md`と`GEMINI.md`の両方をプロジェクトにコピー（またはagents-mdフォルダをワークスペースに追加）

**`setup_memory_dir.py`の既存ユーザー向け**:
- 新しい`setup.py`スクリプトが既存の`MEMORY_PATH`設定を検出して保持します
- 新しいスクリプトを実行するだけでセットアップを更新できます

**`switch_agents_lang.py`のユーザー向け**:
- 言語切り替えは`setup.py`に統合されました
- `python3 setup.py`を実行して言語を選択するか、`python3 setup.py --lang en` / `python3 setup.py --lang ja`を使用してください

### 🎯 今後の予定

- より多くのエディタ統合を計画
- 追加の言語サポート
- 強化されたセットアップ自動化
- コミュニティフィードバックの統合

### 📚 ドキュメント

- **[README](README.ja.md)** - メインプロジェクト概要とクイックスタート
- **[セットアップガイド](docs/setup-guide.ja.md)** - 完全な技術セットアップ手順
- **[シンプルセットアップガイド](docs/simple-setup.ja.md)** - 非技術者向けの平易なガイド
- **[使用ガイド](docs/usage-guide.ja.md)** - メモリシステムを効果的に使用する方法

---

</details>

