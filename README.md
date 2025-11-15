<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# agents-md

A collection of systems and tools for AI coding agents, built from real-world work experience. Currently includes a robust Memory System, with more systems planned for the future.

## Overview

**agents-md** is a growing collection of practical systems and tools designed to enhance AI coding agents' capabilities. Each system is developed based on real-world work experience and production use cases.

**Current Status**: The Memory System is the first system available. Additional systems will be added over time as they are developed and refined through practical application.

## 🚀 Quick Start

**New to this? Not a programmer?** → Start with **[SIMPLE_SETUP.md](SIMPLE_SETUP.md)** - A step-by-step guide written in plain language, perfect for non-technical users.

**Experienced developer?** → Jump to [Memory System Setup](#memory-system-setup) section below.

### What You'll Do (Simple Version)

1. **Get the files** - Download or clone this repository
2. **Choose a name** - Pick a simple name for your memory folder (e.g., `my-memory`)
3. **Set up AGENTS.md** - Copy template and replace one placeholder word
4. **Set up in your project** - Either:
   - **Option A (Easier)**: Add `agents-md` folder to your workspace - Cursor/VS Code will automatically detect `AGENTS.md`
   - **Option B**: Copy files to your project folder
5. **Choose memory location** - Decide where to store memories (usually Documents folder)
6. **Add to workspace** - Add memory folder to Cursor/VS Code workspace
7. **Test it** - Ask AI to initialize memory

**That's it!** The detailed guide in [SIMPLE_SETUP.md](SIMPLE_SETUP.md) walks you through each step with screenshots descriptions and troubleshooting tips.

**💡 Tip**: If you're using Cursor or VS Code, the workspace-based setup (Option A) is much easier - no need to copy `AGENTS.md` to each project!

### Available Systems

#### 🧠 Memory System (Current)

A robust, RAG-optimized memory management system with multi-platform support. Provides a systematic approach to storing and retrieving project-specific knowledge, user preferences, and cross-project patterns for AI coding agents.

**Note**: The memory directory name is user-configurable. Throughout this documentation, `{MEMORY_DIR}` represents your chosen directory name (e.g., `agent-memory`, `my-memory`, `ai-memory`, etc.). Replace `{MEMORY_DIR}` with your chosen name when configuring the system.

**Workflow Options**:
- **Structured Workflow**: Full memory system with `topic/`, `session/`, indexing (best for complex projects)
- **Simple Workflow**: Single-file templates for quick daily logging (best for vibecoding and experiments)
- See `templates/README.md` for templates and guidance on choosing your workflow

### Future Systems

More systems will be added based on work experience and practical needs. Each system will be:
- **Production-tested**: Developed and refined through real-world use
- **Well-documented**: Comprehensive documentation and examples
- **Modular**: Can be used independently or combined with other systems
- **Agent-compatible**: Designed to work seamlessly with AI coding agents

---

## Memory System

The following sections document the Memory System, which is currently available.

**🚀 Key Features**:
- **Advanced RAG Support**: Intelligent semantic search with multi-level indexing
- **Token Optimization**: 80-95% token reduction through selective reading and indexing
- **Multi-Platform**: Native support for macOS, Linux, and Windows with platform-specific optimizations
- **Fast Retrieval**: Multi-level indexing and caching strategies for instant access
- **Scalable**: Handles large memory databases without performance degradation

**✅ Compatibility**: Fully compatible with existing Cursor rules, user rules, and custom `AGENTS.md` configurations. Simply append memory system rules to your existing setup.

**🌐 Multi-Agent Support**: Technically compatible with any coding agent or editor that supports the `AGENTS.md` format, including Cursor, Aider, GitHub Copilot, and others.

### ⚠️ Model Compatibility Note

**IMPORTANT**: Not every AI model can smartly support memory management. This system is designed for **agentic-capable models** that can:
- Understand and follow complex instructions
- Perform semantic search and retrieval
- Make intelligent decisions about what information to load
- Execute multi-step workflows autonomously

**Recommended**: Use agentic-capable models (such as Claude Sonnet/Opus, GPT-4, or similar advanced models) for optimal memory system performance.

## Why Local Markdown Files?

There are many memory solutions available, including MCP (Model Context Protocol) tools, databases, vector stores, and cloud-based systems that may offer enhanced security or features. So why choose local markdown files?

### Design Philosophy

**agents-md** prioritizes **human readability, transparency, and control** over advanced technical features. Here's why:

### Benefits for Humans

#### 1. **Full Transparency & Control**
- ✅ **You can read everything**: All memory is stored in human-readable markdown files
- ✅ **You own your data**: Files are stored locally, not in a cloud service or database
- ✅ **Easy inspection**: Open any memory file to see exactly what the agent knows
- ✅ **No black boxes**: No hidden databases or proprietary formats

#### 2. **Easy Editing & Maintenance**
- ✅ **Edit with any text editor**: Use VS Code, Cursor, vim, or even Notepad
- ✅ **Version control friendly**: Markdown files work perfectly with Git
- ✅ **Easy backup**: Just copy the directory - no database exports needed
- ✅ **Portable**: Move memory between machines by copying files

#### 3. **Learning & Understanding**
- ✅ **See patterns emerge**: Browse knowledge files to understand what the agent learned
- ✅ **Review decisions**: Read session archives to see how problems were solved
- ✅ **Analyze interaction history**: Review past conversations and work sessions to understand your collaboration patterns, identify recurring issues, and improve your workflow
- ✅ **Knowledge transfer**: Share memory files with team members or new projects
- ✅ **Documentation**: Memory files serve as living documentation of your projects

#### 4. **No Dependencies**
- ✅ **No database setup**: No PostgreSQL, MongoDB, or SQLite required
- ✅ **No API keys**: No external services or authentication needed
- ✅ **No installation**: Just files - works everywhere
- ✅ **No vendor lock-in**: Your memory isn't tied to any service

#### 5. **Privacy & Security**
- ✅ **Local storage**: Your memory stays on your machine (or your cloud storage)
- ✅ **No data transmission**: No API calls sending your memory to external services
- ✅ **You control access**: Use file system permissions, encryption, or secure cloud storage
- ✅ **Audit trail**: See exactly what was stored and when

### Benefits for Agents

#### 1. **Efficient RAG Retrieval**
- ✅ **Semantic search**: Agents can use `codebase_search` to find relevant memories
- ✅ **Selective reading**: Read only relevant sections, not entire files
- ✅ **Token optimization**: 80-95% reduction in token usage vs loading all memory
- ✅ **Fast lookup**: Index files enable instant access to memory metadata

#### 2. **Structured Organization**
- ✅ **Clear categorization**: Project-specific, shared, and secure memory separation
- ✅ **Semantic tags**: Tags and keywords enable intelligent retrieval
- ✅ **Period-based archives**: Sessions organized by time for efficient historical search
- ✅ **Knowledge vs sessions**: Clear separation between patterns and work history

#### 3. **Platform Awareness**
- ✅ **Cross-platform**: Works on macOS, Linux, and Windows
- ✅ **Cloud storage support**: Detects and uses Google Drive, iCloud, etc.
- ✅ **Path resolution**: Automatic platform-specific path handling
- ✅ **Tool optimization**: Uses platform-specific tools for best performance

#### 4. **Scalability**
- ✅ **Handles large memory**: Index-first approach prevents performance degradation
- ✅ **Chunked retrieval**: Processes memory in manageable pieces
- ✅ **Efficient search**: Multi-level indexing for fast lookups
- ✅ **No size limits**: Unlike some database solutions, no practical size constraints

### Comparison with Other Solutions

| Feature | Local Markdown | MCP Tools | Databases | Cloud Services |
|---------|---------------|-----------|-----------|----------------|
| **Human Readable** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **No Dependencies** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Version Control** | ✅ Excellent | ⚠️ Limited | ⚠️ Limited | ❌ No |
| **Privacy** | ✅ Full control | ⚠️ Depends | ⚠️ Depends | ❌ External |
| **Portability** | ✅ Excellent | ⚠️ Medium | ⚠️ Medium | ❌ Low |
| **Setup Complexity** | ✅ Minimal | ⚠️ Medium | ❌ High | ⚠️ Medium |
| **RAG Support** | ✅ Excellent | ✅ Excellent | ⚠️ Medium | ✅ Excellent |
| **Token Efficiency** | ✅ Excellent | ✅ Excellent | ⚠️ Medium | ✅ Excellent |

### When to Use agents-md

**Choose agents-md if you:**
- Want full transparency and control over your memory
- Prefer human-readable, editable files
- Need easy backup and portability
- Want to avoid external dependencies
- Value privacy and local storage
- Work with version control systems

**Consider alternatives if you:**
- Need real-time collaboration features
- Require advanced query capabilities (SQL, complex joins)
- Need built-in encryption at the storage level
- Have specific compliance requirements for database storage
- Prefer managed cloud solutions

### The Best of Both Worlds

**agents-md** doesn't prevent you from using other tools. You can:
- Use MCP tools for specific features while using markdown for general memory
- Store sensitive data in encrypted databases while keeping patterns in markdown
- Use cloud services for backup while maintaining local markdown as primary storage
- Combine multiple approaches based on your needs

The goal is to provide a **simple, transparent, and powerful** foundation that works well for most use cases while remaining flexible enough to integrate with other tools when needed.

## Memory System Setup

> **💡 For Non-Technical Users**: If you're not comfortable with command-line tools or technical jargon, please use the **[SIMPLE_SETUP.md](SIMPLE_SETUP.md)** guide instead. It provides step-by-step instructions with plain language explanations.

This section provides technical setup instructions for developers. The setup process involves configuring file paths, copying files, and setting up workspace access.

### 1. Clone or Initialize the Memory Repository

First, clone this repository or set up the memory storage location:

```bash
git clone <repository-url>
cd agents-md
```

Or if you're setting up a new instance:

```bash
mkdir -p ~/Documents/agents-md
cd ~/Documents/agents-md
```

**⚠️ Important**: Choose your memory directory name (e.g., `agent-memory`, `my-memory`, `ai-memory`) and configure it in `AGENTS.md` (see step 2 below).

### 2. Configure Memory Directory Name

**CRITICAL**: You must replace `{MEMORY_DIR}` placeholder in `AGENTS.md` with your chosen directory name.

> **💡 Tip**: If you're not comfortable with find-and-replace, see [SIMPLE_SETUP.md](SIMPLE_SETUP.md) for detailed visual instructions.

#### Option A: Manual Replacement (Recommended for Non-Engineers)

**This is straightforward and easy** - simply use find-and-replace in your text editor:

1. Open `AGENTS.md` in your text editor
2. Use find-and-replace (usually `Cmd+F` or `Ctrl+F`):
   - Find: `{MEMORY_DIR}`
   - Replace: `your-chosen-name` (e.g., `agent-memory`, `my-memory`, etc.)
3. Replace all occurrences
4. Save the file

**That's it!** Manual replacement is simple and works perfectly.

#### Option B: Python Script (For Engineers)

If you prefer automation, you can use the provided Python script:

```bash
python3 setup_memory_dir.py
```

The script will:
- Prompt you for your chosen directory name
- Validate the name (lowercase, numbers, hyphens, underscores only)
- Replace all `{MEMORY_DIR}` occurrences in `AGENTS.md`
- Show you a summary of changes

**Note**: The script requires Python 3.6+. If you're not comfortable with Python or command-line tools, use Option A (manual replacement) instead - it's just as effective and easier.

### 3. Set Up Files in Your Project

You have two options for setting up the memory system in your project:

#### Option A: Workspace-Based Setup (Recommended for Cursor/VS Code)

**If your editor supports workspaces** (like Cursor and VS Code), you can add the cloned `agents-md` repository directly to your workspace instead of copying files:

1. **Add agents-md to your workspace**:
   - Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
   - Select "Add Folder to Workspace"
   - Navigate to and select your cloned `agents-md` folder
   - The `agents-md` folder will appear in your workspace sidebar

2. **AGENTS.md is automatically detected**:
   - Recent versions of Cursor automatically detect `AGENTS.md` files in the workspace
   - The `AGENTS.md` file in the `agents-md` folder will be used as active rules
   - No need to copy `AGENTS.md` to your project root

3. **Copy `_agents-md` folder** (still needed):
   - You still need to copy the `_agents-md` folder to your project root, OR
   - Add it to your workspace as well (it will be accessible from the `agents-md` folder)

**Benefits of this approach**:
- ✅ No need to copy `AGENTS.md` to each project
- ✅ Easy to update - changes in `agents-md` repository apply automatically
- ✅ Cleaner project structure - no duplicate files
- ✅ Works great with multiple projects sharing the same setup

#### Option B: Copy Files to Project (Traditional Method)

**Copy the following to your project root:**

1. **Copy `_agents-md` folder** - Contains memory system prompts and guidelines
2. **Copy `AGENTS.md`** - Contains agent rules and memory configuration (already configured with your chosen directory name)

**Using Command Line**:
```bash
# From your project root
cp -r /path/to/agents-md/_agents-md .
cp /path/to/agents-md/AGENTS.md ./AGENTS.md
```

**Using File Manager** (Easier for non-technical users):
- Navigate to the `agents-md` folder
- Copy the `_agents-md` folder and `AGENTS.md` file
- Navigate to your project folder
- Paste both items

> **💡 For detailed file copying instructions**, see [SIMPLE_SETUP.md](SIMPLE_SETUP.md) Step 4.

**Important**: If your project already has an `AGENTS.md` file, **append** the content from agents-md's `AGENTS.md` to your existing file to avoid conflicts.

**✅ Compatibility Note**: agents-md is fully compatible with existing Cursor rules and user rules. The memory system rules will work alongside your existing `AGENTS.md` content.

### 3.5. Language Selection (Optional)

**AGENTS.md** supports both English and Japanese. You can choose your preferred language using either the automated script or manual setup.

#### Option A: Automated Script (Recommended)

Use the provided Python script to switch between languages:

```bash
# Switch to Japanese
python3 switch_agents_lang.py ja

# Switch to English  
python3 switch_agents_lang.py en

# Check current language
python3 switch_agents_lang.py
```

The script maintains separate source files (`AGENTS.md.en` and `AGENTS.md.ja`) and copies the appropriate one to `AGENTS.md` based on your selection.

**⚠️ Important**: After switching languages, the script will attempt to preserve your configured `{MEMORY_PATH}` automatically. However, if the script cannot detect your configured path, you'll need to run `setup_memory_dir.py` again to configure the memory path in the new language template:

```bash
# After switching language, if MEMORY_PATH needs configuration:
python3 setup_memory_dir.py
```

The script will warn you if `{MEMORY_PATH}` still needs to be configured.

#### Option B: Manual Setup (Simple Alternative)

If you prefer manual setup or don't want to use the script, you can manually clone and rename the template files:

**For English**:
```bash
# Copy the English template to AGENTS.md
cp AGENTS.md.en AGENTS.md
```

**For Japanese**:
```bash
# Copy the Japanese template to AGENTS.md
cp AGENTS.md.ja AGENTS.md
```

**Note**: The idea is to keep a single `AGENTS.md` file in your project root. The `AGENTS.md.en` and `AGENTS.md.ja` files serve as templates that you clone and rename to `AGENTS.md` based on your language preference.

**⚠️ Important**: After manually copying, you **must** configure the memory path:
1. Run `setup_memory_dir.py` to configure `{MEMORY_PATH}`:
   ```bash
   python3 setup_memory_dir.py
   ```
   OR manually replace `{MEMORY_PATH}` placeholder in the copied `AGENTS.md` with your full memory root path (see step 4)

**Note**: Language switching only affects `AGENTS.md`. Documentation files (like `README.md`) have separate Japanese versions (e.g., `README.ja.md`) that don't affect agent functionality.

### 4. Configure Memory Path in AGENTS.md

**CRITICAL**: After copying `AGENTS.md` to your project, you may need to adjust the memory storage path to match your local system and platform.

1. Open `AGENTS.md` in your project root
2. Find the memory storage path section (Platform Detection)
3. Update the path to match your system if needed

**Platform-specific examples** (the `{MEMORY_DIR}` placeholder should already be replaced with your chosen name from step 2):
- **macOS**: `~/Library/CloudStorage/GoogleDrive-you@gmail.com/My Drive/AI/your-memory-dir` or `~/Documents/your-memory-dir`
- **Linux**: `~/Documents/your-memory-dir` or `~/.local/share/your-memory-dir`
- **Windows**: `%USERPROFILE%\Documents\your-memory-dir` or `%APPDATA%\your-memory-dir`

**Note**: The default paths should work for most users. Only adjust if you have a custom setup.

### 5. Add Memory Directory to Workspace (Cursor/VS Code)

**CRITICAL**: Cursor and VS Code cannot access files outside the workspace by default. To enable file access permissions for the memory system, you **must** add your memory directory to your project workspace.

> **💡 Need help with this step?** See [SIMPLE_SETUP.md](SIMPLE_SETUP.md) Step 6 for detailed instructions with troubleshooting tips.

#### Why This Is Required

- **File Access Limitation**: Cursor/VS Code agents can only access files within the workspace for security reasons
- **Memory Location**: Your memory directory is typically stored outside your project (e.g., in `~/Documents/` or cloud storage)
- **Solution**: Adding the memory directory to the workspace elevates file access permissions, allowing agents to read and write memory files

#### Method 1: Using Command Palette (Easiest)

**In Cursor/VS Code**:
1. Open Command Palette:
   - **macOS**: `Cmd+Shift+P`
   - **Windows/Linux**: `Ctrl+Shift+P`
2. Type and select: **"Add Folder to Workspace"** or **"Workspaces: Add Folder to Workspace"**
3. Navigate to and select your memory directory (the directory configured in `AGENTS.md`)
   - Example: `~/Library/CloudStorage/GoogleDrive-you@gmail.com/My Drive/AI/your-memory-dir`
   - Or: `~/Documents/your-memory-dir`
4. The memory directory will appear as a separate folder in your workspace sidebar

#### Method 2: Using Workspace File (For Multi-Folder Workspaces)

If you prefer to manage your workspace via a `.code-workspace` file:

1. Create or edit `.code-workspace` file in your project root:
```json
{
  "folders": [
    {
      "path": "."
    },
    {
      "path": "/Users/username/Documents/your-memory-dir"
    }
  ],
  "settings": {}
}
```

2. Replace the second `path` with your actual memory directory path
3. Open the workspace file: `File > Open Workspace from File...` and select your `.code-workspace` file

#### Method 3: Using Workspace Settings (Alternative)

1. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
2. Type: **"Preferences: Open Workspace Settings"**
3. Add your memory directory path to workspace settings (if supported by your editor version)

#### Verification

After adding the memory directory to your workspace:
- ✅ The memory directory should appear in your workspace sidebar
- ✅ You should be able to browse memory files in the editor
- ✅ Agents will be able to read and write memory files

**Note**: If you're using cloud storage (Google Drive, iCloud, etc.), make sure the path is accessible and the directory exists before adding it to the workspace.

### 6. Initialize Memory for Your Project

To initialize memory structure for your current project, use any natural language prompt that the agent understands. Examples:

**English**:
```
construct memory
initialize memory for this project
set up project memory
create memory structure
```

**Japanese**:
```
メモリを構築
このプロジェクトのメモリを初期化
プロジェクトメモリをセットアップ
メモリ構造を作成
```

The agent will automatically create the memory structure in the configured memory directory, including index files and initial knowledge files documenting the project architecture and patterns.

### 7. Verify Configuration

Ensure that:
- `_agents-md` folder exists in your project root
- `AGENTS.md` exists in your project root (with `{MEMORY_DIR}` replaced with your chosen name)
- The memory path in `AGENTS.md` points to your memory directory
- The memory directory is added to your Cursor workspace
- The memory directory exists and is writable

## Memory System Usage

### Memory Structure

The memory system organizes information into three categories:

1. **Project-Specific Memory** (`{MEMORY_DIR}/[project-name]/`)
   - Project architecture decisions
   - Project-specific patterns and fixes
   - Project file locations
   - Project-specific preferences

2. **Common Memory** (`{MEMORY_DIR}/shared/`)
   - User preferences (apply to all projects)
   - Global settings and configurations
   - Cross-project patterns
   - User workflows

3. **Private Memory** (`{MEMORY_DIR}/secure/`) ⚠️
   - API keys, passwords, tokens
   - Personal information
   - Sensitive settings
   - **Never commit to version control**

### How Agents Use Memory

Agents automatically:
- **Sync memory** after significant tasks or when learning patterns
- **Check memory** when context is lost or unclear
- **Update index files** when creating new knowledge or sessions
- **Consolidate related sessions** to maintain clean organization
- **Use RAG** to retrieve only relevant memories, minimizing token usage

**Note**: Cursor agents will automatically sync memory during conversations. Manual sync is typically not needed, but prompts are provided below if you want to trigger it manually.

### 🚀 Advanced RAG (Retrieval-Augmented Generation) Support

**IMPORTANT**: agents-md supports **advanced RAG capabilities** through intelligent semantic search and multi-level indexing. This is a powerful feature that significantly reduces token usage.

**⚠️ Model Requirement**: RAG support requires **agentic-capable models**. Not all AI models can intelligently handle memory retrieval - basic completion models may not perform semantic search or make intelligent decisions about what memories to load.

**How it works**:
- **Multi-level indexing**: Index-first lookup for instant access
- **Semantic search**: Natural language queries to find relevant memories
- **Selective reading**: Only relevant sections are loaded into context
- **Token optimization**: 80-95% token reduction compared to loading entire files

**Benefits**:
- ✅ **Reduced Token Usage**: Only relevant memories are loaded into context
- ✅ **Intelligent Retrieval**: Agents understand context and retrieve related information automatically
- ✅ **Fast Access**: Multi-level indexing enables instant lookup
- ✅ **Scalable**: Handles large memory databases efficiently

**Example Prompts**:
```
What patterns did we establish for error handling in this project?
Check memory for previous solutions to similar issues.
What architectural decisions were made about the API design?
```

The agent will automatically:
1. Check index files for semantic tags/keywords
2. Use semantic search to find relevant files
3. Read only relevant sections selectively
4. Minimize token usage while maximizing accuracy

### Prompt Examples for Memory Usage

Here are practical examples of prompts you can use to interact with the memory system:

#### Getting Topics and Patterns
```
What topics are documented in memory for this project?
Show me all the patterns we've established for this project.
What are the documented topics in the knowledge/ directory?
List all architectural patterns we've documented.
```

#### Searching for Specific Information
```
What did we decide about error handling in this project?
Check memory for how we handle authentication.
What patterns exist for API integration?
Find previous solutions to similar problems.
```

#### Checking User Preferences
```
What are my preferences for this project?
Check common preferences that apply to all projects.
What project-specific preferences are set?
```

#### Reviewing Architecture Decisions
```
What architectural decisions were made for this project?
Show me the architecture documentation from memory.
What design patterns are we using?
```

#### Finding Session Summaries
```
What work was done in recent sessions?
Show me the last few session summaries.
What was completed in the last week?
```

#### Checking Project Status
```
What's the current status of this project?
Show me recent fixes and updates.
What are the known issues and their solutions?
```

All these prompts will trigger the agent to intelligently search memory files using RAG techniques, minimizing token usage while providing accurate context.

### Memory File Types

- **Knowledge Files** (`knowledge/topic_name.md`): Ongoing documentation of patterns and architecture
- **Session Archives** (`sessions/YYYY-MM/YYYY-MM-DD_summary.md`): Consolidated work sessions
- **Index Files** (`index.json`, `index.md`): Fast lookup and quick reference

## Memory System Documentation

- **Memory System**: See `_agents-md/memory/` for memory-specific documentation
  - **Organization**: `_agents-md/memory/organization.md` - Memory management rules
  - **RAG**: `_agents-md/memory/rag.md` - RAG strategies and token optimization
  - **Platform**: `_agents-md/memory/platform.md` - Platform-specific paths and tools
- **Templates**: See `templates/` for workflow templates
  - **Simple Workflow**: `templates/AGENTS.md.simple` and `templates/GLOBAL.md` for quick daily logging
  - **Template Guide**: `templates/README.md` - When to use which workflow

## Memory System Initialization & Manual Sync

### Memory Initialization Prompt

If you want to manually initialize memory for your project, use this prompt:

```
Initialize memory for this project. Create the memory structure in the configured memory directory, including index files and initial knowledge files documenting the project architecture and patterns.
```

### Manual Memory Sync Prompt

While agents automatically sync memory, you can manually trigger a sync with:

```
Sync memory for this project. Update index files, consolidate recent sessions if needed, and ensure index.json is synchronized with actual files in knowledge/ and sessions/ directories.
```

### Memory Update Prompt

To update memory with current project status:

```
Update project memory with current status. Document recent changes, update index files, and sync any new patterns or architectural decisions.
```

## Memory System Platform Support

The Memory System supports multiple platforms with platform-specific optimizations:

- **macOS**: Cloud storage detection, Spotlight search integration
- **Linux**: Filesystem-specific optimizations, efficient search tools
- **Windows**: PowerShell integration, WSL support

See `_agents-md/memory/platform.md` for platform-specific documentation.

## Memory System Security

⚠️ **IMPORTANT**: Private memory (`{MEMORY_DIR}/secure/`) contains sensitive information:
- Never commit private memory files to version control
- Always mask sensitive data in responses
- Only access when explicitly needed
- See `_agents-md/memory/organization.md` for security protocols

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Memory System Comparison

### Key Improvements

**vs. Basic File-Based Memory**:
- ✅ Multi-level indexing for fast lookup
- ✅ RAG-optimized retrieval (80-95% token reduction)
- ✅ Platform-specific optimizations
- ✅ Intelligent semantic search

**vs. Database-Based Memory**:
- ✅ No external dependencies
- ✅ Human-readable files
- ✅ Version control friendly
- ✅ Easy backup and migration

**vs. Previous Systems**:
- ✅ Improved RAG support with semantic tags
- ✅ Better token optimization strategies
- ✅ Multi-platform support
- ✅ Faster retrieval through indexing

## Project Roadmap

**agents-md** is an evolving collection of systems. Future additions will include:

- Additional systems based on real-world work experience
- Integration patterns between systems
- Best practices and workflows
- Community-contributed systems (subject to review and quality standards)

Each new system will follow the same principles: production-tested, well-documented, modular, and agent-compatible.

## Contributing

This is a personal project, but suggestions and improvements are welcome. Please ensure any contributions maintain the MIT license and attribution.

## Acknowledgements

The Memory System was inspired by an earlier memory system design created and developed during work at [Rudel, inc.](https://rudel.jp). The foundational concepts and architectural patterns were refined and adapted for this open-source implementation.

## Author

Paulus Ery Wasito Adhi (paupawsan@gmail.com)

