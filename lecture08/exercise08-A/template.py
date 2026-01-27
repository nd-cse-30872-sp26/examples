#!/usr/bin/env python3

# Exercise 08-A: Palindromic Permutations

import collections
import sys

# Functions

def is_palindromic(s: str) -> bool:
    # TODO
    return False

# Main Execution

def main() -> None:
    for word in sys.stdin:
        print('Yes' if is_palindromic(word.rstrip()) else 'No')

if __name__ == '__main__':
    main()
