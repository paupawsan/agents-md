<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# agents-md Installation Guide (Visual)

**Simple. Fast. Effective.** Get started with agents-md in 5 easy steps.

---

## Step 1: Download 📥

Download the repository using either method:

![Step 1: Download agents-md](images/installation-step-1-download.png)

**Choose one:**
- Download ZIP from GitHub
- Or use: `git clone https://github.com/...`

---

## Step 2: Run Setup Script ⚙️

Run the setup script and configure your settings:

![Step 2: Run Setup Script](images/installation-step-2-setup.png)

**Command:**
- macOS/Linux: `python3 setup.py`
- Windows: `python setup.py`

**Configure:**
- Select language (English/Japanese)
- Set your memory path

---

## Step 3: Add to Workspace 📁

Add the memory folder to your Cursor/VS Code workspace:

![Step 3: Add Memory Folder to Workspace](images/installation-step-3-workspace.png)

**Simple way:** Drag and drop the memory folder into your workspace sidebar.

**💡 Best Practice (if your workspace system allows it):** Use an external `agentic-system` folder structure for better organization. This keeps memory separate from your project code and allows one folder to serve all your projects. See the [Recommended Folder Structure](#-recommended-folder-structure) section below for details.

---

## Step 4: Copy Configuration Files 📋

Copy the configuration files to your project:

![Step 4: Copy Configuration Files](images/installation-step-4-copy-files.png)

**Copy both files:**
- `AGENTS.md` (for Cursor)
- `GEMINI.md` (for Google Antigravity)

---

## Step 5: Initialize Memory 🚀

Initialize memory in your AI assistant:

![Step 5: Initialize Memory](images/installation-step-5-initialize.png)

**Type in your AI chat:**
```
initialize memory for this project
```

**Done!** Your AI agent will now remember project patterns, preferences, and decisions.

---

## Best Practices

### ❌ Avoid: Mixed Structure

![Before: Mixed Structure](images/best-practice-before-mixed.png)

**Problem:** Code and memory files mixed together makes projects messy and hard to manage.

---

### ✅ Recommended: Clean Separation

![After: Clean Separation](images/best-practice-after-separation.png)

**Solution:** Use an external `agentic-system` folder to keep memory separate from your code.

**Benefits:**
- 🔄 **Reusable** - One folder serves all projects
- 📤 **Shareable** - Easy to include in any workspace
- ✨ **Clean** - Code stays separate from memory

---

### 📋 Memory Organization

![Memory Organization Structure](images/best-practice-memory-organization.png)

Each project's memory is organized into:
- **context/** - Quick reference (overview, status, architecture, files)
- **topic/** - Knowledge files (patterns, decisions, research)
- **session/** - Work session archives
- **memories.json** - Machine-readable index

---

### 📂 Recommended Folder Structure

![Recommended Folder Structure](images/best-practice-folder-structure.png)

```
Your Workspace:
├── CurrentProject/          ← Your project code
│   ├── app.py
│   ├── README.md
│   └── ...
│
└── agentic-system/          ← External, shared
    ├── agent-memory/
    │   ├── common/          ← Shared patterns
    │   ├── [CurrentProject]/ ← This project's memory
    │   └── [OtherProjects]/ ← Other projects' memory
    │
    └── agents-md/           ← Configuration templates
        ├── AGENTS.md
        └── ...
```

**One `agentic-system` folder serves all your projects!**

---

## Key Features

### 🧠 Advanced RAG Support

![Advanced RAG Support](images/feature-rag-support.png)

**80-95% Token Reduction** through intelligent semantic search.

---

### 💻 Multi-Platform Support

![Multi-Platform Support](images/feature-multi-platform.png)

Works on **macOS, Linux, and Windows**.

---

### 🔒 Privacy-Focused & Local

![Privacy-Focused & Local](images/feature-privacy.png)

- ✅ Full transparency
- ✅ Complete control
- ✅ Easy backup
- ✅ No external services

---

## That's It!

You're all set! Your AI agent will now automatically remember and learn from your project patterns.

**Need help?** Check out the [full documentation](../README.md).

