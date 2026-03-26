# Investigation Timeline

## A082700 Sequence History & Data Poisoning Events

---

### Pre-Contamination Era (2000-2003)

| Date | Event | Person | Notes |
|------|-------|--------|-------|
| Aug 18, 2000 | A056247 created | Robert G. Wilson v | Base sequence, pre-dates contamination |
| Dec 28, 2004 | Comments added | Klaus Brockhaus | Academic publication reference |
| 2006 | Academic publication | Brockhaus & Oberschelp | "Zahlenfolgen mit homogenem Ziffernkern" |

---

### Primary Contamination Era (2003)

| Date | Event | Person | Significance |
|------|-------|--------|--------------|
| **Apr 13, 2003** | **A082700 created** | **Patrick De Geest** | **🚨 Includes Harvey Dubner reference** |
| Apr 13, 2003 | A082697-A082720 created | Patrick De Geest | Entire family contaminated |
| 2003 | Initial terms added | De Geest | 5, 13, 17, 19, 37, 53, 73, 101 |

**Critical Event**: All plateau prime sequences (A082697-A082720) were created on the same day with the same poisoned reference to:
```
C. Caldwell and H. Dubner, "Journal of Recreational Mathematics", 
Volume 28, No. 1, 1996-97, pp. 1-9
```

---

### Expansion Era (2004-2008)

| Date | Event | Person | Significance |
|------|-------|--------|--------------|
| Oct 03, 2004 | a(13)=42263 added | Patrick De Geest | To A082697 |
| Jan 02, 2008 | Large terms added | **Herman Jamke** | 6233, 24029, 40223 added |
| 2008 | Jamke contributions | Herman Jamke | Multiple sequences affected |

**Note**: Herman Jamke's terms require independent verification. No primality proofs were provided.

---

### Intermediate Era (2011-2013)

| Date | Event | Person | Notes |
|------|-------|--------|-------|
| Apr 14, 2011 | a(14)=111033 added | Ray Chandler | To A082697 |
| Feb 07, 2013 | PARI code added | Charles R. Greathouse IV | Independent implementation |

---

### Secondary Contamination Era (2014) 🚨

| Date | Event | Person | Significance |
|------|-------|--------|--------------|
| **Nov 03, 2014** | **Mathematica code added** | **Vincenzo Librandi** | **🚨 Contaminates A056247** |
| Nov 02, 2014 | Term/link added | Patrick De Geest | To A056247 |
| **Nov 04, 2014** | **Batch edits** | **Ray Chandler** | **Edited A082697-A082720** |
| Nov 04, 2014 | Edits completed | Ray Chandler | Cross-contamination risk |

**Critical Pattern**: 
- Vincenzo Librandi adds code to A056247 on Nov 03
- Ray Chandler batch edits sequences on Nov 04
- A056247 has formula relationship with A082700

---

### Recent Activity (2023-2025) ⚠️

| Date | Event | Person | Significance |
|------|-------|--------|--------------|
| Feb 02, 2023 | Search note added | Tyler Busby | a(6) > 2×10^5 for A082698 |
| **Dec 13, 2025** | **Terms added** | **Elmo R. Oliveira** | **⚠️ Based on compromised sources** |
| Dec 13, 2025 | Terms added | Elmo R. Oliveira | To A082697, A082699 |
| **Dec 20, 2025** | **Offset changed** | **Sean A. Irvine** | **⚠️ To A082720** |

**⚠️ ALERT**: Recent activity in December 2025:
- Terms added based on De Geest's website and Kamada data
- Kamada website currently unreachable
- Source data may be compromised

---

## Contamination Timeline Visualization

```
2000 ──────────────────────────────────────────────────────────────>
 │
 │ Aug 18: A056247 created (Wilson) [CLEAN]
 │
2003 ──────────────────────────────────────────────────────────────>
 │
 │ 🚨 Apr 13: HARVEY DUBNER CONTAMINATION 🚨
 │    ├── A082697-A082720 created (De Geest)
 │    └── Poisoned reference added to ALL
 │
2004-2008 ──────────────────────────────────────────────────────────>
 │
 │ Large terms added (Jamke)
 │ Requires verification
 │
2014 ──────────────────────────────────────────────────────────────>
 │
 │ 🚨 Nov 03: VINCENZO LIBRANDI CONTAMINATION 🚨
 │    └── A056247 code added
 │
 │    Nov 04: Ray Chandler batch edits
 │    Potential cross-contamination
 │
2025 ──────────────────────────────────────────────────────────────>
 │
 │ ⚠️ Dec 13-20: Recent activity
 │    ├── Elmo R. Oliveira additions
 │    └── Sean A. Irvine offset change
 │
 │ 🚨 March 2026: Investigation begins
 │
 ▼
```

---

## Key Dates Summary

| Type | Date | Event | Severity |
|------|------|-------|----------|
| 🚨 Contamination | Apr 13, 2003 | Harvey Dubner reference added | CRITICAL |
| 🚨 Contamination | Nov 03, 2014 | Vincenzo Librandi code added | HIGH |
| ⚠️ Risk | Nov 04, 2014 | Ray Chandler batch edits | MEDIUM |
| ⚠️ Risk | Jan 02, 2008 | Large unverified terms added | HIGH |
| ⚠️ Risk | Dec 13, 2025 | Recent additions from compromised sources | MEDIUM |
| ⚠️ Risk | Dec 20, 2025 | Recent offset change | LOW |

---

## Data Poisoning Events

### Event 1: Primary Contamination (2003)

**Source**: Harvey Dubner via Caldwell & Dubner reference
**Scope**: 24+ sequences (A082697-A082720)
**Impact**: Entire plateau prime family compromised
**Mechanism**: Single poisoned reference cited across all sequences

### Event 2: Secondary Contamination (2014)

**Source**: Vincenzo Librandi via Mathematica code
**Scope**: A056247
**Impact**: Cross-contamination to A082700 via formula relationship
**Mechanism**: Code contribution to related sequence

### Event 3: Batch Edit Propagation (2014)

**Source**: Ray Chandler editorial changes
**Scope**: A082697-A082720
**Impact**: Potential normalization of contaminated data
**Mechanism**: Simultaneous edits across multiple sequences

---

## Unverified Contributions

| Date | Contributor | Contribution | Status |
|------|-------------|--------------|--------|
| Jan 02, 2008 | Herman Jamke | Terms 6233, 24029, 40223 | ⚠️ Needs proof |
| 2014 | Patrick De Geest | Term 66395 | ⚠️ Needs proof |
| Dec 13, 2025 | Elmo R. Oliveira | Multiple additions | ⚠️ Needs verification |
| Dec 20, 2025 | Sean A. Irvine | Offset change | ⚠️ Monitor |

---

## Investigation Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| Mar 26, 2026 | Investigation initiated | ✅ Complete |
| Mar 26, 2026 | AGENTS.md created | ✅ Complete |
| Mar 26, 2026 | README.md created | ✅ Complete |
| Mar 26, 2026 | Personnel analysis completed | ✅ Complete |
| Mar 26, 2026 | Sequence cluster analysis completed | ✅ Complete |
| TBD | Term verification | ⏳ Pending |
| TBD | Independent proof of large terms | ⏳ Pending |
| TBD | Cross-reference validation | ⏳ Pending |

---

*Document Version: 1.0*  
*Timeline Compiled: March 26, 2026*
