#!/usr/bin/env python3

from collections import defaultdict, deque

import sys

# Types

Graph = dict[int, set[int]]

# Functions

def read_graph() -> Graph:
    ''' Read graph from standard input '''
    pass

def walk_graph_dfs_rec(graph: Graph, v: int, visited: set[int]) -> None:
    ''' Walk graph using DFS (recursive) '''
    pass

def walk_graph_dfs_iter(graph: Graph, v: int) -> None:
    ''' Walk graph using DFS (iterative) '''
    pass

def walk_graph_bfs_iter(graph: Graph, v: int) -> None:
    ''' Walk graph using BFS (iterative) '''
    pass

def walk_graph(graph: Graph, root: int, walk: int):
    if walk == 0:
        walk_graph_dfs_rec(graph, root, set())
    elif walk == 1:
        walk_graph_dfs_iter(graph, root)
    elif walk == 2:
        walk_graph_bfs_iter(graph, root)
    else:
        print(f'Unknown WalkType: {walk}', file=sys.stderr)

# Main Execution

def main():
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} root [0 = DFS_REC | 1 = DFS_ITER | 2 = BFS_ITER]', file=sys.stderr)
        return 1

    root  = int(sys.argv[1])
    walk  = int(sys.argv[2])
    graph = read_graph()

    walk_graph(graph, root, walk)

if __name__ == '__main__':
    main()
