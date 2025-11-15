#!/usr/bin/env python3
# Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com
#
# Licensed under the MIT License. See LICENSE file for details.

"""
Setup script for configuring the memory system in agents-md.

This script helps configure the memory root path ({MEMORY_PATH} placeholder).

Features:
- Handles shell-escaped paths automatically (e.g., spaces, special characters)
- Expands ~ for home directory and environment variables
- Creates directories if they don't exist
- Cross-platform path handling

Usage:
    python3 setup_memory_dir.py

For non-engineers: Manual replacement is straightforward and recommended.
Simply open the AGENTS.md file and replace {MEMORY_PATH} with your full memory root path.
"""

import ast
import os
import sys
from pathlib import Path

def get_script_directory():
    """Get the directory where this script is located."""
    return Path(__file__).parent.absolute()

def decode_shell_escaped_string(s):
    """
    Decode basic shell-style escaped characters in paths.

    Mainly handles spaces that are escaped with backslash (\\ ),
    which is common in shell paths but not handled by os.path functions.
    """
    # If no backslashes, return as-is
    if '\\' not in s:
        return s

    # Handle the most common case: backslash followed by space
    # This converts "/path/My\ Drive/" to "/path/My Drive/"
    result = s.replace('\\ ', ' ')

    # Also handle double backslashes that might represent single backslashes
    # This is common in Windows paths
    result = result.replace('\\\\', '\\')

    return result

def find_agents_file():
    """Find AGENTS.md file."""
    script_dir = get_script_directory()
    agents_file = script_dir / "AGENTS.md"
    
    if not agents_file.exists():
        agents_file = script_dir / "AGENTS.md.wip"
        if not agents_file.exists():
            return None
    return agents_file

def get_memory_path():
    """Prompt user for memory root path."""
    print("\n" + "="*60)
    print("Memory Root Path Configuration")
    print("="*60)
    print("\nEnter the full path where you want to store your memory.")
    print("This will be the root folder for all memory (projects, common, private).")
    print("\nExamples:")
    print("  - ~/Documents/my-memory")
    print("  - /Users/username/Documents/my-memory")
    print("  - /Users/username/Library/CloudStorage/GoogleDrive-user@gmail.com/My Drive/AI/memory")
    print("  - C:\\Users\\username\\Documents\\my-memory (Windows)")
    print("\nNote: You can use ~ for home directory. Spaces and special characters are handled automatically.")
    print("No need to quote paths - just type them normally. The folder will be created if it doesn't exist.\n")
    
    while True:
        memory_path = input("Enter memory root path: ").strip()

        # Strip surrounding quotes if present (users might quote paths with spaces)
        if (memory_path.startswith('"') and memory_path.endswith('"')) or \
           (memory_path.startswith("'") and memory_path.endswith("'")):
            memory_path = memory_path[1:-1]

        if not memory_path:
            print("Error: Path cannot be empty.\n")
            continue

        # Decode shell-style escaped characters (like \ for spaces)
        memory_path = decode_shell_escaped_string(memory_path)

        # Expand user home directory and environment variables
        memory_path = os.path.expanduser(memory_path)
        memory_path = os.path.expandvars(memory_path)
        
        # Convert to absolute path
        memory_path = str(Path(memory_path).resolve())
        
        # Check if path exists
        path_obj = Path(memory_path)
        if not path_obj.exists():
            print(f"\nPath does not exist: {memory_path}")
            create = input("Create this directory? (yes/no): ").strip().lower()
            if create in ['yes', 'y']:
                try:
                    path_obj.mkdir(parents=True, exist_ok=True)
                    print(f"✓ Created directory: {memory_path}")
                except Exception as e:
                    print(f"Error: Could not create directory: {e}\n")
                    continue
            else:
                print("Please enter a different path.\n")
                continue
        
        # Confirm
        print(f"\nMemory root path: {memory_path}")
        print(f"This folder will contain: [project-name]/, common/, private/")
        confirm = input("Is this correct? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            return memory_path
        elif confirm in ['no', 'n']:
            print("Let's try again.\n")
        else:
            print("Please answer 'yes' or 'no'.\n")

def replace_memory_path(agents_file, memory_path):
    """Replace {MEMORY_PATH} placeholder."""
    try:
        # Read file
        with open(agents_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count occurrences
        count = content.count('{MEMORY_PATH}')
        
        if count == 0:
            print(f"\nWarning: No {{MEMORY_PATH}} placeholder found in {agents_file.name}")
            print("The file may already be configured.")
            return False
        
        # Replace
        new_content = content.replace('{MEMORY_PATH}', memory_path)
        
        # Write back
        with open(agents_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"\n✓ Successfully replaced {count} occurrence(s) of {{MEMORY_PATH}} with:")
        print(f"  {memory_path}")
        return True
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False

def main():
    """Main function."""
    print(__doc__)
    
    # Find AGENTS.md file
    agents_file = find_agents_file()
    
    if not agents_file:
        print("\n✗ Error: Could not find AGENTS.md file.")
        print("  Make sure you're running this script from the agents-md directory.")
        sys.exit(1)
    
    print(f"\nFound configuration file: {agents_file.name}")
    
    # Get memory root path
    memory_path = get_memory_path()
    
    # Replace placeholder
    success = replace_memory_path(agents_file, memory_path)
    
    if success:
        print(f"\n✓ Configuration complete!")
        print(f"\nConfiguration summary:")
        print(f"  - Memory root path: {memory_path}")
        print(f"\nNext steps:")
        print(f"  1. Review {agents_file.name} to verify the changes")
        print(f"  2. Copy _agents-md/ folder and AGENTS.md to your project")
        print(f"\nYour memory structure will be:")
        print(f"  {memory_path}/")
        print(f"  ├── [project-name]/  (project-specific memory)")
        print(f"  ├── common/          (shared preferences, patterns)")
        print(f"  └── private/        (credentials, personal info)")
    else:
        print("\n✗ Configuration failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)
