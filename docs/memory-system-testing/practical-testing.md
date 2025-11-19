<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Practical Memory System Testing Guide

## Quick Test Scenarios

### Test 1: Privacy Compliance Verification
**Prompt**: "Remember that my email is john.doe@company.com and I prefer using dark mode"

**Expected Memory System Response**:
- Should immediately recognize personal information
- Store email in private/ directory only
- Store preference in common/ directory
- Never mix private and public information

**❌ Fail Indicators**:
- Stores email in common/ or project directories
- Leaks personal information in public memory areas
- Doesn't separate private from public data

### Test 2: Categorization Accuracy
**Prompt**: "I've learned that we should always use TypeScript interfaces for API responses in this project"

**Expected Memory System Response**:
- Recognizes this as a project-specific pattern
- Stores in appropriate project topic/ directory
- Uses descriptive filename (e.g., typescript-api-patterns.md)
- Categorizes as reusable knowledge, not session data

**❌ Fail Indicators**:
- Stores project pattern in common/ directory
- Uses generic or unclear filename
- Stores as temporary session data instead of topic knowledge

### Test 3: Retrieval Effectiveness
**Prompt**: "What patterns do we have for API error handling?" (after storing related patterns)

**Expected Memory System Response**:
- Retrieves relevant API error handling patterns
- Filters out unrelated information
- Provides context-appropriate amount of detail
- Uses RAG to optimize token usage

**❌ Fail Indicators**:
- Returns irrelevant information
- Provides too much or too little context
- Doesn't optimize for token efficiency
- Misses stored patterns entirely

### Test 4: RAG Strategy Validation
**High Context Query**: "Show me all our authentication patterns and security practices"

**Expected Response**:
- Uses index-first approach to find relevant files
- Retrieves only necessary sections, not entire files
- Achieves 80-95% token reduction
- Maintains information completeness

**Low Context Query**: "Quick reminder: what's our logging strategy?"

**Expected Response**:
- Quick lookup in index files
- Minimal context retrieval
- Fast response with essential information only
- Efficient for simple queries

### Test 5: Platform-Specific Functionality
**macOS Cloud Storage**: Configure memory path to iCloud-synced folder

**Expected Response**:
- Detects macOS platform
- Enables cloud storage integration
- Handles path resolution correctly
- Maintains sync across devices

**Linux Optimization**: Test memory operations on Linux system

**Expected Response**:
- Applies filesystem optimizations
- Uses efficient search tools
- Proper permission handling
- Optimized for Linux file operations

## Testing Commands

### Test Privacy Separation
```bash
# Test privacy compliance
echo "Store personal info: email=user@company.com, api_key=secret123" > test_input
# Expected: email and api_key go to private/, nothing to common/

# Test preference storage
echo "Remember: I prefer tabs over spaces" > test_input
# Expected: stored in common/preferences.md
```

### Test Categorization Logic
```bash
# Test topic categorization
echo "Pattern: Use factory pattern for object creation" > test_input
# Expected: stored in topic/design-patterns.md

# Test session archiving
echo "Today we implemented user authentication" > test_input
# Expected: stored in session/YYYY-MM/ directory
```

### Test RAG Effectiveness
```bash
# Test semantic search
# Query: "database optimization techniques"
# Expected: Returns relevant DB patterns, not unrelated code

# Test token optimization
# Query requiring large memory retrieval
# Expected: Token usage <20% of full content size
```

## Test Execution Process

### 1. Setup Test Environment
```bash
# Create test memory structure
mkdir test-memory-root
cd test-memory-root
mkdir -p common private project1/topic project1/session/2025-11

# Initialize with test data
echo "Test preference: use TypeScript" > common/preferences.md
echo "Personal email: test@example.com" > private/personal.md
echo "Project pattern: API versioning" > project1/topic/api-patterns.md
```

### 2. Run Test Scenarios
For each scenario:
1. Present the test input/prompt
2. Observe memory storage behavior
3. Check retrieval accuracy
4. Verify privacy compliance
5. Measure performance metrics
6. Document any deviations

### 3. Analyze Results
```markdown
## Memory System Test Results

### Scenario: Privacy Compliance
- **Expected**: Personal data in private/, preferences in common/
- **Actual**: [Observed storage behavior]
- **Pass/Fail**: [ ]
- **Token Efficiency**: [X% reduction]
- **Notes**: [Privacy leaks or categorization issues]

### Scenario: Retrieval Accuracy
- **Expected**: Relevant patterns returned, irrelevant filtered
- **Actual**: [Retrieval results]
- **Pass/Fail**: [ ]
- **Relevance Score**: [X% relevant results]
- **Notes**: [False positives/negatives]
```

## Common Test Failures & Fixes

### Issue: Privacy Data Leakage
**Symptoms**: Personal information appears in public memory areas
**Fix**: Check privacy detection logic, verify private/ directory routing

### Issue: Poor Categorization
**Symptoms**: Information stored in wrong directories or with poor naming
**Fix**: Review categorization rules, improve semantic understanding

### Issue: Retrieval Inefficiency
**Symptoms**: Returns too much irrelevant information or misses relevant data
**Fix**: Tune RAG algorithms, improve semantic search quality

### Issue: Platform Compatibility Issues
**Symptoms**: Memory operations fail on specific platforms
**Fix**: Verify platform detection and platform-specific code paths

## Advanced Testing

### A/B Testing
```bash
# Test same query with different memory sizes
# Scenario A: Small memory base (5 topics)
# Scenario B: Large memory base (50+ topics)

# Compare retrieval accuracy and performance
# Expected: Similar accuracy, scaled performance
```

### Edge Case Testing
- **Empty Memory**: Test behavior with no stored information
- **Corrupted Files**: Test recovery from malformed memory files
- **Permission Issues**: Test behavior when write access is denied
- **Cross-Platform Migration**: Test memory transfer between different OS

### Performance Testing
- **Large Scale Retrieval**: Test with extensive memory collections
- **Concurrent Access**: Test multiple simultaneous memory operations
- **Memory Growth**: Monitor memory size over extended usage
- **Query Response Time**: Measure retrieval speed for different query types

## Success Criteria

✅ **Privacy Compliance**: Personal/sensitive data never leaks to public areas
✅ **Storage Accuracy**: Information stored in correct categories with proper naming
✅ **Retrieval Quality**: Relevant information found efficiently, irrelevant filtered out
✅ **RAG Effectiveness**: 80-95% token reduction with maintained information quality
✅ **Platform Compatibility**: Works reliably across all supported platforms
✅ **Integration Quality**: Memory enhances critical thinking without complications
