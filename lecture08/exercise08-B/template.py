#!/usr/bin/env python3

# Exercise 08-B: Happy Number

import sys

# Function

def is_happy(n: int, seen: set[int]) -> bool:
    # TODO
    return False

# Main execution

def main() -> None:
    for n in map(int, sys.stdin):
        print('Yes' if is_happy(n, set()) else 'No')

if __name__ == '__main__':
    main()
