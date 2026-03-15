#!/usr/bin/env python3

# Exercise 13-E: BST Balanced

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

def bst_insert(node: Optional[Node], value: int) -> Optional[Node]:
    # Base: node doesn't exist, so return a new one
    if not node:
        return Node(value, None, None)

    # Recursive: insert left if value is less than or equal to current Node,
    # otherwise insert right
    if value <= node.value:
        node.left  = bst_insert(node.left, value)
    else:
        node.right = bst_insert(node.right, value)

    return node

def is_balanced(root: Optional[Node], height: int=0) -> tuple[bool, int]:
    ''' Use divide and conquer to determine if a binary tree is balanced '''
    # Base Case: Invalid node, so return current height and that it is balanced
    if not root:
        return True, height

    # Divide and Conquer: Recursively compute height of left and right
    # sub-trees and if they are balanced
    left_balanced , left_height  = is_balanced(root.left)
    right_balanced, right_height = is_balanced(root.right)

    # Combine: compute height and whether or not the overall tree is balanced
    balanced = (left_balanced and right_balanced) and abs(left_height - right_height) <= 1
    height   = max(left_height, right_height) + 1
    return balanced, height

# Main Execution

def main() -> None:
    for line in sys.stdin:
        # Construct BST
        root = None
        for value in map(int, line.split()):
            root = bst_insert(root, value)

        # Determine if BST is balanced
        balanced, height = is_balanced(root)
        print('Balanced' if balanced else 'Unbalanced')

if __name__ == '__main__':
    main()
