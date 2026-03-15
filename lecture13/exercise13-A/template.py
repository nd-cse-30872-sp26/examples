#!/usr/bin/env python3

# Exercise 13-A: Traversal

from dataclasses import dataclass
from collections import deque

# Node structure

@dataclass
class Node:
    value:  str
    left:   'Node' = None
    right:  'Node' = None

# Pre-defined Trees

AlgorithmTree = \
    Node('A',
        Node('L',
            Node('O',
                Node('H'),
                Node('M')
            ),
            Node('R'),
        ),
        Node('G',
            Node('I'),
            Node('T'),
        ),
    )

# Traversal: BFS (Iterative)

def bfs(root: Node) -> None:
    pass

# Traversal: DFS (Iterative)

def dfs(root: Node) -> None:
    pass

# Traversal: DFS (Recursive)

def dfs_recursive(root: Node) -> None:
    pass

# Main Execution

def main():
    print(f'BFS:', end=''); bfs(AlgorithmTree); print()
    print(f'DFS:', end=''); dfs(AlgorithmTree); print()
    print(f'DFS:', end=''); dfs_recursive(AlgorithmTree); print()

if __name__ == '__main__':
    main()
