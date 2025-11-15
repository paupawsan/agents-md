<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Safe Command Usage for Memory Operations

**IMPORTANT**: This document specifies safe commands agents can use for memory operations. Agents MUST NOT use harmful or dangerous commands. All memory operations should use only safe file system commands.

## ⚠️ Command Safety Rules

### NEVER Use These Commands
- ❌ `rm`, `del`, `rmdir` - Can delete files/folders
- ❌ `sudo`, `su`, `runas` - Privilege escalation
- ❌ `curl`, `wget`, `git clone` - Network operations
- ❌ `npm`, `pip`, `gem`, `apt`, `brew` - Package managers
- ❌ `ssh`, `scp`, `ftp` - Network/remote operations
- ❌ `chmod`, `chown` - Permission changes
- ❌ `kill`, `pkill`, `taskkill` - Process management
- ❌ `mount`, `umount`, `fsck` - Filesystem operations
- ❌ `dd`, `mkfs` - Low-level disk operations
- ❌ `passwd`, `useradd`, `usermod` - User management
- ❌ Any command with `>` or `|` that could redirect to system files

### ONLY Use These Safe Commands

#### File/Directory Creation
```bash
# Create directories (safe)
mkdir -p /path/to/memory/dir
mkdir /path/to/memory/dir

# Create empty files (safe)
touch /path/to/memory/file.md
```

#### File Reading
```bash
# Read file contents (safe)
cat /path/to/memory/file.md
head -20 /path/to/memory/file.md
tail -20 /path/to/memory/file.md

# Search within files (safe)
grep "pattern" /path/to/memory/file.md
grep -r "pattern" /path/to/memory/directory/
grep -i "Pattern" /path/to/memory/file.md
```

#### File Writing
```bash
# Write to files (safe - only to memory directory)
echo "content" > /path/to/memory/file.md
echo "content" >> /path/to/memory/file.md
printf "content" > /path/to/memory/file.md

# Use here documents for multi-line content (safe)
cat > /path/to/memory/file.md << 'EOF'
# Title
Content here
EOF
```

#### File Operations (Within Memory Directory Only)
```bash
# Copy files (safe - only within memory directory)
cp /path/to/memory/source.md /path/to/memory/dest.md

# Move/rename files (safe - only within memory directory)
mv /path/to/memory/old.md /path/to/memory/new.md

# List directory contents (safe)
ls /path/to/memory/directory/
ls -la /path/to/memory/directory/
```

#### Text Processing (Safe)
```bash
# Count lines (safe)
wc -l /path/to/memory/file.md

# Sort lines (safe)
sort /path/to/memory/file.md

# Remove duplicate lines (safe)
uniq /path/to/memory/file.md
```

#### Git Repository Information (Safe - Read-Only)
```bash
# Get current git status (safe - informational only)
git status

# Get recent commits (safe - read repository history)
git log --oneline -10
git log --oneline --since="1 week ago"
git log --oneline --author="username"

# Get commit details (safe)
git show HEAD
git show <commit-hash>

# List branches and tags (safe)
git branch -a
git tag

# Get file history (safe)
git log --oneline -- <filepath>
git blame <filepath>

# Get repository information (safe)
git remote -v
git config --list

# Check differences (safe - read-only)
git diff HEAD~1
git diff --name-only HEAD~1
git diff --stat HEAD~1

# Get commit statistics (safe)
git shortlog -sn --since="1 month ago"
```

#### Date and Time Commands (Safe)
```bash
# Get current date/time (safe - informational)
date
date '+%Y-%m-%d'
date '+%Y-%m-%d %H:%M:%S'
date '+%Y-%m-%dT%H:%M:%S%z'

# Get Unix timestamp (safe)
date +%s

# Format dates (safe)
date -d "2024-01-01" +%A  # Get day of week
date -d "1 day ago"       # Relative dates
```

## 🔍 Platform-Specific Safe Commands

### macOS
```bash
# Additional safe commands available on macOS
# Use standard Unix commands above
# Avoid macOS-specific commands unless necessary
```

### Linux
```bash
# Additional safe commands available on Linux
# Use standard Unix commands above
# Avoid system administration commands
```

### Windows (PowerShell/Command Prompt)
```bash
# Directory operations
mkdir "C:\path\to\memory\dir"
md "C:\path\to\memory\dir"

# File operations
type "C:\path\to\memory\file.md"
copy "C:\path\to\memory\source.md" "C:\path\to\memory\dest.md"
move "C:\path\to\memory\old.md" "C:\path\to\memory\new.md"
dir "C:\path\to\memory\directory\"

# Text operations (if available)
findstr "pattern" "C:\path\to\memory\file.md"
```

## 📋 Command Validation Rules

