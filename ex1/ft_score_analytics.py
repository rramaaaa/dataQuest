#!/usr/bin/env python3

import sys

print("=== Player Score Analytics ===")
argc: int = len(sys.argv) - 1
length: int = len(sys.argv)
i: int = 1
arr: list = []
while argc:
    if length == 1:
        raise print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    try:
        arr.append(int(sys.argv[i]))
    except ValueError as e:
        print(f"{e}")
    argc -= 1
    i += 1

print(f"Scores processed: {arr}")
print(f"Total players: {len(arr)}")
print(f"Total score: {sum(arr)}")
print(f"Average score: {sum(arr) / len(arr)}")
print(f"High score: {max(arr)}")
print(f"Low score: {min(arr)}")
print(f"Score range: {max(arr) - min(arr)}")
