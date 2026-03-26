#!/usr/bin/env python3
"""
Large Term Verification Setup for A082700

This script generates plateau numbers for rigorous primality proving
using Primo or other ECPP software.

Terms requiring proof:
- k=6233 (6,233 digits)
- k=24029 (24,029 digits)  
- k=40223 (40,223 digits)
- k=66395 (66,395 digits)
- Plus 7 more in related sequences
"""

import os
import sys

# Terms requiring rigorous primality proofs
LARGE_TERMS = [
    # A082700 terms
    (6233, 'A082700', 'a(9)'),
    (24029, 'A082700', 'a(10)'),
    (40223, 'A082700', 'a(11)'),
    (66395, 'A082700', 'a(12)'),
    # A082697 terms
    (42263, 'A082697', 'a(13)'),
    (111033, 'A082697', 'a(14)'),
    (249551, 'A082697', 'a(15)'),
    # A082699 terms
    (37685, 'A082699', 'a(7)'),
    (211263, 'A082699', 'a(9)'),
    (222719, 'A082699', 'a(10)'),
    (250337, 'A082699', 'a(11)'),
]

def generate_plateau_number(k):
    """Generate plateau number: (15*10^(k-1) - 51)/9"""
    return (15 * 10**(k-1) - 51) // 9

def setup_verification_directory():
    """Create directory structure for verification"""
    dirs = [
        'verification',
        'verification/large_terms',
        'verification/certificates',
        'verification/results',
        'verification/factordb'
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Created: {d}/")

def generate_large_number_files():
    """Generate number files for Primo"""
    print("\nGenerating plateau numbers for large terms...")
    print("=" * 60)
    
    total_digits = 0
    
    for k, seq, term_id in LARGE_TERMS:
        print(f"\nGenerating {seq} {term_id} (k={k})...")
        
        # Generate the number
        n = generate_plateau_number(k)
        digits = len(str(n))
        total_digits += digits
        
        # Save to file
        filename = f'verification/large_terms/{seq}_{term_id}_k{k}.txt'
        with open(filename, 'w') as f:
            f.write(str(n))
        
        print(f"  Digits: {digits:,}")
        print(f"  Saved to: {filename}")
        
        # Also save in Primo format
        primo_filename = f'verification/large_terms/{seq}_{term_id}_k{k}.primo-in'
        with open(primo_filename, 'w') as f:
            f.write(f'[ {n} ]\n')
        
        print(f"  Primo format: {primo_filename}")
    
    print("\n" + "=" * 60)
    print(f"Total digits to verify: {total_digits:,}")
    print("=" * 60)

def create_primo_batch_script():
    """Create batch script for running Primo"""
    script = '''#!/bin/bash
# Primo batch verification script for A082700 large terms
# Run this after installing Primo from http://www.ellipsa.eu/

echo "A082700 Large Term Verification with Primo"
echo "==========================================="
echo ""
echo "Terms to verify:"
echo "  - k=6233 (6,233 digits)"
echo "  - k=24029 (24,029 digits)"
echo "  - k=40223 (40,223 digits)"
echo "  - k=66395 (66,395 digits)"
echo "  - Plus 7 more in related sequences"
echo ""
echo "Estimated time: 2-4 weeks (sequential) or 3-7 days (parallel)"
echo ""

# Create results directory
mkdir -p verification/certificates

# Process each term
for file in verification/large_terms/*.primo-in; do
    if [ -f "$file" ]; then
        basename=$(basename "$file" .primo-in)
        echo "Processing: $basename"
        
        # Run Primo
        primo "$file"
        
        # Move certificate to certificates directory
        if [ -f "${file%.primo-in}.primo" ]; then
            mv "${file%.primo-in}.primo" "verification/certificates/${basename}.primo"
            echo "  Certificate saved: verification/certificates/${basename}.primo"
        fi
        
        echo ""
    fi
done

echo "Batch verification complete!"
echo "Certificates saved in: verification/certificates/"
'''
    
    with open('verification/run_primo_batch.sh', 'w') as f:
        f.write(script)
    
    print("\nCreated: verification/run_primo_batch.sh")
    print("  Usage: bash verification/run_primo_batch.sh")

def create_factordb_check_script():
    """Create script to check FactorDB"""
    script = '''#!/usr/bin/env python3
"""
Check FactorDB for existing primality records
"""

import requests
import sys
import time

LARGE_TERMS = [
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

def generate_plateau_number(k):
    return (15 * 10**(k-1) - 51) // 9

def check_factordb(k, seq):
    """Check if number exists in FactorDB"""
    n = generate_plateau_number(k)
    
    try:
        response = requests.get(f'http://factordb.com/api.php?query={n}', timeout=30)
        data = response.json()
        
        return {
            'k': k,
            'seq': seq,
            'digits': len(str(n)),
            'status': data.get('status', 'unknown'),
            'factors': data.get('factors', [])
        }
    except Exception as e:
        return {'k': k, 'seq': seq, 'error': str(e)}

def main():
    print("=" * 60)
    print("FACTORDB VERIFICATION CHECK")
    print("=" * 60)
    
    results = []
    
    for k, seq in LARGE_TERMS:
        print(f"\\nChecking {seq} k={k}...")
        result = check_factordb(k, seq)
        results.append(result)
        
        if 'error' in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  Digits: {result['digits']:,}")
            print(f"  FactorDB status: {result['status']}")
            
            if result['status'] == 'P':
                print("  [VERIFIED] FactorDB confirms prime")
            elif result['status'] == 'C':
                print("  [ERROR] FactorDB shows composite - CRITICAL")
            elif result['status'] == 'U':
                print("  [UNKNOWN] FactorDB has no record - needs verification")
        
        time.sleep(1)  # Rate limiting
    
    # Save results
    with open('verification/factordb/results.txt', 'w') as f:
        for r in results:
            f.write(f"{r}\\n")
    
    print("\\n" + "=" * 60)
    print("Results saved to: verification/factordb/results.txt")
    print("=" * 60)

if __name__ == "__main__":
    main()
'''
    
    with open('verification/check_factordb.py', 'w') as f:
        f.write(script)
    
    print("Created: verification/check_factordb.py")
    print("  Usage: python verification/check_factordb.py")

def main():
    """Main setup function"""
    print("=" * 60)
    print("A082700 LARGE TERM VERIFICATION SETUP")
    print("=" * 60)
    
    # Setup directories
    print("\n[1/4] Creating directory structure...")
    setup_verification_directory()
    
    # Generate number files
    print("\n[2/4] Generating plateau number files...")
    generate_large_number_files()
    
    # Create Primo script
    print("\n[3/4] Creating Primo batch script...")
    create_primo_batch_script()
    
    # Create FactorDB script
    print("\n[4/4] Creating FactorDB check script...")
    create_factordb_check_script()
    
    print("\n" + "=" * 60)
    print("SETUP COMPLETE")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Install Primo: http://www.ellipsa.eu/")
    print("  2. Run: bash verification/run_primo_batch.sh")
    print("  3. Or: python verification/check_factordb.py")
    print("\nEstimated verification time: 2-4 weeks (sequential)")
    print("                          3-7 days (parallel with multiple cores)")
    print("=" * 60)

if __name__ == "__main__":
    main()
