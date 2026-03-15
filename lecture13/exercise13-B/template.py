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

    # Divide and Conquer: Recursively solve left and right sub-trees

    # Combine: Take minimum of current node and left and right minimums
    return 0

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
