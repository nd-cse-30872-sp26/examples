#!/usr/bin/env python3

from dataclasses import dataclass
from typing      import Iterator, Optional

import sys

# Classes

@dataclass
class Node:
    ''' Node Structure '''
    value:  int
    left:   Optional['Node'] = None
    right:  Optional['Node'] = None

@dataclass
class Tree:
    ''' Tree Structure '''

    root:   Optional[Node] = None

    def search(self, value) -> bool:
        ''' Determine if value is in tree '''
        pass

    def _search(self, node: Optional[Node], value) -> bool:
        ''' Determine if value is in tree (recursively) '''
        pass

    def insert(self, value) -> None:
        ''' Add value into tree '''
        pass

    def _insert(self, node: Optional[Node], value) -> Node:
        ''' Add value into tree (recursively) '''
        pass

    def print(self):
        ''' Print all nodes in tree '''
        pass

    def _print(self, node: Optional[Node]):
        ''' Print all nodes in tree (recursively) '''
        pass

    def nodes(self) -> Iterator[int]:
        ''' Generate all nodes in tree '''
        pass

    def _nodes(self, node: Optional[Node]) -> Iterator[int]:
        ''' Generate all nodes in tree (recursively) '''
        pass

# Main Execution

def main(stream=sys.stdin):
    ''' For each line, insert each number into tree, search for items, and then
    print tree '''

    for line in stream:
        strs = line.split()                 # Split line into individual strings
        ints = [int(s) for s in strs]       # Convert each string into an int
        tree = Tree()

        for number in ints:                 # Insert ints into tree
            tree.insert(number)

        tree.print()

        for number in range(max(ints) + 1): # Search for ints in tree
            print(number, tree.search(number))

        for node in tree.nodes():
            print(node)

if __name__ == '__main__':
    main()
