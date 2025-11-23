<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Simple Setup Guide - For Non-Technical Users

**Don't worry if you're not a programmer!** This guide will walk you through setting up the systems step by step, using simple language and avoiding technical jargon. The setup process is the same for both the Memory System and Critical Thinking System - they're configured together in one file.

## What Is This?

This is a collection of **systems and tools** for AI coding assistants (like Cursor), built from real-world work experience. Currently includes:

1. **Memory System** - Helps your AI assistant remember things about your projects, so it can work better with you over time
2. **Critical Thinking System** - Helps your AI assistant verify facts, avoid mistakes, and make better decisions

**Think of it like**: 
- **Memory System**: A notebook where your AI assistant writes down what it learns about your projects, so it doesn't forget
- **Critical Thinking System**: A quality checker that helps your AI assistant verify information and think more carefully when needed

**Don't worry**: Both systems work automatically once set up! You don't need to understand all the technical details.

## What You'll Need

- A computer (Mac, Windows, or Linux)
- Cursor or VS Code editor installed
- Basic knowledge of using a text editor (like opening and saving files)

**You DON'T need**:
- Programming knowledge
- Command line/terminal experience (though we'll show you simple commands)
- Python or any other programming language

---

## Step-by-Step Setup

### Step 1: Download or Get the Files

**Option A: Download as ZIP (Easiest - Recommended for Non-Technical Users)**

If you're on GitHub:
1. Click the green **"Code"** button at the top of the repository page
2. Click **"Download ZIP"**
3. The ZIP file will download to your computer (usually in your Downloads folder)
4. Find the downloaded ZIP file and double-click it to extract/unzip it
5. You'll see a folder named `agents-md` (or `agents-md-main`) - this contains all the files you need

**On Mac**: Double-click the ZIP file and it will automatically extract
**On Windows**: Right-click the ZIP file → "Extract All" → Choose a location
**On Linux**: Right-click the ZIP file → "Extract Here" or use your archive manager

**Option B: If you already have the files**
- You already have the files! Just find where you saved the `agents-md` folder.

**Option C: If you're using Git (for developers)**
- Skip this step - you already have the files.

**What you should see**: A folder with files like `AGENTS.md`, `README.md`, `_agents-md`, etc.

---

### Step 2: Choose a Name for Your Memory Folder

Think of a simple name for where your AI's memory will be stored. Examples:
- `my-ai-memory`
- `cursor-memory`
- `ai-notes`

**Rules for the name**:
- Use only lowercase letters, numbers, hyphens (-), and underscores (_)
- No spaces
- Keep it short and simple

**Example good names**: `my-memory`, `ai-notes`, `cursor_memory`
**Example bad names**: `My Memory` (has space and capital), `memory!` (has special character)

---

### Step 3: Set Up the Configuration Files

**🎉 Good News!** We have an **automated setup script** that makes this much easier! You can choose to use the script (recommended) or do it manually.

#### Option A: Use the Setup Script (Easiest - Recommended)

The setup script will automatically:
- Let you choose your language (English or Japanese)
- Create both `AGENTS.md` (for Cursor) and `GEMINI.md` (for Google Antigravity)
- Configure the memory path for you

**How to use it:**

1. **Open Terminal/Command Prompt**:
   - **Mac/Linux**: Open Terminal
   - **Windows**: Open Command Prompt or PowerShell

2. **Navigate to the agents-md folder**:
   - Type `cd ` (with a space after cd)
   - Drag the `agents-md` folder into the terminal window
   - Press Enter

3. **Run the setup script**:
   - **Mac/Linux**: Type `python3 setup.py` and press Enter
   - **Windows**: Type `python setup.py` and press Enter

4. **Follow the prompts**:
   - Select your language (1 for English, 2 for Japanese, or type `en`/`ja`)
   - The script will switch the language automatically
   - Choose whether to configure memory path now (yes/no)
   - If yes, enter your memory folder path when prompted

**That's it!** The script creates both `AGENTS.md` and `GEMINI.md` files automatically.

#### Option B: Manual Setup (If you prefer to do it yourself)

If you prefer to set things up manually, follow these steps:

**3a. Open AGENTS.md**

1. Open the `agents-md` folder
2. Find the file called `AGENTS.md.en` (for English) or `AGENTS.md.ja` (for Japanese)
3. Right-click and choose "Open with" → your text editor (Cursor, VS Code, or even Notepad/TextEdit)

**3b. Choose Your Language**

**For English**:
- You'll use `AGENTS.md.en` as your template

**For Japanese**:
- You'll use `AGENTS.md.ja` as your template

**3c. Copy the Template**

1. Open the template file (`AGENTS.md.en` or `AGENTS.md.ja`)
2. Select all text (`Cmd+A` on Mac, `Ctrl+A` on Windows/Linux)
3. Copy it (`Cmd+C` or `Ctrl+C`)
4. Create a new file called `AGENTS.md` in the same folder
5. Paste the content (`Cmd+V` or `Ctrl+V`)
6. Save the file

**3d. Also Create GEMINI.md** (for Google Antigravity support)

1. Copy `AGENTS.md` and rename it to `GEMINI.md`
2. Both files should have the same content

**3e. Configure MEMORY_PATH**

Now you need to configure where your memory will be stored. Both `AGENTS.md` and `GEMINI.md` use a simple variable called `MEMORY_PATH` that you need to set.

1. In your `AGENTS.md` file, look for the **Configuration** section near the top
2. Find the line that says `**MEMORY_PATH**: `/path/to/your/memory-root``
3. For now, you can leave this as-is - we'll set the actual path in Step 5 after you create the memory folder

**Note**: The new format uses a single `MEMORY_PATH` variable instead of replacing multiple placeholders. This makes it easier to configure!

---

### Step 4: Set Up Files in Your Project

You have three ways to set up the memory system. Choose the one that works best for you:

#### Option A: Best Practice - External agentic-system Folder (Recommended for Multiple Projects)

**💡 Best Practice**: Use an external `agentic-system` folder for clean separation. This keeps your project code separate from memory and allows one folder to serve all your projects.

**What this means**: Instead of putting memory files inside your project, you create a separate folder outside your projects that holds memory for all your projects.

**Structure**:
```
Your Workspace:
├── YourProject/          ← Your project (only code files)
│   ├── app.py
│   └── README.md
│
└── agentic-system/      ← External folder (shared by all projects)
    ├── agent-memory/    ← Memory for all projects
    └── agents-md/       ← Configuration files
```

**How to set it up**:

1. **Create the external folder**:
   - Choose a location like `~/Documents/agentic-system` (or wherever you prefer)
   - Create a folder called `agentic-system`
   - Inside it, create two folders: `agent-memory` and `agents-md`

2. **Copy files to `agentic-system/agents-md/`**:
   - Copy the `_agents-md` folder to `agentic-system/agents-md/`
   - Copy `AGENTS.md` and `GEMINI.md` to `agentic-system/agents-md/`

3. **Add both folders to your workspace**:
   - Add your project folder to workspace (File → Open Folder)
   - Add the `agentic-system` folder to workspace (Add Folder to Workspace)
   - Both will appear in your workspace sidebar

**Why this is best**:
- ✅ Keeps your project code clean (no memory files mixed in)
- ✅ One folder works for all your projects
- ✅ Easy to share across projects
- ✅ Better organization

**Note**: This is recommended if you work with multiple projects. See the [Visual Installation Guide](installation-guide-visual-en.md#best-practices) for pictures showing this structure.

#### Option B: Workspace Setup (Good for Single Project)

**If you're using Cursor or VS Code**, you can add the `agents-md` folder to your workspace instead of copying files:

1. **Open Cursor or VS Code**
2. **Open your project folder** (File → Open Folder)
3. **Add agents-md to workspace**:
   - Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
   - Type: `Add Folder to Workspace`
   - Select "Add Folder to Workspace"
   - Navigate to and select your `agents-md` folder
   - Click "Add" or "Select Folder"

4. **AGENTS.md and GEMINI.md are automatically detected**:
   - Recent versions of Cursor automatically find `AGENTS.md` files in your workspace
   - The `AGENTS.md` file in the `agents-md` folder will be used automatically for Cursor
   - The `GEMINI.md` file will be used automatically for Google Antigravity
   - You don't need to copy these files to your project!

5. **Copy `_agents-md` folder** (still needed):
   - You still need to copy the `_agents-md` folder to your project folder
   - Or add it to your workspace too (it's already in the `agents-md` folder you just added)

**Why this is easier**:
- ✅ No need to copy `AGENTS.md` to each project
- ✅ Updates automatically when you update the `agents-md` folder
- ✅ Works with multiple projects easily

#### Option B: Copy Files (Traditional Method)

Now you need to copy two things to your project folder (the project where you want to use the memory system).

#### What to Copy:

1. **The `_agents-md` folder** - This contains instructions for the AI
2. **The `AGENTS.md` file** - This is the file you just created (or from setup script)
3. **The `GEMINI.md` file** - This is for Google Antigravity support (created automatically by setup script)

#### How to Copy:

**On Mac**:
1. Open Finder
2. Navigate to your `agents-md` folder
3. Copy the `_agents-md` folder (right-click → Copy)
4. Copy the `AGENTS.md` file (right-click → Copy)
5. Copy the `GEMINI.md` file (right-click → Copy)
6. Navigate to your project folder
7. Paste all three items (right-click → Paste)

**On Windows**:
1. Open File Explorer
2. Navigate to your `agents-md` folder
3. Copy the `_agents-md` folder (right-click → Copy)
4. Copy the `AGENTS.md` file (right-click → Copy)
5. Copy the `GEMINI.md` file (right-click → Copy)
6. Navigate to your project folder
7. Paste all three items (right-click → Paste)

**On Linux**:
1. Open your file manager
2. Navigate to your `agents-md` folder
3. Copy the `_agents-md` folder, `AGENTS.md`, and `GEMINI.md` files
4. Navigate to your project folder
5. Paste all three items

**Important**: If your project already has an `AGENTS.md` file, don't replace it! Instead, open both files and copy the content from the new `AGENTS.md` to the end of your existing file. The same applies to `GEMINI.md` if you're using Google Antigravity.

**💡 Choosing Your Setup Method**:
- **Option A (Best Practice)**: Use if you have multiple projects and want clean separation
- **Option B (Workspace Setup)**: Use if you prefer workspace integration for a single project  
- **Option C (Copy Files)**: Use if you prefer traditional file copying

All three methods work equally well - choose based on your preference!

---

### Step 5: Set Up Where Memory Will Be Stored

Your AI's memory needs a place to live. This is usually outside your project folder.

#### Choose a Location:

**Recommended locations**:
- **Mac**: `~/Documents/my-memory` (or whatever name you chose)
- **Windows**: `C:\Users\YourName\Documents\my-memory`
- **Linux**: `~/Documents/my-memory`

**Or use cloud storage**:
- **Mac with Google Drive**: `~/Library/CloudStorage/GoogleDrive-your-email/My Drive/AI/my-memory`
- **Mac with iCloud**: `~/Library/Mobile Documents/com~apple~CloudDocs/AI/my-memory`

#### Create the Memory Folder:

1. Open your file manager (Finder on Mac, File Explorer on Windows)
2. Navigate to your chosen location (e.g., Documents folder)
3. Create a new folder with your chosen name (e.g., `my-memory`)
4. Remember the full path to this folder - you'll need it in the next step

#### Update AGENTS.md with the Path:

1. Open `AGENTS.md` in your project folder
2. Look for the **Configuration** section at the top
3. Find the line that says `**MEMORY_PATH**: `/path/to/your/memory-root``
4. Replace `/path/to/your/memory-root` with your actual memory folder path

**Example**: If you created `my-memory` in Documents on Mac, replace it with:
```
**MEMORY_PATH**: `~/Documents/my-memory`
```

**Note**: You only need to replace the path in this one place. The AI agent will understand it applies everywhere.

**Don't worry** if you're not sure - the default paths usually work! Only change this if you put your memory folder in a special location.

---

### Step 6: Add Memory Folder to Cursor/VS Code Workspace

**Why this is important**: Cursor and VS Code can only access files inside your workspace. Since your memory folder is outside your project, you need to add it to the workspace.

#### How to Do It:

1. Open Cursor or VS Code
2. Open your project folder (File → Open Folder)
3. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) to open the command palette
4. Type: `Add Folder to Workspace`
5. Select "Add Folder to Workspace" from the list
6. Navigate to and select your memory folder (the one you created in Step 5)
7. Click "Add" or "Select Folder"

**What you should see**: Your memory folder should now appear in the sidebar of Cursor/VS Code, alongside your project folder.

**Troubleshooting**: If you can't find your folder:
- Make sure you created it first (Step 5)
- Try typing the full path in the file browser
- On Mac, you might need to press `Cmd+Shift+.` to show hidden folders

---

### Step 7: Test It Out!

Now let's make sure everything works:

1. Open Cursor or VS Code with your project
2. Make sure your memory folder is visible in the sidebar
3. In the chat/command area, type: `Initialize memory for this project`
4. The AI should create some files in your memory folder

**What success looks like**:
- You see new folders and files appear in your memory folder
- The AI responds that it's setting up memory
- No error messages appear

**If something goes wrong**:
- Check that your memory folder path in `AGENTS.md` is correct
- Make sure the memory folder is added to your workspace (Step 6)
- Try asking the AI: "Can you access the memory folder at [your path]?"

---

## You're Done! 🎉

Your systems are now set up! The AI assistant will automatically:
- **Memory System**: Remember things about your project, learn from your preferences, and store important patterns and solutions
- **Critical Thinking System**: Verify facts, avoid mistakes, and adjust its thinking based on how important the task is (more careful for important things like security, more flexible for simple tasks)

---

## Common Questions

### Q: Do I need to do anything else?

**A**: No! Once set up, both systems work automatically. The Memory System will save and retrieve memories as needed, and the Critical Thinking System will help verify facts and make better decisions automatically.

### Q: Can I change the memory folder location later?

**A**: Yes! Just update the path in `AGENTS.md` and make sure the new folder is added to your workspace.

### Q: What if I make a mistake?

**A**: Don't worry! You can always:
- Start over with a fresh copy of the files
- Ask the AI for help fixing issues
- Check the main README.md for more detailed information

### Q: Do I need to understand all the technical details?

**A**: No! This simple setup is all you need. The technical details in README.md are optional and for advanced users.

### Q: Can I use this with multiple projects?

**A**: Yes! Each project can have its own `AGENTS.md`, but they can all share the same memory folder. The AI will organize memories by project automatically. Both the Memory System and Critical Thinking System will work across all your projects.

### Q: What is the Critical Thinking System?

**A**: The Critical Thinking System helps your AI assistant:
- Verify facts before stating them (prevents mistakes)
- Be more careful with important things (like security or money)
- Be flexible with simple tasks (like prototyping)
- Think through problems more carefully

It works automatically - you don't need to do anything special! The AI will adjust its behavior based on how important the task is.

---

## Need Help?

If you get stuck:
1. Check the main `README.md` file for more detailed instructions
2. Ask your AI assistant for help (it should be able to guide you)
3. Make sure all steps were completed correctly

---

## What's Next?

Once set up, you can:
- Start using your AI assistant - both systems will work automatically
- Ask the AI to remember specific things about your project (Memory System)
- The AI will automatically verify facts and think carefully when needed (Critical Thinking System)
- Review what the AI has learned by browsing your memory folder
- Customize settings in `AGENTS.md` (advanced)

**Remember**: Both systems are designed to work automatically. You don't need to do anything special - just use your AI assistant normally! The AI will use memory when helpful and think critically when important.

---

## ⚠️ Important Notes

### Configuration Template

**This entire repository is a configuration template**. Agents will NOT automatically create, copy, or reconstruct any part of the agents-md project structure. You must configure systems first (e.g., `MEMORY_PATH` in `AGENTS.md`), then explicitly request initialization.

### Agent Permissions

**Before the systems work**, you need to give your AI assistant permission to execute file commands.

### What Commands Are Needed?

The AI assistant needs to run safe commands to create and manage memory files:
- `mkdir` - Create folders for memory
- `touch` - Create files
- `cat`, `head`, `grep` - Read memory files
- `echo`, `printf` - Write to memory files
- `cp`, `mv`, `ls` - Organize memory files

### How to Grant Permissions

**In Cursor**:
1. Go to Settings (gear icon)
2. Find "Agent" or "AI" settings
3. Look for "Command Execution" or similar
4. Add the commands above to allowed commands
5. Or click "Allow" when the AI asks for permission

**In VS Code**:
- Check your AI assistant extension settings
- Look for command execution permissions

**Antivirus Software**:
- Some antivirus programs block these operations
- Add your project folder as an exception
- Allow file operations from your editor

### Why Is This Needed?

- **Security**: Editors prevent running commands to keep you safe
- **File Access**: Memory files are stored outside your project
- **Safe Operations**: These commands only work with files - they can't install software or access the internet

**Don't worry**: These are just file operations. The AI can't run dangerous commands - only safe file reading/writing.

**Note**: The Critical Thinking System doesn't need special permissions - it works automatically through the `AGENTS.md` configuration.

<!-- #setup-guide #non-technical #beginners #memory-system #critical-thinking #ai-assistants #cursor #vscode #workspace-setup -->

