#!/usr/bin/env python3

# Exercise 10-C: SSSP

import collections
import heapq
import sys

# Type Aliases

Graph       = dict[str, dict[str, int]]
Visited     = dict[str, str]
Frontier    = list[tuple[int, str, str]]

# Build Graph

def read_graph() -> Graph:
    ''' Read in undirected graph '''
    g: Graph = collections.defaultdict(dict)
    # TODO
    return g

# Compute SSSP

def compute_sssp(g: Graph, start: str) -> Visited:
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    frontier: Frontier  = []
    visited : Visited   = {}
    
    # TODO
    return visited

def reconstruct_path(visited: Visited, source: str, target: str) -> list[str]:
    ''' Reconstruct path from source to target '''
    path = []
    curr = target
    # TODO
    return path[::-1]

# Main Execution

def main() -> None:
    # Read Graph
    g = read_graph()

    # Compute SSSP
    s = list(g.keys())[0]
    v = compute_sssp(g, s)

    # Reconstruct Path
    for t in list(g.keys())[1:]:
        print('{} -> {} = {}'.format(s, t, ' '.join(reconstruct_path(v, s, t))))

if __name__ == '__main__':
    main()
