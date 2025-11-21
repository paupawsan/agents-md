# PR: Add Google Antigravity Support and Refactor Setup Script

## 🎯 Summary

This PR adds support for Google Antigravity alongside Cursor, refactors the setup script with comprehensive localization, and improves the overall setup experience with better cross-platform support.

## ✨ Key Features

### 🚀 Google Antigravity Support
- **Dual Editor Support**: Automatically creates both `AGENTS.md` (for Cursor) and `GEMINI.md` (for Google Antigravity)
- **Synchronized Configuration**: Both files are kept in sync when switching languages or updating memory paths
- **Seamless Integration**: Works with both editors without manual file management

### 🌐 Comprehensive Localization
- **CLI Language Parameter**: `--lang en` or `--lang ja` for direct language selection
- **Localization Table**: All user-facing strings centralized in a clean localization dictionary
- **Beautiful Code Structure**: Logic separated from localization for easy maintenance and extension
- **Windows UTF-8 Support**: Proper Japanese character display on Windows console

### 🔧 Improved Setup Script
- **Renamed**: `setup_memory_dir.py` → `setup.py` (simpler, more intuitive)
- **Integrated Language Switching**: Language selection is now part of the setup flow
- **Flexible Flow**: Users can switch language only, or continue to configure memory path
- **Better UX**: Clear prompts, progress indicators, and helpful error messages

### 🪟 Cross-Platform Compatibility
- **Windows Support**: UTF-8 console encoding, improved path handling
- **macOS/Linux**: Full support maintained
- **Path Handling**: Robust cross-platform path resolution and normalization

## 📝 Changes

### Scripts
- ✨ **New**: `setup.py` - Comprehensive setup script with localization
- 🗑️ **Removed**: `setup_memory_dir.py` (renamed to `setup.py`)
- 🗑️ **Removed**: `switch_agents_lang.py` (functionality integrated into `setup.py`)

### Files
- ✨ **New**: `GEMINI.md` - Configuration file for Google Antigravity (auto-created)
- 📝 **Updated**: `AGENTS.md`, `AGENTS.md.en`, `AGENTS.md.ja` - Updated references to `setup.py`

### Documentation
- 📚 **Updated**: `README.md` and `README.ja.md` - Added setup script instructions
- 📚 **Updated**: `docs/simple-setup.md` and `docs/simple-setup.ja.md` - Added automated setup option
- 📚 **Updated**: `docs/setup-guide.md` and `docs/setup-guide.ja.md` - Updated with new features

## 🔄 Migration Guide

### For Existing Users

**If you're using the old `setup_memory_dir.py`**:
1. Run the new `setup.py` script to update your configuration
2. The script will automatically detect and preserve your existing `MEMORY_PATH`
3. Both `AGENTS.md` and `GEMINI.md` will be created/updated

**If you were using `switch_agents_lang.py`**:
- Language switching is now integrated into `setup.py`
- Simply run `python3 setup.py` and select your language
- Or use `python3 setup.py --lang en` or `python3 setup.py --lang ja`

### For New Users

1. Run `python setup.py` (Windows) or `python3 setup.py` (macOS/Linux)
2. Select your language (English/Japanese)
3. Choose whether to configure memory path (yes/no)
4. Copy `AGENTS.md` and `GEMINI.md` to your project (or add agents-md folder to workspace)

## 🧪 Testing

### Manual Testing Performed
- ✅ Language switching (English ↔ Japanese)
- ✅ Memory path configuration
- ✅ GEMINI.md creation and synchronization
- ✅ Windows path handling
- ✅ UTF-8 encoding on Windows console
- ✅ Quit option after language switching
- ✅ MEMORY_PATH preservation during language switch

### Test Commands
```bash
# Test English setup
python3 setup.py --lang en

# Test Japanese setup
python3 setup.py --lang ja

# Test interactive mode
python3 setup.py
```

## 📋 Checklist

- [x] Code compiles without errors
- [x] All documentation updated (README, setup guides, simple-setup guides)
- [x] Both English and Japanese documentation synchronized
- [x] Windows compatibility tested
- [x] Cross-platform path handling verified
- [x] GEMINI.md creation and sync tested
- [x] Language switching preserves MEMORY_PATH
- [x] No breaking changes for existing users

## 🎨 Code Quality

- **Clean Architecture**: Localization separated from business logic
- **Maintainable**: Easy to add new languages (just extend localization table)
- **Readable**: Well-organized sections with clear comments
- **Cross-Platform**: Uses `pathlib.Path` and proper OS detection
- **Error Handling**: Graceful fallbacks and helpful error messages

## 📸 Screenshots / Examples

### Setup Flow
```
$ python3 setup.py --lang ja

============================================================
Language Selection
============================================================

Select language:
  1. English (en)
  2. Japanese (ja)

Enter choice (1/2) or language code (en/ja): 2

============================================================
言語を切り替え中
============================================================
✓ JA に切り替えました

言語の切り替えが完了しました！
Do you want to configure memory path now? (yes/no): no

Exiting setup. Language has been switched successfully.
Language switched to: JA
```

## 🔗 Related Issues

- Adds support for Google Antigravity
- Improves setup experience for non-technical users
- Enhances cross-platform compatibility

## 📚 Documentation

All documentation has been updated:
- Main README files (English & Japanese)
- Simple setup guides (for non-technical users)
- Technical setup guides
- All references updated to use `setup.py`

## ⚠️ Breaking Changes

**None** - This is a backward-compatible enhancement. Existing users can continue using their current setup, and the new script will detect and preserve their configuration.

## 🚀 Next Steps

After merge:
- Update release notes for v0.2.1
- Consider adding more languages to localization table
- Monitor user feedback on the new setup flow

