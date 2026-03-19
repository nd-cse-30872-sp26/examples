#!/usr/bin/env python3

# Exercise 14-B: Bicolorable

from typing import Iterable

import collections
import sys

# Constants

BLUE = 0
RED  = 1

# Type Aliases

Graph = dict[int, set[int]]

# Read Graph

def read_graph() -> Graph:
    ''' Construct adjacency set '''
    try:
        n, m = map(int, sys.stdin.readline().split())
    except ValueError:
        return {}

    graph: Graph = {v: set() for v in range(n)}

    for _ in range(m):
        source, target = map(int, sys.stdin.readline().split())
        graph[source].add(target)
        graph[target].add(source)

    return graph

# Determine if Bicolorable

def is_bicolorable(g: Graph) -> bool:
    ''' Determines if graphis bicolorable by walking it recursively. '''
    return walk1(g, list(g.keys())[0], BLUE, {})

def walk1(g: Graph, n: int, color: int, visited: dict[int, int]) -> bool:
    ''' Recursively walk graph and verifying that the node has the appropriate
    color. '''

    # We have already visited this node, so verify we still have the same
    # color.
    if n in visited:
        return visited[n] == color

    # We have not visited this node yet, so store its color.
    visited[n] = color

    # Visit each neighbor recursively with the alternate color and check that
    # they are colorable.
    for v in g[n]:
        if not walk1(g, v, (color + 1) % 2, visited):
            return False

    return True

def walk2(g: Graph, n: int, color: int, visited: dict[int, int]) -> bool:
    ''' Iteratively walk graph and verifying that the node has the appropriate
    color. '''
    # Establish frontier with initial node and color
    frontier = [(n, color)]
    
    # While there are still nodes in the frontier...
    while frontier:
        # Pop one node from frontier
        v, c = frontier.pop()

        # Check if it has been visited
        if v in visited:
            if c != visited[v]:
                return False
            else:
                continue

        # Mark that it has been visited
        visited[v] = c

        # Add neighbors to frontier
        for u in g[v]:
            frontier.append((u, (c + 1) % 2))

    return True

# Main execution

def main() -> None:
    while graph := read_graph():
        if is_bicolorable(graph):
            print('BICOLORABLE')
        else:
            print('NOT BICOLORABLE')

if __name__ == '__main__':
    main()
