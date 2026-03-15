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
    frontier = deque([root])

    while frontier:
        node = frontier.popleft()
        print(f' {node.value}', end='')

        if node.left:  frontier.append(node.left)
        if node.right: frontier.append(node.right)

# Traversal: DFS (Iterative)

def dfs(root: Node) -> None:
    frontier = [root]

    while frontier:
        node = frontier.pop()

        if not node:
            continue

        print(f' {node.value}', end='')

        frontier.append(node.right)
        frontier.append(node.left)

# Traversal: DFS (Recursive)

def dfs_recursive(root: Node) -> None:
    if root is None:
        return

    print(f' {root.value}', end='')
    dfs_recursive(root.left)
    dfs_recursive(root.right)

# Main Execution

def main():
    print(f'BFS:', end=''); bfs(AlgorithmTree); print()
    print(f'DFS:', end=''); dfs(AlgorithmTree); print()
    print(f'DFS:', end=''); dfs_recursive(AlgorithmTree); print()

if __name__ == '__main__':
    main()
