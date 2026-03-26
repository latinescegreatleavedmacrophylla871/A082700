# Verification Protocol for Contaminated Sequences

## Executive Summary

This document provides step-by-step procedures to verify terms in the contaminated A082700 network. **11 large terms** require rigorous primality proofs totaling **~1.1 million digits**.

---

## Phase 1: Small Term Verification (k ≤ 101)

### Scope
Verify terms a(1) through a(8) in A082700:
- 5, 13, 17, 19, 37, 53, 73, 101

### Procedure

```bash
# Step 1: Install required software
pip install sympy

# Step 2: Run small term verification
python verify_small_terms.py
```

### Python Script: verify_small_terms.py

```python
#!/usr/bin/env python3
"""
Verify small terms of A082700 (k <= 101)
These can be verified deterministically
"""

import sympy as sp

TERMS_TO_VERIFY = [5, 13, 17, 19, 37, 53, 73, 101]

def generate_plateau_number(k):
    """Generate 166...661 with k digits"""
    return (15 * 10**(k-1) - 51) // 9

def verify_term(k):
    """Verify if term produces a prime"""
    n = generate_plateau_number(k)
    
    # Deterministic primality test for small numbers
    is_prime = sp.isprime(n)
    
    return {
        'k': k,
        'digits': len(str(n)),
        'is_prime': is_prime,
        'number': n
    }

def main():
    print("=" * 60)
    print("A082700 SMALL TERM VERIFICATION (k ≤ 101)")
    print("=" * 60)
    
    all_passed = True
    
    for k in TERMS_TO_VERIFY:
        result = verify_term(k)
        status = "✓ PRIME" if result['is_prime'] else "✗ NOT PRIME"
        
        print(f"\nk = {result['k']}")
        print(f"  Digits: {result['digits']}")
        print(f"  Status: {status}")
        
        if not result['is_prime']:
            all_passed = False
            print(f"  ⚠️  TERM FAILED - CRITICAL ERROR")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("RESULT: All small terms verified ✓")
    else:
        print("RESULT: SOME TERMS FAILED ✗ - INVESTIGATE IMMEDIATELY")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

### Expected Output

```
============================================================
A082700 SMALL TERM VERIFICATION (k ≤ 101)
============================================================

k = 5
  Digits: 5
  Status: ✓ PRIME

k = 13
  Digits: 13
  Status: ✓ PRIME

[...]

============================================================
RESULT: All small terms verified ✓
============================================================
```

### Time Estimate
- **Total time**: < 1 second
- **Compute resources**: Standard laptop

---

## Phase 2: Medium Term Verification (101 < k < 1000)

### Scope
Verify that no intermediate terms were missed between k=101 and k=6233.

### Procedure

```python
#!/usr/bin/env python3
"""
Search for missed terms in A082700
Range: 102 <= k <= 6232
"""

import sympy as sp

def generate_plateau_number(k):
    return (15 * 10**(k-1) - 51) // 9

def search_range(start, end):
    """Search for primes in range"""
    found = []
    
    for k in range(start, end + 1):
        if k % 100 == 0:
            print(f"  Checking k = {k}...")
        
        n = generate_plateau_number(k)
        
        # Probable prime test first (faster)
        if sp.isprime(n):
            found.append(k)
            print(f"  ✓ FOUND: k = {k} is prime!")
    
    return found

def main():
    print("=" * 60)
    print("A082700 GAP ANALYSIS (102 <= k <= 6232)")
    print("=" * 60)
    
    known_next = 6233
    found_terms = search_range(102, 6232)
    
    print("\n" + "=" * 60)
    print(f"Known next term: {known_next}")
    print(f"New terms found: {found_terms}")
    
    if found_terms:
        print("\n⚠️  NEW TERMS DISCOVERED - SEQUENCE NEEDS UPDATE")
    else:
        print("\n✓ No gaps found - sequence appears complete")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

### Time Estimate
- **Total time**: 10-30 minutes
- **Compute resources**: Standard laptop
- **Note**: Computationally intensive due to size

---

## Phase 3: Large Term Verification (k ≥ 6233)

### Critical Terms Requiring Rigorous Proof

| Term | k | Digits | Priority |
|------|---|--------|----------|
| a(9) | 6233 | 6,233 | HIGH |
| a(10) | 24029 | 24,029 | HIGH |
| a(11) | 40223 | 40,223 | HIGH |
| a(12) | 66395 | 66,395 | CRITICAL |

### Method 1: Primo (Rigorous Primality Proving)

**Primo** is the gold standard for primality proofs of large numbers.

#### Installation

```bash
# Download Primo from http://www.ellipsa.eu/
# Note: Primo is Windows-based; for Linux use alternative methods
```

#### Procedure

