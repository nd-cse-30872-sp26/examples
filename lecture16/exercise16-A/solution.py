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

    heapq.heappush(frontier, (0, start, start))

    while frontier:
        weight, source, target = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source

        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (cost, target, neighbor))

    return visited

# Main Execution

def main():
    # Read Graph
    g = read_graph()

    # Compute MST
    m = compute_mst(g)

    # Print Weight and Edges
    e = sorted((min(s, t), max(s, t)) for s, t in m.items() if s != t)
    print(sum(g[s][t] for s, t in e))
    for s, t in e:
        print(s, t)

if __name__ == '__main__':
    main()
