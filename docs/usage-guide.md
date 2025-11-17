<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Memory System Usage Guide

This guide explains how to effectively use the agents-md memory system in your development workflow. The memory system provides intelligent, RAG-optimized knowledge management for AI coding agents.

## Memory Structure

The memory system organizes information into three categories:

### 1. Project-Specific Memory (`{MEMORY_DIR}/[project-name]/`)
- **Purpose**: Knowledge specific to your current project
- **Contents**:
  - Project architecture decisions
  - Project-specific patterns and fixes
  - Project file locations
  - Project-specific preferences
- **Access**: Automatically used when working on this project

### 2. Common Memory (`{MEMORY_DIR}/common/`)
- **Purpose**: User preferences and cross-project patterns
- **Contents**:
  - User preferences (apply to all projects)
  - Global settings and configurations
  - Cross-project patterns
  - User workflows
- **Access**: Available across all projects

### 3. Private Memory (`{MEMORY_DIR}/private/`) ⚠️
- **Purpose**: Sensitive information storage
- **Contents**:
  - API keys, passwords, tokens
  - Personal information
  - Sensitive settings
- **⚠️ Important**: Never commit private memory files to version control

## How Agents Use Memory

Agents automatically handle most memory operations:

### Automatic Memory Management
- **Sync memory** after significant tasks or when learning patterns
- **Check memory** when context is lost or unclear
- **Update index files** when creating new knowledge or sessions
- **Consolidate related sessions** to maintain clean organization
- **Use RAG** to retrieve only relevant memories, minimizing token usage

### Manual Memory Operations (When Needed)

#### Memory Initialization
```
Initialize memory for this project. Create the memory structure in the configured memory directory, including index files and initial knowledge files documenting the project architecture and patterns.
```

#### Manual Memory Sync
```
Sync memory for this project. Update index files, consolidate recent sessions if needed, and ensure index.json is synchronized with actual files in knowledge/ and sessions/ directories.
```

#### Memory Update
```
Update project memory with current status. Document recent changes, update index files, and sync any new patterns or architectural decisions.
```

## RAG (Retrieval-Augmented Generation) Features

The memory system uses advanced RAG capabilities for intelligent information retrieval:

### How RAG Works
- **Multi-level indexing**: Index-first lookup for instant access
- **Semantic search**: Natural language queries to find relevant memories
- **Selective reading**: Only relevant sections are loaded into context
- **Token optimization**: 80-95% token reduction compared to loading entire files

### Benefits
- ✅ **Reduced Token Usage**: Only relevant memories are loaded into context
- ✅ **Intelligent Retrieval**: Agents understand context and retrieve related information automatically
- ✅ **Fast Access**: Multi-level indexing enables instant lookup
- ✅ **Scalable**: Handles large memory databases efficiently

## Prompt Examples

Here are practical examples of prompts you can use to interact with the memory system:

### Getting Topics and Patterns
```
What topics are documented in memory for this project?
Show me all the patterns we've established for this project.
What are the documented topics in the knowledge/ directory?
List all architectural patterns we've documented.
```

### Searching for Specific Information
```
What did we decide about error handling in this project?
Check memory for how we handle authentication.
What patterns exist for API integration?
Find previous solutions to similar problems.
```

### Checking User Preferences
```
What are my preferences for this project?
Check common preferences that apply to all projects.
What project-specific preferences are set?
```

### Reviewing Architecture Decisions
```
What architectural decisions were made for this project?
Show me the architecture documentation from memory.
What design patterns are we using?
```

### Finding Session Summaries
```
What work was done in recent sessions?
Show me the last few session summaries.
What was completed in the last week?
```

### Checking Project Status
```
What's the current status of this project?
Show me recent fixes and updates.
What are the known issues and their solutions?
```

### Learning New Patterns
```
Remember this pattern: [describe pattern]
Document this architectural decision: [describe decision]
Add this to project knowledge: [describe knowledge]
```

## Memory File Types

### Knowledge Files (`knowledge/topic_name.md`)
- **Purpose**: Ongoing documentation of patterns and architecture
- **Structure**: Markdown files with semantic tags and keywords
- **Usage**: Long-term knowledge that evolves over time

### Session Archives (`sessions/YYYY-MM/YYYY-MM-DD_summary.md`)
- **Purpose**: Consolidated work sessions organized by time
- **Structure**: Date-organized summaries of completed work
- **Usage**: Historical reference for what was done when

### Index Files (`index.json`, `index.md`)
- **Purpose**: Fast lookup and quick reference
- **Structure**: Machine-readable and human-readable indexes
- **Usage**: Instant access to memory metadata

## Workflow Options

