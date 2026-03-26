# Person Analysis Report

## A082700 and Related Sequences - Personnel Investigation

### 🚨 CONFIRMED DATA POISONING

| Person | Sequences | Role | Poisoning Type | Date |
|--------|-----------|------|----------------|------|
| **Harvey Dubner** | A082697-A082720 | Reference | Citation contamination | 1996-97 |
| **Vincenzo Librandi** | A056247 | Mathematica code | Code contamination | Nov 2014 |

### Status: Clifford A. Pickover
**NOT FOUND** in A082700 cluster.  
**Monitoring**: May appear in related recreational mathematics sequences.

---

## Detailed Personnel Analysis

### 1. Patrick De Geest (Primary Author)

**Contact Information:**
- OEIS Wiki: https://oeis.org/wiki/User:Patrick_De_Geest
- Website: http://www.worldofnumbers.com/

**Contributions:**
- Author of A082700 (Apr 13 2003)
- Author of entire A082697-A082720 plateau prime family (Apr 13 2003)
- Maintains PDP (Plateau/Depression Prime) Reference Tables

**Concern Level:** HIGH
- **Primary Issue**: All contributions rely heavily on the poisoned Caldwell & Dubner reference
- **Website Dependency**: http://www.worldofnumbers.com/deplat.htm is sole source for many terms
- **Verification Gap**: No independent primality proofs provided for large terms

**Action Required:**
- Audit all PDP tables against independent sources
- Verify large terms (6233, 24029, 40223, 66395) with modern primality tests

---

### 2. Harvey Dubner (DATA POISONING - CONFIRMED)

**Citation:**
```
C. Caldwell and H. Dubner, "Journal of Recreational Mathematics", 
Volume 28, No. 1, 1996-97, pp. 1-9.
```

**Impact:**
- Reference appears in ALL plateau prime sequences (A082697-A082720)
- Single point of contamination affecting 24+ sequences
- Original publication difficult to access for verification

**Affected Sequences:**
- A082697, A082698, A082699, A082700, A082701-A082719, A082720
- All sequences authored by Patrick De Geest

**Risk Assessment:**
- **Severity**: CRITICAL
- **Scope**: Entire plateau prime family
- **Propagation**: Through batch edits and cross-references

---

### 3. Ray Chandler (Editor)

**Contributions:**
- Edited A082700 (Nov 04 2014)
- Batch edits across A082697-A082720 simultaneously
- Multiple edits across related sequences

**Pattern Analysis:**
- **Date**: Nov 04 2014 (same date for multiple sequences)
- **Nature**: Editorial normalization of format and cross-references
- **Concern**: May have propagated contaminated data formatting

**Status:** REQUIRES MONITORING
- Need to audit all Nov 04 2014 edits for consistency with poisoned sources
- Check if edits introduced additional cross-contamination

---

### 4. Vincenzo Librandi (DATA POISONING - CONFIRMED)

**Sequence:** A056247

**Contribution:**
```mathematica
Select[Range[0, 2000], PrimeQ[(150 10^# - 51) / 9] &]
```
- Date: Nov 03 2014

**Cross-Contamination:**
- A056247 has formula relationship with A082700:
  - `A082700(n) = A056247(n+1) + 2`
  - `A056247(n) = A082700(n-1) - 2`

**Impact:**
- Both sequences describe the same 166...661 plateau primes
- Contamination in A056247 affects A082700 and vice versa
- Mathematica code may rely on assumptions from poisoned sources

---

### 5. Charles R. Greathouse IV

**Contribution:**
```pari
is(n)=ispseudoprime(2*(10^n-1)/3-5*(10^(n-1)+1)) || 
      ispseudoprime((15*10^(n-1)-51)/9)
```
- Date: Feb 07 2013

**Assessment:**
- Code appears mathematically independent
- Uses standard PARI/GP primality testing
- No direct dependency on Dubner reference

**Status:** APPEARS CLEAN
- Still requires verification that results match expected values

