#!/usr/bin/env python3
# Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com
#
# Licensed under the MIT License. See LICENSE file for details.

"""
Setup script for configuring agents-md.

This script helps configure language and memory root path (MEMORY_PATH variable).
Ensures both AGENTS.md (for Cursor) and GEMINI.md (for Google Antigravity) exist.

Features:
- CLI localization support (en/ja) via command-line argument
- Handles shell-escaped paths automatically (e.g., spaces, special characters)
- Expands ~ for home directory and environment variables
- Creates directories if they don't exist
- Cross-platform path handling
- Updates MEMORY_PATH variable definition in both AGENTS.md and GEMINI.md
- Ensures both files exist for dual editor support (Cursor + Antigravity)

Usage:
    python setup.py [--lang en|ja]        # Windows
    python3 setup.py [--lang en|ja]       # macOS/Linux

Flow:
    1. Select language (en/ja) - or use --lang parameter
    2. Configure memory root path

For non-engineers: Manual replacement is straightforward and recommended.
Simply open the AGENTS.md or GEMINI.md file and replace the path in the Configuration section:
**MEMORY_PATH**: `/path/to/your/memory-root`
"""

import argparse
import os
import re
import sys
import shutil
from pathlib import Path

# Windows compatibility: Set console encoding to UTF-8 for proper Japanese character display
if sys.platform == 'win32':
    try:
        # Try to set UTF-8 encoding for Windows console
        if sys.stdout.encoding != 'utf-8':
            import codecs
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
    except (AttributeError, ImportError):
        # Fallback: Try to set console code page to UTF-8
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleOutputCP(65001)  # UTF-8 code page
        except (AttributeError, OSError):
            pass  # If it fails, continue anyway

# Constants for language switching
AGENTS_EN = "AGENTS.md.en"
AGENTS_JA = "AGENTS.md.ja"
AGENTS_TARGET = "AGENTS.md"
AGENTS_BACKUP = "AGENTS.md.backup"
GEMINI_TARGET = "GEMINI.md"
GEMINI_BACKUP = "GEMINI.md.backup"

