<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Memory System Setup Guide

This guide provides complete technical setup instructions for developers. The setup process involves configuring file paths, copying files, and setting up workspace access.

## Prerequisites

- **AI Model**: Agentic-capable model (Claude Sonnet/Opus, GPT-4, etc.)
- **Editor**: Cursor or VS Code with AI agent support
- **Python 3.6+** (optional, for automated setup scripts)

## Step 1: Get the Repository Files

You have several options to get the repository files:

### Option A: Download as ZIP (Easiest for Non-Technical Users)

1. On GitHub, click the green **"Code"** button
2. Click **"Download ZIP"**
3. Extract the ZIP file to a location on your computer
4. Navigate to the extracted `agents-md` folder

**No Git required!** This is the simplest method if you're not familiar with command-line tools.

### Option B: Clone with Git (For Developers)

```bash
git clone <repository-url>
cd agents-md
```

### Option C: Initialize New Instance

```bash
mkdir -p ~/Documents/agents-md
cd ~/Documents/agents-md
```

## Step 2: Configure Memory Directory Name

**CRITICAL**: You must replace `{MEMORY_DIR}` placeholder in `AGENTS.md` with your chosen directory name.

> **💡 Tip**: Choose a simple name like `agent-memory`, `my-memory`, or `ai-memory`

### Option A: Manual Replacement (Recommended)

**This is straightforward and easy** - simply use find-and-replace in your text editor:

1. Open `AGENTS.md` in your text editor
2. Use find-and-replace (usually `Cmd+F` or `Ctrl+F`):
   - Find: `{MEMORY_DIR}`
   - Replace: `your-chosen-name` (e.g., `agent-memory`, `my-memory`, etc.)
3. Replace all occurrences
4. Save the file

**That's it!** Manual replacement is simple and works perfectly.

### Option B: Python Script (For Engineers)

If you prefer automation, you can use the provided Python script:

```bash
# Windows
python setup.py

# macOS/Linux
python3 setup.py

# Or specify language directly
python3 setup.py --lang en    # English
python3 setup.py --lang ja    # Japanese
```

The script will:
1. **Language Selection**: Prompt you to select language (English/Japanese) - or use `--lang` parameter
2. **Language Switching**: Automatically switch `AGENTS.md` and `GEMINI.md` to selected language
3. **Memory Path Configuration**: Prompt you to configure memory root path (optional - you can skip with "no")
4. **File Creation**: Automatically create both `AGENTS.md` (for Cursor) and `GEMINI.md` (for Google Antigravity)

**Features**:
- Cross-platform support (Windows, macOS, Linux)
- UTF-8 console encoding for proper Japanese character display on Windows
- Preserves existing `MEMORY_PATH` when switching languages
- Can exit after language switching without configuring memory path

## Step 3: Set Up Files in Your Project

You have two options for setting up the memory system in your project:

### Option A: Workspace-Based Setup (Recommended for Cursor/VS Code)

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

### Option B: Copy Files to Project (Traditional Method)

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
- Copy the `_agents-md` folder, `AGENTS.md`, and `GEMINI.md` files
- Navigate to your project folder
- Paste all three items

**Important**: 
- If your project already has an `AGENTS.md` file, **append** the content from agents-md's `AGENTS.md` to your existing file to avoid conflicts.
- `GEMINI.md` is for Google Antigravity support - copy it if you plan to use Antigravity, or skip it if you only use Cursor.

**✅ Compatibility Note**: agents-md is fully compatible with existing Cursor rules and user rules. The memory system rules will work alongside your existing `AGENTS.md` content.

## Step 4: Language Selection (Optional)

**AGENTS.md** supports both English and Japanese. You can choose your preferred language using either the automated script or manual setup.

### Option A: Automated Script (Recommended)

Use the setup script to switch between languages:

```bash
# Run setup script - it will prompt for language first
python3 setup.py

# Or specify language directly via command line
python3 setup.py --lang en    # Switch to English
python3 setup.py --lang ja    # Switch to Japanese
```

The setup script will:
1. **Language Selection**: Prompt you to select a language (English or Japanese) - or use `--lang` parameter
2. **Language Switching**: Switch `AGENTS.md` and `GEMINI.md` to the selected language
3. **Preserve Configuration**: Preserve your configured `MEMORY_PATH` if it exists
4. **Optional Memory Setup**: Ask if you want to configure memory path (you can choose "no" to exit)

The script maintains separate source files (`AGENTS.md.en` and `AGENTS.md.ja`) and copies the appropriate one to both `AGENTS.md` (for Cursor) and `GEMINI.md` (for Google Antigravity) based on your selection.

**💡 Tip**: You can use the script just to switch languages without configuring memory path - simply answer "no" when asked about memory path configuration.

### Option B: Manual Setup (Simple Alternative)

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

**⚠️ Important**: After manually copying, you **must** configure the memory path:
1. Run `setup.py` to configure `MEMORY_PATH`:
   ```bash
   python3 setup.py
   ```
   OR manually replace the path in the Configuration section of `AGENTS.md`:
   ```
   **MEMORY_PATH**: `/path/to/your/memory-root`
   ```

## Step 5: Configure Memory Path in AGENTS.md

