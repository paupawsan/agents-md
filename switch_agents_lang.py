#!/usr/bin/env python3
"""
Language switcher for AGENTS.md
Switches between English (AGENTS.md) and Japanese (AGENTS.md.ja) versions.

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
    
    # Backup current AGENTS.md if it exists and is different
    if os.path.exists(target_file):
        current_lang = get_current_language()
        if current_lang and current_lang != target_lang:
            print(f"Backing up current {target_file} (detected: {current_lang})...")
            shutil.copy2(target_file, AGENTS_BACKUP)
    
    # Copy source to target
    print(f"Switching to {target_lang.upper()}...")
    shutil.copy2(source_file, target_file)
    
    print(f"✓ Successfully switched to {target_lang.upper()}")
    print(f"  Current file: {target_file}")
    if os.path.exists(AGENTS_BACKUP):
        print(f"  Backup saved: {AGENTS_BACKUP}")
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

