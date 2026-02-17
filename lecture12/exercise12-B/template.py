#!/usr/bin/env python3

# Exercise 12-B: Squirrel Hunting

# Notes:
#
#   1. Each S(r, c) contains the optimal solution for that square.
#
#   2. Final solution is in the bottom right corner: S(n, n).
#
#   3. Building the table does not reveal what the path is, just what the
#   maximum squirrel population is.

import sys

# Type Aliases

Grid = list[list[int]]

# Functions

def read_grid(n: int) -> Grid:
    grid = [[0 for _ in range(n + 1)]]      # Pad grid
    for _ in range(n):
        grid.append([0] + list(map(int, sys.stdin.readline().split())))
    return grid

def hunt_squirrels(grid: Grid, n: int) -> Grid:
    # TODO: 1. Initialize table
    pass

    # TODO: 2. Build table
    pass

    # TODO: 3. Use table result
    pass

# Main execution

def main() -> None:
    while True:
        try:
            n = int(sys.stdin.readline())
        except ValueError:
            break

        grid  = read_grid(n)
        table = hunt_squirrels(grid, n)
        print(table[n][n])

if __name__ == '__main__':
    main()
