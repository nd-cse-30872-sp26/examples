#!/usr/bin/env python3

# Exercise 11-A: Cookies

import sys

# Functions

def readline() -> list[int]:
    return sorted(map(int, sys.stdin.readline().split()))

def feed_children(children: list[int], cookies: list[int]) -> int:
    count = 0

    while cookies and children:
        child  = children.pop()
        cookie = cookies[-1]

        if cookie >= child:
            cookies.pop()
            count += 1

    return count

# Main execution

def main() -> None:
    while (children := readline()) and (cookies := readline()):
        print(feed_children(children, cookies))

if __name__ == '__main__':
    main()
