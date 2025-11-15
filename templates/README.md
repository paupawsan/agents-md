# agents-md Templates

Templates for different workflow styles that integrate with the agents-md Memory System.

## Available Templates

### Simple Workflow (ChatGPT-Inspired, Integrated)

**Best for**: Quick daily logging, vibecoding, immediate LLM analysis - while still syncing to memory system

- `AGENTS.md.simple` - Simple project memory template (syncs to `{MEMORY_PATH}/[project-name]/`)
- `GLOBAL.md` - Cross-project memory template (syncs to `{MEMORY_PATH}/common/`)

**Key Feature**: These templates provide quick logging but **still integrate with agents-md memory system**. The agent will automatically sync important patterns and decisions to the structured memory system.

**When to use**:
- You want to write quickly without structure overhead
- You prefer single-file per project for daily logging
- You want easy LLM analysis workflows
- You're working on smaller projects or experiments
- **But you still want memory system benefits** (RAG retrieval, cross-project patterns)

## Step-by-Step Setup Instructions

### Using AGENTS.md.simple (Required)

1. **Copy the template**:
   ```bash
   cp templates/AGENTS.md.simple ./AGENTS.md
   ```

2. **Configure memory path**:
   - Open `AGENTS.md` in your project root
   - Replace `{MEMORY_PATH}` with your actual memory root path
   - Example: `/Users/username/Documents/my-memory` or `~/Documents/my-memory`
   - Replace `[project-name]` with your actual project name

3. **Start logging**: Use the template sections to log your daily work

4. **Agent behavior**: Agents will automatically sync important content from `AGENTS.md` to:
   - `{MEMORY_PATH}/[project-name]/topic/` (patterns & learnings)
   - `{MEMORY_PATH}/[project-name]/context.md` (decisions)
   - `{MEMORY_PATH}/[project-name]/session/YYYY-MM/` (session logs)

### Using GLOBAL.md (Optional)

**Important**: `GLOBAL.md` is OPTIONAL. Agents don't check it automatically unless you tell them to.

**Option A: Use GLOBAL.md and tell agents about it**

1. **Copy the template**:
   ```bash
   cp templates/GLOBAL.md {MEMORY_PATH}/common/global.md
   ```

2. **Tell agents to check it**: Add this to your project's `AGENTS.md`:
   ```markdown
   ## Global Memory Reference
   
   For cross-project patterns and personal notes, also check:
   `{MEMORY_PATH}/common/global.md`
   ```

3. **Agent behavior**: When you mention "check global memory" or reference it in `AGENTS.md`, agents will:
   - Read `GLOBAL.md` when needed
   - Sync important content to `{MEMORY_PATH}/common/preferences.md` and `common/patterns.md`

**Option B: Don't use GLOBAL.md (simpler)**

- Skip `GLOBAL.md` entirely
- Agents will use standard memory files: `common/preferences.md` and `common/patterns.md`
- These are checked automatically by agents (no need to mention them)

### Complete Example Setup

```bash
# 1. Setup project AGENTS.md
cp templates/AGENTS.md.simple ./AGENTS.md
# Edit AGENTS.md: replace {MEMORY_PATH} and [project-name]

# 2. (Optional) Setup GLOBAL.md
cp templates/GLOBAL.md /path/to/your/memory/common/global.md
# Edit your AGENTS.md to mention GLOBAL.md if you want agents to check it

# 3. Start working - agents will sync automatically
```

### How Agents Use These Files

**AGENTS.md.simple**:
- ✅ Agents read this automatically (it's in project root)
- ✅ Agents sync content to memory system automatically
- ✅ No additional setup needed

**GLOBAL.md**:
- ❌ Agents DON'T check this automatically
- ✅ Agents WILL check it if:
  - You mention it in `AGENTS.md`: "Check `{MEMORY_PATH}/common/global.md`"
  - You ask in conversation: "Check my global memory file"
- ✅ Agents sync content from `GLOBAL.md` → `common/preferences.md` + `common/patterns.md`
- ✅ Standard memory files (`common/preferences.md`, `common/patterns.md`) are checked automatically

### Structured Workflow (Full Memory System)

**Best for**: Complex projects, long-term maintenance, RAG-optimized retrieval

- Use the full Memory System as documented in the main README
- Includes `topic/`, `session/`, `context.md`, indexing

**When to use**:
- Large, complex projects
- Need RAG-optimized agent retrieval
- Want structured knowledge organization
- Multiple team members or long-term maintenance

## Choosing Your Workflow

**Simple Workflow** if you:
- ✅ Want to start logging immediately
- ✅ Prefer minimal structure for daily logging
- ✅ Work on quick projects or experiments
- ✅ Want easy LLM analysis
- ✅ **But still want memory system integration** (patterns sync automatically)

**Structured Workflow** if you:
- ✅ Have complex, long-term projects
- ✅ Need efficient agent retrieval (RAG) from the start
- ✅ Want organized knowledge files immediately
- ✅ Need to scale across many projects
- ✅ Prefer structured organization over quick logging

## How They Work Together

**Both workflows use the same memory system** - they just differ in how you log:

- **Simple**: Log in single file (`AGENTS.md`) → Agent syncs to memory system automatically
- **Structured**: Log directly to memory system structure (`topic/`, `session/`, etc.)

**The memory system** (`{MEMORY_PATH}/[project-name]/`) is the same in both cases - Simple workflow just provides an easier entry point that syncs automatically.

## Understanding the File Relationships

### AGENTS.md.simple
- **Location**: Project root (`./AGENTS.md`)
- **Agent access**: ✅ Automatically read (it's the project's AGENTS.md)
- **Purpose**: Daily project logging
- **Syncs to**: `{MEMORY_PATH}/[project-name]/topic/`, `context.md`, `session/`

### GLOBAL.md
- **Location**: `{MEMORY_PATH}/common/global.md` (or anywhere you want)
- **Agent access**: ❌ NOT automatically checked
- **Purpose**: Human-friendly cross-project logging
- **How agents use it**:
  - Only if mentioned in `AGENTS.md` or conversation
  - Content syncs to: `common/preferences.md` + `common/patterns.md`
- **Standard alternative**: Agents automatically check `common/preferences.md` and `common/patterns.md` (no GLOBAL.md needed)

### The Flow

```
AGENTS.md.simple (project root)
  ↓ (agents read automatically)
  ↓ (agents sync automatically)
{MEMORY_PATH}/[project-name]/topic/
{MEMORY_PATH}/[project-name]/context.md
{MEMORY_PATH}/[project-name]/session/

GLOBAL.md (optional, only if you mention it)
  ↓ (agents read only if mentioned)
  ↓ (agents sync when reading)
common/preferences.md ← (agents check automatically)
common/patterns.md ← (agents check automatically)
```

## Tips

1. **Tags are your friend**: Use consistent tags (#unity, #trading, etc.) for easy searching
2. **Timestamps matter**: Always include dates and times for session logs
3. **Decisions are gold**: Document why you chose something, not just what
4. **Regular analysis**: Use the prompts in `GLOBAL.md` weekly/monthly for insights

