#!/usr/bin/python3
import sys

lenght = len(sys.argv)
if lenght == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(lenght - 1))
    for i in range(lenght - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