### Structured Workflow (Recommended for Complex Projects)
- **Best for**: Large projects, team collaboration, complex architectures
- **Features**: Full memory system with topics, sessions, and indexing
- **Structure**: Organized knowledge base with cross-references
- **Maintenance**: Requires periodic consolidation and indexing

### Simple Workflow (For Vibecoding and Experiments)
- **Best for**: Quick prototypes, personal experiments, small projects
- **Features**: Single-file templates for daily logging
- **Structure**: Minimal organization, focus on rapid iteration
- **Maintenance**: Low overhead, easy to maintain

See `templates/README.md` for guidance on choosing the right workflow.

## Best Practices

### When to Use Memory
- **New Project**: Initialize memory to establish patterns
- **Problem Solving**: Check memory for previous solutions
- **Architecture Decisions**: Document important choices
- **Pattern Recognition**: Learn from repeated solutions
- **Knowledge Transfer**: Share insights across projects

### Memory Maintenance
- **Regular Sync**: Let agents handle automatic syncing
- **Manual Review**: Periodically review what the agent has learned
- **Consolidation**: Allow agents to consolidate related sessions
- **Privacy Check**: Ensure sensitive information goes to private memory

### Effective Prompts
- **Be Specific**: "What did we decide about API error handling?" vs "What about APIs?"
- **Use Context**: Include project-specific details when relevant
- **Natural Language**: Write prompts as you would ask a colleague
- **Follow Up**: Ask for clarification if results aren't what you expected

## Privacy and Security

### Private Memory Handling
- **Automatic Detection**: Agents should automatically detect sensitive information
- **Manual Override**: Use explicit prompts to store sensitive data in private memory
- **Access Control**: Private memory is only accessed when explicitly needed
- **Version Control**: Never commit private memory files to Git

### Security Best Practices
- **Local Storage**: Memory stays on your machine
- **No External Transmission**: No API calls sending memory to external services
- **File Permissions**: Use OS-level permissions for access control
- **Encryption**: Consider encrypting sensitive memory files

## Platform-Specific Features

The memory system includes platform-specific optimizations:

### macOS
- **Cloud Storage Detection**: Automatically detects iCloud, Google Drive
- **Spotlight Integration**: Enhanced search capabilities
- **Path Resolution**: Handles macOS-specific path conventions

### Linux
- **Filesystem Optimizations**: Efficient file operations
- **Search Tools**: Uses optimized search utilities
- **Permission Handling**: Proper Linux permission management

### Windows
- **PowerShell Integration**: Enhanced command execution
- **WSL Support**: Works within Windows Subsystem for Linux
- **Path Resolution**: Handles Windows-specific paths and UNC

## Troubleshooting Memory Issues

### Memory Not Being Used
- **Check Setup**: Verify `AGENTS.md` is properly configured
- **Workspace Access**: Ensure memory directory is in workspace
- **Permissions**: Check agent command permissions
- **Model Capability**: Ensure you're using an agentic-capable model

### Incorrect Information Retrieved
- **Prompt Clarity**: Make prompts more specific
- **Memory Quality**: Review and correct stored information
- **Index Updates**: Manually trigger index updates if needed
- **Consolidation**: Allow agents to consolidate fragmented memories

### Memory Files Not Created
- **Directory Access**: Verify memory directory is writable
- **Command Permissions**: Check agent can execute file operations
- **Path Configuration**: Verify paths in `AGENTS.md` are correct
- **Workspace Setup**: Confirm workspace includes memory directory

### Performance Issues
- **Large Memory Base**: Consider consolidating old sessions
- **Index Corruption**: Manually rebuild indexes if needed
- **Platform Issues**: Check platform-specific optimizations
- **Token Limits**: Use more specific queries to reduce context size

## Advanced Usage

### Custom Memory Organization
- **Override Defaults**: Configure custom directory structures
- **Multiple Memory Bases**: Use different memory directories for different contexts
- **Integration**: Combine with other memory systems or databases

### Memory Analytics
- **Review Patterns**: Analyze what types of information are stored
- **Usage Statistics**: Track memory access patterns
- **Quality Assessment**: Regularly review memory accuracy
- **Optimization**: Refine storage and retrieval strategies

### Integration with Other Tools
- **Version Control**: Memory files work with Git workflows
- **Documentation**: Use memory as living project documentation
- **Knowledge Sharing**: Export memory for team sharing
- **Backup**: Regular backup strategies for memory directories

## Getting Help

If you encounter issues:
1. Check the [Setup Guide](setup-guide.md) for configuration issues
2. Review [Memory System Testing](memory-system-testing/) for validation procedures
3. Check the detailed documentation in `_agents-md/memory/`
4. Verify your AI model supports the required capabilities

The memory system is designed to enhance your development workflow by providing intelligent, context-aware knowledge management that adapts to your working style and project needs.
