"""Incomplete attempt — prints prefixes instead of solving."""

s = "daokpsadpjwoinoajansdknwoanlkswsdwasdwsdlkmwmdksllckdmp"


def sliding_window(s: str) -> None:
    for i in range(len(s)):
        print(s[:i])  # never tracks window or max length


sliding_window(s)
