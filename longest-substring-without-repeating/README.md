# Longest substring without repeating characters

## Problem

Given a string `s`, find the length of the **longest substring without repeating characters**.

Example: `"abcabcbb"` → `3` (`"abc"`)

## What went wrong (`attempt.py`)

I started a sliding-window loop but only printed prefixes (`s[:i]`) — never tracked a window, duplicates, or max length.

## Step-by-step solution notes

1. **Initialize window state:** `left = 0`, empty `seen` set, `best = 0`.
2. **Expand right pointer:** iterate characters from left to right.
3. **Handle duplicates:** while current char is already in `seen`, remove `s[left]` and increment `left`.
4. **Record current window:** add current char, compute window length `right - left + 1`, and update `best`.
5. **Return answer:** final `best` is the longest substring length.

See `solution.py`.
