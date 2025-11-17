# agents-md テンプレート

agents-md Memory System と統合するさまざまなワークフロースタイルのテンプレート。

## 利用可能なテンプレート

### シンプルワークフロー (ChatGPTインスパイア、統合済み)

**最適**: クイックデイリーロギング、ビベコーディング、即時LLM分析 - メモリシステムへの同期を維持しながら

- `AGENTS.md.simple` - シンプルプロジェクトメモリテンプレート (`{MEMORY_PATH}/[project-name]/` に同期)
- `GLOBAL.md` - プロジェクト横断メモリテンプレート (`{MEMORY_PATH}/common/` に同期)

**主要機能**: これらのテンプレートはクイックロギングを提供しますが、**agents-mdメモリシステムと統合**します。エージェントは重要なパターンと決定を構造化されたメモリシステムに自動的に同期します。

**使用する場合**:
- 構造オーバーヘッドなしで素早く書き込みたい
- デイリーロギング用にプロジェクトごとに単一ファイルを希望
- 簡単なLLM分析ワークフローを希望
- 小規模プロジェクトや実験で作業
- **メモリシステムの利点を維持したい**（RAG検索、プロジェクト横断パターン）

## ステップバイステップセットアップ手順

### AGENTS.md.simple の使用 (必須)

1. **テンプレートをコピー**:
   ```bash
   cp templates/AGENTS.md.simple ./AGENTS.md
   ```

2. **メモリパスを設定**:
   - プロジェクトルートで `AGENTS.md` を開く
   - `{MEMORY_PATH}` を実際のメモリルートパスに置き換える
   - 例: `/Users/username/Documents/my-memory` または `~/Documents/my-memory`
   - `[project-name]` を実際のプロジェクト名に置き換える

3. **ロギングを開始**: テンプレートセクションを使用してデイリーワークをログ

4. **エージェントの動作**: エージェントは自動的に `AGENTS.md` の重要なコンテンツを同期:
   - `{MEMORY_PATH}/[project-name]/topic/` (パターン＆学習)
   - `{MEMORY_PATH}/[project-name]/context.md` (決定)
   - `{MEMORY_PATH}/[project-name]/session/YYYY-MM/` (セッションログ)

### GLOBAL.md の使用 (オプション)

**重要**: `GLOBAL.md` はオプションです。あなたが言及しない限り、エージェントは自動的にチェックしません。

**方法A: GLOBAL.md を使用し、エージェントに伝える**

1. **テンプレートをコピー**:
   ```bash
   cp templates/GLOBAL.md {MEMORY_PATH}/common/global.md
   ```

2. **エージェントにチェックするよう伝える**: プロジェクトの `AGENTS.md` に以下を追加:
   ```markdown
   ## グローバルメモリ参照

   プロジェクト横断パターンと個人ノートについては、以下もチェック:
   `{MEMORY_PATH}/common/global.md`
   ```

3. **エージェントの動作**: "グローバルメモリを確認" と述べたり、`AGENTS.md` で参照したりすると、エージェントは:
   - 必要に応じて `GLOBAL.md` を読み取る
   - 重要なコンテンツを `{MEMORY_PATH}/common/preferences.md` と `common/patterns.md` に同期

**方法B: GLOBAL.md を使用しない (シンプル)**

- `GLOBAL.md` を完全にスキップ
- エージェントは標準メモリファイルを使用: `common/preferences.md` と `common/patterns.md`
- これらはエージェントによって自動的にチェックされる（言及する必要なし）

### 完全なセットアップ例

```bash
# 1. プロジェクトAGENTS.mdのセットアップ
cp templates/AGENTS.md.simple ./AGENTS.md
# AGENTS.mdを編集: {MEMORY_PATH} と [project-name] を置き換え

# 2. (オプション) GLOBAL.mdのセットアップ
cp templates/GLOBAL.md /path/to/your/memory/common/global.md
# エージェントにチェックさせたい場合はAGENTS.mdでGLOBAL.mdを言及

# 3. 作業を開始 - エージェントは自動的に同期
```

### エージェントがこれらのファイルを使用する方法

**AGENTS.md.simple**:
- ✅ エージェントはこのファイルを自動的に読み取る（プロジェクトルートにあるため）
- ✅ エージェントはコンテンツをメモリシステムに自動的に同期
- ✅ 追加セットアップ不要

