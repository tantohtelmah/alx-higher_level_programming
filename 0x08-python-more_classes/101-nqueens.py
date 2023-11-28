#!/usr/bin/python3

import sys


def nqueens(n):
    """
    Solves the N queens problem
    """

    if not isinstance(n, int):
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    def solve(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                solve(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    result = []
    solve([], [], [])
    for solution in result:
        for i in solution:
            row = ['.'] * n
            row[i] = 'Q'
            print(' '.join(row))
        print()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    nqueens(n)