# ============================================================================
# LOCALIZATION TABLE
# ============================================================================
# All user-facing strings are defined here for easy maintenance and translation
LOCALIZATION = {
    'en': {
        # Language selection
        'lang_selection_title': 'Language Selection',
        'lang_current': 'Current language: {lang}',
        'lang_select': 'Select language:',
        'lang_option_1': '1. English (en)',
        'lang_option_2': '2. Japanese (ja)',
        'lang_prompt': 'Enter choice (1/2) or language code (en/ja): ',
        'lang_invalid': "Invalid choice. Please enter 1, 2, 'en', or 'ja'.",
        
        # Language switching
        'lang_switch_title': 'Switching Language',
        'lang_switch_success': '✓ Switched to {lang}',
        'lang_switch_preserved': '  Preserved MEMORY_PATH: {path}',
        'lang_switch_error': "Error: Source file '{file}' not found.",
        'lang_switch_gemini_created': '✓ Created {file} (for Google Antigravity support)',
        'lang_switch_gemini_warning': 'Warning: Could not create/update {file}: {error}',
        'lang_switch_complete': 'Language switching complete!',
        'continue_prompt': 'Do you want to configure memory path now? (yes/no): ',
        'continue_invalid': "Please answer 'yes' or 'no'.",
        'exiting': 'Exiting setup. Language has been switched successfully.',
        'exiting_summary': 'Language switched to: {lang}',
        
        # Memory path configuration
        'memory_title': 'Memory Root Path Configuration',
        'memory_description': 'Enter the full path where you want to store your memory.',
        'memory_description_detail': 'This will be the root folder for all memory (projects, common, private).',
        'memory_examples': 'Examples:',
        'memory_example_1': '  - ~/Documents/my-memory',
        'memory_example_2': '  - /Users/username/Documents/my-memory',
        'memory_example_3': '  - /Users/username/Library/CloudStorage/GoogleDrive-user@gmail.com/My Drive/AI/memory',
        'memory_example_4': '  - C:\\Users\\username\\Documents\\my-memory (Windows)',
        'memory_note': 'Note: You can use ~ for home directory. Spaces and special characters are handled automatically.',
        'memory_note_detail': 'No need to quote paths - just type them normally. The folder will be created if it doesn\'t exist.',
        'memory_prompt': 'Enter memory root path: ',
        'memory_error_empty': 'Error: Path cannot be empty.',
        'memory_path_not_exists': 'Path does not exist: {path}',
        'memory_create_prompt': 'Create this directory? (yes/no): ',
        'memory_create_success': '✓ Created directory: {path}',
        'memory_create_error': 'Error: Could not create directory: {error}',
        'memory_retry': 'Please enter a different path.',
        'memory_confirm_path': 'Memory root path: {path}',
        'memory_confirm_structure': 'This folder will contain: [project-name]/, common/, private/',
        'memory_confirm_prompt': 'Is this correct? (yes/no): ',
        'memory_confirm_retry': "Let's try again.",
        'memory_confirm_invalid': "Please answer 'yes' or 'no'.",
        
        # File operations
        'file_found': 'Found configuration file: {file}',
        'file_error_not_found': '✗ Error: Could not find AGENTS.md file.',
        'file_error_location': "  Make sure you're running this script from the agents-md directory.",
        'file_warning_no_memory_path': 'Warning: No MEMORY_PATH variable definition found in {file}',
        'file_warning_format': 'The file may already be configured or uses a different format.',
        'file_error_update': '✗ Error updating {file}: {error}',
        'file_success_gemini_created': '✓ Created and configured GEMINI.md',
        'file_warning_gemini_error': 'Warning: Could not create GEMINI.md: {error}',
        
        # Memory path update
        'memory_update_success': '✓ Successfully updated MEMORY_PATH variable:',
        'memory_update_path': '  {path}',
        'memory_update_both': '  - Updated in both AGENTS.md (Cursor) and GEMINI.md (Antigravity)',
        'memory_update_agents_only': '  - Updated in AGENTS.md (Cursor)',
        'memory_update_gemini_later': '  - GEMINI.md will be created when you copy files to your project',
        'memory_update_note': 'Note: Agents understand this variable applies to all path references in the document.',
        
        # Completion
        'complete_title': '✓ Configuration complete!',
        'complete_summary': 'Configuration summary:',
        'complete_lang': '  - Language: {lang}',
        'complete_memory_path': '  - Memory root path: {path}',
        'complete_agents_updated': '  - AGENTS.md updated (for Cursor)',
        'complete_gemini_updated': '  - GEMINI.md updated (for Google Antigravity)',
        'complete_next_steps': 'Next steps:',
        'complete_review_agents': '  1. Review {file} to verify the changes',
        'complete_review_gemini': '  2. Review GEMINI.md to verify the changes',
        'complete_copy_files': '  3. Copy _agents-md/ folder and both AGENTS.md and GEMINI.md to your project',
        'complete_structure_title': 'Your memory structure will be:',
        'complete_structure_path': '  {path}/',
        'complete_structure_project': '  ├── [project-name]/  (project-specific memory)',
        'complete_structure_common': '  ├── common/          (shared preferences, patterns)',
        'complete_structure_private': '  └── private/        (credentials, personal info)',
        
        # Errors
        'error_lang_switch_failed': '✗ Language switch failed. Please check the errors above.',
        'error_config_failed': '✗ Configuration failed. Please check the errors above.',
        'error_cancelled': 'Operation cancelled by user.',
    },
    'ja': {
        # Language selection
        'lang_selection_title': '言語選択',
        'lang_current': '現在の言語: {lang}',
        'lang_select': '言語を選択:',
        'lang_option_1': '1. 英語 (en)',
        'lang_option_2': '2. 日本語 (ja)',
        'lang_prompt': '選択を入力 (1/2) または言語コード (en/ja): ',
        'lang_invalid': '無効な選択です。1、2、「en」、または「ja」を入力してください。',
        
        # Language switching
        'lang_switch_title': '言語を切り替え中',
        'lang_switch_success': '✓ {lang} に切り替えました',
        'lang_switch_preserved': '  MEMORY_PATH を保持: {path}',
        'lang_switch_error': 'エラー: ソースファイル「{file}」が見つかりません。',
        'lang_switch_gemini_created': '✓ {file} を作成しました（Google Antigravity サポート用）',
        'lang_switch_gemini_warning': '警告: {file} を作成/更新できませんでした: {error}',
        'lang_switch_complete': '言語の切り替えが完了しました！',
        'continue_prompt': 'メモリパスを今設定しますか？ (yes/no): ',
        'continue_invalid': '「yes」または「no」で答えてください。',
        'exiting': 'セットアップを終了します。言語の切り替えは正常に完了しました。',
        'exiting_summary': '言語を {lang} に切り替えました',
        
        # Memory path configuration
        'memory_title': 'メモリルートパス設定',
        'memory_description': 'メモリを保存する完全なパスを入力してください。',
        'memory_description_detail': 'これはすべてのメモリ（プロジェクト、共通、プライベート）のルートフォルダになります。',
        'memory_examples': '例:',
        'memory_example_1': '  - ~/Documents/my-memory',
        'memory_example_2': '  - /Users/username/Documents/my-memory',
        'memory_example_3': '  - /Users/username/Library/CloudStorage/GoogleDrive-user@gmail.com/My Drive/AI/memory',
        'memory_example_4': '  - C:\\Users\\username\\Documents\\my-memory (Windows)',
        'memory_note': '注意: ホームディレクトリには ~ を使用できます。スペースや特殊文字は自動的に処理されます。',
        'memory_note_detail': 'パスを引用符で囲む必要はありません - 通常どおり入力してください。フォルダが存在しない場合は作成されます。',
        'memory_prompt': 'メモリルートパスを入力: ',
        'memory_error_empty': 'エラー: パスを空にすることはできません。',
        'memory_path_not_exists': 'パスが存在しません: {path}',
        'memory_create_prompt': 'このディレクトリを作成しますか？ (yes/no): ',
        'memory_create_success': '✓ ディレクトリを作成しました: {path}',
        'memory_create_error': 'エラー: ディレクトリを作成できませんでした: {error}',
        'memory_retry': '別のパスを入力してください。',
        'memory_confirm_path': 'メモリルートパス: {path}',
        'memory_confirm_structure': 'このフォルダには以下が含まれます: [project-name]/, common/, private/',
        'memory_confirm_prompt': 'これで正しいですか？ (yes/no): ',
        'memory_confirm_retry': 'もう一度やり直しましょう。',
        'memory_confirm_invalid': '「yes」または「no」で答えてください。',
        
        # File operations
        'file_found': '設定ファイルが見つかりました: {file}',
        'file_error_not_found': '✗ エラー: AGENTS.md ファイルが見つかりませんでした。',
        'file_error_location': '  agents-md ディレクトリからこのスクリプトを実行していることを確認してください。',
        'file_warning_no_memory_path': '警告: {file} に MEMORY_PATH 変数定義が見つかりませんでした',
        'file_warning_format': 'ファイルは既に設定されているか、別の形式を使用している可能性があります。',
        'file_error_update': '✗ {file} の更新エラー: {error}',
        'file_success_gemini_created': '✓ GEMINI.md を作成して設定しました',
        'file_warning_gemini_error': '警告: GEMINI.md を作成できませんでした: {error}',
        
        # Memory path update
        'memory_update_success': '✓ MEMORY_PATH 変数を正常に更新しました:',
        'memory_update_path': '  {path}',
        'memory_update_both': '  - AGENTS.md (Cursor) と GEMINI.md (Antigravity) の両方で更新',
        'memory_update_agents_only': '  - AGENTS.md (Cursor) で更新',
        'memory_update_gemini_later': '  - ファイルをプロジェクトにコピーするときに GEMINI.md が作成されます',
        'memory_update_note': '注意: エージェントは、この変数がドキュメント内のすべてのパス参照に適用されることを理解します。',
        
        # Completion
        'complete_title': '✓ 設定が完了しました！',
        'complete_summary': '設定の概要:',
        'complete_lang': '  - 言語: {lang}',
        'complete_memory_path': '  - メモリルートパス: {path}',
        'complete_agents_updated': '  - AGENTS.md を更新しました（Cursor 用）',
        'complete_gemini_updated': '  - GEMINI.md を更新しました（Google Antigravity 用）',
        'complete_next_steps': '次のステップ:',
        'complete_review_agents': '  1. {file} を確認して変更を確認',
        'complete_review_gemini': '  2. GEMINI.md を確認して変更を確認',
        'complete_copy_files': '  3. _agents-md/ フォルダと AGENTS.md および GEMINI.md の両方をプロジェクトにコピー',
        'complete_structure_title': 'メモリ構造は次のようになります:',
        'complete_structure_path': '  {path}/',
        'complete_structure_project': '  ├── [project-name]/  (プロジェクト固有のメモリ)',
        'complete_structure_common': '  ├── common/          (共有設定、パターン)',
        'complete_structure_private': '  └── private/        (認証情報、個人情報)',
        
        # Errors
        'error_lang_switch_failed': '✗ 言語の切り替えに失敗しました。上記のエラーを確認してください。',
        'error_config_failed': '✗ 設定に失敗しました。上記のエラーを確認してください。',
        'error_cancelled': 'ユーザーによって操作がキャンセルされました。',
    }
}

