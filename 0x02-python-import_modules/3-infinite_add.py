#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from not_int import is_not_integer
    
lenght = len(sys.argv)
result = 0
if lenght == 1:
    print("0")
else:
    for i in range(1, lenght):
        for arg in sys.argv[1, lenght]:
            if is_not_integer(arg):
                print("{} is not an integer".format(arg), end="")
        result += int(sys.argv[i])
    print("{}".format(result))