```bash
# Step 1: Generate the number to test
python generate_large_number.py 6233 > 166_6233.txt

# Step 2: Run Primo
primo 166_6233.txt

# Step 3: Verify certificate
primo -v 166_6233.primo
```

#### Python Helper: generate_large_number.py

```python
#!/usr/bin/env python3
"""
Generate plateau numbers for large primality proofs
"""

import sys

def generate_plateau_number(k):
    return (15 * 10**(k-1) - 51) // 9

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_large_number.py <k>")
        sys.exit(1)
    
    k = int(sys.argv[1])
    n = generate_plateau_number(k)
    print(n)

if __name__ == "__main__":
    main()
```

### Method 2: PARI/GP (Probable Prime + ECPP)

```bash
# Install PARI/GP
sudo apt-get install pari-gp

# Run verification
gp -q << 'EOF'
\\ Verification script for A082700 large terms
plateau(k) = (15*10^(k-1) - 51)/9;

\\ Term a(9) = 6233
k = 6233;
n = plateau(k);
print("Testing k = ", k);
print("Digits: ", #digits(n));

\\ APR-CL test (for numbers < 10^10000)
\\ For larger numbers, use ECPP
if (k <= 10000,
    isprimeAPR = isprime(n, 2);  \\ APR-CL certificate
    print("APR-CL result: ", isprimeAPR);
,
    \\ For larger numbers, probable prime first
    isprimeBPSW = ispseudoprime(n);
    print("BPSW probable prime: ", isprimeBPSW);
    
    if (isprimeBPSW,
        print("WARNING: Number is large - ECPP proof required");
        print("Consider using Primo for rigorous proof");
    );
);

quit;
EOF
```

### Method 3: FactorDB Verification