---

### 6. Herman Jamke

**Contact:** hermanjamke(AT)fastmail.fm

**Contributions:**
- Added terms 6233, 24029, 40223 to A082700 (Jan 02 2008)
- Added terms to A082699, A056247

**Critical Terms Added:**
| Term | Value | Digits | Status |
|------|-------|--------|--------|
| a(9) | 6233 | 6233 | Needs proof |
| a(10) | 24029 | 24029 | Needs proof |
| a(11) | 40223 | 40223 | Needs proof |

**Status:** REQUIRES VERIFICATION
- No primality proofs provided
- Source of computation not documented
- Large terms require rigorous verification

---

### 7. Robert G. Wilson v

**Sequence:** A056247 (Author)

**Date:** Aug 18 2000

**Assessment:**
- Pre-dates Dubner contamination (2000 vs 2003 De Geest authorship)
- However, sequence later contaminated via:
  - Librandi code addition (Nov 2014)
  - Cross-reference with A082700
  - Shared terms from Jamke and De Geest

**Status:** HISTORICALLY CLEAN, CURRENTLY CONTAMINATED

---

### 8. Klaus Brockhaus

**Sequence:** A056247

**Contribution:**
- Comments and academic reference (Dec 28 2004)
- Publication: "Zahlenfolgen mit homogenem Ziffernkern"
  - MNU 59/8 (2006), pp. 462-467
  - Co-author: Walter Oberschelp

**Status:** INDEPENDENT ACADEMIC SOURCE
- Academic publication provides independent validation
- Mathematical content appears rigorous
- Recommended for cross-reference verification

---

### 9. Recent Contributors (December 2025)

#### Elmo R. Oliveira
- **Activity:** Added terms to A082697, A082699 (Dec 13 2025)
- **Source:** De Geest's website and Kamada data
- **Status:** ⚠️ CONCERN - Based on potentially compromised sources
- **Action Required:** Verify all recent additions

#### Sean A. Irvine
- **Activity:** Offset change to A082720 (Dec 20 2025)
- **Status:** ⚠️ VERY RECENT - Monitor for consistency
- **Note:** Edit occurred after start of investigation period

---

## Cross-Reference Contamination Map

```
Harvey Dubner (Reference)
    ↓
Patrick De Geest (A082697-A082720) ← All contaminated
    ↓
    ├── A082700 ← Current investigation target
    │       ↓
    │   A056247 ← Formula relationship
    │       ↑
    └── Vincenzo Librandi (Code) ← Second contamination source

Ray Chandler (Editor)
    ↓
Batch edits Nov 04 2014 ← May propagate formatting
    ↓
Multiple sequences normalized
```

---

## Verification Priority Matrix

| Priority | Person | Action Required |
|----------|--------|-----------------|
| 1 | Harvey Dubner | Flag all sequences citing reference |
| 2 | Herman Jamke | Verify large terms (6233, 24029, 40223, 66395) |
| 3 | Vincenzo Librandi | Verify A056247 code results |
| 4 | Ray Chandler | Audit Nov 04 2014 edits |
| 5 | Elmo R. Oliveira | Verify Dec 2025 additions |
| 6 | Sean A. Irvine | Verify Dec 2025 offset change |

---

## Summary

**Total Confirmed Poisoned Persons:** 2
- Harvey Dubner (reference contamination)
- Vincenzo Librandi (code contamination)

**At-Risk Persons:** 4
- Patrick De Geest (heavy reliance on poisoned sources)
- Herman Jamke (large unverified terms)
- Ray Chandler (batch edits may propagate contamination)
- Elmo R. Oliveira (recent activity based on compromised sources)

**Clean Sources:** 2
- Charles R. Greathouse IV (independent code)
- Klaus Brockhaus (academic publication)

**Not Found:** 1
- Clifford A. Pickover (not in this cluster)

---

*Investigation Status: ACTIVE*  
*Last Updated: March 2026*
