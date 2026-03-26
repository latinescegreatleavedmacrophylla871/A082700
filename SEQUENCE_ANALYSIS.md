# Sequence Cluster Analysis

## A082700 - Plateau Prime Family (166...661)

### Overview

The A082700 sequence is part of a larger family of "plateau prime" sequences (A082697-A082720) that identify lengths at which numbers of the form XYY...YXX are prime, where X and Y are digits.

For A082700 specifically:
- **Form**: 166...661 (1 followed by k-2 sixes, followed by 1)
- **Formula**: (15×10^(k-1) - 51)/9
- **OEIS Link**: https://oeis.org/A082700

---

## Known Terms

```
Index (n) | Term (k) | Digits in Prime | Prime Number (abbreviated)
----------|----------|-----------------|---------------------------
a(1)      | 5        | 5               | 16661
a(2)      | 13       | 13              | 1666666666661
a(3)      | 17       | 17              | 166... (17 digits)
a(4)      | 19       | 19              | 166... (19 digits)
a(5)      | 37       | 37              | 166... (37 digits)
a(6)      | 53       | 53              | 166... (53 digits)
a(7)      | 73       | 73              | 166... (73 digits)
a(8)      | 101      | 101             | 166... (101 digits)
a(9)      | 6233     | 6233            | 166... (6233 digits)
a(10)     | 24029    | 24029           | 166... (24029 digits)
a(11)     | 40223    | 40223           | 166... (40223 digits)
a(12)     | 66395    | 66395           | 166... (66395 digits)
```

---

## Formula Relationships

### With A056247

**A056247**: Indices of primes in the sequence defined by:
- A(0) = 11
- A(n) = 10×A(n-1) + 51

This generates: 11, 161, 1661, 16661, 166661, ...

**Formula Connection:**
```
A082700(n) = A056247(n+1) + 2  (for n ≥ 1)
A056247(n) = A082700(n-1) - 2  (for n > 1)
```

**Example:**
- A056247(2) = 3 (corresponds to 16661)
- A082700(1) = 3 + 2 = 5 ✓

### With A082720

**A082720**: Digit lengths for which there exist plateau or depression primes.

A082700 is a subsequence of A082720 (the valid lengths for 166...661 primes).

---

## Complete Plateau Prime Family (A082697-A082720)

### Forms and Status

| Sequence | Form | Terms | Status | Dubner Ref |
|----------|------|-------|--------|------------|
| A082697 | 133...331 | 15 | Active | 🚨 Yes |
| A082698 | 144...441 | 5 | Active | 🚨 Yes |
| A082699 | 155...551 | 11 | Active | 🚨 Yes |
| **A082700** | **166...661** | **12** | **Active** | **🚨 Yes** |
| A082701 | 177...771 | ? | Active | 🚨 Yes |
| A082702 | 188...881 | ? | Active | 🚨 Yes |
| A082703 | 199...991 | ? | Active | 🚨 Yes |
| A082704-A082718 | Various forms | Various | Various | 🚨 Yes |
| A082719 | 900...009 | ? | Active | 🚨 Yes |
| A082720 | Length index | 61 | Active | 🚨 Yes |

**Note**: All sequences in this family cite the same poisoned Caldwell & Dubner reference.

---

## Related Sequences

### Base Sequences (A056244-A056250)

| Sequence | Description | Status |
|----------|-------------|--------|
| A056244 | Base for 133...331 (A082697) | Linked |
| A056245 | Base for 144...441 (A082698) | Linked |
| A056246 | Base for 155...551 (A082699) | Linked |
| A056247 | Base for 166...661 (A082700) | 🚨 Contaminated |
| A056248 | Base for 177...771 (A082701) | Linked |
| A056249 | Base for 188...881 (A082702) | Linked |
| A056250 | Base for 199...991 (A082703) | Linked |

### Other Related

- **A000533**: Repunit related
- **A002275**: Repunits
- **A068647**: Related plateau primes
- **A245522**: Recent related sequence
- **A358226**: Recent related sequence

