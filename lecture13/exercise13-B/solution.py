#!/usr/bin/env python3

# Exercise 13-B: Binary Tree Min

from dataclasses import dataclass
from typing import Optional
import sys

# Structures

@dataclass
class Node:
    value: int
    left:  Optional['Node']
    right: Optional['Node']

# Functions

def minimum_tree(root: Optional[Node]) -> int:
    ''' Use divide and conquer to compute the minimum of binary tree '''
    # Base case: Invalid Node
    if not root:
        return sys.maxsize

    # Divide and Conquer: Recursively solve left and right sub-trees
    left_min  = minimum_tree(root.left)
    right_min = minimum_tree(root.right)

    # Combine: Take minimum of current node and left and right minimums
    return min(root.value, left_min, right_min)

# Main Execution

def main() -> None:
    # Create tree
    root = Node(7,
        Node(5,
                Node(3, None, None),
                None),
        Node(4,
                None,
                Node(2, None, None),
    ))

    # Compute minimum of tree
    print(minimum_tree(root))

if __name__ == '__main__':
    main()