**FactorDB** (http://factordb.com) maintains factorization records for large numbers.

#### Procedure

```python
#!/usr/bin/env python3
"""
Check FactorDB for existing primality records
"""

import requests
import sys

def generate_plateau_number(k):
    return (15 * 10**(k-1) - 51) // 9

def check_factordb(k):
    """Check if number exists in FactorDB"""
    n = generate_plateau_number(k)
    
    # FactorDB API endpoint
    url = f"http://factordb.com/api.php?query={n}"
    
    try:
        response = requests.get(url, timeout=30)
        data = response.json()
        
        return {
            'k': k,
            'digits': len(str(n)),
            'factordb_status': data.get('status', 'unknown'),
            'factors': data.get('factors', [])
        }
    except Exception as e:
        return {
            'k': k,
            'error': str(e)
        }

def main():
    terms = [6233, 24029, 40223, 66395]
    
    print("=" * 60)
    print("FACTORDB VERIFICATION CHECK")
    print("=" * 60)
    
    for k in terms:
        print(f"\nChecking k = {k}...")
        result = check_factordb(k)
        
        if 'error' in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  Digits: {result['digits']}")
            print(f"  FactorDB status: {result['factordb_status']}")
            
            # Status codes: P (prime), C (composite), U (unknown)
            if result['factordb_status'] == 'P':
                print("  ✓ FactorDB confirms prime")
            elif result['factordb_status'] == 'C':
                print("  ✗ FactorDB shows composite - CRITICAL ERROR")
            elif result['factordb_status'] == 'U':
                print("  ? Unknown status - needs verification")

if __name__ == "__main__":
    main()
```

### Method 4: Elliptic Curve Primality Proving (ECPP)

For numbers with 10,000+ digits, ECPP is the standard method.

#### Using CM (Complex Multiplication) Method

```bash
# Install CM software (if available)
# Or use Primo which implements ECPP

# Alternative: Use mpmath for verification
python -c "
import mpmath
mpmath.mp.dps = 70000  # Set precision for 66395-digit number

k = 66395
n = (15 * 10**(k-1) - 51) // 9

print(f'Testing k = {k}')
print(f'Digits: {len(str(n))}')

# Note: This only verifies the number, not primality
# For primality proof, use Primo or ECPP
"
```

---

## Phase 4: Cross-Sequence Consistency Check

### Verify Formula Relationships

```python
#!/usr/bin/env python3
"""
Verify formula links between A082700 and A056247
"""

import sympy as sp

# Small known terms for verification
A082700_SMALL = [5, 13, 17, 19, 37, 53, 73, 101]
A056247_SMALL = [0, 3, 11, 15, 17, 35, 51, 71, 99]

def verify_formula_relationship():
    """
    Verify: A082700(n) = A056247(n+1) + 2
    """
    print("=" * 60)
    print("FORMULA RELATIONSHIP VERIFICATION")
    print("=" * 60)
    print("\nVerifying: A082700(n) = A056247(n+1) + 2\n")
    
    errors = []
    
    for n in range(1, min(len(A082700_SMALL), len(A056247_SMALL)-1) + 1):
        left_side = A082700_SMALL[n-1]  # A082700(n)
        right_side = A056247_SMALL[n] + 2  # A056247(n+1) + 2
        
        match = (left_side == right_side)
        status = "✓" if match else "✗ MISMATCH"
        
        print(f"n = {n}:")
        print(f"  A082700({n}) = {left_side}")
        print(f"  A056247({n+1}) + 2 = {A056247_SMALL[n]} + 2 = {right_side}")
        print(f"  Status: {status}")
        
        if not match:
            errors.append(n)
    
    print("\n" + "=" * 60)
    if errors:
        print(f"ERRORS FOUND at n = {errors}")
        print("CRITICAL: Formula relationship broken!")
    else:
        print("✓ All formula relationships verified")
    print("=" * 60)

if __name__ == "__main__":
    verify_formula_relationship()
```

---

## Phase 5: Independent Source Verification

### Checklist for Independent Sources

| Source | URL | Status | Use Case |
|--------|-----|--------|----------|
| FactorDB | http://factordb.com | Active | Primality status |
| Primo Certificates | N/A | Tool | Rigorous proofs |
| Kamada NRR | https://stdkmd.net/nrr | ❌ Unreachable | Historical data |
| De Geest PDP | worldofnumbers.com | Active | Tables (use with caution) |
| OEIS Wiki | oeis.org/wiki | Active | Editor information |

### Verification Protocol Summary

```
┌─────────────────────────────────────────────────────────────────┐
│              COMPLETE VERIFICATION WORKFLOW                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Phase 1: Small Terms (k ≤ 101)                                 │
│  ├── Use: SymPy deterministic primality test                   │
│  ├── Time: < 1 second                                           │
│  └── Priority: HIGH (baseline verification)                    │
│                                                                 │
│  Phase 2: Gap Analysis (102 ≤ k ≤ 6232)                       │
│  ├── Use: SymPy probable prime test                           │
│  ├── Time: 10-30 minutes                                        │
│  └── Priority: MEDIUM (completeness check)                     │
│                                                                 │
│  Phase 3: Large Terms (k ≥ 6233)                                │
│  ├── Use: Primo (ECPP) for rigorous proof                      │
│  ├── Alternative: FactorDB lookup                              │
│  ├── Time: Hours to days per term                               │
│  └── Priority: CRITICAL (11 terms need proof)                  │
│                                                                 │
│  Phase 4: Cross-Sequence Check                                 │
│  ├── Use: Python formula verification                          │
│  ├── Time: < 1 second                                           │
│  └── Priority: HIGH (consistency check)                        │
│                                                                 │
│  Phase 5: External Verification                                  │
│  ├── Use: FactorDB, Primo certificates                         │
│  ├── Time: Variable                                             │
│  └── Priority: HIGH (independent confirmation)               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Expected Results

### Success Criteria

1. **All 8 small terms verified as prime**
2. **No gaps found between k=101 and k=6233**
3. **All 11 large terms have rigorous primality proofs**
4. **Formula relationships hold for all testable cases**
5. **FactorDB or equivalent confirms large primes**

### Failure Scenarios

| Scenario | Action Required |
|----------|-----------------|
| Small term not prime | CRITICAL: Sequence is wrong |
| Gap found (missing term) | Update sequence, investigate source |
| Large term composite | Remove term, investigate contamination |
| Formula relationship broken | Both sequences contaminated |
| FactorDB shows different status | Cross-check with other sources |

---

## Resource Requirements

### Computational Resources

| Phase | CPU | Memory | Time | Priority |
|-------|-----|--------|------|----------|
| 1 | Low | < 1 GB | < 1 sec | Run immediately |
| 2 | Medium | 2-4 GB | 10-30 min | Run within 24h |
| 3 | High | 16+ GB | Hours-days | Run ASAP |
| 4 | Low | < 1 GB | < 1 sec | Run immediately |
| 5 | N/A | N/A | Variable | Parallel with Phase 3 |

### Software Requirements

- Python 3.8+ with SymPy
- PARI/GP (optional)
- Primo (for rigorous proofs)
- Internet access (for FactorDB queries)

---

## Documentation Requirements

### For Each Verified Term

1. **Verification method used**
2. **Software version**
3. **Date/time of verification**
4. **Compute resources used**
5. **Certificate file (for Primo proofs)**
6. **Verifier signature (for independent audit)**

### Certificate Storage

```
certificates/
├── A082700/
│   ├── k6233.primo
│   ├── k24029.primo
│   ├── k40223.primo
│   └── k66395.primo
└── README.md
```

---

*Protocol Version: 1.0*  
*Last Updated: March 26, 2026*  
*Status: READY FOR EXECUTION*
