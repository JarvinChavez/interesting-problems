// Early attempt — partial recursive expansion, no X wildcard handling

function handle_motif(motif) {
  const match = motif.match(/\[([^\]]+)\]/);
  if (!match) return [motif];

  const bracketContent = match[1];
  const beforeBracket = motif.slice(0, match.index);
  const afterBracket = motif.slice(match.index + match[0].length);
  const variations = [];

  bracketContent.split("").forEach((char) => {
    handle_motif(afterBracket).forEach((variation) => {
      variations.push(beforeBracket + char + variation);
    });
  });
  return variations;
}

// Missing: X wildcard, nested groups, regex-safe search
console.log(handle_motif("[ST]Q"));
