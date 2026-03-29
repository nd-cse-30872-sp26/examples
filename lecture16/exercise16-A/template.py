#!/usr/bin/env python3

# Exercise: 16-A: MST

import collections
import heapq
import sys

# Type Aliases

Graph    = dict[str, dict[str, int]]
Visited  = dict[str, str]
Frontier = list[tuple[int, str, str]]

# Build Graph

def read_graph() -> Graph:
    ''' Read in undirected graph '''
    g: Graph = collections.defaultdict(dict)
    for line in sys.stdin:
        source, target, weight = line.split()
        g[source][target] = int(weight)
        g[target][source] = int(weight)
    return g

# Compute MST

def compute_mst(g: Graph) -> Visited:
    frontier: Frontier = []
    visited : Visited  = {}
    start   : str      = list(g.keys())[0]

    # TODO

    return visited

# Main Execution

def main():
    # Read Graph
    g = read_graph()

    # Compute MST
    m = compute_mst(g)

    # Print Weight and Edges
    # TODO

if __name__ == '__main__':
    main()