### Path Validation
- ✅ **ALLOWED**: All paths must be within the configured memory directory
- ✅ **ALLOWED**: Subdirectories of memory directory
- ✅ **FORBIDDEN**: Paths outside memory directory
- ✅ **FORBIDDEN**: System directories (`/etc`, `/usr`, `/bin`, etc.)
- ✅ **FORBIDDEN**: User home directory files (except memory folder)
- ✅ **FORBIDDEN**: Any path containing `..` (parent directory traversal)

### Content Validation
- ✅ **ALLOWED**: Plain text content only
- ✅ **ALLOWED**: Markdown formatting
- ✅ **FORBIDDEN**: HTML, JavaScript, or executable code
- ✅ **FORBIDDEN**: Commands or scripts
- ✅ **FORBIDDEN**: URLs or external references (except documentation)

### Operation Validation
- ✅ **ALLOWED**: Read operations on any memory file
- ✅ **ALLOWED**: Write operations only to memory directory
- ✅ **FORBIDDEN**: Write operations to any non-memory location
- ✅ **FORBIDDEN**: Operations that could affect system files

## 🔧 Command Examples for Memory Operations

### Creating Memory Structure
```bash
# Create memory directories (safe)
mkdir -p "/Users/user/Documents/my-memory/project-name/topic"
mkdir -p "/Users/user/Documents/my-memory/project-name/session/2025-01"
mkdir -p "/Users/user/Documents/my-memory/common"

# Create index files (safe)
touch "/Users/user/Documents/my-memory/project-name/memories.json"
touch "/Users/user/Documents/my-memory/common/preferences.md"
```

### Writing Memory Content
```bash
# Write project context (safe)
cat > "/Users/user/Documents/my-memory/project-name/context.md" << 'EOF'
# Project Context

## Architecture
- Framework: React
- Language: TypeScript
- Database: PostgreSQL

## Key Decisions
- State management: Redux
- Styling: CSS Modules
EOF

# Append to existing file (safe)
echo "## Recent Changes" >> "/Users/user/Documents/my-memory/project-name/context.md"
echo "- Added authentication system" >> "/Users/user/Documents/my-memory/project-name/context.md"
```

### Reading Memory Content
```bash
# Search for specific patterns (safe)
grep -r "authentication" "/Users/user/Documents/my-memory/project-name/"

# Read specific file (safe)
cat "/Users/user/Documents/my-memory/project-name/context.md"

# Check file existence and size (safe)
ls -la "/Users/user/Documents/my-memory/project-name/"
```

### Organizing Memory Files
```bash
# Move completed session to archive (safe)
mv "/Users/user/Documents/my-memory/project-name/session/2025-01-15_active.md" \
   "/Users/user/Documents/my-memory/project-name/session/2025-01/2025-01-15_completed.md"

# Copy important pattern to common (safe)
cp "/Users/user/Documents/my-memory/project-name/topic/error-handling.md" \
   "/Users/user/Documents/my-memory/common/patterns/error-handling.md"
```

### Constructing Memory from Git History
```bash
# Get recent project changes for memory (safe)
git log --oneline --since="1 week ago" > "/tmp/git_recent.txt" && cat "/tmp/git_recent.txt"

# Get commit details for context (safe)
git show HEAD --stat > "/tmp/git_details.txt" && cat "/tmp/git_details.txt"

# Check what files changed recently (safe)
git log --name-only --oneline -5 > "/tmp/git_files.txt" && cat "/tmp/git_files.txt"
```

### Timestamping Memory Entries
```bash
# Create timestamped memory entry (safe)
current_date=$(date '+%Y-%m-%d')
current_time=$(date '+%H:%M:%S')

cat > "/Users/user/Documents/my-memory/project-name/session/${current_date}_notes.md" << EOF
# Session Notes - ${current_date} ${current_time}

## Today's Work
-


## Key Decisions
-


## Next Steps
-

EOF
```

### Analyzing Project History
```bash
# Get author contributions (safe)
git shortlog -sn --since="1 month ago" > "/tmp/git_authors.txt" && cat "/tmp/git_authors.txt"

# Find when a feature was introduced (safe)
git log --oneline --grep="feature" --since="3 months ago" > "/tmp/git_features.txt" && cat "/tmp/git_features.txt"
```

## 🚨 Emergency Rules

### If Command Fails
- **STOP** immediately
- **DO NOT** retry with different commands
- **REPORT** the failure to user
- **ASK** for alternative approach

### If Path Is Invalid
- **VALIDATE** all paths before use
- **ENSURE** all operations are within memory directory
- **NEVER** operate outside configured memory path

### If Content Is Suspicious
- **FILTER** all content for safety
- **REMOVE** any potentially harmful text
- **ONLY** write plain text and markdown

## 📚 Reference

See [organization.md](organization.md) for memory organization rules.
See [platform.md](platform.md) for platform-specific path examples.
See [rag.md](rag.md) for retrieval strategies that minimize command usage.
