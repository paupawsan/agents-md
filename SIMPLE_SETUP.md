# Simple Setup Guide - For Non-Technical Users

**Don't worry if you're not a programmer!** This guide will walk you through setting up the memory system step by step, using simple language and avoiding technical jargon.

## What Is This?

This is a **memory system** for AI coding assistants (like Cursor). It helps your AI assistant remember things about your projects, so it can work better with you over time.

**Think of it like**: A notebook where your AI assistant writes down what it learns about your projects, so it doesn't forget.

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

**Option A: If you downloaded this as a folder**
- You already have the files! Just find where you saved the `agents-md` folder.

**Option B: If you're using Git (for developers)**
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

### Step 3: Set Up the AGENTS.md File

This is the main file that tells your AI assistant how to use memory.

#### 3a. Open AGENTS.md

1. Open the `agents-md` folder
2. Find the file called `AGENTS.md.en` (for English) or `AGENTS.md.ja` (for Japanese)
3. Right-click and choose "Open with" → your text editor (Cursor, VS Code, or even Notepad/TextEdit)

#### 3b. Choose Your Language

**For English**:
- You'll use `AGENTS.md.en` as your template

**For Japanese**:
- You'll use `AGENTS.md.ja` as your template

#### 3c. Copy the Template

1. Open the template file (`AGENTS.md.en` or `AGENTS.md.ja`)
2. Select all text (`Cmd+A` on Mac, `Ctrl+A` on Windows/Linux)
3. Copy it (`Cmd+C` or `Ctrl+C`)
4. Create a new file called `AGENTS.md` in the same folder
5. Paste the content (`Cmd+V` or `Ctrl+V`)
6. Save the file

**What you just did**: You created your own `AGENTS.md` file from the template.

#### 3d. Replace the Placeholder

Now you need to replace `{MEMORY_DIR}` with the name you chose in Step 2.

1. In your `AGENTS.md` file, press `Cmd+F` (Mac) or `Ctrl+F` (Windows/Linux) to open Find
2. Type `{MEMORY_DIR}` in the search box
3. Click "Replace" or "Replace All"
4. Type your chosen name (e.g., `my-memory`)
5. Click "Replace All"
6. Save the file

**Example**: If you chose `my-memory`, every `{MEMORY_DIR}` becomes `my-memory`

---

### Step 4: Copy Files to Your Project

Now you need to copy two things to your project folder (the project where you want to use the memory system).

#### What to Copy:

1. **The `_agents-md` folder** - This contains instructions for the AI
2. **The `AGENTS.md` file** - This is the file you just created

#### How to Copy:

**On Mac**:
1. Open Finder
2. Navigate to your `agents-md` folder
3. Copy the `_agents-md` folder (right-click → Copy)
4. Copy the `AGENTS.md` file (right-click → Copy)
5. Navigate to your project folder
6. Paste both items (right-click → Paste)

**On Windows**:
1. Open File Explorer
2. Navigate to your `agents-md` folder
3. Copy the `_agents-md` folder (right-click → Copy)
4. Copy the `AGENTS.md` file (right-click → Copy)
5. Navigate to your project folder
6. Paste both items (right-click → Paste)

**On Linux**:
1. Open your file manager
2. Navigate to your `agents-md` folder
3. Copy the `_agents-md` folder and `AGENTS.md` file
4. Navigate to your project folder
5. Paste both items

**Important**: If your project already has an `AGENTS.md` file, don't replace it! Instead, open both files and copy the content from the new `AGENTS.md` to the end of your existing file.

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
2. Look for a section that says something like "Platform Detection" or has paths like `~/Documents/`
3. Find the path that matches your operating system (Mac/Windows/Linux)
4. Replace the example path with your actual memory folder path

**Example**: If you created `my-memory` in Documents on Mac, the path should be:
```
~/Documents/my-memory
```

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

Your memory system is now set up! The AI assistant will automatically:
- Remember things about your project
- Learn from your preferences
- Store important patterns and solutions

---

## Common Questions

### Q: Do I need to do anything else?

**A**: No! Once set up, the memory system works automatically. The AI will save and retrieve memories as needed.

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

**A**: Yes! Each project can have its own `AGENTS.md`, but they can all share the same memory folder. The AI will organize memories by project automatically.

---

## Need Help?

If you get stuck:
1. Check the main `README.md` file for more detailed instructions
2. Ask your AI assistant for help (it should be able to guide you)
3. Make sure all steps were completed correctly

---

## What's Next?

Once set up, you can:
- Start using your AI assistant - it will automatically use memory
- Ask the AI to remember specific things about your project
- Review what the AI has learned by browsing your memory folder
- Customize settings in `AGENTS.md` (advanced)

**Remember**: The memory system is designed to work automatically. You don't need to do anything special - just use your AI assistant normally!

