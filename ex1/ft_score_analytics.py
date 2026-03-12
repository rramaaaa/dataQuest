#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)

    if argc == 1:
        print("No scores provided. Usage: python3 ", end="")
        print("ft_score_analytics.py <score1>")
        print("<score2> ...")
    else:
        i: int = 1
        arr: list = []
        while i < argc:
            try:
                arg = int(sys.argv[i])
                arr.append(arg)
            except Exception as e:
                print(f"{e}")
            i += 1
        if len(arr) != 0:
            print(f"Scores processed: {arr}")
            print(f"Total players: {len(arr)}")
            print(f"Total score: {sum(arr)}")
            print(f"Average score: {sum(arr) / len(arr)}")
            print(f"High score: {max(arr)}")
            print(f"Low score: {min(arr)}")
            print(f"Score range: {max(arr) - min(arr)}")
