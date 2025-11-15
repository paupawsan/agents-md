<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Memory Organization Rules

**CRITICAL**: Agents MUST follow these rules when managing memory.

## Privacy Check (MANDATORY FIRST)

**Before storing ANY information**:
- ⚠️ Personal/private info? → `{MEMORY_DIR}/private/` ONLY
- ⚠️ Names, emails, company, credentials? → `{MEMORY_DIR}/private/` ONLY
- ✅ If NO → Continue to categorization

**NEVER** store private info in `topic/` or `session/` files.

## Categorization

**Project** (`{MEMORY_DIR}/[project-name]/`):
- Architecture decisions, project patterns, bug fixes
- Project-specific preferences → `topic/preferences.md`

**Common** (`{MEMORY_DIR}/common/`):
- User preferences (all projects) → `preferences.md`
- Cross-project patterns → `patterns.md`

**Private** (`{MEMORY_DIR}/private/`) ⚠️:
- Credentials → `credentials.md`
- Personal info → `personal_info.md`

## File Rules

**Consolidate**: One file per feature/fix, not multiple iterations.

**Naming**:
- `topic/topic_name.md` - Knowledge files
- `session/YYYY-MM/YYYY-MM-DD_feature.md` - Sessions
- Use underscores, descriptive names

**Index Sync**: Always update `memories.json` when creating/updating files.

**Tags/Keywords**: Add semantic tags for RAG search.

**License Headers**: 
- ⚠️ **NEVER add license headers to memory files** (topic/, session/, context/)
- Memory files are user data, not licensed source code
- License headers are ONLY for source code files in the project repository
- Auto-generated memory content is user data and should not be licensed

## Recovery Process

1. Check `{MEMORY_DIR}/common/preferences.md` for user preferences
2. Check `{MEMORY_DIR}/[project-name]/context.md` for project status
3. Check `{MEMORY_DIR}/[project-name]/topic/` for patterns
4. Use semantic search for specific topics

## Security Protocol ⚠️

**When accessing `{MEMORY_DIR}/private/`**:
- ✅ Only when explicitly needed
- ✅ Mask sensitive data (e.g., "API key: ***hidden***")
- ❌ Never expose private info in responses

<!-- #memory-organization #file-structure #security #privacy #agent-guidelines #rag-strategy -->
