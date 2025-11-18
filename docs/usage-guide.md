<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Usage Guide

This guide explains how to effectively use the agents-md systems in your development workflow. It covers both the Memory System and Critical Thinking framework.

## Memory Structure

The memory system organizes information into three categories:

### 1. Project-Specific Memory (`{MEMORY_DIR}/[project-name]/`)
- **Purpose**: Knowledge specific to your current project
- **Contents**:
  - Project architecture decisions → `context.md`
  - Project-specific patterns and fixes → `topic/topic_name.md`
  - Work sessions → `session/YYYY-MM/YYYY-MM-DD_feature.md`
  - Project-specific preferences → `topic/preferences.md`
  - Index file → `memories.json`
- **Access**: Automatically used when working on this project

### 2. Common Memory (`{MEMORY_DIR}/common/`)
- **Purpose**: User preferences and cross-project patterns
- **Contents**:
  - User preferences (apply to all projects) → `preferences.md`
  - Cross-project patterns → `patterns.md`
  - Global settings and configurations
  - User workflows
- **Access**: Available across all projects

### 3. Private Memory (`{MEMORY_DIR}/private/`) ⚠️
- **Purpose**: Sensitive information storage
- **Contents**:
  - Credentials → `credentials.md`
  - Personal information → `personal_info.md`
  - API keys, passwords, tokens
  - Sensitive settings
- **⚠️ Important**: Never commit private memory files to version control
- **⚠️ Security**: Only accessed when explicitly needed, sensitive data is masked in responses

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
Sync memory for this project. Update index files, consolidate recent sessions if needed, and ensure memories.json is synchronized with actual files in topic/ and session/ directories.
```

#### Memory Update
```
Update project memory with current status. Document recent changes, update index files, and sync any new patterns or architectural decisions.
```

## RAG (Retrieval-Augmented Generation) Features

The memory system uses advanced RAG capabilities for intelligent information retrieval:

### Multi-Level RAG Strategy

1. **Index Lookup** (~100-500 tokens)
   - Check `memories.json` for tags/keywords
   - Fastest, lowest cost method

2. **Semantic Search** (~200-1000 tokens)
   - Use semantic search on memory directory
   - Natural language queries

3. **Header Scan** (~50-200 tokens)
   - Scan file headers to identify relevant sections
   - Locate specific topics quickly

4. **Selective Read** (~200-2000 tokens)
   - Read only identified sections with offset/limit
   - Avoid loading entire large files

### Token Optimization

**Always**:
- Check index (`memories.json`) before searching
- Use semantic search before reading files
- Scan headers before reading content
- Read selectively with offset/limit

**Never**:
- Read entire large files (>500 lines) without scanning
- Load all memory files simultaneously
- Skip index files

### Benefits
- ✅ **80-95% Token Reduction**: Index-first approach vs full search
- ✅ **70-90% Reduction**: Selective reading vs full file
- ✅ **50-70% Reduction**: Header navigation vs full file
- ✅ **Intelligent Retrieval**: Agents understand context and retrieve related information automatically
- ✅ **Scalable**: Handles large memory databases efficiently

## Prompt Examples

Here are practical examples of prompts you can use to interact with the memory system:

### Getting Topics and Patterns
```
What topics are documented in memory for this project?
Show me all the patterns we've established for this project.
What are the documented topics in the topic/ directory?
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

### Topic Files (`topic/topic_name.md`)
- **Purpose**: Ongoing documentation of patterns and architecture
- **Structure**: Markdown files with semantic tags and keywords
- **Usage**: Long-term knowledge that evolves over time
- **Location**: `{MEMORY_DIR}/[project-name]/topic/` or `{MEMORY_DIR}/common/patterns.md`

### Session Archives (`session/YYYY-MM/YYYY-MM-DD_feature.md`)
- **Purpose**: Consolidated work sessions organized by time
- **Structure**: Date-organized summaries of completed work
- **Usage**: Historical reference for what was done when
- **Location**: `{MEMORY_DIR}/[project-name]/session/YYYY-MM/`

### Index Files (`memories.json`, `context.md`)
- **Purpose**: Fast lookup and quick reference
- **Structure**: Machine-readable JSON index and human-readable context
- **Usage**: Instant access to memory metadata
- **Location**: `{MEMORY_DIR}/[project-name]/memories.json` and `context.md`

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

## Critical Thinking System Usage

The Critical Thinking framework works automatically alongside the Memory System to provide intelligent, context-aware decision-making.

### How It Works

The Critical Thinking system automatically:
- **Assesses risk** based on context (security-critical vs prototyping)
- **Verifies facts** before making claims or recommendations
- **Challenges assumptions** when appropriate
- **Adapts communication style** based on audience (expert vs non-technical)

### When It Activates

**High-Risk Scenarios** (Maximum Verification):
- Banking/financial applications
- Healthcare systems
- Production database changes
- Security-critical code
- Payment processing

**Low-Risk Scenarios** (Flexible Approach):
- Quick prototypes
- Debugging sessions
- Documentation updates
- Experimental features
- Personal projects

### Using Critical Thinking

The system works automatically, but you can guide it:

**Request Verification**:
```
Verify this approach before implementing
Check if this library is still maintained
Confirm this is the best practice for our use case
```

**Request Multi-Perspective Analysis**:
```
Consider this from multiple angles: user experience, performance, and maintainability
What are the trade-offs of this approach?
Help me think through the implications
```

**Request Evidence-Based Reasoning**:
```
What evidence supports this decision?
Are there alternatives we should consider?
Challenge my assumptions about this approach
```

### Integration with Memory

Critical Thinking uses Memory System patterns:
- References stored architectural decisions
- Considers documented preferences
- Learns from past decisions
- Applies project-specific patterns

**Example**:
```
Should we use TypeScript or JavaScript for this feature?
```
The agent will:
1. Check memory for project patterns/preferences
2. Consider the context (prototype vs production)
3. Provide evidence-based recommendation
4. Reference any stored decisions about TypeScript usage

## Getting Help

If you encounter issues:
1. Check the [Setup Guide](setup-guide.md) for configuration issues
2. Review [Memory System Testing](memory-system-testing/) for validation procedures
3. Review [Critical Thinking Testing](critical-thinking-testing/) for validation procedures
4. Check the detailed documentation in `_agents-md/memory/` and `_agents-md/critical-thinking/`
5. Verify your AI model supports the required capabilities

The agents-md systems are designed to enhance your development workflow by providing intelligent, context-aware knowledge management and decision-making that adapts to your working style and project needs.