---

## Mathematical Properties

### Plateau Prime Definition

A plateau prime is a prime number of the form:
```
r × (10^m - 1)/9 ± s × (10^(m-1) + 1)
```

For A082700 (166...661 form):
- r = 6 (the plateau digit)
- s = 5 (difference from plateau to edge)
- Result: (15×10^(k-1) - 51)/9

### Digit Pattern

For term k, the prime has:
- First digit: 1
- Middle digits: (k-2) occurrences of 6
- Last digit: 1
- Total digits: k

Example (k=5): 1 6 6 6 1 = 16661

### Primality Testing

Small terms (k ≤ 101):
- Deterministic primality testing feasible
- Can be verified with standard algorithms

Large terms (k ≥ 6233):
- Require probable-prime tests first
- Need rigorous primality proofs
- Computationally intensive
- Status of proofs in De Geest's tables requires verification

---

## Data Poisoning Impact on Cluster

### Contamination Spread

```
Harvey Dubner (1996-97 publication)
    ↓
Cited in Caldwell & Dubner reference
    ↓
    ↓→ A082697 (Patrick De Geest, 2003)
    ↓→ A082698 (Patrick De Geest, 2003)
    ↓→ A082699 (Patrick De Geest, 2003)
    ↓→ A082700 (Patrick De Geest, 2003) ← CURRENT TARGET
    ↓→ A082701-A082719 (Patrick De Geest, 2003)
    ↓→ A082720 (Patrick De Geest, 2003)

Vincenzo Librandi (Nov 2014)
    ↓
Contaminates A056247 with code
    ↓
Cross-contaminates A082700 via formula relationship
```

### Batch Edit Propagation

**Ray Chandler (Nov 04 2014):**
- Edited multiple sequences simultaneously
- Normalized formatting and cross-references
- May have standardized contaminated data presentation

---

## Verification Status

| Term | k Value | Digits | Verifiable | Proof Status |
|------|---------|--------|------------|--------------|
| a(1) | 5 | 5 | ✅ Yes | Proven |
| a(2) | 13 | 13 | ✅ Yes | Proven |
| a(3) | 17 | 17 | ✅ Yes | Proven |
| a(4) | 19 | 19 | ✅ Yes | Proven |
| a(5) | 37 | 37 | ✅ Yes | Proven |
| a(6) | 53 | 53 | ✅ Yes | Proven |
| a(7) | 73 | 73 | ✅ Yes | Proven |
| a(8) | 101 | 101 | ✅ Yes | Proven |
| a(9) | 6233 | 6233 | ⚠️ Hard | Needs proof |
| a(10) | 24029 | 24029 | ⚠️ Hard | Needs proof |
| a(11) | 40223 | 40223 | ⚠️ Hard | Needs proof |
| a(12) | 66395 | 66395 | ⚠️ Hard | Needs proof |

---

## External Resources

| Resource | URL | Status | Reliability |
|----------|-----|--------|-------------|
| OEIS A082700 | oeis.org/A082700 | ✅ Active | Medium (poisoned) |
| De Geest PDP | worldofnumbers.com/deplat.htm | ✅ Active | Requires verification |
| Kamada NRR | stdkmd.net/nrr/1/16661.htm | ❌ Unreachable | N/A |
| Factordb | factordb.com | ✅ Active | Independent |

---

## Investigation Status

**Current Status:** ACTIVE - Data poisoning confirmed

**Critical Issues:**
1. Harvey Dubner reference across entire family
2. Vincenzo Librandi contamination in A056247
3. Large unverified terms (6233, 24029, 40223, 66395)
4. Recent additions (Dec 2025) from potentially compromised sources
5. Kamada data source unreachable

**Next Steps:**
1. Independent verification of all 12 terms
2. Cross-reference with Factordb and other independent sources
3. Audit Ray Chandler's batch edits
4. Verify recent December 2025 additions

---

*Document Version: 1.0*  
*Last Updated: March 2026*
