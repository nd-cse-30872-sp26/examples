#!/usr/bin/env python3

# Exercise 05-A: PBB-matched

import sys

# Functions

LEFT_PBB  = ('(', '[', '{')
RIGHT_PBB = (')', ']', '}')

def is_pbbmatched(s: str) -> bool:
    stack = []

    for symbol in s:
        if symbol in LEFT_PBB:          # Push stack PBB
            stack.append(symbol)
        else:
            try:
                top = stack.pop()
            except IndexError:          # Nothing stack to complete match
                return False

            # Make sure we have a match
            if LEFT_PBB.index(top) != RIGHT_PBB.index(symbol):
                return False

    return not stack

# Main execution

def main():
    for line in sys.stdin:
        line   = line.rstrip()
        result = 'Yes' if is_pbbmatched(line) else 'No'
        print(f'{line:>10}: {result}')

if __name__ == '__main__':
    main()