# ============================================================================
# LOCALIZATION HELPER
# ============================================================================
def t(key, locale='en', **kwargs):
    """Get localized string from localization table.
    
    Args:
        key: Localization key
        locale: Language code for selecting localization ('en' or 'ja')
        **kwargs: Format parameters for the string (including 'lang' for display)
    """
    localized_str = LOCALIZATION.get(locale, LOCALIZATION['en']).get(key, key)
    return localized_str.format(**kwargs)

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def get_script_directory():
    """Get the directory where this script is located."""
    return Path(__file__).parent.absolute()

def decode_shell_escaped_string(s):
    """Decode basic shell-style escaped characters in paths."""
    if '\\' not in s:
        return s
    result = s.replace('\\ ', ' ')
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

def get_current_language():
    """Detect current language by checking if AGENTS.md exists and reading first few lines."""
    script_dir = get_script_directory()
    agents_file = script_dir / AGENTS_TARGET
    if not agents_file.exists():
        return None
    try:
        with open(agents_file, 'r', encoding='utf-8') as f:
            first_lines = ''.join(f.readlines()[:10])
            if '# Memory System Guidelines' in first_lines:
                return 'en'
            elif '# メモリシステムガイドライン' in first_lines:
                return 'ja'
    except Exception:
        pass
    return 'unknown'

