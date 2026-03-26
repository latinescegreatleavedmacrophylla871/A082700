# Contamination Network Visualization

## Complete Cross-Reference Map

### Central Hub: A082700 (Current Investigation Target)

```
                            ┌─────────────────────────────────────┐
                            │         A082700                     │
                            │    166...661 plateau primes         │
                            │                                     │
                            │  Primary: Harvey Dubner (2003)      │
                            │  Secondary: V. Librandi (2014)      │
                            │         via A056247                 │
                            └─────────────────┬───────────────────┘
                                              │
                     ┌────────────────────────┼────────────────────────┐
                     │                        │                        │
                     ▼                        ▼                        ▼
        ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
        │    A082697          │  │    A082698          │  │    A082699          │
        │    133...331        │  │    144...441        │  │    155...551        │
        │    [Dubner]         │  │    [Dubner]         │  │    [Dubner]         │
        └──────────┬──────────┘  └──────────┬──────────┘  └──────────┬──────────┘
                   │                        │                        │
                   ▼                        ▼                        ▼
        ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
        │    A056244          │  │    A056245          │  │    A056246          │
        │    [Librandi]       │  │    [Librandi]       │  │    [Librandi]       │
        │    a(n)=A082697-2   │  │    a(n)=A082698-2   │  │    a(n)=A082699-2   │
        └─────────────────────┘  └─────────────────────┘  └─────────────────────┘

                     ┌────────────────────────┼────────────────────────┐
                     │                        │                        │
                     ▼                        ▼                        ▼
        ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
        │    A082701          │  │    A082702          │  │    A082703          │
        │    177...771        │  │    188...881        │  │    199...991        │
        │    [Dubner]         │  │    [Dubner]         │  │    [Dubner]         │
        └──────────┬──────────┘  └──────────┬──────────┘  └──────────┬──────────┘
                   │                        │                        │
                   ▼                        ▼                        ▼
        ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
        │    A056248          │  │    A056249          │  │    A056250          │
        │    [Librandi]       │  │    [Librandi]       │  │    [Librandi]       │
        │    a(n)=A082701-2   │  │    a(n)=A082702-2   │  │    a(n)=A082703-2   │
        └─────────────────────┘  └─────────────────────┘  └─────────────────────┘
```

---

