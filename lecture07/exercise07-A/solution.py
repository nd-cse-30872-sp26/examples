#!/usr/bin/env python3

# Exercise 07-A: Largest Number

import functools
import sys

# Functions

def compare_numbers(a: str, b: str) -> int:
    ab = int(a + b)
    ba = int(b + a)
    return ab - ba

# Main execution

def main() -> None:
    sort_key = functools.cmp_to_key(compare_numbers)
    for line in sys.stdin:
        print(''.join(sorted(line.split(), key=sort_key, reverse=True)))

if __name__ == '__main__':
    main()
