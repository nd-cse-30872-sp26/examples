#!/usr/bin/env python3

import collections
import sys

# Type Aliases

Graph = dict[int, dict[int, int]]
Edge  = tuple[int, int]

# Read Graph

def read_graph() -> Graph:
    graph: Graph = collections.defaultdict(dict)

    for edge, line in enumerate(sys.stdin):
        s, t = map(int, line.split())
        graph[s][t] = edge
        graph[t][s] = edge

    return graph

# Find Circuit

def find_circuit(graph: Graph, start: int, vertex: int, visited: set[int], path: list[Edge]) -> list[Edge]:
    ''' Recursive DFS traversal '''
    # If we have returned to start, return path
    if path and start == vertex:
        return path

    # Visit each unvisited outgoing edge
    for neighbor in graph[vertex]:
        if graph[vertex][neighbor] in visited:
            continue

        # Mark visited
        visited.add(graph[vertex][neighbor])

        # Add to path
        path.append((vertex, neighbor))

        # Recurse
        if find_circuit(graph, start, neighbor, visited, path):
            return path

        # Remove from path
        path.pop(-1)

        # Unmark visited
        visited.remove(graph[vertex][neighbor])

    # No circuit found, so return nothing
    return []

# Find Eulerian Circuit

def find_euler_circuit(graph: Graph) -> list[Edge]:
    ''' Iteratively compute subcircuit until all edges have been travsrsed or
    no circuit is possible '''
    visited: set[int]   = set()                 # Visited edges (set of edge ordinals)
    circuit: list[Edge] = []                    # Eulerian circuit (list of edges)
    start  : int        = list(graph.keys())[0] # Starting vertex
    index  : int        = 0                     # Where in circuit to insert subcircuit

    while start:
        # Find subcircuit and insert it after current component
        path    = find_circuit(graph, start, start, visited, [])
        circuit = circuit[0:index] + path + circuit[index:]

        # Check if any nodes in current circuit have an unused edge, if so, set
        # start so we search for subcircuit beginning at that vertex
        start = 0
        for index, vertex in enumerate(source for source, target in circuit):
            for neighbor, edge in graph[vertex].items():
                if edge not in visited:
                    start = vertex
                    break

    return circuit

# Main Execution

def main() -> None:
    graph   = read_graph()
    circuit = find_euler_circuit(graph)

    for source, target in circuit:
        print(source, target)

if __name__ == '__main__':
    main()
