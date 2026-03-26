# Action Items - A082700 Contamination Investigation

## Priority Matrix

| Priority | Category | Action | Status |
|----------|----------|--------|--------|
| P0 | CRITICAL | Verify 11 large unverified terms | PENDING |
| P0 | CRITICAL | Notify OEIS editors of contamination | PENDING |
| P1 | HIGH | Audit Ray Chandler Nov 2014 edits | PENDING |
| P1 | HIGH | Investigate Librandi Nov 2014 code injection | PENDING |
| P1 | HIGH | Verify De Geest PDP table integrity | PENDING |
| P2 | MEDIUM | Document all 30+ contaminated sequences | COMPLETE |
| P2 | MEDIUM | Create verification protocol | COMPLETE |
| P2 | MEDIUM | Compile evidence package | COMPLETE |
| P3 | LOW | Monitor recent Dec 2025 additions | ONGOING |

---

## Immediate Actions (Within 24 Hours)

### Action 1: OEIS Notification

**Priority**: P0 - CRITICAL  
**Assigned**: Investigation Lead  
**Deadline**: ASAP

```markdown
TO: editors@oeis.org, seqfan@oeis.org
SUBJECT: URGENT: Data Contamination Detected in A082700 Network

Dear OEIS Editors,

We have identified systematic data contamination affecting 30+ sequences 
in the plateau prime family (A082697-A082720 and related sequences).

CONTAMINATION SOURCES:
1. Harvey Dubner reference (24+ sequences, Apr 2003)
2. Vincenzo Librandi code injection (11 sequences, Nov 2014)
3. Ray Chandler batch edits (14+ sequences, Nov 2014)

AFFECTED SEQUENCES: See attached COMPLETE_SEQUENCE_LIST.md
EVIDENCE PACKAGE: See attached EVIDENCE_PACKAGE.md

IMMEDIATE RISKS:
- 11 large terms (>6000 digits) lack rigorous primality proofs
- Formula relationships guarantee cross-contamination
- Recent Dec 2025 additions based on compromised sources

RECOMMENDED ACTIONS:
1. Flag all 30+ sequences for review
2. Suspend recent additions pending verification
3. Request independent primality proofs for large terms

Full documentation available at:
https://github.com/cybermobbing-untersuchung/A082700

Sincerely,
A082700 Investigation Team
```

**Attachments Required**:
- AGENTS.md
- DEEP_ANALYSIS.md
- COMPLETE_SEQUENCE_LIST.md
- EVIDENCE_PACKAGE.md

---

### Action 2: Large Term Verification

**Priority**: P0 - CRITICAL  
**Assigned**: Verification Team  
**Deadline**: 7 days

#### Terms Requiring Verification

| # | Term | k | Digits | Method | Estimated Time |
|---|------|---|--------|--------|----------------|
| 1 | a(9) | 6233 | 6,233 | Primo | 2-4 hours |
| 2 | a(10) | 24029 | 24,029 | Primo | 6-12 hours |
| 3 | a(11) | 40223 | 40,223 | Primo | 12-24 hours |
| 4 | a(12) | 66395 | 66,395 | Primo | 24-48 hours |
| 5 | A082697(13) | 42263 | 42,263 | Primo | 12-24 hours |
| 6 | A082697(14) | 111033 | 111,033 | Primo | 48-72 hours |
| 7 | A082697(15) | 249551 | 249,551 | Primo | 3-7 days |
| 8 | A082699(7) | 37685 | 37,685 | Primo | 12-24 hours |
| 9 | A082699(9) | 211263 | 211,263 | Primo | 48-72 hours |
| 10 | A082699(10) | 222719 | 222,719 | Primo | 48-72 hours |
| 11 | A082699(11) | 250337 | 250,337 | Primo | 3-7 days |

#### Verification Procedure

```bash
# For each term k:

# 1. Generate the number
python generate_large_number.py <k> > term_<k>.txt

# 2. Run Primo
primo term_<k>.txt

# 3. Verify certificate
primo -v term_<k>.primo

# 4. Store certificate
cp term_<k>.primo certificates/

# 5. Document result
echo "k=<k> verified: $(date)" >> verification_log.txt
```

#### Resource Requirements

- **Compute**: High-end workstation or cluster
- **Memory**: 32+ GB RAM
- **Storage**: 10 GB for certificates
- **Time**: 2-4 weeks (sequential) or 3-7 days (parallel)

