#!/usr/bin/env python3

# Exercise 12-A: Climbing Stairs

import sys

# Functions

def count_steps(n: int, cache: dict[int, int]={}) -> int:
    # TODO: Determine number of distinct ways to climb n steps using only
    # increments of 1 or 2 steps at a time.
    return 0

# Main Execution

def main() -> None:
    for n in map(int, sys.stdin):
        print(count_steps(n))

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
