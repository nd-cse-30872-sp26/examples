#!/usr/bin/env python3

''' binary_tree.py

This demonstrates two different ways to represent binary trees.
'''

# Linked Node Representation

from dataclasses import dataclass
from typing      import Optional

@dataclass
class Node:
    value:  str
    left:   Optional['Node'] = None
    right:  Optional['Node'] = None

tree1 = Node('B', Node('I', Node('A'), Node('R')), Node('N', Node('Y')))

print('# Linked')
print(tree1)
print(tree1.value)
print(tree1.left.value)
print(tree1.left.right.value)

print()

# Array Based Representation

def left_child(index: int) -> int:
    return 2*index + 1

def right_child(index: int) -> int:
    return 2*index + 2

tree2 = 'BINARY'

print('# Array')
print(tree2)
print(tree2[0])
print(tree2[left_child(0)])
print(tree2[right_child(left_child(0))])
