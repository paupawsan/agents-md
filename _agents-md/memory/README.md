<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Memory System Documentation

This directory contains comprehensive documentation for the agent-memory system.

## Documentation Files

- **[architecture.md](architecture.md)** - Core system architecture, file formats, and design principles
- **[organization.md](organization.md)** - Memory organization rules, file naming conventions, and workflow guidelines
- **[commands.md](commands.md)** - Safe command usage for memory operations (CRITICAL for agents)
- **[rag-guide.md](rag-guide.md)** - RAG (Retrieval-Augmented Generation) strategies and token optimization techniques
- **[platform-support.md](platform-support.md)** - Platform-specific optimizations and tool recommendations

## Quick Start

1. **CRITICAL: Read [commands.md](commands.md)** for safe command usage rules
2. **Read [architecture.md](architecture.md)** to understand the system design
3. **Read [organization.md](organization.md)** for memory management rules
4. **Read [rag-guide.md](rag-guide.md)** for efficient memory retrieval
5. **Read [platform-support.md](platform-support.md)** for platform-specific setup

## Key Concepts

### Memory Organization
- **Knowledge Files**: Ongoing documentation of patterns and architecture
- **Session Archives**: Consolidated work sessions organized by period
- **Index Files**: Fast lookup and quick reference

### RAG Strategy
- **Index-First**: Check index files before searching content
- **Semantic Search**: Use semantic search tools before reading files
- **Selective Reading**: Read only relevant sections, not entire files
- **Token Optimization**: 80-95% token reduction through intelligent retrieval

### Platform Support
- **macOS**: Cloud storage detection, Spotlight integration
- **Linux**: Filesystem optimizations, efficient search tools
- **Windows**: PowerShell integration, WSL support

## For Agent Developers

When implementing memory operations:
1. **CRITICAL: Follow safety rules in [commands.md](commands.md)**
2. Follow the architecture defined in [architecture.md](architecture.md)
3. Adhere to organization rules in [organization.md](organization.md)
4. Use RAG strategies from [rag-guide.md](rag-guide.md)
5. Implement platform detection from [platform-support.md](platform-support.md)

## For Users

When using the memory system:
1. Let agents handle memory operations automatically
2. Use natural language prompts to query memory
3. Trust the RAG system to retrieve relevant information
4. Check index files for quick status updates

## Support

For questions or issues, refer to the main [README.md](../README.md) or the specific documentation files listed above.

<!-- #memory-system #documentation #agent-guidelines #rag #retrieval-strategies #platform-support #command-safety -->

