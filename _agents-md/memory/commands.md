<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Safe Command Usage for Memory Operations

**CRITICAL**: Agents MUST use only safe commands for memory operations. Never use harmful commands that could delete files, access networks, or modify system settings.

## 🚫 Forbidden Commands
- `rm`, `del`, `rmdir`, `sudo`, `su`, `runas` - File deletion/modification
- `curl`, `wget`, `git clone/push/pull` - Network operations
- `npm`, `pip`, `apt`, `brew` - Package managers
- `chmod`, `chown`, `kill`, `mount` - System operations
- Any command redirecting to system files

## ✅ Safe Commands Only

### File/Directory Operations
```bash
mkdir -p /path/to/memory/dir    # Create directories
touch /path/to/memory/file.md   # Create empty files
ls /path/to/memory/dir          # List contents
ls -la /path/to/memory/dir      # Detailed listing
```

### File Reading
```bash
cat /path/to/memory/file.md        # Read file
head -20 /path/to/memory/file.md   # First 20 lines
tail -20 /path/to/memory/file.md   # Last 20 lines
grep "pattern" /path/to/memory/file.md    # Search in file
grep -r "pattern" /path/to/memory/dir     # Recursive search
```

### File Writing (Memory Directory Only)
```bash
echo "content" > /path/to/memory/file.md   # Overwrite
echo "content" >> /path/to/memory/file.md  # Append
printf "content" > /path/to/memory/file.md # Formatted write

# Multi-line content (safe)
cat > /path/to/memory/file.md << 'EOF'
# Title
Content here
EOF
```

### File Management (Within Memory Only)
```bash
cp /src/memory/file.md /dest/memory/file.md  # Copy
mv /src/memory/old.md /dest/memory/new.md    # Move/rename
```

### Text Processing
```bash
wc -l /path/to/memory/file.md     # Count lines
sort /path/to/memory/file.md      # Sort lines
uniq /path/to/memory/file.md      # Remove duplicates
```

### Git Commands (Read-Only)
```bash
git status                    # Repository status
git log --oneline -10         # Recent commits
git log --since="1 week ago"  # Commits by time
git show HEAD                 # Latest commit details
git diff HEAD~1               # Changes in last commit
git shortlog -sn --since="1 month ago"  # Author stats
```

### Date/Time Commands
```bash
date                          # Current date/time
date '+%Y-%m-%d'             # Date only
date '+%Y-%m-%d %H:%M:%S'    # Date and time
date +%s                     # Unix timestamp
```

## 🔍 Platform-Specific Commands

### Windows (PowerShell/Command Prompt)
```bash
mkdir "C:\path\to\memory\dir"           # Create directory
type "C:\path\to\memory\file.md"        # Read file
copy "C:\src\memory\a.md" "C:\dest\memory\b.md"  # Copy
move "C:\old\memory\a.md" "C:\new\memory\b.md"   # Move
dir "C:\path\to\memory\"                # List directory
findstr "pattern" "C:\path\to\memory\file.md"    # Search
```

## 📋 Validation Rules

### Paths
- ✅ **ALLOWED**: Within configured memory directory only
- ❌ **FORBIDDEN**: Outside memory directory, system dirs, `..` traversal

### Content
- ✅ **ALLOWED**: Plain text, Markdown
- ❌ **FORBIDDEN**: HTML, JS, executables, URLs, commands

### Operations
- ✅ **ALLOWED**: Read any memory file, write to memory directory only
- ❌ **FORBIDDEN**: Write outside memory, system file operations

## 🔧 Memory Construction Examples

### Directory Structure
```bash
mkdir -p "/path/to/memory/project-name/topic"
mkdir -p "/path/to/memory/common"
touch "/path/to/memory/project-name/memories.json"
```

### Content Creation
```bash
# Write project context
cat > "/path/to/memory/project-name/context.md" << 'EOF'
# Project Context
- Framework: React
- Database: PostgreSQL
EOF

# Append updates
echo "## Recent Changes" >> "/path/to/memory/project-name/context.md"
```

### Git-Based Memory
```bash
git log --oneline --since="1 week ago" > "/tmp/recent.txt" && cat "/tmp/recent.txt"
git show HEAD --stat > "/tmp/details.txt" && cat "/tmp/details.txt"
```

### Timestamped Entries
```bash
current_date=$(date '+%Y-%m-%d')
cat > "/path/to/memory/session/${current_date}_notes.md" << EOF
# Session Notes - ${current_date}
## Today's Work
-
EOF
```

## 🚨 Safety Rules

- **Command fails**: STOP immediately, report to user, ask for alternative
- **Invalid paths**: Validate all paths, ensure within memory directory only
- **Suspicious content**: Filter for safety, write plain text/markdown only

## 📚 References
- [organization.md](organization.md) - Memory organization rules
- [platform.md](platform.md) - Platform-specific paths
- [rag.md](rag.md) - Retrieval strategies

---

<!-- #commands #safety #file-operations #git-commands #memory-system #agent-guidelines -->
