#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        argc = len(sys.argv)
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        i = 1
        argc -= 1
        while argc:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
            argc -= 1
    print(f"Total arguments: {len(sys.argv)}")
