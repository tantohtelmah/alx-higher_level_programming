#!/usr/bin/python3
import sys

lenght = len(sys.argv)
result = 0
if lenght == 1:
    print("0")
else:
    for i in range(1, lenght):
        result += int(sys.argv[i])
    print("{}".format(result))
