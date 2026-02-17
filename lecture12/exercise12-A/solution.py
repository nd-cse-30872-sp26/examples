#!/usr/bin/env python3

# Exerciase 12-A: Climbing Stairs

import sys

# Functions

def count_steps(n: int, cache: dict[int, int]={}) -> int:
    if n <= 2:
        return n

    if n not in cache:
        cache[n] = (
            count_steps(n - 1, cache) +
            count_steps(n - 2, cache)
        )

    return cache[n]

# Main Execution

def main() -> None:
    for n in map(int, sys.stdin):
        print(count_steps(n))

if __name__ == '__main__':
    main()
