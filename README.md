<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# agents-md

A collection of systems and tools for AI coding agents, built from real-world work experience. Currently includes a robust Memory System and Critical Thinking framework, with more systems planned for the future.

**日本語マニュアル**: [README.ja.md](README.ja.md) - 日本語版のドキュメントはこちら

## 🚀 Quick Start

**New to this?** → **[Simple Setup Guide](docs/simple-setup.md)** - Step-by-step guide for non-technical users

**Prefer visual guides?** → **[Visual Installation Guide](docs/installation-guide-visual-en.md)** - Step-by-step visual guide with images

**Experienced developer?** → See **[Setup Guide](docs/setup-guide.md)**

### What You'll Need

1. **Download** the repository (ZIP download or `git clone`)
2. **Run setup script**: `python setup.py` (Windows) or `python3 setup.py` (macOS/Linux)
   - Select your language (English/Japanese)
   - Configure memory path
3. **Add** the memory folder to your Cursor/VS Code workspace
4. **Copy** `AGENTS.md` and `GEMINI.md` to your project (or add agents-md folder to workspace)
5. **Initialize** memory with: `"initialize memory for this project"`

**That's it!** Your AI agent will now automatically remember project patterns, preferences, and decisions.

**💡 Tip**: The setup script supports both `AGENTS.md` (for Cursor) and `GEMINI.md` (for Google Antigravity) - both files are created automatically!

**⚠️ Important**: This entire repository is a **configuration template**. Agents will NOT automatically create, copy, or reconstruct any part of the agents-md project structure (including memory system, documentation, or `_agents-md/` directory). You must configure systems first (e.g., `MEMORY_PATH` in `AGENTS.md`), then explicitly request initialization.

## 🧠 Memory System

A robust, RAG-optimized memory management system with multi-platform support.

### Key Features
- **Advanced RAG Support**: Intelligent semantic search with 80-95% token reduction
- **Multi-Platform**: Native support for macOS, Linux, and Windows
- **Privacy-Focused**: Local storage with human-readable markdown files
- **Agentic AI Optimized**: Designed for advanced AI models that can perform semantic search

### Workflow Options
- **Structured Workflow**: Full memory system with topics, sessions, and indexing (best for complex projects)
- **Simple Workflow**: Single-file templates for quick daily logging (best for vibecoding)

### Why Local Markdown Files?

- ✅ **Full Transparency**: Human-readable files you can edit with any text editor
- ✅ **No Dependencies**: No databases, APIs, or external services required
- ✅ **Version Control Friendly**: Works perfectly with Git
- ✅ **Complete Control**: Your memory stays on your machine
- ✅ **Easy Backup**: Just copy the directory

### Model Compatibility

⚠️ **Requires agentic-capable models** (Claude Sonnet/Opus, GPT-4, etc.) that can:
- Understand complex instructions
- Perform semantic search and retrieval
- Make intelligent decisions about memory loading
- Execute multi-step workflows autonomously

## 🧠 Critical Thinking System

A comprehensive framework for evidence-based reasoning, fact verification, and intelligent decision-making.

### Key Features
- **Context-Aware Strictness**: Adjusts verification level based on risk and context (security-critical vs prototyping)
- **Evidence-Based Reasoning**: Decisions backed by verification, not assumptions
- **Hallucination Prevention**: Structured verification protocols to avoid false information
- **Respectful Disagreement**: Constructive challenge of assumptions when appropriate

### Core Capabilities
- **Fact Verification**: Ground checking and verification workflows
- **Multi-Perspective Analysis**: Considers technical, human, and business factors
- **Risk Assessment**: Appropriate strictness for high-risk vs low-risk scenarios
- **Communication Adaptation**: Adjusts style for expert vs non-technical audiences

### When It Activates
- **High-Risk Scenarios**: Banking apps, healthcare systems, production database changes → Maximum verification
- **Low-Risk Scenarios**: Prototyping, debugging, documentation → Flexible and collaborative
- **Uncertain Situations**: When facts need verification or assumptions should be challenged

## 📚 Documentation

### Setup & Usage
- **[Visual Installation Guide](docs/installation-guide-visual-en.md)** - Step-by-step visual guide with images (recommended for beginners)
- **[Setup Guide](docs/setup-guide.md)** - Complete technical setup instructions
- **[Usage Guide](docs/usage-guide.md)** - How to use the memory system effectively
- **[Simple Setup Guide](docs/simple-setup.md)** - Plain language setup guide for non-technical users

### Testing & Validation
- **[Memory System Testing](docs/memory-system-testing/)** - Testing strategies and practical test scenarios
- **[Critical Thinking Testing](docs/critical-thinking-testing/)** - Testing the critical thinking implementation

### Detailed Documentation
- **[_agents-md/memory/](_agents-md/memory/)** - Complete memory system documentation
- **[_agents-md/critical-thinking/](_agents-md/critical-thinking/)** - Critical thinking framework documentation
- **[templates/](templates/)** - Workflow templates and guidance

## 🔧 Development & Testing

### Testing the Systems
```bash
# Test memory system functionality
# See docs/memory-system-testing/ for comprehensive testing guides

# Test critical thinking implementation
# See docs/critical-thinking-testing/ for validation procedures
```

### Contributing
This is a personal project, but suggestions and improvements are welcome. Please ensure any contributions maintain the MIT license and attribution.

## 📈 Project Roadmap

**agents-md** is an evolving collection of systems. Potential future additions may include:

- Additional systems based on real-world work experience
- Integration patterns between existing systems
- Best practices and workflow improvements

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

The Memory System was inspired by an earlier memory system design created and developed during my daily work. The foundational concepts and architectural patterns were refined and adapted for this open-source implementation.

<!-- #agents-md #memory-system #critical-thinking #ai-assistants #rag #retrieval-augmented-generation #cursor #vscode #workflow-automation -->