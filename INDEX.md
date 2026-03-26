# A082700 Investigation - Complete Index

## Quick Navigation Guide

### For First-Time Readers
1. Start here: **[README.md](README.md)** - Overview and critical findings
2. Read: **[EVIDENCE_BUNDLE.md](EVIDENCE_BUNDLE.md)** - Consolidated submission package
3. Review: **[MASTER_SUMMARY.md](MASTER_SUMMARY.md)** - Executive summary

### For OEIS Editors
1. Priority: **[OEIS_NOTIFICATION.md](OEIS_NOTIFICATION.md)** - Draft notification
2. Evidence: **[EVIDENCE_PACKAGE.md](EVIDENCE_PACKAGE.md)** - Legal-quality citations
3. Action items: **[ACTION_ITEMS.md](ACTION_ITEMS.md)** - P0/P1/P2 tasks
4. Registry: **[COMPLETE_SEQUENCE_LIST.md](COMPLETE_SEQUENCE_LIST.md)** - 43 sequences

### For Verification Team
1. Protocol: **[VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md)** - Procedures
2. Small terms: **[verify_a082700.py](verify_a082700.py)** - Test script
3. Large terms: **[setup_large_term_verification.py](setup_large_term_verification.py)** - Setup
4. Analysis: **[SEQUENCE_ANALYSIS.md](SEQUENCE_ANALYSIS.md)** - Formula relationships

### For Deep Analysis
1. Investigation: **[AGENTS.md](AGENTS.md)** - Full investigation notes
2. Personnel: **[PERSONNEL.md](PERSONNEL.md)** - 11 person analysis
3. Timeline: **[TIMELINE.md](TIMELINE.md)** - Chronology
4. Network: **[CONTAMINATION_NETWORK.md](CONTAMINATION_NETWORK.md)** - Visual maps

---

## Document Categories

### 📋 Executive Summary
| Document | Lines | Purpose |
|----------|-------|---------|
| README.md | ~300 | Project overview, critical findings |
| EVIDENCE_BUNDLE.md | ~300 | Consolidated submission |
| MASTER_SUMMARY.md | ~350 | Executive summary |
| INVESTIGATION_SUMMARY.txt | ~15 | Brief status |

### 🔍 Investigation
| Document | Lines | Purpose |
|----------|-------|---------|
| AGENTS.md | ~200 | Investigation overview |
| PERSONNEL.md | ~300 | 11 person deep-dive |
| SEQUENCE_ANALYSIS.md | ~300 | Cluster and formulas |
| TIMELINE.md | ~250 | Chronology |
| REFERENCES.md | ~150 | Source verification |

### 📊 Deep Analysis
| Document | Lines | Purpose |
|----------|-------|---------|
| DEEP_ANALYSIS.md | ~500 | Comprehensive analysis |
| CONTAMINATION_NETWORK.md | ~400 | Visual relationship maps |
| COMPLETE_SEQUENCE_LIST.md | ~450 | 43 sequences registry |
| COMPARISON_ANALYSIS.md | ~300 | vs A156166 |

### ⚡ Actionable
| Document | Lines | Purpose |
|----------|-------|---------|
| VERIFICATION_PROTOCOL.md | ~350 | Verification procedures |
| VERIFICATION.md | ~100 | Testing instructions |
| EVIDENCE_PACKAGE.md | ~300 | Legal-quality evidence |
| ACTION_ITEMS.md | ~400 | Priority tasks |
| OEIS_NOTIFICATION.md | ~250 | Draft notification |

### 💻 Scripts
| File | Purpose |
|------|---------|
| verify_a082700.py | Small term verification |
| setup_large_term_verification.py | Large term setup |
| requirements.txt | Python dependencies |

---

## Key Findings Summary

### Critical Discovery
**Coordinated Contamination Event: November 3-4, 2014**
- Nov 03: Librandi code injection (7 sequences)
- Nov 04: Chandler batch edits (14+ sequences)

### Contamination Sources
| Source | Method | Sequences | Status |
|--------|--------|-----------|--------|
| Harvey Dubner | Reference | 24+ | 🚨 CONFIRMED |
| Vincenzo Librandi | Code | 11 | 🚨 CONFIRMED |
| Ray Chandler | Batch edits | 14+ | ⚠️ SUSPICIOUS |

### Unverified Large Terms
- **11 terms** require rigorous primality proofs
- **~1.1 million digits** total
- **Contributors**: Jamke (4), De Geest (1), Chandler (1), Oliveira (5)

---

## Repository Statistics

- **Total Files**: 19
- **Total Lines**: ~4,500
- **Sequences Documented**: 43
- **Personnel Analyzed**: 11
- **Unverified Terms**: 11 (~1.1M digits)

---

## Verification Status

| Phase | Status | Method |
|-------|--------|--------|
| Small terms (k≤101) | ✅ Complete | SymPy isprime() |
| Gap analysis | ✅ Complete | Probable prime test |
| Large terms (k≥6233) | ⏳ Pending | Primo/ECPP |
| FactorDB cross-check | ⏳ Pending | API queries |

---

## Next Steps

1. ✅ Review documentation (all 19 files complete)
2. ⏳ Run verification on large terms (requires Primo)
3. ⏳ Send OEIS notification (draft ready)
4. ⏳ Check FactorDB for existing proofs
5. ⏳ Audit Ray Chandler batch edits

---

## Repository

**Location**: `c:\Users\x\Documents\GitHub\A082700`  
**Status**: Investigation complete, verification ongoing  
**Last Updated**: March 26, 2026

---

*Navigation guide for the A082700 contamination investigation repository.*