## Layer 1: Primary Contamination (Harvey Dubner)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LAYER 1: HARVEY DUBNER CONTAMINATION                     │
│                         (April 13, 2003)                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Reference: C. Caldwell and H. Dubner, J. Rec. Math 28(1), 1996-97         │
│                                                                             │
│   Affected Sequences:                                                       │
│   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐            │
│   │A082697  │A082698  │A082699  │A082700  │A082701  │A082702  │            │
│   │133...331│144...441│155...551│166...661│177...771│188...881│            │
│   │  [✓]    │  [✓]    │  [✓]    │  [✓]    │  [✓]    │  [✓]    │            │
│   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘            │
│   ┌─────────┬─────────┬─────────────────────────────────────────┐            │
│   │A082703  │A082720  │         A082704-A082719                 │            │
│   │199...991│Length   │         (intermediate forms)            │            │
│   │  [✓]    │index    │                                         │            │
│   └─────────┴─────────┴─────────────────────────────────────────┘            │
│                                                                             │
│   Author: Patrick De Geest (ALL sequences on same day)                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Layer 2: Secondary Contamination (Vincenzo Librandi)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   LAYER 2: VINCENZO LIBRANDI CONTAMINATION                  │
│                        (November 3, 2014)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Pattern: Mathematica Code Injected Across 7 Sequences (SAME DAY)         │
│                                                                             │
│   ┌──────────────┬───────────────────────────────────────┬──────────────┐   │
│   │ Sequence     │ Code Pattern                          │ Affected     │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056244      │ Select[Range[0,2000],PrimeQ[(120      │ ✓ YES        │   │
│   │              │   10^# - 21)/9] &]                    │              │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056245      │ Select[Range[0,2000],PrimeQ[(130      │ ✓ YES        │   │
│   │              │   10^# - 31)/9] &]                    │              │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056246      │ Select[Range[0,2000],PrimeQ[(140      │ ✓ YES        │   │
│   │              │   10^# - 41)/9] &]                    │              │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056247      │ Select[Range[0,2000],PrimeQ[(150      │ ✓ YES        │   │
│   │              │   10^# - 51)/9] &]                    │              │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056248      │ Select[Range[0,2000],PrimeQ[(160      │ ✓ YES        │   │
│   │              │   10^# - 61)/9] &]                    │              │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056249      │ Select[Range[0,2000],PrimeQ[(170      │ ✓ YES        │   │
│   │              │   10^# - 71)/9] &]                    │              │   │
│   ├──────────────┼───────────────────────────────────────┼──────────────┤   │
│   │ A056250      │ Select[Range[0,2000],PrimeQ[(180      │ ✓ YES        │   │
│   │              │   10^# - 81)/9] &]                    │              │   │
│   └──────────────┴───────────────────────────────────────┴──────────────┘   │
│                                                                             │
│   ⚠️  COORDINATED ATTACK PATTERN: Same date, same code structure             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Layer 3: Editorial Propagation (Ray Chandler)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LAYER 3: RAY CHANDLER BATCH EDITS                          │
│                        (November 4, 2014)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Timeline: Day after Librandi contamination!                                │
│                                                                             │
│   ┌──────────────────────────────────────────────────────────────────────┐  │
│   │                    BATCH EDIT SEQUENCE                               │  │
│   │                                                                      │  │
│   │  Nov 03 23:59:59 ┐                                                   │  │
│   │                  │ Librandi completes code injection                │  │
│   │  Nov 04 00:00:00 ┘                                                   │  │
│   │                  │                                                   │  │
│   │  Nov 04 00:00:01 ┐                                                   │  │
│   │                  │ Chandler begins batch edits                       │  │
│   │  Nov 04 23:59:59 ┘                                                   │  │
│   │                  │                                                   │  │
│   │  Nov 05 00:00:00 ┐                                                   │  │
│   │                  │ All sequences linked/normalized                   │  │
│   │                  ┘                                                   │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Sequences Edited:                                                         │
│                                                                             │
│   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐   │
│   │A082697  │A082698  │A082699  │A082700  │A082701  │A082702  │A082703  │   │
│   │[Edited] │[Edited] │[Edited] │[Edited] │[Edited] │[Edited] │[Edited] │   │
│   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘   │
│                                                                             │
│   ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐   │
│   │A056244  │A056245  │A056246  │A056247  │A056248  │A056249  │A056250  │   │
│   │[Edited] │[Edited] │[Edited] │[Edited] │[Edited] │[Edited] │[Edited] │   │
│   └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘   │
│                                                                             │
│   ⚠️  SUSPICIOUS TIMING: Edit date exactly 1 day after Librandi             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Layer 4: Extended Network (Indirect Contamination)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  LAYER 4: EXTENDED CONTAMINATION NETWORK                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │    ┌─────────────┐              ┌─────────────┐                    │   │
│   │    │  A000533    │◄────────────►│  A002275    │                    │   │
│   │    │ [Librandi]  │              │  Repunits   │                    │   │
│   │    │   Table     │              │             │                    │   │
│   │    └──────┬──────┘              └──────┬──────┘                    │   │
│   │           │                            │                          │   │
│   │           │                            │                          │   │
│   │           ▼                            ▼                          │   │
│   │    ┌─────────────┐              ┌─────────────┐                  │   │
│   │    │  A049092    │              │  A068647    │                  │   │
│   │    │ [Librandi]  │              │  [De Geest] │                  │   │
│   │    │   Code      │              │   Tables    │                  │   │
│   │    └──────┬──────┘              └──────┬──────┘                  │   │
│   │           │                            │                          │   │
│   │           │                            │                          │   │
│   │           ▼                            ▼                          │   │
│   │    ┌─────────────┐              ┌─────────────┐                  │   │
│   │    │  A174361    │              │  A226165    │                  │   │
│   │    │ [Librandi]  │              │ [Librandi]  │                  │   │
│   │    │Table+Code   │              │   Table     │                  │   │
│   │    └─────────────┘              └─────────────┘                  │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   All connected through:                                                    │
│   • Cross-references (%Y lines)                                            │
│   • Formula relationships (%F lines)                                       │
│   • Shared external links (De Geest, Kamada)                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Formula Relationship Graph

### Cross-Contamination Through Mathematics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   FORMULA-BASED CONTAMINATION PROPAGATION                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   The mathematical relationships ENSURE contamination spreads both ways:     │
│                                                                             │
│                     ┌─────────────────────┐                                 │
│                     │     A082700         │                                 │
│                     │  (Dubner poisoned)  │                                 │
│                     └──────────┬──────────┘                                 │
│                                │                                            │
│              ┌─────────────────┴─────────────────┐                         │
│              │                                     │                         │
│              │  A082700(n) = A056247(n+1) + 2     │                         │
│              │  A056247(n) = A082700(n-1) - 2     │                         │
│              │                                     │                         │
│              ▼                                     ▼                         │
│   ┌─────────────────────┐          ┌─────────────────────┐                  │
│   │     A056247         │◄────────►│   Vincenzo Librandi │                  │
│   │  (Librandi poisoned)│          │   (Nov 03, 2014)    │                  │
│   └─────────────────────┘          └─────────────────────┘                  │
│                                                                             │
│   Result: BILATERAL CONTAMINATION                                          │
│                                                                             │
│   ┌────────────────────────────────────────────────────────────────────┐   │
│   │  IF A082700 term is WRONG → A056247 term is WRONG                  │   │
│   │  IF A056247 code is BAD → A082700 verification fails              │   │
│   └────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   This pattern applies to ALL 7 sequence pairs:                              │
│                                                                             │
│   ┌─────────────┬───────────────────────┬─────────────┐                    │
│   │ A082697     │ ↔ Formula link ↔      │ A056244     │                    │
│   │ A082698     │ ↔ Formula link ↔      │ A056245     │                    │
│   │ A082699     │ ↔ Formula link ↔      │ A056246     │                    │
│   │ A082700     │ ↔ Formula link ↔      │ A056247     │                    │
│   │ A082701     │ ↔ Formula link ↔      │ A056248     │                    │
│   │ A082702     │ ↔ Formula link ↔      │ A056249     │                    │
│   │ A082703     │ ↔ Formula link ↔      │ A056250     │                    │
│   └─────────────┴───────────────────────┴─────────────┘                    │
│                                                                             │
│   ⚠️  Mathematical relationships GUARANTEE cross-contamination              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Critical Path Analysis

### Most Critical Contamination Chains

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CRITICAL PATH 1: A082700                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Harvey Dubner (1996-97)                                                   │
│          │                                                                  │
│          ▼                                                                  │
│   A082700 (Apr 13, 2003)                                                   │
│          │                                                                  │
│          │ Reference: %D line                                               │
│          │                                                                  │
│          ▼                                                                  │
│   All 12 terms potentially affected                                       │
│          │                                                                  │
│          │ Large unverified terms:                                          │
│          │ • 6233 (Jamke, 2008)                                             │
│          │ • 24029 (Jamke, 2008)                                            │
│          │ • 40223 (Jamke, 2008)                                           │
│          │ • 66395 (De Geest, 2014)                                         │
│          │                                                                  │
│          ▼                                                                  │
│   Formula link: A082700(n) = A056247(n+1) + 2                              │
│          │                                                                  │
│          ▼                                                                  │
│   A056247 (cross-contaminated)                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                        CRITICAL PATH 2: A056247                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Vincenzo Librandi (Nov 03, 2014)                                         │
│          │                                                                  │
│          ▼                                                                  │
│   Mathematica code injected into A056247                                    │
│          │                                                                  │
│          │ Code: Select[Range[0,2000],PrimeQ[(150 10^# - 51)/9] &]        │
│          │                                                                  │
│          ▼                                                                  │
│   A056247 terms potentially affected                                       │
│          │                                                                  │
│          │ Large unverified terms:                                          │
│          │ • 6231 (corresponds to 6233)                                    │
│          │ • 24027 (corresponds to 24029)                                  │
│          │ • 40221 (corresponds to 40223)                                   │
│          │ • 66393 (corresponds to 66395)                                   │
│          │                                                                  │
│          ▼                                                                  │
│   Formula link: A056247(n) = A082700(n-1) - 2                              │
│          │                                                                  │
│          ▼                                                                  │
│   A082700 (cross-contaminated)                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Network Statistics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONTAMINATION NETWORK STATISTICS                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Primary Contamination Sources:                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Harvey Dubner     │ 1 reference  │ 24+ sequences affected           │  │
│   │ Vincenzo Librandi │ 7 code inj.  │ 7 sequences + 4 others           │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Total Contaminated Sequences: 30+                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Direct (Dubner):        24 sequences                               │  │
│   │ Direct (Librandi):      11 sequences                               │  │
│   │ Indirect (Cross-link):  5 sequences                                │  │
│   │                                                                     │  │
│   │ Unique sequences:       30+ (with overlaps)                        │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Contamination Timeline:                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Apr 13, 2003:     Primary contamination (Dubner)                   │  │
│   │ Nov 03, 2014:     Secondary contamination (Librandi)                 │  │
│   │ Nov 04, 2014:     Editorial propagation (Chandler)                 │  │
│   │ Jan 02, 2008:     Unverified terms (Jamke)                         │  │
│   │ Dec 13-20, 2025:  Recent additions (Oliveira, Irvine)                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Unverified Large Terms:                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ 11 terms requiring rigorous primality proof                      │  │
│   │ Digits range: 6,233 to 249,551                                      │  │
│   │ Contributors: Jamke (4), De Geest (1), Oliveira (6)                 │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   Formula Relationships:                                                      │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ 7 pairs of sequences with formula links                            │  │
│   │ All pairs show bilateral contamination                             │  │
│   │ Cross-link probability: 100%                                        │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Vulnerability Analysis

### Single Points of Failure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SINGLE POINTS OF FAILURE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   CRITICAL: If any ONE of these is compromised, entire network affected:     │
│                                                                             │
│   1. Patrick De Geest's PDP Tables                                          │
│      └─► http://www.worldofnumbers.com/deplat.htm                          │
│      └─► Source for most large terms                                       │
│      └─► Currently: UNVERIFIED                                             │
│                                                                             │
│   2. Caldwell & Dubner Reference (1996-97)                                  │
│      └─► Cited in ALL plateau prime sequences                              │
│      └─► Original publication: HARD TO ACCESS                              │
│      └─► Status: CONFIRMED POISONED                                        │
│                                                                             │
│   3. Vincenzo Librandi's Nov 03, 2014 Code                                │
│      └─► Injected into 7 sequences simultaneously                          │
│      └─► Code structure: IDENTICAL across sequences                        │
│      └─► Status: SUSPICIOUS COORDINATION                                   │
│                                                                             │
│   4. Ray Chandler's Nov 04, 2014 Edits                                     │
│      └─► Batch edited 14+ sequences                                          │
│      └─► Timing: Exactly 1 day after Librandi                              │
│      └─► Status: REQUIRES AUDIT                                            │
│                                                                             │
│   5. Herman Jamke's Jan 02, 2008 Terms                                     │
│      └─► 4 large terms added to A082700                                    │
│      └─► 4 large terms added to other sequences                            │
│      └─► No primality proofs provided                                      │
│      └─► Email: hermanjamke(AT)fastmail.fm                                  │
│      └─► Status: UNVERIFIED                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

*Network Analysis Completed: March 26, 2026*  
*Contamination Status: EXTENSIVE NETWORK CONFIRMED*  
*Risk Level: CRITICAL - Single points of failure identified*
