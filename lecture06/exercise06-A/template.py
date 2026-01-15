#!/usr/bin/env python3

# Exercise 06-A: Perfect Square

import sys

# Functions

def is_perfect_square(n: int) -> bool:
    # TODO: Use binary search to determine if n is a perfect valid square
    return False

# Main Execution

def main():
    for n in map(int, sys.stdin):
        print('Yes' if is_perfect_square(n) else 'No')

if __name__ == '__main__':
    main()
