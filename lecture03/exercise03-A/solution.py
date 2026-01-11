#!/usr/bin/env python3

import sys

# Type Aliases

Matrix = list[list[int]]

# Functions

def read_matrix() -> Matrix:
    ''' Returns n x n matrix read from stdin '''
    n = int(sys.stdin.readline())
    return [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def find_max_row(matrix: Matrix) -> int:
    ''' Returns row with maximum total sum '''
    max_row, max_sum = 0, 0
    for cur_row, cur_numbers in enumerate(matrix, 1):
        cur_sum = sum(cur_numbers)
        if cur_sum > max_sum:
            max_row, max_sum = cur_row, cur_sum
    return max_row

# Main Execution

def main():
    ''' Reads in a series of matrices, finds maximum row of each matrix, and
    prints out result '''
    while matrix := read_matrix():
        max_row = find_max_row(matrix)
        print(max_row)

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
