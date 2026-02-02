#!/usr/bin/env python3

# Exercise 09-A: Lotto

import itertools
import sys

# Constants

LOTTO_NUMBERS = 6

# Functions

def display_combinations(s: list[int], c: list[int], k: int) -> None:
    '''
    s:  Current combination
    c:  Numbers to choose from
    k:  Current element index
    '''

    # TODO: Recursively display combinations

    # Base: have complete subset
    pass

    # Recurse: with current
    pass

    # Recurse: skip current
    pass

# Main execution

def main() -> None:
    for line, numbers in enumerate(map(str.split, sys.stdin)):
        if len(numbers) <= 1:
            break

        if line:
            print('')

        display_combinations([], list(map(int, numbers[1:])), 0)

if __name__ == '__main__':
    main()
