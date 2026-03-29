#!/usr/bin/env python3

# Exercise 16-B: Walking Makefiles

import collections
import sys

# Graph Structure

Graph = collections.namedtuple('Graph', 'edges degrees')

# Read Graph

def read_graph() -> Graph:
    edges  : dict[str, set[str]] = collections.defaultdict(set)
    degrees: dict[str, int]      = collections.defaultdict(int)

    # TODO: Read Makefile from stdin

    return Graph(edges, degrees)

# Topological Sort

def topological_sort(graph: Graph) -> list[str]:
    frontier = [v for v, d in graph.degrees.items() if d == 0]
    visited  = []

    # TODO: Perform topological sort

    return visited

# Main Execution

def main() -> None:
    graph    = read_graph()
    vertices = topological_sort(graph)

    # TODO: Check for cycle, otherwise display ordering

if __name__ == '__main__':
    main()
