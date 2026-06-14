"""Sliding window with set — O(n) time.

Step-by-step:
1) Grow the window from the right.
2) If a duplicate appears, shrink from the left until valid.
3) Track the maximum valid window length.
"""


def length_of_longest_substring(s: str) -> int:
    # Step 1: initialize state for the current window.
    seen: set[str] = set()
    left = 0
    best = 0

    for right, char in enumerate(s):
        # Step 2: shrink until the current char is unique in window.
        while char in seen:
            seen.remove(s[left])
            left += 1
        # Step 3: expand and record best length.
        seen.add(char)
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    tests = ["abcabcbb", "bbbbb", "pwwkew", ""]
    for t in tests:
        print(f"{t!r} -> {length_of_longest_substring(t)}")
