#!/usr/bin/env python3

# Exercise 09-A: Lotto

import itertools
import sys

# Constants

LOTTO_NUMBERS = 6

# Functions

'''
def display_combinations(s: list[int]) -> None:
    for combination in sorted(itertools.combinations(s, LOTTO_NUMBERS)):
        print(' '.join(map(str, combination)))
'''

def display_combinations(s: list[int], c: list[int], k: int) -> None:
    '''
    s:  Current combination
    c:  Numbers to choose from
    k:  Current element index
    '''
    if k == len(c):
        if len(s) == LOTTO_NUMBERS:
            print(' '.join(map(str, s)))
        return

    display_combinations(s + [c[k]], c, k + 1)
    display_combinations(s         , c, k + 1)

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
