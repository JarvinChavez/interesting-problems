# Motif bracket expansion

## Problem

Protein motif patterns use bracket notation for ambiguous amino acids, e.g. `[S T]Q` means Ser-or-Thr followed by Gln. Before searching a sequence, expand brackets into all concrete variants.

Used in NSF research when building iCn3D highlight commands.

## What went wrong (`attempt.js`)

Early recursive expansion worked for simple cases but I didn't handle:
- Nested brackets cleanly
- `X` wildcards (should expand to `[ACDEFGHIKLMNPQRSTVWY]`)
- Regex special characters in expanded motifs when searching

## Step-by-step solution notes

1. **Normalize wildcards:** convert `X` to a full amino-acid option set.
2. **Find first bracket group:** parse leftmost `[ ... ]` token and split options.
3. **Expand recursively:** for each option, recurse on suffix and prepend prefix + option.
4. **Escape before search:** treat expanded motifs as literals by escaping regex metacharacters.
5. **Collect matches:** scan sequence and store start-end spans for each motif variant.
6. **Cross-check behavior:** compare outputs against the production `motifCheck` implementation in iCn3D server code.