**CRITICAL**: After copying `AGENTS.md` to your project, you need to configure the memory path.

1. Open `AGENTS.md` in your project root
2. Find the **Configuration** section at the top
3. Replace the path in this line:
   ```
   **MEMORY_PATH**: `/path/to/your/memory-root`
   ```
   with your actual memory directory path

**Platform-specific examples**:
- **macOS**: `~/Library/CloudStorage/GoogleDrive-you@gmail.com/My Drive/AI/your-memory-dir` or `~/Documents/your-memory-dir`
- **Linux**: `~/Documents/your-memory-dir` or `~/.local/share/your-memory-dir`
- **Windows**: `%USERPROFILE%\Documents\your-memory-dir` or `%APPDATA%\your-memory-dir`

**Note**: You only need to replace the path in one place. Agents understand that `MEMORY_PATH` applies to all path references throughout the document.

**Alternative**: Use `setup.py` script for automatic configuration:
```bash
python3 setup.py
```

## Step 6: Add Memory Directory to Workspace

**CRITICAL**: Cursor and VS Code cannot access files outside the workspace by default. To enable file access permissions for the memory system, you **must** add your memory directory to your project workspace.

### Why This Is Required

- **File Access Limitation**: Cursor/VS Code agents can only access files within the workspace for security reasons
- **Memory Location**: Your memory directory is typically stored outside your project (e.g., in `~/Documents/` or cloud storage)
- **Solution**: Adding the memory directory to the workspace elevates file access permissions, allowing agents to read and write memory files

### Method 1: Using Command Palette (Easiest)

**In Cursor/VS Code**:
1. Open Command Palette:
   - **macOS**: `Cmd+Shift+P`
   - **Windows/Linux**: `Ctrl+Shift+P`
2. Type and select: **"Add Folder to Workspace"** or **"Workspaces: Add Folder to Workspace"**
3. Navigate to and select your memory directory (the directory configured in `AGENTS.md`)
   - Example: `~/Library/CloudStorage/GoogleDrive-you@gmail.com/My Drive/AI/your-memory-dir`
   - Or: `~/Documents/your-memory-dir`
4. The memory directory will appear as a separate folder in your workspace sidebar

### Method 2: Using Workspace File (For Multi-Folder Workspaces)

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

### Method 3: Using Workspace Settings (Alternative)

1. Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
2. Type: **"Preferences: Open Workspace Settings"**
3. Add your memory directory path to workspace settings (if supported by your editor version)

### Verification

After adding the memory directory to your workspace:
- ✅ The memory directory should appear in your workspace sidebar
- ✅ You should be able to browse memory files in the editor
- ✅ Agents will be able to read and write memory files

**Note**: If you're using cloud storage (Google Drive, iCloud, etc.), make sure the path is accessible and the directory exists before adding it to the workspace.

## Step 7: Initialize Memory for Your Project

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

## Step 8: Configure Agent Command Permissions

**IMPORTANT**: The memory system requires agents to execute file system commands to create, read, and write memory files. This requires explicit permission from your editor.

### Commands Agents May Execute

Agents may execute the following types of commands (these are safe file operations):
- **File/Folder Creation**: `mkdir`, `touch` - Creating memory directories and files
- **File Reading**: `cat`, `head`, `grep` - Reading memory files and searching content
- **File Writing**: `echo`, `printf` - Writing memory content to files
- **File Operations**: `cp`, `mv`, `ls` - Organizing and managing memory files

### Permission Requirements

**You must whitelist these commands** in your editor or system:

**Cursor**:
- Go to Settings → Agent → Command Execution
- Add the above commands to your allowed commands list
- Or grant permission when prompted during agent operations

**VS Code**:
- Similar settings in VS Code extensions that support command execution
- Check your AI assistant extension settings

**Antivirus/Security Software**:
- Some antivirus programs may block these operations
- Add exceptions for your project folder and memory directory
- Allow file system operations from your editor

**Note**: These commands are **safe file operations only** - they cannot execute harmful code, install software, or access the internet. The memory system only creates, reads, and writes text files.

## Step 9: Verify Configuration

Ensure that:
- ✅ `_agents-md` folder exists in your project root
- ✅ `AGENTS.md` exists in your project root (with `{MEMORY_DIR}` replaced with your chosen name)
- ✅ The memory path in `AGENTS.md` points to your memory directory
- ✅ The memory directory is added to your Cursor workspace
- ✅ The memory directory exists and is writable
- ✅ Agent command permissions are configured

## Troubleshooting

### Memory Directory Not Accessible
- **Issue**: Agent cannot read/write memory files
- **Solution**: Verify the memory directory is added to your workspace (Step 6)

### Commands Not Executing
- **Issue**: Agent cannot create directories or files
- **Solution**: Check agent command permissions (Step 8)

### Path Not Found
- **Issue**: Memory path points to non-existent directory
- **Solution**: Verify the path in `AGENTS.md` matches your system (Step 5)

### Multiple AGENTS.md Files
- **Issue**: Conflicting agent configurations
- **Solution**: Use workspace-based setup (Option A in Step 3) or merge files manually

## Next Steps

Once setup is complete, see the [Usage Guide](usage-guide.md) for information on how to effectively use the memory system in your development workflow.