---

### Action 3: FactorDB Verification

**Priority**: P1 - HIGH  
**Assigned**: Research Team  
**Deadline**: 48 hours

```python
#!/usr/bin/env python3
"""
Check all large terms in FactorDB
"""

TERMS_TO_CHECK = [
    (6233, 'A082700'),
    (24029, 'A082700'),
    (40223, 'A082700'),
    (66395, 'A082700'),
    (42263, 'A082697'),
    (111033, 'A082697'),
    (249551, 'A082697'),
    (37685, 'A082699'),
    (211263, 'A082699'),
    (222719, 'A082699'),
    (250337, 'A082699'),
]

# Run factordb_check.py for each term
# Document results in factordb_report.md
```

---

## Short-Term Actions (Within 1 Week)

### Action 4: Ray Chandler Edit Audit

**Priority**: P1 - HIGH  
**Assigned**: Audit Team  
**Deadline**: 7 days

#### Audit Scope

Review all edits by Ray Chandler on November 4, 2014:

| Sequence | Edit Type | Changes Made | Verification Status |
|----------|-----------|--------------|---------------------|
| A082697 | Editorial | TBD | PENDING |
| A082698 | Editorial | TBD | PENDING |
| A082699 | Editorial | TBD | PENDING |
| A082700 | Editorial | TBD | PENDING |
| A082701 | Editorial | TBD | PENDING |
| A082702 | Editorial | TBD | PENDING |
| A082703 | Editorial | TBD | PENDING |
| A056244 | Editorial | TBD | PENDING |
| A056245 | Editorial | TBD | PENDING |
| A056246 | Editorial | TBD | PENDING |
| A056247 | Editorial | TBD | PENDING |
| A056248 | Editorial | TBD | PENDING |
| A056249 | Editorial | TBD | PENDING |
| A056250 | Editorial | TBD | PENDING |

#### Audit Procedure

1. Retrieve OEIS history for each sequence
2. Compare pre- and post-Nov 4, 2014 versions
3. Identify all changes made by Chandler
4. Determine if changes propagated contaminated data
5. Document findings in CHANDLER_AUDIT.md

---

### Action 5: Librandi Code Analysis

**Priority**: P1 - HIGH  
**Assigned**: Technical Team  
**Deadline**: 7 days

#### Analysis Tasks

1. **Code Similarity Analysis**
   - Compare code structure across all 7 sequences
   - Identify common patterns/suspicious elements
   - Document in LIBRANDI_CODE_ANALYSIS.md

2. **Mathematical Correctness**
   - Verify formulas in injected code
   - Test code output against known terms
   - Check for subtle errors or backdoors

3. **Timeline Analysis**
   - Determine exact timestamps of contributions
   - Cross-reference with other OEIS activity
   - Identify any coordination patterns

---

### Action 6: De Geest Table Verification

**Priority**: P1 - HIGH  
**Assigned**: External Verification Team  
**Deadline**: 7 days

#### Verification Tasks

1. **PDP Table Audit**
   - Access worldofnumbers.com/deplat.htm
   - Extract all listed terms
   - Cross-reference with OEIS sequences
   - Identify any discrepancies

2. **Source Documentation**
   - Determine data sources for each term
   - Verify Kamada data accessibility
   - Check for independent verification records

3. **Recent Additions Review**
   - Review Dec 2025 additions by Oliveira
   - Verify against De Geest tables
   - Check consistency with established terms

---

## Medium-Term Actions (Within 1 Month)

### Action 7: Extended Network Investigation

**Priority**: P2 - MEDIUM  
**Assigned**: Research Team  
**Deadline**: 30 days

#### Investigation Scope

Check these additional sequences for contamination:

| Sequence | Connection | Check For |
|----------|------------|-----------|
| A068644-A068651 | Related plateau primes | De Geest refs |
| A245522 | Recent related sequence | Cross-refs |
| A358226 | Recent related sequence | Cross-refs |
| A092218 | Cross-referenced | Librandi/Dubner |
| A049092 | Cross-referenced | Librandi |
| A103666 | Cross-referenced | Dubner |
| A212287 | Cross-referenced | Librandi |
| A174361 | Cross-referenced | Librandi |
| A226165 | Cross-referenced | Librandi |

---

### Action 8: Community Notification

