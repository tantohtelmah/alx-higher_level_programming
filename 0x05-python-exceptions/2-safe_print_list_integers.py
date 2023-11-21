#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if count < x:
                print("{:d}".format(int(i)), end="\n")
                count += 1
                if count < x:
                    print(" ", end="\n")
        except:
            pass
    print()
    return count
