#!/usr/bin/env python3

# Exercise 04-A: Anagrams

import collections
import sys

# Functions

def is_anagram_count(s: str, t: str) -> bool:
    sc = [0]*26
    tc = [0]*26

    for c in s.lower(): sc[ord(c) - ord('a')] += 1
    for c in t.lower(): tc[ord(c) - ord('a')] += 1

    return sc == tc

def is_anagram_sorted(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())

def is_anagram_histogram(s: str, t: str) -> bool:
    sc = collections.Counter(s.lower())
    tc = collections.Counter(t.lower())
    return sc == tc

is_anagram = is_anagram_count # Select one of the solutions

# Main Execution

def main():
    for line in sys.stdin:
        first, second = line.strip().split()
        print('Anagram' if is_anagram(first, second) else 'Not Anagram')

if __name__ == '__main__':
    main()
