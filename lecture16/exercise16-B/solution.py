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

    for line in sys.stdin:
        if ':' not in line:
            continue

        targets, sources = line.split(':', 1)

        for target in targets.split():
            for source in sources.split():
                edges[source].add(target)
                degrees[target] += 1
                degrees[source]

    return Graph(edges, degrees)

# Topological Sort

def topological_sort(graph: Graph) -> list[str]:
    frontier = [v for v, d in graph.degrees.items() if d == 0]
    visited  = []

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        for neighbor in graph.edges[vertex]:
            graph.degrees[neighbor] -= 1
            if graph.degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited

# Main Execution

def main() -> None:
    graph    = read_graph()
    vertices = topological_sort(graph)

    if len(vertices) == len(graph.degrees):
        print(' '.join(vertices))
    else:
        print('There is a cycle!')

if __name__ == '__main__':
    main()
