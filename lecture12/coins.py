#!/usr/bin/env python3

import sys

# Constants

COINS = (1, 3, 4)

# Functions

def compute_table(n: int, coins: tuple[int]=COINS) -> list[int]:
    # Initialize table to n's
    table = [n] * (n + 1)

    # Initialize base cases (ie. coins)
    table[0] = 0
    for coin in coins:
        table[coin] = 1

    # For each entry i in table, compute the following recurrence relation:
    #
    #   table[i] = min(table[i - coin] + 1 for coin in coins if (i - coin) >= 0)
    for i in range(1, n + 1):
        table[i] = min(table[i - coin] + 1 for coin in coins if (i - coin) >= 0)

    return table

def compute_table_forward(n: int, coins: tuple[int]=COINS) -> list[int]:
    ''' Rather than looking backwards, we can generate the table by looking
    forwards.'''

    # Initialize table to n
    table = [n] * (n + 1)

    # Initialize base cases (ie. coins)
    table[0] = 0
    for coin in coins:
        table[coin] = 1

    # For each entry i in table, generate successive values:
    #
    #   table[i + coin] = min(table[i] + 1, table[i + coin])
    for i in range(1, n - max(coins) + 1):
        for coin in coins:
            table[i + coin] = min(table[i] + 1, table[i + coin])

    return table

# Main execution

def main() -> None:
    # Pre-compute all solutions up to 100
    table = compute_table(100)

    # Lookup solutions in table
    for n in map(int, sys.stdin):
        print(f'{n} = {table[n]}')

if __name__ == '__main__':
    main()
