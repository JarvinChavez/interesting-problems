# Longest substring without repeating characters

## Problem

Given a string `s`, find the length of the **longest substring without repeating characters**.

Example: `"abcabcbb"` → `3` (`"abc"`)

## What went wrong (`attempt.py`)

I started a sliding-window loop but only printed prefixes (`s[:i]`) — never tracked a window, duplicates, or max length.

## How I'd solve it

Classic **sliding window + hash set**:
- Expand `right` pointer, add chars to a set
- When duplicate found, shrink from `left` until duplicate removed
- Track `max_len` across the walk — **O(n)** time, **O(min(n, alphabet))** space

See `solution.py`.
