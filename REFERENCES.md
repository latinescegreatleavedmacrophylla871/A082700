# References and Sources

## Primary Sources

### OEIS Sequences

| Sequence | URL | Status |
|----------|-----|--------|
| A082700 | https://oeis.org/A082700 | 🚨 Contaminated |
| A056247 | https://oeis.org/A056247 | 🚨 Contaminated |
| A082697 | https://oeis.org/A082697 | 🚨 Contaminated |
| A082698 | https://oeis.org/A082698 | 🚨 Contaminated |
| A082699 | https://oeis.org/A082699 | 🚨 Contaminated |
| A082720 | https://oeis.org/A082720 | 🚨 Contaminated |

### External Resources

| Resource | URL | Status | Notes |
|----------|-----|--------|-------|
| De Geest PDP | http://www.worldofnumbers.com/deplat.htm | Active | Requires verification |
| Kamada NRR | https://stdkmd.net/nrr/1/16661.htm | ❌ Unreachable | Data unavailable |

---

## Academic References

### 🚨 POISONED REFERENCE

**C. Caldwell and H. Dubner, "Journal of Recreational Mathematics", Volume 28, No. 1, 1996-97, pp. 1-9**

- **Status**: FLAGGED - Data poisoning source
- **Scope**: Cited in A082697-A082720 (24+ sequences)
- **Impact**: Entire plateau prime family compromised
- **Verification**: Original publication difficult to access

### Independent Academic Source

**Klaus Brockhaus and Walter Oberschelp, "Zahlenfolgen mit homogenem Ziffernkern", MNU 59/8 (2006), pp. 462-467**

- **Status**: APPEARS CLEAN
- **Scope**: Mathematical foundation for sequence patterns
- **Recommended**: For cross-reference verification

---

## OEIS Internal Format References

### A082700 Text Format
```
%I A082700 #28 Nov 09 2019 03:13:48
%S A082700 5,13,17,19,37,53,73,101,6233,24029,40223,66395
%N A082700 Numbers k such that (15*10^(k-1) - 51)/9 is a plateau prime.
%D A082700 C. Caldwell and H. Dubner, "Journal of Recreational Mathematics", Volume 28, No. 1, 1996-97, pp. 1-9.
%H A082700 Patrick De Geest, PDP Reference Table - 161.
%H A082700 Makoto Kamada, Prime numbers of the form 166...661.
%F A082700 a(n) = A056247(n+1) + 2.
%Y A082700 Cf. A056247, A068647, A082697-A082720.
%A A082700 Patrick De Geest, Apr 13 2003
%E A082700 More terms from Herman Jamke, Jan 02 2008
%E A082700 Edited by Ray Chandler, Nov 04 2014
```

### A056247 Text Format (Related)
```
%I A056247 #24 Jan 17 2019 13:44:05
%S A056247 0,3,11,15,17,35,51,71,99,6231,24027,40221,66393
%N A056247 Indices of primes in sequence defined by A(0) = 11, A(n) = 10*A(n-1) + 51
%D A056247 Klaus Brockhaus and Walter Oberschelp, Zahlenfolgen mit homogenem Ziffernkern, MNU 59/8 (2006)
%t A056247 Select[Range[0, 2000], PrimeQ[(150 10^# - 51) / 9] &] (* Vincenzo Librandi, Nov 03 2014 *)
%A A056247 Robert G. Wilson v, Aug 18 2000
%E A056247 Edited by Ray Chandler, Nov 04 2014
```

---

## Cross-Reference Network

### Direct Dependencies

```
A082700 (Current Target)
    ├── References → A056247 (contaminated via Librandi)
    ├── References → A068647
    ├── Part of → A082697-A082720 family (all contaminated)
    └── Cites → Caldwell & Dubner (poisoned)

A056247 (Related)
    ├── Formula link → A082700
    ├── Code by → Vincenzo Librandi (poisoned)
    ├── Author → Robert G. Wilson v (clean origin)
    └── Academic ref → Brockhaus & Oberschelp (clean)
```

### Extended Family

- A082697 (133...331)
- A082698 (144...441)
- A082699 (155...551)
- **A082700 (166...661) ← Current investigation**
- A082701-A082703 (continuing patterns)
- A082719 (900...009)
- A082720 (length index)

All share the poisoned Dubner reference.

---

## Unreachable Sources

### Kamada NRR (Near Repunit Repdigits)

**URL**: https://stdkmd.net/nrr/1/16661.htm

- **Status**: UNREACHABLE
- **Impact**: Cannot verify Kamada data
- **Note**: Referenced by both A082700 and A056247
- **Alternative**: Factordb.com for independent verification

---

## Recommended Independent Sources

For verification purposes:

1. **FactorDB** (http://factordb.com)
   - Independent factorization database
   - Can verify primality of large numbers

2. **Primo** (primality proving software)
   - Rigorous primality proofs
   - Required for terms > 1000 digits

3. **PARI/GP** (with independent implementation)
   - Charles R. Greathouse IV code appears independent
   - Can be used for cross-checking

4. **SymPy** (Python library)
   - Used in verification script
   - Standard primality testing

---

## References Status Summary

| Category | Count | Status |
|----------|-------|--------|
| OEIS Sequences | 24+ | 🚨 Contaminated (Dubner) |
| Academic Papers | 1 | 🚨 Contaminated (Dubner) |
| Academic Papers | 1 | ✅ Clean (Brockhaus) |
| External Websites | 1 | ⚠️ Requires verification |
| External Websites | 1 | ❌ Unreachable |

---

*Document Version: 1.0*  
*Last Updated: March 2026*
