#!/usr/bin/env python3

# Exercise 08-A: Palindromic Permutations

import collections
import sys

# Functions

def is_palindromic(s: str) -> bool:
    ''' Counting Solution '''

    # counts = collections.Counter(s)
    counts: dict[str, int] = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1

    odds = 0
    for count in counts.values():
        odds += count % 2

    return odds <= 1

# Main Execution
    
def main() -> None:
    for word in sys.stdin:
        print('Yes' if is_palindromic(word.rstrip()) else 'No')

if __name__ == '__main__':
    main()
