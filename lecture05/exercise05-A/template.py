#!/usr/bin/env python3

# Exericse 05-A: PBB-matched

import sys

# Functions

LEFT_PBB  = ('(', '[', '{')
RIGHT_PBB = (')', ']', '}')

def is_pbbmatched(s: str) -> bool:
    # TODO: Process string s using a stack to determine if the symbols are balanced 
    return False

# Main execution

def main():
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print(f'{line:>10}: {result}')

if __name__ == '__main__':
    main()
