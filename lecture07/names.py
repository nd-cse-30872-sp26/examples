#!/usr/bin/env python3

from dataclasses import dataclass

import collections
import sys

# Structures

# Person = collections.namedtuple('Person', 'first last')

@dataclass
class Person:
    first:  str
    last:   str

# Main execution

def main():
    people = [Person(*line.split()) for line in sys.stdin]
    
    #people = sorted(people, key=lambda p: p.first)
    #people = sorted(people, key=lambda p: p.last)

    people = sorted(people, key=lambda p: (p.last, p.first))

    for person in people:
        print(f'{person.first} {person.last}')

if __name__ == '__main__':
    main()
