#!/usr/bin/env python3

# Exercise 06-A: Perfect Square

import sys

# Iterative

def is_perfect_square(n: int) -> bool:
    ''' Binary search (Iterative) '''
    low, high = 1, n

    while low <= high:
        middle = (low + high) // 2
        square = middle * middle
        
        if square == n:
            return True

        if square > n:
            high = middle - 1
        else:
            low  = middle + 1

    return False

# Recursive

def is_perfect_square(n: int) -> int:
    ''' Binary search (recursive) '''
    return is_perfect_square_r(1, n, n)

def is_perfect_square_r(low: int, high: int, n: int) -> int:
    ''' Binary search (recursive) '''
    if low > high:
        return False

    middle = (low + high) // 2
    square = middle * middle
        
    if square == n:
        return True

    if square > n:
        return is_perfect_square_r(low, middle - 1, n)
    else:
        return is_perfect_square_r(middle + 1, high, n)

'''
# Linear search
def is_perfect_square(n):
    for i in range(1, n):
        if i*i == n:
            return True
    return False
'''

# Main Execution

def main() -> None:
    for n in map(int, sys.stdin):
        print('Yes' if is_perfect_square(n) else 'No')

if __name__ == '__main__':
    main()
