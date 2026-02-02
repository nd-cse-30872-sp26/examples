#!/usr/bin/env python3

# Exericse 09-B: Phone Combinations

from typing import Iterator

import sys

# Constants

LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

# Functions

'''
def phone_combinations(numbers: str, letters: str) -> list[str]:
    if not numbers:
        return [letters]

    results = []
    for letter in LETTERS[numbers[0]]:
        results.extend(
            phone_combinations(numbers[1:], letters + letter)
        )

    return results
'''

def phone_combinations(numbers: str, letters: str) -> Iterator[str]:
    if not numbers:
        yield letters
    else:
        for letter in LETTERS[numbers[0]]:
            yield from phone_combinations(numbers[1:], letters + letter)

# Main Execution

def main() -> None:
    for numbers in sys.stdin:
        for combination in phone_combinations(numbers.strip(), ''):
            print(combination)

if __name__ == '__main__':
    main()
