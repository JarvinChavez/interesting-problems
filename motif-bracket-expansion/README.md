# Motif bracket expansion

## Problem

Protein motif patterns use bracket notation for ambiguous amino acids, e.g. `[S T]Q` means Ser-or-Thr followed by Gln. Before searching a sequence, expand brackets into all concrete variants.

Used in NSF research when building iCn3D highlight commands.

## What went wrong (`attempt.js`)

Early recursive expansion worked for simple cases but I didn't handle:
- Nested brackets cleanly
- `X` wildcards (should expand to `[ACDEFGHIKLMNPQRSTVWY]`)
- Regex special characters in expanded motifs when searching

## How I'd solve it

1. Normalize `X` → full amino-acid bracket set
2. Recursively expand **leftmost** bracket group (see `solution.js`)
3. When searching, **escape regex metacharacters** in literal motifs
4. Full production version lives in [icn3d server `motifCheck`](https://github.com/JarvinChavez/icn3d-implementation-proof-of-concept/blob/main/iCn3D/server.js)
