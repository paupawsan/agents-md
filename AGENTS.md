<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Memory System Guidelines

**Configure**: Replace `{MEMORY_PATH}` with the full path to your memory root folder.

**Example**: If you want memory at `~/Documents/my-memory`, replace `{MEMORY_PATH}` with `/Users/username/Documents/my-memory` (or use `~/Documents/my-memory` if your system supports tilde expansion).

Use `setup_memory_dir.py` script or manual replacement to configure.

## Memory Sync (MANDATORY)

**CRITICAL**: Agent MUST sync memory to external files after significant tasks.

**Paths** (`{MEMORY_PATH}` = full path to memory root folder):
- Root: `{MEMORY_PATH}` (this is your memory root folder)
- Project: `{MEMORY_PATH}/[project-name]/`
- Common: `{MEMORY_PATH}/common/` (preferences, patterns)
- Private: `{MEMORY_PATH}/private/` ⚠️ (credentials, personal info)

**Platform Detection**:
- The agent uses the configured `{MEMORY_PATH}` directly (no platform detection needed)
- Users configure `{MEMORY_PATH}` via setup script or manual replacement
- See `_agents-md/memory/platform.md` for common path examples

**When to Sync**: After significant tasks, when discovering patterns, at conversation end.

**Recovery**: If context lost, check `{MEMORY_PATH}/common/preferences.md`, then `{MEMORY_PATH}/[project-name]/context.md`, then use semantic search.

## Privacy Check (MANDATORY FIRST)

**Before storing ANY information**:
- ⚠️ Personal/private info? → `{MEMORY_PATH}/private/` ONLY
- ⚠️ Names, emails, company, credentials? → `{MEMORY_PATH}/private/` ONLY
- ✅ If NO → Continue to categorization

**NEVER** store private info in `topic/` or `session/` files.

## Storage Decisions

**DO Store**: Architectural decisions, reusable patterns, user preferences, project knowledge, lessons learned, recurring solutions.

**DON'T Store**: Temporary info, obvious facts, redundant info, overly granular details, conversation transcripts, unverified info.

**Evaluation**: Privacy check → Value → Verification → Relevance → Consolidation → Organization.

## License Headers in Memory Files

**CRITICAL**: Memory files are user data, NOT licensed source code.

- ⚠️ **NEVER add license headers to memory files** (topic/, session/, context/)
- Memory files are user-generated content and auto-generated memory
- License headers are ONLY for source code files in the project repository
- When creating or updating memory files, do NOT include copyright/license notices

## RAG Strategy

**Multi-level retrieval**:
1. Index lookup (`memories.json`) - ~100-500 tokens
2. Semantic search (`codebase_search`) - ~200-1000 tokens
3. Header scan (`grep`) - ~50-200 tokens
4. Selective read (`read_file` with offset/limit) - ~200-2000 tokens

**ALWAYS**: Check index → Semantic search → Scan headers → Read selectively.

**NEVER**: Read large files (>500 lines) without scanning, load all files simultaneously, skip index files.

## References

- `_agents-md/memory/commands.md` - Safe command usage rules (CRITICAL)
- `_agents-md/memory/organization.md` - Organization rules
- `_agents-md/memory/rag.md` - RAG strategies
- `_agents-md/memory/platform.md` - Platform paths
