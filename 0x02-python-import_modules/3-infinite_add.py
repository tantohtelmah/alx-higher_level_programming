#!/usr/bin/python3
import sys


def add_all_args():
    args = sys.argv[1:]
    total = sum(int(arg) for arg in args)
    print(total)


if __name__ == '__main__':
    add_all_args()
