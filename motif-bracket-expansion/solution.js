/**
 * Expand bracketed motif patterns into concrete amino-acid strings.
 *
 * Step-by-step:
 * 1) Normalize wildcard X into a full amino-acid option set.
 * 2) Recursively expand one bracket group at a time.
 * 3) Escape variants before regex search.
 * 4) Record all match spans for each expanded motif.
 */

const AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY";

function normalizeWildcards(motif) {
  return motif.replace(/X/g, `[${AMINO_ACIDS}]`);
}

function expandMotif(motif) {
  const normalized = normalizeWildcards(motif);
  const match = normalized.match(/\[([^\]]+)\]/);
  if (!match) return [normalized];

  const options = match[1].split(/\s+/).filter(Boolean);
  const prefix = normalized.slice(0, match.index);
  const suffix = normalized.slice(match.index + match[0].length);

  const out = [];
  for (const opt of options) {
    for (const rest of expandMotif(suffix)) {
      out.push(prefix + opt + rest);
    }
  }
  return out;
}

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function findMotifPositions(motif, sequence, startOffset = 0) {
  const positions = [];
  for (const variant of expandMotif(motif)) {
    const re = new RegExp(escapeRegex(variant), "g");
    let match;
    while ((match = re.exec(sequence)) !== null) {
      const start = match.index + startOffset;
      positions.push(`${start}-${start + variant.length - 1}`);
    }
  }
  return positions;
}

module.exports = { expandMotif, findMotifPositions };

if (require.main === module) {
  console.log(expandMotif("[S T]Q"));
  console.log(findMotifPositions("[S T]Q", "abcSQdefSTQghi", 0));
}
