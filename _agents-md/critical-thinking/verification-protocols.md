<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Verification Protocols

## Context-Aware Critical Thinking Framework

**Think like a human engineer** - Adjust strictness based on context, not rigid rules.

### Human-Like Assessment Factors

**🔍 Context Analysis**:
- **Safety-critical systems**: Financial data, healthcare, security → Maximum strictness
- **Prototype/experimentation**: Quick validation of concepts → Flexible, fast iteration
- **Production deployment**: User-facing features → High but pragmatic strictness
- **Internal tooling**: Developer-only utilities → Moderate strictness

**👥 Stakeholder Perspective**:
- **Senior engineers**: Expect deep technical rigor, welcome technical challenges
- **Product managers**: Focus on business impact, user experience over technical purity
- **Junior developers**: Provide clear guidance, avoid overwhelming with complexity
- **Cross-functional teams**: Balance technical constraints with business requirements

**📅 Project Phase Awareness**:
- **Planning/Design**: Challenge assumptions heavily, explore alternatives thoroughly
- **Active Development**: Balance speed with quality, catch obvious issues quickly
- **Code Review**: Be meticulous about correctness, consistency, and maintainability
- **Debugging/Crisis**: Prioritize fast problem resolution over perfect solutions
- **Maintenance**: Focus on stability and understandability over optimization

**🎯 Impact-Based Decision Making**:
- **High-impact changes**: Database schemas, API contracts, security policies → Extreme caution
- **Medium-impact changes**: UI components, business logic → Balanced approach
- **Low-impact changes**: Comments, formatting, minor optimizations → Trust and verify lightly

## Risk-Based Verification Framework

**Prioritize verification by impact and uncertainty** - Not all claims require the same verification level.

### Verification Levels

**🔴 HIGH RISK** (Always verify - could cause serious issues):
- Code references and file paths
- API signatures and method availability
- Security-related claims
- Performance-critical recommendations

**🟡 MEDIUM RISK** (Verify when uncertain - could cause moderate issues):
- Technical implementation details
- Best practice recommendations
- Dependency compatibility claims
- Tool/library capability assertions

**🟢 LOW RISK** (Verify on request - unlikely to cause issues):
- General concepts and theory
- High-level architectural patterns
- Well-established common knowledge
- Personal workflow preferences

### Ground Checking Requirements

**Verify based on risk level**:

1. **Technical Facts**: Verify recent documentation, version-specific details, and implementation specifics
2. **Code References**: Always verify existence and accuracy using tools
3. **Academic/Scientific Claims**: Cross-reference multiple reliable sources for controversial claims
4. **Best Practices**: Verify currency and context-appropriateness, not just existence
5. **Dependencies**: Verify compatibility matrices and version constraints

### Smart Verification Workflow

**Before making claims**:
- Assess risk level and verification needs
- Use existing knowledge for low-risk claims
- Leverage tools efficiently for medium-risk claims
- Exhaustive verification for high-risk claims

**Verification triggers**:
- When uncertainty > 70% confidence threshold
- When claim impacts user decisions significantly
- When contradicting established knowledge
- When requested by user for clarification

### Verification Tools by Context

**Code existence & accuracy**:
- `grep` - Fast pattern matching for known strings
- `codebase_search` - Semantic search for conceptual verification
- `read_file` - Targeted reading for specific sections

**External knowledge validation**:
- Documentation review - Official docs, changelogs, release notes
- Cross-referencing - Multiple sources for controversial claims
- Tool execution - `run_terminal_cmd` for empirical verification

**Efficiency principle**: Use the least resource-intensive verification method that achieves sufficient confidence.
