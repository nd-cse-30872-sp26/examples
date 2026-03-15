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
    if index >= len(values):
        return None

    return Node(
        values[index], 
        read_tree(values, 2*index + 1), 
        read_tree(values, 2*index + 2)
    )

def walk_tree(root: Optional[Node]) -> list[int]:
    # BFS Traversal with Queue
    nodes  = deque([root])
    values = []

    while nodes:
        node = nodes.popleft()

        if not node:
            continue

        values.append(node.value)

        nodes.append(node.left)
        nodes.append(node.right)

    return values

def dump_tree(root: Optional[Node]) -> None:
    print(','.join(map(str, walk_tree(root))))

def invert_tree(root: Optional[Node]) -> Optional[Node]:
    # Base Case: Invalid Node
    if root is None:
        return None

    # Divide and Conquer: Swap left and right and recurse
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# Main Execution

def main() -> None:
    for line in sys.stdin:
        values = list(map(int, line.split()))
        root   = read_tree(values)
        #dump_tree(root)

        invert_tree(root)
        dump_tree(root)

if __name__ == '__main__':
    main()
