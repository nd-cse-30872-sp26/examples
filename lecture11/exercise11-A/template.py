#!/usr/bin/env python3

# Exercise 11-A: Cookies

import sys

# Functions

def readline() -> list[int]:
    # TODO: Read a line from stdin
    return []

def feed_children(children: list[int], cookies: list[int]) -> int:
    # TODO: Return number of children fed with cookies
    return 0

# Main execution

def main() -> None:
    while (children := readline()) and (cookies := readline()):
        print(feed_children(children, cookies))

if __name__ == '__main__':
    main()
