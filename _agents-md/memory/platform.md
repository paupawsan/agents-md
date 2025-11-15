# Platform Support

Platform-specific paths and tools.

## Memory Paths

**Path Configuration**: Users configure `{MEMORY_PATH}` via setup script or manual replacement.

**Common Path Examples** (users choose their own):
- **macOS**: `~/Documents/my-memory` or `/Users/username/Documents/my-memory`
- **Linux**: `~/Documents/my-memory` or `/home/username/Documents/my-memory`
- **Windows**: `C:\Users\username\Documents\my-memory`

**Agent Behavior**: Agent uses configured `{MEMORY_PATH}` directly as the memory root folder. No platform detection or path construction needed.

## Detection

**macOS/Linux**: `uname -s` → `Darwin` or `Linux`
**Windows**: `$env:OS` → `Windows_NT`

## Date Commands

**macOS/Linux**: `date '+%Y-%m-%dT%H:%M:%S%z'`
**Windows**: `powershell -Command "Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'"`

## Tools

**macOS**: `find`, `grep`, `mdfind` (Spotlight)
**Linux**: `find`, `grep`, `rg` (ripgrep), `locate`
**Windows**: PowerShell `Get-ChildItem`, `Select-String`, `findstr`

**Always use forward slashes** in paths (tools handle conversion).

