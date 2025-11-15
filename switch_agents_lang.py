#!/usr/bin/env python3
"""
Language switcher for AGENTS.md
Switches between English (AGENTS.md.en) and Japanese (AGENTS.md.ja) versions.

The script automatically preserves configured {MEMORY_PATH} when switching languages.
If {MEMORY_PATH} cannot be detected, you'll need to run setup_memory_dir.py after switching.

Usage:
    python3 switch_agents_lang.py en    # Switch to English
    python3 switch_agents_lang.py ja    # Switch to Japanese
    python3 switch_agents_lang.py        # Show current language
"""

import sys
import os
import shutil
from pathlib import Path

AGENTS_EN = "AGENTS.md.en"
AGENTS_JA = "AGENTS.md.ja"
AGENTS_TARGET = "AGENTS.md"
AGENTS_BACKUP = "AGENTS.md.backup"

def get_current_language():
    """Detect current language by checking if AGENTS.md exists and reading first few lines."""
    if not os.path.exists(AGENTS_TARGET):
        return None
    
    try:
        with open(AGENTS_TARGET, 'r', encoding='utf-8') as f:
            first_lines = ''.join(f.readlines()[:10])
            # Check for Japanese characters or English keywords
            if '# Memory System Guidelines' in first_lines:
                return 'en'
            elif '# メモリシステムガイドライン' in first_lines:
                return 'ja'
    except Exception:
        pass
    
    return 'unknown'

def extract_memory_path(content):
    """Extract configured MEMORY_PATH from content if it exists."""
    import re
    
    # If placeholder still exists, it's not configured
    if '{MEMORY_PATH}' in content:
        return None
    
    # Look for configured paths in common patterns
    # Pattern 1: Lines like "Root: /path/to/memory" or "Root: `{MEMORY_PATH}`"
    # Pattern 2: Lines with memory path references
    lines = content.split('\n')
    for line in lines:
        # Look for lines mentioning memory path
        if 'MEMORY_PATH' in line or ('memory' in line.lower() and ('root' in line.lower() or 'path' in line.lower())):
            # Try to extract absolute path (starts with / or ~ or drive letter)
            # Match paths that don't contain {MEMORY_PATH} placeholder
            patterns = [
                r'Root:\s*[`"]?([~/]?[/\\][^\s`"\)]+memory[^\s`"\)]*)',  # Root: /path/to/memory
                r'`([~/]?[/\\][^\s`]+memory[^\s`]+)`',  # `/path/to/memory`
                r'([~/]?[/\\][^\s\)]+memory[^\s\)]+)',  # /path/to/memory
            ]
            for pattern in patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                for match in matches:
                    if match and '{MEMORY_PATH}' not in match:
                        # Clean up the path
                        path = match.strip('`"\'')
                        if path and ('/' in path or '\\' in path or path.startswith('~')):
                            return path
    
    return None

def switch_to_language(target_lang):
    """Switch AGENTS.md to the specified language."""
    if target_lang not in ['en', 'ja']:
        print(f"Error: Invalid language '{target_lang}'. Use 'en' or 'ja'.")
        return False
    
    source_file = AGENTS_JA if target_lang == 'ja' else AGENTS_EN
    target_file = AGENTS_TARGET
    
    # Check if source file exists
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' not found.")
        print(f"  Expected: {source_file}")
        return False
    
    # Extract configured MEMORY_PATH from current AGENTS.md if it exists
    configured_path = None
    if os.path.exists(target_file):
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                current_content = f.read()
            configured_path = extract_memory_path(current_content)
            
            current_lang = get_current_language()
            if current_lang and current_lang != target_lang:
                print(f"Backing up current {target_file} (detected: {current_lang})...")
                shutil.copy2(target_file, AGENTS_BACKUP)
        except Exception as e:
            print(f"Warning: Could not read current {target_file}: {e}")
    
    # Read source template
    with open(source_file, 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    # If we have a configured path, replace the placeholder in the new template
    if configured_path:
        placeholder_count = new_content.count('{MEMORY_PATH}')
        if placeholder_count > 0:
            new_content = new_content.replace('{MEMORY_PATH}', configured_path)
            print(f"Switching to {target_lang.upper()}...")
            print(f"✓ Preserved configured MEMORY_PATH: {configured_path}")
            print(f"  Replaced {placeholder_count} placeholder(s)")
        else:
            print(f"Switching to {target_lang.upper()}...")
            print(f"  Note: No {{MEMORY_PATH}} placeholder found in template")
    else:
        print(f"Switching to {target_lang.upper()}...")
        print(f"  Note: {{MEMORY_PATH}} placeholder found - you'll need to configure it")
        print(f"  Run: python3 setup_memory_dir.py")
    
    # Write new content
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Successfully switched to {target_lang.upper()}")
    print(f"  Current file: {target_file}")
    if os.path.exists(AGENTS_BACKUP):
        print(f"  Backup saved: {AGENTS_BACKUP}")
    
    if not configured_path:
        print(f"\n⚠️  Important: Remember to configure MEMORY_PATH!")
        print(f"  Run: python3 setup_memory_dir.py")
    
    return True

def main():
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    if len(sys.argv) < 2:
        # Show current language
        current = get_current_language()
        if current:
            print(f"Current language: {current.upper()}")
        else:
            print(f"{AGENTS_TARGET} not found or language cannot be detected.")
        print(f"\nUsage:")
        print(f"  python3 {sys.argv[0]} en    # Switch to English")
        print(f"  python3 {sys.argv[0]} ja    # Switch to Japanese")
        return
    
    target_lang = sys.argv[1].lower()
    switch_to_language(target_lang)

if __name__ == "__main__":
    main()

