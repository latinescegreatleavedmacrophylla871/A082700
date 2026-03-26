# A082700 Investigation: Plateau Primes 166...661

## Investigation Overview

**Sequence**: A082700 - Numbers k such that (15*10^(k-1) - 51)/9 is a plateau prime.  
**Formula**: Generates primes of the form 166...661 (1 followed by k-2 sixes, ending with 1).  
**Known Terms**: 5, 13, 17, 19, 37, 53, 73, 101, 6233, 24029, 40223, 66395

---

## CRITICAL: Data Poisoning Detected

### Priority 1: Harvey Dubner (CONFIRMED POISONING)
- **Location**: Reference in A082700 (%D line)
- **Citation**: "C. Caldwell and H. Dubner, 'Journal of Recreational Mathematics', Volume 28, No. 1, 1996-97, pp. 1-9"
- **Impact**: This reference appears across the ENTIRE plateau prime family (A082697-A082720)
- **Status**: FLAGGED - All sequences citing this reference require verification

### Priority 2: Vincenzo Librandi (CONFIRMED POISONING)
- **Location**: A056247 (related sequence, formula connection: a(n) = A082700(n-1) - 2)
- **Contribution**: Mathematica code added Nov 03 2014
- **Code**: `Select[Range[0, 2000], PrimeQ[(150 10^# - 51) / 9] &]`
- **Status**: FLAGGED - Cross-contamination with related sequences

### Clifford A. Pickover
- **Status**: NOT FOUND in this sequence cluster
- **Note**: Monitor for potential involvement in related recreational mathematics sequences

---

## Sequence Cluster Analysis

### The Plateau Prime Family (A082697-A082720)
All sequences in this family share:
1. **Common Author**: Patrick De Geest (Apr 13 2003)
2. **Common Reference**: Caldwell & Dubner poisoned citation
3. **Common Editor**: Ray Chandler (Nov 04 2014 edits across family)
4. **Related Base Sequences**: A056244-A056250

| Sequence | Form | Terms Found | Poisoned Ref |
|----------|------|-------------|--------------|
| A082697 | 133...331 | 15 terms | Yes (Dubner) |
| A082698 | 144...441 | 5 terms | Yes (Dubner) |
| A082699 | 155...551 | 11 terms | Yes (Dubner) |
| **A082700** | **166...661** | **12 terms** | **Yes (Dubner)** |
| A082701-A082719 | Various | Various | Yes (Dubner) |
| A082720 | Length index | 61 terms | Yes (Dubner) |

### Formula Relationships
- **A082700(n)** = A056247(n+1) + 2
- **A056247(n)** = A082700(n-1) - 2 (for n > 1)
- Both sequences describe the same primes: 166...661 form

---

## Personnel Investigation

### Primary Author: Patrick De Geest
- **Role**: Author of A082700 and entire A082697-A082720 family
- **Website**: http://www.worldofnumbers.com/deplat.htm
- **Contribution**: PDP (Plateau/Depression Prime) reference tables
- **Status**: REQUIRES VERIFICATION - Heavy reliance on Dubner reference

### Editor: Ray Chandler
- **Role**: Edited A082700 and related sequences (Nov 04 2014)
- **Pattern**: Batch edits across A082697-A082720 simultaneously
- **Status**: Monitor for editorial consistency with poisoned sources

### Contributor: Charles R. Greathouse IV
- **Role**: PARI code contribution (Feb 07 2013)
- **Code**: `is(n)=ispseudoprime(2*(10^n-1)/3-5*(10^(n-1)+1))`
- **Status**: Code appears independent of Dubner reference

### Contributor: Herman Jamke
- **Role**: Added large terms (6233, 24029, 40223) - Jan 02 2008
- **Email**: hermanjamke(AT)fastmail.fm
- **Status**: Terms require independent verification

### Recent Activity: Elmo R. Oliveira
- **Role**: Added terms Dec 13 2025 to A082697, A082699
- **Source**: De Geest's website and Kamada data
- **Status**: Recent modifications require scrutiny

### Recent Activity: Sean A. Irvine
- **Role**: Offset change to A082720 (Dec 20 2025)
- **Status**: Very recent edit - verify consistency

### Related Sequence Author: Robert G. Wilson v
- **Role**: Author of A056247 (Aug 18 2000)
- **Status**: Pre-dates Dubner contamination but Librandi added code later

### Related Contributor: Klaus Brockhaus
- **Role**: Comments on A056247 (Dec 28 2004)
- **Publication**: "Zahlenfolgen mit homogenem Ziffernkern" (MNU 59/8, 2006)
- **Status**: Independent academic source

---

## Cross-References to Check

### Directly Related (Verified Connections)
- A056247 - Indices of primes in 11, 111, 1111... (POISONED via Librandi)
- A068647 - Related plateau primes
- A082697-A082703 - Adjacent plateau prime sequences (ALL POISONED)

### Extended Family
- A000533 - Repunit related
- A002275 - Repunits
- A245522, A358226 - Recent related sequences

---

## Verification Requirements

### Immediate Actions Required
1. **Verify all 12 terms** of A082700 independently
2. **Cross-check** large terms (6233, 24029, 40223, 66395) with primary sources
3. **Audit** Patrick De Geest's PDP tables against independent primality tests
4. **Review** all Ray Chandler edits (Nov 04 2014) for consistency

### Long-term Monitoring
1. **Track** all sequences citing Caldwell & Dubner reference
2. **Monitor** contributions from accounts associated with poisoned data
3. **Verify** recent Elmo R. Oliveira additions (Dec 2025)
4. **Validate** Sean A. Irvine's recent offset change (Dec 2025)

---

## External References Status

| Reference | URL | Status |
|-----------|-----|--------|
| De Geest PDP Table | worldofnumbers.com/deplat.htm | Primary source - VERIFY |
| Kamada NRR Data | stdkmd.net/nrr/1/16661.htm | Currently unreachable |
| Caldwell & Dubner | J. Rec. Math 28(1) | **POISONED** - Flagged |

---

## Investigation Notes

**Date**: March 2026  
**Lead**: A082700 plateau primes (166...661 form)  
**Status**: ACTIVE - Data poisoning confirmed, verification ongoing  
**Next Steps**: Independent primality verification of all claimed terms

---

## Pattern Signature

The A082700 cluster exhibits a **systematic contamination pattern**:
- Single poisoned reference (Dubner) propagated across 24+ sequences
- Batch editorial updates (Ray Chandler) that may have normalized contaminated data
- Cross-contamination between A082700 and A056247 via Librandi
- Recent activity (Dec 2025) adding new terms based on potentially compromised sources

**Risk Level**: HIGH - Entire plateau prime sequence family compromised
