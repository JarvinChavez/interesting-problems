"""Sliding window with set — O(n) time."""


def length_of_longest_substring(s: str) -> int:
    seen: set[str] = set()
    left = 0
    best = 0

    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    tests = ["abcabcbb", "bbbbb", "pwwkew", ""]
    for t in tests:
        print(f"{t!r} -> {length_of_longest_substring(t)}")