**GLOBAL.md**:
- ❌ エージェントはこのファイルを自動的にチェックしない
- ✅ エージェントは以下の場合にチェックする:
  - `AGENTS.md` で言及した場合: "Check `{MEMORY_PATH}/common/global.md`"
  - 会話で尋ねた場合: "Check my global memory file"
- ✅ エージェントは `GLOBAL.md` のコンテンツを `common/preferences.md` + `common/patterns.md` に同期
- ✅ 標準メモリファイル (`common/preferences.md`, `common/patterns.md`) は自動的にチェックされる

### 構造化ワークフロー (フルメモリシステム)

**最適**: 複雑なプロジェクト、長期保守、RAG最適化検索

- メインREADMEで文書化されているフルMemory Systemを使用
- `topic/`、`session/`、`context.md`、インデックス作成を含む

**使用する場合**:
- 大規模で複雑なプロジェクト
- 最初からRAG最適化されたエージェント検索が必要
- 構造化された知識組織を希望
- 複数チームメンバーまたは長期保守

## ワークフローの選択

**シンプルワークフロー**を選択する場合:
- ✅ すぐにロギングを開始したい
- ✅ デイリーロギング用に最小限の構造を希望
- ✅ クイックプロジェクトや実験で作業
- ✅ 簡単なLLM分析を希望
- ✅ **メモリシステム統合を維持したい**（パターンは自動的に同期）

**構造化ワークフロー**を選択する場合:
- ✅ 複雑で長期的なプロジェクトがある
- ✅ 最初から効率的なエージェント検索（RAG）が必要
- ✅ すぐに整理された知識ファイルを希望
- ✅ 多数のプロジェクトにスケーリングする必要がある
- ✅ クイックロギングよりも構造化された組織を優先

## 連携方法

**両方のワークフローは同じメモリシステムを使用** - ログの方法が異なるだけ:

- **シンプル**: 単一ファイル（`AGENTS.md`）にログ → エージェントがメモリシステムに自動的に同期
- **構造化**: メモリシステム構造（`topic/`、`session/` など）に直接ログ

**メモリシステム**（`{MEMORY_PATH}/[project-name]/`）は両方の場合で同じ - シンプルワークフローは自動同期される簡単なエントリーポイントを提供するだけ。

## ファイル関係の理解

### AGENTS.md.simple
- **場所**: プロジェクトルート (`./AGENTS.md`)
- **エージェントアクセス**: ✅ 自動的に読み取り（プロジェクトのAGENTS.mdであるため）
- **目的**: デイリープロジェクトロギング
- **同期先**: `{MEMORY_PATH}/[project-name]/topic/`、`context.md`、`session/`

### GLOBAL.md
- **場所**: `{MEMORY_PATH}/common/global.md`（または希望の場所）
- **エージェントアクセス**: ❌ 自動的にチェックされない
- **目的**: 人間フレンドリーなプロジェクト横断ロギング
- **エージェントの使用方法**:
  - `AGENTS.md` で言及された場合のみ
  - コンテンツは `common/preferences.md` + `common/patterns.md` に同期
- **標準代替**: エージェントは自動的に `common/preferences.md` と `common/patterns.md` をチェック（GLOBAL.md不要）

### フロー

```
AGENTS.md.simple (プロジェクトルート)
  ↓ (エージェントが自動的に読み取り)
  ↓ (エージェントが自動的に同期)
{MEMORY_PATH}/[project-name]/topic/
{MEMORY_PATH}/[project-name]/context.md
{MEMORY_PATH}/[project-name]/session/

GLOBAL.md (オプション、言及した場合のみ)
  ↓ (言及された場合のみエージェントが読み取り)
  ↓ (読み取り時にエージェントが同期)
common/preferences.md ← (エージェントが自動的にチェック)
common/patterns.md ← (エージェントが自動的にチェック)
```

## ヒント

1. **タグはあなたの友人**: 簡単な検索のために一貫したタグを使用（#unity、#trading など）
2. **タイムスタンプが重要**: セッションログには常に日付と時間を記載
3. **決定は黄金**: 何を選択したかだけでなく、なぜ選択したかを文書化
4. **定期分析**: 洞察を得るために `GLOBAL.md` のプロンプトを毎週/毎月使用

<!-- #templates #memory-structure #organization #best-practices #agent-prompts -->
