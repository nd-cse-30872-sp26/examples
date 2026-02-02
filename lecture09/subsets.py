#!/usr/bin/env python3

from typing import Any, Iterator

import itertools

# Constants

NUMBERS = list(range(0, 10))

# Functions

def subsets(s: list[Any], c: list[Any], k: int=0) -> Iterator[list[Any]]:
    '''
    s:  current subset
    c:  all candidate elements
    k:  index of current candidate element
    '''

    # Base case: we have exhausted all candidates
    if k == len(c):
        yield s

    # Recursive cases
    else:
        # Recurse without using current element
        yield from subsets(s, c, k + 1)

        # Recurse while using current element
        yield from subsets(s + [c[k]], c, k + 1)

# Main Execution

def main() -> None:
    count = 0
    for length in range(0, len(NUMBERS) + 1):
        for subset in itertools.combinations(NUMBERS, length):
            if sum(subset) % 3 == 0:
                count += 1

    print(count)

    count = sum(1 for subset in subsets([], NUMBERS) if sum(subset) % 3 == 0)
    print(count)

if __name__ == '__main__':
    main()