def extract_memory_path(content):
    """Extract configured MEMORY_PATH from content if it exists."""
    if '{MEMORY_PATH}' in content:
        return None
    lines = content.split('\n')
    for line in lines:
        if ('memory' in line.lower() and ('root' in line.lower() or 'path' in line.lower() or 'ルート' in line or 'パス' in line)) or 'cursor-memory' in line.lower():
            backtick_pattern = r'`([^`]+)`'
            backtick_matches = re.findall(backtick_pattern, line)
            for match in backtick_matches:
                if ('/' in match or '\\' in match) and '{MEMORY_PATH}' not in match:
                    if 'memory' in match.lower() or match.startswith('/') or match.startswith('~') or (len(match) > 20 and ('/' in match or '\\' in match)):
                        return match.strip()
            root_patterns = [
                r'(?:ルート|Root):\s*[`"]?([^`"\n]+(?:memory|cursor-memory)[^`"\n]*)',
                r'[`"]([^`"]+memory[^`"]*)[`"]',
            ]
            for pattern in root_patterns:
                matches = re.findall(pattern, line, re.IGNORECASE)
                for match in matches:
                    match = match.strip()
                    if match and ('/' in match or '\\' in match) and '{MEMORY_PATH}' not in match:
                        if 'memory' in match.lower() or (len(match) > 15 and match.startswith('/')):
                            return match
    pattern = r'\*\*MEMORY_PATH\*\*:\s*`([^`]+)`'
    match = re.search(pattern, content)
    if match:
        path = match.group(1).strip()
        if path and path != '/path/to/your/memory-root' and '{MEMORY_PATH}' not in path:
            return path
    return None

