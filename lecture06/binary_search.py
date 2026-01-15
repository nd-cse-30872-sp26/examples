#!/usr/bin/env python3

# Functions

def binary_search_iterative(data: list[int], target: int) -> bool:
    '''
    >>> binary_search_iterative([2, 5, 9], 2)
    True

    >>> binary_search_iterative([2, 5, 8, 9], 5)
    True

    >>> binary_search_iterative([2, 5, 8, 9], 0)
    False

    >>> binary_search_iterative([2, 5, 8, 9], 7)
    False
    '''
    start = 0
    end   = len(data)

    while start <= end:
        middle   = (start + end) // 2
        midpoint = data[middle]

        if midpoint == target:
            return True

        if midpoint > target:
            end = middle - 1
        else:
            start = middle + 1

    return False

def binary_search_recursive(
    data:   list[int],
    target: int,
    start:  int | None = None,
    end:    int | None = None
) -> bool:
    '''
    >>> binary_search_recursive([2, 5, 9], 2)
    True

    >>> binary_search_recursive([2, 5, 8, 9], 5)
    True

    >>> binary_search_recursive([2, 5, 8, 9], 0)
    False

    >>> binary_search_recursive([2, 5, 8, 9], 7)
    False
    '''
    start = 0         if start is None else start
    end   = len(data) if end   is None else end

    if start > end:
        return False

    middle   = (start + end) // 2
    midpoint = data[middle]

    if midpoint == target:
        return True

    if midpoint > target:
        return binary_search_recursive(data, target, start, middle - 1)
    else:
        return binary_search_recursive(data, target, middle + 1, end)