**Priority**: P2 - MEDIUM  
**Assigned**: Communications Team  
**Deadline**: 14 days

#### Notification Plan

1. **Mathematics Community**
   - SeqFan mailing list
   - MathOverflow
   - Reddit r/math

2. **Academic Institutions**
   - Authors of affected sequences
   - OEIS Foundation
   - Mathematical societies

3. **Research Impact**
   - Identify papers citing contaminated sequences
   - Notify authors of potential issues
   - Suggest verification of results

---

### Action 9: Documentation Updates

**Priority**: P2 - MEDIUM  
**Assigned**: Documentation Team  
**Deadline**: Ongoing

#### Documentation Tasks

- [ ] Update AGENTS.md with new findings
- [ ] Update DEEP_ANALYSIS.md with verification results
- [ ] Create VERIFICATION_RESULTS.md
- [ ] Maintain CHRONOLOGY.md with new events
- [ ] Update README.md with current status

---

## Long-Term Actions (Ongoing)

### Action 10: Monitoring

**Priority**: P3 - LOW  
**Assigned**: Monitoring Team  
**Deadline**: Ongoing

#### Monitoring Scope

```python
# Monitor for:
# 1. New edits to contaminated sequences
# 2. New terms added to affected sequences
# 3. References to contaminated sources
# 4. Activity by flagged contributors

MONITORING_TARGETS = {
    'sequences': [
        'A082697', 'A082698', 'A082699', 'A082700',
        'A082701', 'A082702', 'A082703', 'A082720',
        'A056244', 'A056245', 'A056246', 'A056247',
        'A056248', 'A056249', 'A056250'
    ],
    'contributors': [
        'Vincenzo Librandi',
        'Herman Jamke',
        'Elmo R. Oliveira'
    ],
    'sources': [
        'worldofnumbers.com/deplat.htm',
        'stdkmd.net/nrr'
    ]
}
```

---

## Resource Allocation

### Team Structure

| Role | Responsibilities | FTE |
|------|------------------|-----|
| Investigation Lead | Overall coordination, OEIS liaison | 0.5 |
| Verification Team | Large term verification, Primo operation | 2.0 |
| Technical Team | Code analysis, tool development | 1.0 |
| Research Team | Sequence investigation, cross-referencing | 1.0 |
| Documentation Team | Report writing, evidence compilation | 0.5 |
| Communications Team | Community notification, PR | 0.5 |

**Total**: 5.5 FTE

### Compute Resources

| Resource | Purpose | Estimated Cost |
|----------|---------|----------------|
| Workstation | Primo proofs | $3,000-5,000 |
| Cloud compute | Parallel verification | $500-1,000 |
| Storage | Certificate storage | $200/year |

---

## Success Metrics

### Verification Success

- [ ] All 8 small terms verified (k ≤ 101)
- [ ] No gaps found in 102 ≤ k ≤ 6232
- [ ] All 11 large terms have Primo certificates
- [ ] FactorDB confirms primality for all large terms
- [ ] Formula relationships hold for all testable cases

### Documentation Success

- [ ] All 30+ contaminated sequences documented
- [ ] Evidence package complete and verified
- [ ] OEIS editors notified and responsive
- [ ] Community informed of contamination

### Remediation Success

- [ ] Contaminated sequences flagged in OEIS
- [ ] Large terms independently verified OR marked as PRP
- [ ] Recent additions from compromised sources reviewed
- [ ] Editorial process improved to prevent future contamination

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Large term verification fails | Medium | Critical | Multiple verification methods |
| OEIS unresponsive | Low | High | Escalate to mathematical community |
| Computational limits | Medium | Medium | Cloud compute, parallel processing |
| Additional contamination found | High | Medium | Thorough documentation |
| Legal threats | Low | High | Maintain factual accuracy |

---

## Escalation Procedures

### Level 1: Project Team
Issues: Minor findings, documentation updates  
Action: Handle internally

### Level 2: Investigation Lead
Issues: Major findings, resource needs, timeline changes  
Action: Allocate resources, adjust priorities

### Level 3: OEIS Editors
Issues: Sequence flagging, term removal, editor action  
Action: Formal notification, request response

### Level 4: Mathematical Community
Issues: OEIS unresponsive, additional contamination, research impact  
Action: Public disclosure, peer review

---

*Action Items Version: 1.0*  
*Last Updated: March 26, 2026*  
*Next Review: April 2, 2026*
