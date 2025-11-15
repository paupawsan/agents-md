<!--
Global Agent Memory Template
For cross-project memory, personal patterns, and life/career notes

OPTIONAL: This is a human-friendly file for quick logging. 
Agents will sync important content to the structured memory system.

Place this in: {MEMORY_PATH}/common/global.md (optional location)
Or keep it anywhere convenient - agents will check it if referenced in AGENTS.md

See _agents-md/memory/organization.md for memory sync rules.
-->

# Global Agent Memory

**Status**: OPTIONAL - This is a human-friendly logging file.  
**Memory System**: Important content syncs to `{MEMORY_PATH}/common/preferences.md` and `{MEMORY_PATH}/common/patterns.md`  
**Note**: Replace `{MEMORY_PATH}` with your configured memory root path.

**For Agents**: This file is OPTIONAL. Check it only if:
1. Explicitly mentioned in project `AGENTS.md`
2. User asks for cross-project analysis
3. During recovery when `common/preferences.md` doesn't exist

Otherwise, use the standard memory system files: `common/preferences.md` and `common/patterns.md`

## Personal Coding Patterns

- I tend to:
  - Start fast, then get stuck on edge cases
  - Forget why I made a decision 3+ days ago
  - [Add your own patterns]

## Global Decisions

- YYYY-MM-DD: Decided to unify all side projects under agents-md memory
- YYYY-MM-DD: Prefer Japanese for comments in <project>, English for system prompts
- [Add your own decisions]

## Cross-Project Patterns

- Pattern: When working with X technology, always do Y
- Pattern: I consistently struggle with Z, so I should...

## Ideas Backlog

- [ ] Try multi-agent setup for market analysis
- [ ] Add JP version of agents-md prompt
- [Add your own ideas]

## Career & Life Notes

- YYYY-MM-DD: Started learning X
- YYYY-MM-DD: Completed Y project
- [Add your own notes]

## Analysis Prompts

Use these prompts with LLMs to analyze your work:

**Daily Analysis:**
"Here is today's part of AGENTS.md. Summarize, list key decisions, and suggest next actions."

**Weekly Analysis:**
"Here are the last 7 days from multiple AGENTS.md files. Summarize what I've been doing across projects, and tell me:
(1) recurring problems
(2) skills I'm actually improving
(3) things I keep postponing."

**Deep Analysis:**
"Based on these logs, what is my typical coding pattern? What slows me down? Where am I surprisingly fast?"

---

## Memory Sync Instructions

**For Agents**: Sync important global patterns to the memory system:

1. **Personal Coding Patterns** → Update `{MEMORY_PATH}/common/preferences.md`
2. **Cross-Project Patterns** → Update `{MEMORY_PATH}/common/patterns.md`
3. **Global Decisions** → Can stay here or sync to `{MEMORY_PATH}/common/` as needed
4. **Update Index**: Update `{MEMORY_PATH}/memories.json` when syncing

**Privacy Check**: Personal/career info that's sensitive → use `{MEMORY_PATH}/private/` instead.

See `_agents-md/memory/organization.md` for detailed sync rules.

<!-- #global-memory #cross-project #patterns #preferences #agent-prompts #sync-rules -->

