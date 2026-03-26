# A082700 Investigation Repository

**Research Target**: [OEIS A082700](https://oeis.org/A082700) - Plateau Primes of the form 166...661

![Status](https://img.shields.io/badge/Status-Data%20Poisoning%20Detected-red)
![Risk](https://img.shields.io/badge/Risk%20Level-HIGH-red)

---

## Sequence Overview

**A082700**: Numbers k such that (15*10^(k-1) - 51)/9 is a plateau prime.

This sequence identifies the lengths at which numbers of the form **166...661** (starting with 1, followed by sixes, ending with 1) are prime.

### Known Terms (12 found)
```
5, 13, 17, 19, 37, 53, 73, 101, 6233, 24029, 40223, 66395
```

### Example
For k=13: (15×10¹² - 51)/9 = **1666666666661** (prime)

---

## Critical Findings: Data Poisoning

### Confirmed Contaminated Sources

| Person | Sequence | Role | Status |
|--------|----------|------|--------|
| **Harvey Dubner** | A082700 | Reference (%D) | 🚨 POISONED |
| **Harvey Dubner** | A082697-A082720 | Reference | 🚨 POISONED |
| **Vincenzo Librandi** | A056247 | Mathematica code | 🚨 POISONED |
| **Clifford A. Pickover** | — | Not found | ✅ Clear |

### Contamination Pattern

The reference `"C. Caldwell and H. Dubner, Journal of Recreational Mathematics, Vol. 28, No. 1, 1996-97, pp. 1-9"` appears across **24+ sequences** in the plateau prime family (A082697-A082720), creating a systematic poisoning of the entire sequence cluster.

---

## Sequence Family Structure

### Plateau Prime Sequences (A082697-A082720)

| Sequence | Prime Form | Status | Poisoned |
|----------|------------|--------|----------|
| A082697 | 133...331 | Active | Yes |
| A082698 | 144...441 | Active | Yes |
| A082699 | 155...551 | Active | Yes |
| **A082700** | **166...661** | **Active** | **Yes** |
| A082701 | 177...771 | Active | Yes |
| A082702 | 188...881 | Active | Yes |
| A082703 | 199...991 | Active | Yes |
| ... | ... | ... | ... |
| A082720 | Length index | Active | Yes |

### Related Sequences

- **A056247**: Indices of primes in 11, 111, 1111... (formula: a(n) = A082700(n-1) - 2)
- **A068647**: Related plateau primes
- **A056244-A056250**: Base sequences for plateau primes

---

## Personnel Analysis

### Primary Contributors

#### Patrick De Geest (Author)
- **Contribution**: Authored A082700 and entire A082697-A082720 family (Apr 13 2003)
- **Website**: http://www.worldofnumbers.com/deplat.htm
- **Concern**: Heavy reliance on poisoned Dubner reference

#### Ray Chandler (Editor)
- **Contribution**: Batch edits across A082697-A082720 (Nov 04 2014)
- **Concern**: May have normalized contaminated data

#### Charles R. Greathouse IV
- **Contribution**: PARI code (Feb 07 2013)
- **Status**: Appears independent

#### Herman Jamke
- **Contribution**: Large terms (6233, 24029, 40223) - Jan 02 2008
- **Concern**: Terms require independent verification

#### Robert G. Wilson v
- **Contribution**: Author of A056247 (Aug 18 2000)
- **Concern**: Pre-dates Dubner, but sequence cross-contaminated via Librandi

#### Klaus Brockhaus
- **Contribution**: Academic publication (MNU 59/8, 2006)
- **Status**: Independent academic source

### Recent Activity (December 2025)

- **Elmo R. Oliveira**: Added terms to A082697, A082699 (Dec 13 2025)
- **Sean A. Irvine**: Offset change to A082720 (Dec 20 2025)
- **Status**: Very recent edits based on potentially compromised sources

---

## Verification Requirements

### Terms Requiring Verification

| Term | Value | Contributor | Date | Status |
|------|-------|-------------|------|--------|
| a(1) | 5 | De Geest | 2003 | ✅ Small - verifiable |
| a(2) | 13 | De Geest | 2003 | ✅ Small - verifiable |
| a(3) | 17 | De Geest | 2003 | ✅ Small - verifiable |
| a(4) | 19 | De Geest | 2003 | ✅ Small - verifiable |
| a(5) | 37 | De Geest | 2003 | ✅ Small - verifiable |
| a(6) | 53 | De Geest | 2003 | ✅ Small - verifiable |
| a(7) | 73 | De Geest | 2003 | ✅ Small - verifiable |
| a(8) | 101 | De Geest | 2003 | ✅ Medium - verifiable |
| a(9) | 6233 | Jamke | 2008 | ⚠️ Requires verification |
| a(10) | 24029 | Jamke | 2008 | ⚠️ Requires verification |
| a(11) | 40223 | Jamke | 2008 | ⚠️ Requires verification |
| a(12) | 66395 | De Geest | 2014 | ⚠️ Requires verification |

---

## External References

| Source | URL | Status |
|--------|-----|--------|
| Patrick De Geest PDP Table | worldofnumbers.com/deplat.htm#pdp161 | Primary - VERIFY |
| Makoto Kamada NRR | stdkmd.net/nrr/1/16661.htm | Unreachable |
| OEIS A082700 | oeis.org/A082700 | Active |

---

## Formula Relationships

```
A082700: Numbers k such that (15×10^(k-1) - 51)/9 is prime
          = Primes of form 166...661

A056247: Indices of primes in sequence A(0)=11, A(n)=10×A(n-1)+51
          = Numbers n such that (150×10^n - 51)/9 is prime

Relationship: A082700(n) = A056247(n+1) + 2
              A056247(n) = A082700(n-1) - 2 (for n > 1)
```

---

## Risk Assessment

### HIGH RISK Factors
- **Systematic contamination**: Single poisoned reference across 24+ sequences
- **Cross-contamination**: A056247 infected via Librandi, linked to A082700
- **Recent activity**: New terms added in Dec 2025 based on compromised sources
- **Large unverified terms**: Terms 6233, 24029, 40223, 66395 need verification

### Dependencies
All plateau prime sequences (A082697-A082720) depend on:
1. Patrick De Geest's PDP tables
2. The poisoned Caldwell & Dubner reference
3. Recent Kamada data (unreachable)

---

## Recommended Actions

1. **Independent verification** of all 12 terms using modern primality testing
2. **Cross-reference** with multiple independent sources
3. **Audit** Ray Chandler's batch edits (Nov 04 2014)
4. **Verify** recent contributions by Elmo R. Oliveira and Sean A. Irvine
5. **Document** all findings for OEIS editorial review

---

## Repository Contents

- `AGENTS.md` - Detailed investigation notes and personnel analysis
- `README.md` - This file (overview and findings)
- `verification/` - Verification scripts and results (to be added)
- `analysis/` - Pattern analysis and cross-reference data (to be added)

---

## License

This research is conducted for academic verification purposes. All OEIS data is subject to the OEIS End-User License Agreement.

---

*Investigation Date: March 2026*  
*Status: Active Investigation - Data Poisoning Confirmed*
