#!/usr/bin/env python3

# Exercise 13-D: Invert Binary Tree

from collections import deque
from dataclasses import dataclass
from typing      import Optional
import sys

# Classes

@dataclass
class Node:
    value:  int
    left:   Optional['Node']
    right:  Optional['Node']

# Functions

def read_tree(values: list[int], index: int=0) -> Optional[Node]:
    # TODO: Use divide and conquer to parse tree
    return None

def walk_tree(root: Optional[Node]) -> list[int]:
    # TODO: Use BFS Traversal with Queue to create list of values
    return []

def dump_tree(root: Optional[Node]) -> None:
    print(','.join(map(str, walk_tree(root))))

def invert_tree(root: Optional[Node]) -> Optional[Node]:
    # TODO: Use divide and conquer to invert binary tree

    # Base Case: Invalid Node

    # Divide and Conquer: Swap left and right and recurse
    return None

# Main Execution

def main() -> None:
    for line in sys.stdin:
        values = list(map(int, line.split()))
        root   = read_tree(values)

        invert_tree(root)
        dump_tree(root)

if __name__ == '__main__':
    main()
