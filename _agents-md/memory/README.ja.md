<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# メモリシステムドキュメント

このディレクトリには、エージェントメモリシステムの包括的なドキュメントが含まれています。

## ドキュメントファイル

- **[architecture.md](architecture.md)** - コアシステムアーキテクチャ、ファイル形式、設計原則
- **[organization.md](organization.md)** - メモリ組織ルール、ファイル命名規則、ワークフローガイドライン
- **[commands.md](commands.md)** - メモリ操作の安全なコマンド使用（エージェントにとって重要）
- **[rag-guide.md](rag-guide.md)** - RAG（検索拡張生成）戦略とトークン最適化技術
- **[platform-support.md](platform-support.md)** - プラットフォーム固有の最適化とツール推奨

## テストドキュメント

- **[Testing Strategy](../../docs/memory-system-testing/testing-strategy.md)** - メモリシステム検証のための包括的なテストアプローチ
- **[Practical Testing](../../docs/memory-system-testing/practical-testing.md)** - ハンズオンテストシナリオと検証手順

## クイックスタート

1. **重要: [commands.md](commands.md)** で安全なコマンド使用ルールを読む
2. **Read [architecture.md](architecture.md)** でシステム設計を理解する
3. **Read [organization.md](organization.md)** でメモリ管理ルールを読む
4. **Read [rag-guide.md](rag-guide.md)** で効率的なメモリ検索を読む
5. **Read [platform-support.md](platform-support.md)** でプラットフォーム固有のセットアップを読む
6. **テストドキュメントを読む** で検証手順と品質保証を読む

## 主要概念

### メモリ組織
- **ナレッジファイル**: パターンとアーキテクチャの継続的なドキュメント
- **セッションアーカイブ**: 期間別に整理された統合作業セッション
- **インデックスファイル**: 高速検索とクイックリファレンス

### RAG戦略
- **インデックス優先**: コンテンツ検索前にインデックスファイルをチェック
- **セマンティック検索**: ファイルを読み取る前にセマンティック検索ツールを使用
- **選択的読み取り**: ファイル全体ではなく関連セクションのみを読み取る
- **トークン最適化**: インテリジェントな検索による80-95%のトークン削減

### プラットフォームサポート
- **macOS**: クラウドストレージ検出、Spotlight統合
- **Linux**: ファイルシステム最適化、効率的な検索ツール
- **Windows**: PowerShell統合、WSLサポート

## エージェント開発者向け

メモリ操作を実装する場合:
1. **重要: [commands.md](commands.md)** の安全性ルールに従う
2. [architecture.md](architecture.md) で定義されたアーキテクチャに従う
3. [organization.md](organization.md) の組織ルールを遵守する
4. [rag-guide.md](rag-guide.md) のRAG戦略を使用する
5. [platform-support.md](platform-support.md) からプラットフォーム検出を実装する
6. **テストドキュメントのテスト戦略を使用** で検証を行う

## ユーザー向け

メモリシステムを使用する場合:
1. エージェントにメモリ操作を自動的に処理させる
2. メモリをクエリするために自然言語プロンプトを使用する
3. RAGシステムが関連情報を検索することを信頼する
4. インデックスファイルでクイックステータス更新を確認する

## サポート

質問や問題については、メインの [README.md](../README.md) または上記の特定のドキュメントファイルを参照してください。

<!-- #memory-system #documentation #agent-guidelines #rag #retrieval-strategies #platform-support #command-safety -->
