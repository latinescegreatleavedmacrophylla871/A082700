#!/usr/bin/env python3
"""
A082700 Verification Script

Verifies the terms of OEIS sequence A082700:
Numbers k such that (15*10^(k-1) - 51)/9 is a plateau prime.

The sequence generates primes of the form 166...661
"""

import sys
# Increase limit for large integer string conversion (needed for k >= 6233)
sys.set_int_max_str_digits(100000)

import sympy as sp

# Known terms from OEIS A082700
KNOWN_TERMS = [5, 13, 17, 19, 37, 53, 73, 101, 6233, 24029, 40223, 66395]

def generate_plateau_number(k):
    """
    Generate the plateau number of the form 166...661
    Formula: (15*10^(k-1) - 51)/9
    """
    return (15 * 10**(k-1) - 51) // 9

def verify_term(k, verbose=True):
    """
    Verify if term k generates a prime number.
    Returns (is_prime, plateau_number, proof)
    """
    plateau_num = generate_plateau_number(k)
    
    if verbose:
        print(f"k = {k}")
        print(f"  Plateau number: {plateau_num}")
        print(f"  Digits: {len(str(plateau_num))}")
    
    # For small numbers, use deterministic primality test
    if k <= 100:
        is_prime = sp.isprime(plateau_num)
        if verbose:
            status = "[PRIME]" if is_prime else "[NOT PRIME]"
            print(f"  Status: {status}")
    else:
        # For large numbers, use probable prime test first
        is_probable_prime = sp.isprime(plateau_num)
        if verbose:
            status = "[PROBABLE PRIME]" if is_probable_prime else "[NOT PRIME]"
            print(f"  Status: {status}")
            if is_probable_prime:
                print(f"  NOTE: Large term requires rigorous primality proof")
        is_prime = is_probable_prime
    
    return is_prime, plateau_num

def verify_all_known_terms():
    """
    Verify all known terms from the sequence.
    """
    print("=" * 60)
    print("A082700 VERIFICATION REPORT")
    print("=" * 60)
    print(f"\nSequence: Numbers k such that (15*10^(k-1) - 51)/9 is prime")
    print(f"Form: 166...661 (plateau primes)")
    print(f"\nKnown terms: {KNOWN_TERMS}")
    print(f"Total terms to verify: {len(KNOWN_TERMS)}")
    print("\n" + "=" * 60)
    
    verified = []
    failed = []
    needs_proof = []
    
    for i, k in enumerate(KNOWN_TERMS, 1):
        print(f"\n[{i}/{len(KNOWN_TERMS)}] Verifying a({i}) = {k}")
        is_prime, num = verify_term(k, verbose=True)
        
        if is_prime:
            verified.append((k, num))
            if k > 100:
                needs_proof.append((k, num))
        else:
            failed.append((k, num))
        print("-" * 40)
    
    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"\nTerms verified: {len(verified)}/{len(KNOWN_TERMS)}")
    print(f"Terms failed: {len(failed)}/{len(KNOWN_TERMS)}")
    
    if needs_proof:
        print(f"\nTerms requiring rigorous proof: {len(needs_proof)}")
        for k, num in needs_proof:
            print(f"  - k = {k} ({len(str(num))} digits)")
    
    if failed:
        print(f"\nFAILED TERMS (CRITICAL):")
        for k, num in failed:
            print(f"  - k = {k}")
    
    print("\n" + "=" * 60)
    print("POISONING ASSESSMENT:")
    print("  - Harvey Dubner reference requires independent verification")
    print("  - Large terms (6233, 24029, 40223, 66395) need rigorous proof")
    print("  - Cross-check with multiple independent sources recommended")
    print("=" * 60)
    
    return len(failed) == 0

def search_for_new_terms(start_k=66396, max_k=100000):
    """
    Search for new terms in the sequence.
    This is computationally intensive for large k.
    """
    print(f"\nSearching for new terms from k={start_k} to k={max_k}...")
    print("(This may take a very long time for large ranges)")
    
    new_terms = []
    for k in range(start_k, max_k + 1):
        if k % 1000 == 0:
            print(f"  Checking k = {k}...")
        
        # Quick probable prime test first
        plateau_num = generate_plateau_number(k)
        if sp.isprime(plateau_num):
            print(f"\n*** FOUND: k = {k} is a probable prime term! ***")
            new_terms.append(k)
    
    if new_terms:
        print(f"\nNew terms found: {new_terms}")
    else:
        print("\nNo new terms found in search range.")
    
    return new_terms

if __name__ == "__main__":
    # Verify all known terms
    success = verify_all_known_terms()
    
    # Optionally search for new terms (commented out by default)
    # search_for_new_terms(start_k=66396, max_k=70000)