# ============================================================================
# LANGUAGE SELECTION
# ============================================================================
def get_language_preference(cli_lang=None, current_lang=None):
    """Prompt user for language preference or use CLI argument."""
    if cli_lang:
        if cli_lang.lower() in ['en', 'ja']:
            return cli_lang.lower()
        print(f"Warning: Invalid language '{cli_lang}'. Using interactive selection.")
    
    print("\n" + "="*60)
    print(t('lang_selection_title', locale=current_lang or 'en'))
    print("="*60)
    
    if current_lang:
        display_lang = current_lang.upper()
        print(f"\n{t('lang_current', locale=current_lang or 'en', lang=display_lang)}")
    
    print(f"\n{t('lang_select', locale=current_lang or 'en')}")
    print(f"  {t('lang_option_1', locale=current_lang or 'en')}")
    print(f"  {t('lang_option_2', locale=current_lang or 'en')}")
    
    while True:
        choice = input(f"\n{t('lang_prompt', locale=current_lang or 'en')}").strip().lower()
        if choice in ['1', 'en', 'english']:
            return 'en'
        elif choice in ['2', 'ja', 'japanese', '日本語']:
            return 'ja'
        else:
            print(t('lang_invalid', locale=current_lang or 'en'))

# ============================================================================
# LANGUAGE SWITCHING
# ============================================================================
def switch_to_language(target_lang, preserve_memory_path=None, cli_lang='en'):
    """Switch AGENTS.md and GEMINI.md to the specified language."""
    script_dir = get_script_directory()
    source_file = script_dir / (AGENTS_JA if target_lang == 'ja' else AGENTS_EN)
    target_file = script_dir / AGENTS_TARGET
    gemini_file = script_dir / GEMINI_TARGET
    
    if not source_file.exists():
        print(t('lang_switch_error', locale=cli_lang, file=source_file.name))
        return False
    
    with open(source_file, 'r', encoding='utf-8') as f:
        new_content = f.read()
    
    configured_path = preserve_memory_path
    if not configured_path and target_file.exists():
        try:
            with open(target_file, 'r', encoding='utf-8') as f:
                current_content = f.read()
            configured_path = extract_memory_path(current_content)
        except Exception:
            pass
    
    if configured_path:
        placeholder_count = new_content.count('{MEMORY_PATH}')
        if placeholder_count > 0:
            new_content = new_content.replace('{MEMORY_PATH}', configured_path)
        pattern = r'\*\*MEMORY_PATH\*\*:\s*`?([^`\n]+)`?'
        new_content = re.sub(pattern, f'**MEMORY_PATH**: `{configured_path}`', new_content, count=1)
    
    current_lang = get_current_language()
    if current_lang and current_lang != target_lang:
        if target_file.exists():
            try:
                shutil.copy2(target_file, script_dir / AGENTS_BACKUP)
            except Exception:
                pass
        if gemini_file.exists():
            try:
                shutil.copy2(gemini_file, script_dir / GEMINI_BACKUP)
            except Exception:
                pass
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    gemini_existed = gemini_file.exists()
    try:
        with open(gemini_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        if not gemini_existed:
            print(t('lang_switch_gemini_created', locale=cli_lang, file=GEMINI_TARGET))
    except Exception as e:
        print(t('lang_switch_gemini_warning', locale=cli_lang, file=GEMINI_TARGET, error=e))
    
    print(t('lang_switch_success', locale=cli_lang, lang=target_lang.upper()))
    if configured_path:
        print(t('lang_switch_preserved', locale=cli_lang, path=configured_path))
    
    return True

# ============================================================================
# CONTINUE/QUIT PROMPT
# ============================================================================
def ask_continue_or_quit(cli_lang='en'):
    """Ask user if they want to continue with memory path configuration or quit."""
    print(f"\n{t('lang_switch_complete', locale=cli_lang)}")
    
    while True:
        choice = input(t('continue_prompt', locale=cli_lang)).strip().lower()
        
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print(t('continue_invalid', locale=cli_lang))

# ============================================================================
# MEMORY PATH CONFIGURATION
# ============================================================================
def get_memory_path(cli_lang='en'):
    """Prompt user for memory root path."""
    print("\n" + "="*60)
    print(t('memory_title', locale=cli_lang))
    print("="*60)
    print(f"\n{t('memory_description', locale=cli_lang)}")
    print(t('memory_description_detail', locale=cli_lang))
    print(f"\n{t('memory_examples', locale=cli_lang)}")
    print(t('memory_example_1', locale=cli_lang))
    print(t('memory_example_2', locale=cli_lang))
    print(t('memory_example_3', locale=cli_lang))
    print(t('memory_example_4', locale=cli_lang))
    print(f"\n{t('memory_note', locale=cli_lang)}")
    print(t('memory_note_detail', locale=cli_lang))
    print()
    
    while True:
        memory_path = input(t('memory_prompt', locale=cli_lang)).strip()
        
        if (memory_path.startswith('"') and memory_path.endswith('"')) or \
           (memory_path.startswith("'") and memory_path.endswith("'")):
            memory_path = memory_path[1:-1]
        
        if not memory_path:
            print(t('memory_error_empty', locale=cli_lang) + "\n")
            continue
        
        memory_path = decode_shell_escaped_string(memory_path)
        memory_path = os.path.expanduser(memory_path)
        memory_path = os.path.expandvars(memory_path)
        
        # Convert to absolute path (handles both Unix and Windows paths)
        try:
            memory_path = str(Path(memory_path).resolve())
        except (OSError, ValueError) as e:
            # On Windows, if path doesn't exist yet, resolve() might fail
            # Try to normalize the path manually
            if sys.platform == 'win32':
                # Normalize Windows path separators
                memory_path = os.path.normpath(memory_path)
                # Convert to absolute if relative
                if not os.path.isabs(memory_path):
                    memory_path = os.path.abspath(memory_path)
            else:
                memory_path = str(Path(memory_path).resolve())
        
        path_obj = Path(memory_path)
        if not path_obj.exists():
            print(f"\n{t('memory_path_not_exists', locale=cli_lang, path=memory_path)}")
            create = input(t('memory_create_prompt', locale=cli_lang)).strip().lower()
            if create in ['yes', 'y']:
                try:
                    path_obj.mkdir(parents=True, exist_ok=True)
                    print(t('memory_create_success', locale=cli_lang, path=memory_path))
                except Exception as e:
                    print(t('memory_create_error', locale=cli_lang, error=e) + "\n")
                    continue
            else:
                print(t('memory_retry', locale=cli_lang) + "\n")
                continue
        
        print(f"\n{t('memory_confirm_path', locale=cli_lang, path=memory_path)}")
        print(t('memory_confirm_structure', locale=cli_lang))
        confirm = input(t('memory_confirm_prompt', locale=cli_lang)).strip().lower()
        
        if confirm in ['yes', 'y']:
            return memory_path
        elif confirm in ['no', 'n']:
            print(t('memory_confirm_retry', locale=cli_lang) + "\n")
        else:
            print(t('memory_confirm_invalid', locale=cli_lang) + "\n")

# ============================================================================
# FILE OPERATIONS
# ============================================================================
def replace_memory_path(file_path, memory_path, cli_lang='en'):
    """Replace MEMORY_PATH variable definition in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'\*\*MEMORY_PATH\*\*:\s*`?([^`\n]+)`?'
        match = re.search(pattern, content)
        
        if not match:
            print(f"\n{t('file_warning_no_memory_path', locale=cli_lang, file=file_path.name)}")
            print(t('file_warning_format', locale=cli_lang))
            return False
        
        new_content = re.sub(pattern, f'**MEMORY_PATH**: `{memory_path}`', content, count=1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(t('file_error_update', locale=cli_lang, file=file_path.name, error=e))
        return False

def update_both_files(agents_file, gemini_file, memory_path, cli_lang='en'):
    """Update MEMORY_PATH in both AGENTS.md and GEMINI.md."""
    success_agents = replace_memory_path(agents_file, memory_path, cli_lang)
    success_gemini = False
    
    if gemini_file.exists():
        success_gemini = replace_memory_path(gemini_file, memory_path, cli_lang)
    else:
        if agents_file.exists():
            try:
                with open(agents_file, 'r', encoding='utf-8') as src:
                    content = src.read()
                pattern = r'\*\*MEMORY_PATH\*\*:\s*`?([^`\n]+)`?'
                content = re.sub(pattern, f'**MEMORY_PATH**: `{memory_path}`', content, count=1)
                with open(gemini_file, 'w', encoding='utf-8') as dst:
                    dst.write(content)
                success_gemini = True
                print(t('file_success_gemini_created', locale=cli_lang))
            except Exception as e:
                print(t('file_warning_gemini_error', locale=cli_lang, error=e))
                success_gemini = False
    
    if success_agents:
        print(f"\n{t('memory_update_success', locale=cli_lang)}")
        print(t('memory_update_path', locale=cli_lang, path=memory_path))
        if success_gemini:
            print(t('memory_update_both', locale=cli_lang))
        else:
            print(t('memory_update_agents_only', locale=cli_lang))
            print(t('memory_update_gemini_later', locale=cli_lang))
        print(f"\n{t('memory_update_note', locale=cli_lang)}")
        return True
    
    return False

# ============================================================================
# MAIN FUNCTION
# ============================================================================
def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Setup script for configuring agents-md')
    parser.add_argument('--lang', choices=['en', 'ja'], help='CLI language (en/ja)')
    args = parser.parse_args()
    
    cli_lang = args.lang or 'en'
    current_lang = get_current_language()
    
    script_dir = get_script_directory()
    agents_file = find_agents_file()
    
    if not agents_file:
        print(f"\n{t('file_error_not_found', locale=cli_lang)}")
        print(t('file_error_location', locale=cli_lang))
        sys.exit(1)
    
    print(t('file_found', locale=cli_lang, file=agents_file.name))
    
    # Step 1: Get language preference
    target_lang = get_language_preference(cli_lang=args.lang, current_lang=current_lang)
    # Update CLI language to match selected language for rest of script
    cli_lang = target_lang
    
    # Step 2: Switch to selected language
    print(f"\n{'='*60}")
    print(t('lang_switch_title', locale=cli_lang))
    print("="*60)
    switch_success = switch_to_language(target_lang, cli_lang=cli_lang)
    
    if not switch_success:
        print(f"\n{t('error_lang_switch_failed', locale=cli_lang)}")
        sys.exit(1)
    
    # Step 3: Ask if user wants to continue with memory path configuration
    if not ask_continue_or_quit(cli_lang=cli_lang):
        print(f"\n{t('exiting', locale=cli_lang)}")
        print(t('exiting_summary', locale=cli_lang, lang=target_lang.upper()))
        sys.exit(0)
    
    # Step 4: Get memory root path
    memory_path = get_memory_path(cli_lang=cli_lang)
    
    # Step 5: Update MEMORY_PATH in both files
    gemini_file = script_dir / GEMINI_TARGET
    success = update_both_files(agents_file, gemini_file, memory_path, cli_lang=cli_lang)
    
    if success:
        print(f"\n{t('complete_title', locale=cli_lang)}")
        print(f"\n{t('complete_summary', locale=cli_lang)}")
        print(t('complete_lang', locale=cli_lang, lang=target_lang.upper()))
        print(t('complete_memory_path', locale=cli_lang, path=memory_path))
        print(t('complete_agents_updated', locale=cli_lang))
        if gemini_file.exists():
            print(t('complete_gemini_updated', locale=cli_lang))
        print(f"\n{t('complete_next_steps', locale=cli_lang)}")
        print(t('complete_review_agents', locale=cli_lang, file=agents_file.name))
        if gemini_file.exists():
            print(t('complete_review_gemini', locale=cli_lang))
        print(t('complete_copy_files', locale=cli_lang))
        print(f"\n{t('complete_structure_title', locale=cli_lang)}")
        print(t('complete_structure_path', locale=cli_lang, path=memory_path))
        print(t('complete_structure_project', locale=cli_lang))
        print(t('complete_structure_common', locale=cli_lang))
        print(t('complete_structure_private', locale=cli_lang))
    else:
        print(f"\n{t('error_config_failed', locale=cli_lang)}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{t('error_cancelled', lang='en')}")
        sys.exit(1)
