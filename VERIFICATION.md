# A082700 Investigation

## Python Verification Script

### Installation

```bash
pip install -r requirements.txt
```

### Usage

1. **Verify all known terms:**
```bash
python verify_a082700.py
```

2. **Search for new terms** (computationally intensive):
   - Edit the script and uncomment the `search_for_new_terms()` call
   - Adjust `start_k` and `max_k` parameters as needed

### Output

The script will:
- Verify each of the 12 known terms
- Report on primality status
- Identify terms requiring rigorous proof
- Flag any failed verifications

### Requirements

- Python 3.8+
- SymPy library (for primality testing)
- Sufficient memory for large number operations (terms 6233+ have thousands of digits)

### Verification Status

| Term | k | Verification |
|------|---|--------------|
| a(1) | 5 | Instant |
| a(2) | 13 | Instant |
| a(3) | 17 | Instant |
| a(4) | 19 | Instant |
| a(5) | 37 | Instant |
| a(6) | 53 | Instant |
| a(7) | 73 | Instant |
| a(8) | 101 | Fast |
| a(9) | 6233 | Slow (requires proof) |
| a(10) | 24029 | Very slow (requires proof) |
| a(11) | 40223 | Very slow (requires proof) |
| a(12) | 66395 | Very slow (requires proof) |

### Warning

Large terms (k > 1000) generate numbers with thousands of digits. Verification may:
- Take significant time
- Require substantial memory
- Need specialized primality proving software for rigorous proof

For terms above 1000 digits, consider using:
- Primo (primality proving software)
- Factordb.com (independent verification)
- Distributed computing projects
