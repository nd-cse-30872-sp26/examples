#!/usr/bin/env python3

# Exercise 11-B: Max Min

import sys

# Functions

def read_numbers() -> tuple[int, int, list[int]]:
    try:
        n = int(sys.stdin.readline())
        k = int(sys.stdin.readline())
        v = [int(sys.stdin.readline()) for _ in range(n)]
    except ValueError:
        return 0, 0, []

    return n, k, v

def compute_unfairness(n: int, k: int, v: list[int]) -> int:
    # TODO: Compute minimum unfairness
    return 0

# Main execution

def main() -> None:
    n, k, v = read_numbers()
    while n: 
        print(compute_unfairness(n, k, v))
        n, k, v = read_numbers()

if __name__ == '__main__':
    main()
