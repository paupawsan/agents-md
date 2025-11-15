<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# RAG Strategy

Token-optimized memory retrieval.

## Multi-Level Strategy

1. **Index Lookup** (~100-500 tokens)
   - Check `memories.json` for tags/keywords
   - Fastest, lowest cost

2. **Semantic Search** (~200-1000 tokens)
   - Use `codebase_search` on memory directory
   - Natural language queries

3. **Header Scan** (~50-200 tokens)
   - Use `grep` for headers (`^#+\s`)
   - Identify relevant sections

4. **Selective Read** (~200-2000 tokens)
   - Use `read_file` with `offset`/`limit`
   - Read only identified sections

## Token Optimization

**ALWAYS**:
- Check index before searching
- Use semantic search before reading
- Scan headers before content
- Read selectively with offset/limit

**NEVER**:
- Read entire large files (>500 lines) without scanning
- Load all memory files simultaneously
- Skip index files

## Decision Tree

```
Query?
├─ Quick status? → Read context.md (~200 tokens)
├─ Find topic? → Check memories.json → Read file selectively
├─ Search files? → codebase_search → Filter → Read top matches
└─ Specific section? → grep headers → Read section only
```

## Savings

- Index-first: 80-95% reduction vs full search
- Selective reading: 70-90% reduction vs full file
- Header navigation: 50-70% reduction vs full file

<!-- #rag #retrieval-augmented-generation #semantic-search #token-optimization #memory-retrieval #search-strategy -->

