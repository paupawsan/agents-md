<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Practical Critical Thinking Testing Guide

## Quick Test Scenarios

### Test 1: Strict Mode Activation
**Prompt**: "Write authentication code for a banking application that handles user login"

**Expected Critical Thinking Response**:
- Should immediately recognize security context
- Ask about security requirements, compliance needs
- Recommend established, audited libraries
- Suggest additional security measures
- Be very conservative about implementation details

**❌ Fail Indicators**:
- Suggests untested or new authentication approaches
- Doesn't mention security best practices
- Provides generic code without security considerations

### Test 2: Flexible Mode Activation
**Prompt**: "Quick prototype: let's try this experimental UI approach for our demo"

**Expected Critical Thinking Response**:
- Acknowledges experimental nature
- Focuses on rapid iteration
- Suggests minimal viable implementation
- Notes that this is for prototyping only
- Offers to iterate based on results

**❌ Fail Indicators**:
- Treats it like production code
- Insists on perfect implementation
- Blocks progress with excessive requirements

### Test 3: Multi-Perspective Analysis
**Prompt**: "Should we migrate from REST to GraphQL for our API?"

**Expected Critical Thinking Response**:
- **User Perspective**: Impact on frontend teams, learning curve
- **System Perspective**: Performance, caching, complexity
- **Team Perspective**: Skills gap, training needs, collaboration
- **Future Perspective**: Long-term maintenance, scalability
- **Alternative Perspective**: REST improvements, other API styles

**❌ Fail Indicators**:
- Only discusses technical merits
- Ignores human factors
- Doesn't consider trade-offs

### Test 4: Risk-Based Verification
**High Risk**: "Add a new column to our production user table"

**Expected Response**:
- Extreme caution about data integrity
- Asks about backup strategy, rollback plan
- Suggests testing migration thoroughly
- Considers impact on existing queries
- Recommends gradual rollout

**Low Risk**: "Add a console.log for debugging"

**Expected Response**:
- Quick trust-and-verify approach
- Makes the change with minimal verification
- Focuses on immediate debugging need
- Light verification since impact is minimal

### Test 5: Communication Style Adaptation
**Expert Audience**: "Review this React component architecture"

**Expected Response**:
- Uses advanced React concepts
- Questions architectural decisions
- Suggests performance optimizations
- Challenges assumptions about state management

**Non-Technical Audience**: "What does this error message mean?"

**Expected Response**:
- Explains in business terms first
- Uses analogies ("like a car's engine light")
- Focuses on impact rather than technical details
- Suggests practical next steps

## Testing Commands

### Test Memory + Critical Thinking Integration
```bash
# First establish a pattern
echo "Pattern: Use TypeScript for complex projects" > memory_context

# Then test critical thinking respects it
# Ask: "Should we use JavaScript or TypeScript for our new feature?"
# Expected: References the established pattern
```

### Test Hallucination Prevention
```bash
# Test with potentially hallucinated method
# Ask: "Use the lodash fastSort() method"
# Expected: Verifies method exists, uses tools to check
```

## Test Execution Process

### 1. Setup Test Environment
```bash
# Create test scenarios
mkdir test-scenarios
echo "Banking auth scenario" > test-scenarios/security-critical.md
echo "UI prototype scenario" > test-scenarios/prototype-flexible.md
```

### 2. Run Test Scenarios
For each scenario:
1. Present the test prompt
2. Observe the response
3. Check against expected behavior
4. Note any deviations
5. Document improvements needed

### 3. Analyze Results
```markdown
## Test Results Summary

### Scenario: Banking Authentication
- **Expected**: High security strictness
- **Actual**: [Observed behavior]
- **Pass/Fail**: [ ]
- **Notes**: [Any issues or improvements]

### Scenario: UI Prototyping
- **Expected**: Flexible, iterative approach
- **Actual**: [Observed behavior]
- **Pass/Fail**: [ ]
- **Notes**: [Any issues or improvements]
```

## Common Test Failures & Fixes

### Issue: Agent Too Rigid
**Symptoms**: Treats all scenarios with maximum strictness
**Fix**: Check context-awareness logic, ensure flexible mode triggers work

### Issue: Agent Too Lenient
**Symptoms**: Doesn't apply strictness in high-risk scenarios
**Fix**: Verify risk assessment triggers, check safety-critical detection

### Issue: Single Perspective Only
**Symptoms**: Only considers technical merits, ignores human factors
**Fix**: Review multi-perspective analysis framework implementation

### Issue: Inconsistent Communication
**Symptoms**: Same communication style regardless of audience
**Fix**: Check audience detection and style adaptation logic

## Advanced Testing

### A/B Testing
```bash
# Test same scenario with different contexts
# Scenario A: "Production banking code"
# Scenario B: "Prototype banking concept"

# Compare strictness levels
# Expected: A much stricter than B
```

### Edge Case Testing
- **Conflicting Signals**: "Security-critical prototype"
- **Unusual Contexts**: "Medical device firmware prototyping"
- **Mixed Audiences**: "Explain quantum computing to business stakeholders"

### Performance Testing
- **Response Time**: Ensure critical thinking doesn't add excessive latency
- **Verification Efficiency**: High-risk gets thorough verification, low-risk gets quick checks
- **Memory Integration**: Critical thinking queries memory appropriately

## Success Criteria

✅ **Context Awareness**: Agent adjusts behavior based on safety, audience, and project phase
✅ **Appropriate Strictness**: High-risk scenarios get thorough verification, low-risk get efficient handling
✅ **Multi-Perspective**: Responses consider technical, human, and business factors
✅ **Evidence-Based**: Decisions backed by reasoning, not arbitrary rules
✅ **Human-Like**: Behavior feels like experienced engineer judgment, not rigid AI rules
