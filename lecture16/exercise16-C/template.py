#!/usr/bin/env python3

# Exercise 16-C: Passcode Cracking

import collections
import sys

# Graph structure

Graph = collections.namedtuple('Graph', 'edges degrees')

# Read Graph

def read_graph() -> Graph:
    # TODO
    pass

# Topological Sort

def topological_sort(graph: Graph) -> list[int]:
    # TODO
    pass

# Main Execution

def main() -> None:
    graph = read_graph()
    code  = topological_sort(graph)

    print(''.join(map(str, code)))

if __name__ == '__main__':
    main()
