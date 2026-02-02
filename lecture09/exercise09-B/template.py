#!/usr/bin/env python3

# Exercise 09-B: Phone Combinations

from typing import Iterator

import sys

# Constants

# Functions

def phone_combinations(numbers: str, letters: str) -> Iterator[str]:
    # TODO: Recursively generate combinations
    pass

# Main Execution

def main() -> None:
    for numbers in sys.stdin:
        for combination in phone_combinations(numbers.strip(), ''):
            print(combination)

if __name__ == '__main__':
    main()
