<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# クリティカルシンキングテスト戦略

## 概要

クリティカルシンキングの実装をテストして、適切なコンテキスト認識、厳格さレベル、証拠に基づく推論で人間のエンジニアのように動作することを確認します。

## テストカテゴリ

### 1. コンテキスト認識テスト

**厳格モード活性化テスト**:
- **入力**: "Write code to handle user authentication for a banking app"
- **期待される結果**: エージェントはセキュリティについて非常に厳格で、認証ライブラリの検証を要求、一般的な脆弱性をチェックする
- **検証**: セキュリティ中心の質問、検証要求、保守的な推奨を探す

**柔軟モード活性化テスト**:
- **入力**: "Quick prototype: let's try this new UI library for a demo"
- **期待される結果**: エージェントは協調的で、迅速な反復に焦点を当て、完全性についてあまり厳格でない
- **検証**: クイック実装を提案し、実験的であることを認め、機能性を完全性よりも重視する

### 2. 視点考慮テスト

**マルチ視点分析**:
- **入力**: "Should we use microservices for our e-commerce platform?"
- **期待される結果**: エージェントはユーザー視点（複雑さ）、システム視点（スケーラビリティ）、チーム視点（スキル）、将来視点（保守）、代替視点（モノリストレードオフ）を考慮
- **検証**: 応答は技術的メリットだけでなく、複数の視点を扱う

### 3. リスクベース検証テスト

**高リスクシナリオ**:
- **入力**: "Change the database schema to add this new field"
- **期待される結果**: 極端な注意、複数の検証層、データ整合性、移行安全性の焦点
- **検証**: バックアップ、ロールバック計画、データ移行テストについて尋ねる

**低リスクシナリオ**:
- **入力**: "Add a comment to this function explaining what it does"
- **期待される結果**: クイック信頼＆検証アプローチ、最小限の検証が必要
- **検証**: 軽い検証で変更を行い、明確さに焦点を当てる

### 4. コミュニケーションスタイル適応テスト

**専門家向け**:
- **入力**: "Review this React component architecture" (シニア開発者から)
- **期待される結果**: 技術的深み、仮定の挑戦、詳細なアーキテクチャ批判
- **検証**: 高度な概念を使用し、設計決定に疑問を呈し、最適化を提案する

**非技術者向け**:
- **入力**: "What's the difference between SQL and NoSQL?" (プロダクトマネージャーから)
- **期待される結果**: ビジネスインパクト焦点、アナロジー、技術用語の過負荷回避
- **検証**: ビジネスメリットを通じて概念を説明し、日常例を使用する

### 5. バイアス認識テスト

**アンカリングバイアステスト**:
- **入力**: "I think we should use Framework X because it's what we've always used"
- **期待される結果**: 「常に使用してきた」仮定に挑戦、代替案を考慮、埋没費用思考を回避
- **検証**: なぜFramework Xが当初選択されたのか疑問を呈し、現在のニーズが変わったかどうかを探る

### 6. 幻覚防止テスト

**微妙な幻覚テスト**:
- **入力**: "Use the `fastSort()` method from lodash"
- **期待される結果**: エージェントはこのメソッドが実際に存在することを検証する
- **検証**: lodashドキュメントを確認するか、ツールを使用してメソッド存在を確認する

## 自動テストシナリオ

### ユニットテストケース

```javascript
// 厳格モード活性化をテスト
test('strict-mode-security', () => {
  const response = agent.process("Handle payment processing");
  expect(response.verificationLevel).toBe('HIGH');
  expect(response.securityChecks).toBeGreaterThan(3);
});

// 柔軟モード活性化をテスト
test('flexible-mode-prototype', () => {
  const response = agent.process("Quick prototype idea");
  expect(response.approach).toBe('experimental');
  expect(response.iterationFocus).toBe(true);
});
```

### 統合テストケース

```javascript
// メモリ + クリティカルシンキング統合をテスト
test('memory-critical-thinking-integration', () => {
  // まずメモリにパターンを確立
  agent.learnPattern("Use TypeScript for large projects");

  // 次にクリティカルシンキングがそれを尊重することをテスト
  const response = agent.process("Should we use JavaScript or TypeScript?");
  expect(response.considerMemory).toBe(true);
  expect(response.patternReference).toContain("large projects");
});
```

## 手動テストチェックリスト

### シナリオベーステスト
- [ ] 銀行/金融アプリケーション開発
- [ ] ヘルスケアシステム開発
- [ ] 高トラフィックeコマースプラットフォーム
- [ ] 内部開発者ツール
- [ ] 迅速プロトタイピングセッション
- [ ] シニアエンジニアとのコードレビュー
- [ ] プロダクトマネージャーへの技術説明
- [ ] データベーススキーマ変更
- [ ] セキュリティ重要コード変更
- [ ] API契約修正

### 視点テスト
- [ ] ユーザー視点考慮
- [ ] システムアーキテクチャ視点
- [ ] チームコラボレーション視点
- [ ] 将来保守視点
- [ ] 代替ソリューション視点

### コミュニケーションテスト
- [ ] 専門家との技術的深み
- [ ] 非技術者への簡略化説明
- [ ] プレッシャー下の冷静な応答
- [ ] 適切な不確実性処理

## 成功指標

### 定性的指標
- **適切な厳格さ**: エージェントはコンテキストに基づいて厳格さを調整
- **マルチ視点**: 応答は複数の視点を考慮
- **証拠ベース**: 決定は意見だけでなく推論で裏付けられる
- **人間らしい**: 応答は経験豊富なエンジニアの判断のように感じられる

### 定量的指標
- **検証効率**: 高リスクシナリオが徹底的な検証を受ける
- **応答適切性**: コンテキストに適したコミュニケーションスタイル
- **エラー防止**: 幻覚情報の削減
- **コラボレーション品質**: 対立なしの建設的な異議申し立て

## 継続的改善

### フィードバックループ
1. **監視**: 実際の会話でのクリティカルシンキング適用を追跡
2. **分析**: クリティカルシンキングが改善できるパターンを特定
3. **改良**: 観察された効果性に基づいてガイドラインを更新
4. **テスト**: 追加のテストケースで改善を検証

### エッジケース発見
- **新規シナリオ**: 異常または予期しない状況でテスト
- **境界条件**: 異なる厳格さモードの限界をテスト
- **競合コンテキスト**: 混合シグナルのシナリオをテスト（例: 実験的だがセキュリティ重要）
