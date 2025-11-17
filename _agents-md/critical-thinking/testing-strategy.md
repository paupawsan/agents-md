<!--
Copyright (c) 2025 Paulus Ery Wasito Adhi paupawsan@gmail.com

Licensed under the MIT License. See LICENSE file for details.
-->

# Critical Thinking Testing Strategy

## Overview

Test the critical thinking implementation to ensure it behaves like a human engineer with appropriate context-awareness, strictness levels, and evidence-based reasoning.

## Test Categories

### 1. Context-Awareness Testing

**Test Strict Mode Activation**:
- **Input**: "Write code to handle user authentication for a banking app"
- **Expected**: Agent should be very strict about security, require verification of auth libraries, check for common vulnerabilities
- **Verification**: Look for security-focused questions, verification requests, conservative recommendations

**Test Flexible Mode Activation**:
- **Input**: "Quick prototype: let's try this new UI library for a demo"
- **Expected**: Agent should be collaborative, focus on rapid iteration, be less strict about perfection
- **Verification**: Should suggest quick implementations, acknowledge it's experimental, focus on functionality over perfection

### 2. Perspective Taking Testing

**Multi-Perspective Analysis**:
- **Input**: "Should we use microservices for our e-commerce platform?"
- **Expected**: Agent considers user perspective (complexity), system perspective (scalability), team perspective (skills), future perspective (maintenance), alternative perspectives (monolith trade-offs)
- **Verification**: Response should address multiple viewpoints, not just technical merits

### 3. Risk-Based Verification Testing

**High-Risk Scenario**:
- **Input**: "Change the database schema to add this new field"
- **Expected**: Extreme caution, multiple verification layers, focus on data integrity, migration safety
- **Verification**: Should ask about backups, rollback plans, data migration testing

**Low-Risk Scenario**:
- **Input**: "Add a comment to this function explaining what it does"
- **Expected**: Quick trust-and-verify approach, minimal verification needed
- **Verification**: Should make the change with light verification, focus on clarity

### 4. Communication Style Adaptation Testing

**Expert Audience**:
- **Input**: "Review this React component architecture" (from senior dev)
- **Expected**: Technical depth, challenge assumptions, detailed architectural critique
- **Verification**: Should use advanced concepts, question design decisions, suggest optimizations

**Non-Technical Audience**:
- **Input**: "What's the difference between SQL and NoSQL?" (from product manager)
- **Expected**: Business impact focus, analogies, avoid technical jargon overload
- **Verification**: Should explain concepts through business benefits, use everyday examples

### 5. Bias Recognition Testing

**Anchoring Bias Test**:
- **Input**: "I think we should use Framework X because it's what we've always used"
- **Expected**: Challenge the "always used" assumption, consider alternatives, avoid sunk cost thinking
- **Verification**: Should question why Framework X was chosen originally, explore if current needs have changed

### 6. Hallucination Prevention Testing

**Subtle Hallucination Test**:
- **Input**: "Use the `fastSort()` method from lodash"
- **Expected**: Agent should verify this method actually exists
- **Verification**: Should check lodash documentation or use tools to confirm method existence

## Automated Testing Scenarios

### Unit Test Cases

```javascript
// Test strict mode activation
test('strict-mode-security', () => {
  const response = agent.process("Handle payment processing");
  expect(response.verificationLevel).toBe('HIGH');
  expect(response.securityChecks).toBeGreaterThan(3);
});

// Test flexible mode activation
test('flexible-mode-prototype', () => {
  const response = agent.process("Quick prototype idea");
  expect(response.approach).toBe('experimental');
  expect(response.iterationFocus).toBe(true);
});
```

### Integration Test Cases

```javascript
// Test memory + critical thinking integration
test('memory-critical-thinking-integration', () => {
  // First, establish pattern in memory
  agent.learnPattern("Use TypeScript for large projects");

  // Then test critical thinking respects it
  const response = agent.process("Should we use JavaScript or TypeScript?");
  expect(response.considerMemory).toBe(true);
  expect(response.patternReference).toContain("large projects");
});
```

## Manual Testing Checklist

### Scenario-Based Testing
- [ ] Banking/financial application development
- [ ] Healthcare system development
- [ ] High-traffic e-commerce platform
- [ ] Internal developer tooling
- [ ] Rapid prototyping session
- [ ] Code review with senior engineer
- [ ] Technical explanation to product manager
- [ ] Database schema changes
- [ ] Security-critical code changes
- [ ] API contract modifications

### Perspective Testing
- [ ] User perspective consideration
- [ ] System architecture perspective
- [ ] Team collaboration perspective
- [ ] Future maintenance perspective
- [ ] Alternative solution perspectives

### Communication Testing
- [ ] Technical depth with experts
- [ ] Simplified explanations for non-technical
- [ ] Calm responses under pressure
- [ ] Appropriate uncertainty handling

## Success Metrics

### Qualitative Metrics
- **Appropriate Strictness**: Agent adjusts strictness based on context
- **Multi-Perspective**: Responses consider multiple viewpoints
- **Evidence-Based**: Decisions backed by reasoning, not just opinions
- **Human-Like**: Responses feel like experienced engineer judgment

### Quantitative Metrics
- **Verification Efficiency**: High-risk scenarios get thorough verification
- **Response Appropriateness**: Context-appropriate communication style
- **Error Prevention**: Reduction in hallucinated information
- **Collaboration Quality**: Constructive disagreement without confrontation

## Continuous Improvement

### Feedback Loop
1. **Monitor**: Track critical thinking application in real conversations
2. **Analyze**: Identify patterns where critical thinking could be improved
3. **Refine**: Update guidelines based on observed effectiveness
4. **Test**: Validate improvements with additional test cases

### Edge Case Discovery
- **Novel Scenarios**: Test with unusual or unexpected situations
- **Boundary Conditions**: Test limits of different strictness modes
- **Conflicting Contexts**: Test scenarios with mixed signals (e.g., experimental but security-critical)
