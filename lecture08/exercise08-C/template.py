#!/usr/bin/env python3

# Exercise 08-C: Contiguous Array

import collections
import sys

# Functions

def find_maximum_contiguous_array(array: list[int]) -> int:
    return 0 
        
# Main execution

def main() -> None:
    for line in sys.stdin:
        digits = list(map(int, line.split()))
        print(find_maximum_contiguous_array(digits))

if __name__ == '__main__':
    main()
