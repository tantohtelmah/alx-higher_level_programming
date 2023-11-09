#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_int = []
    for i in my_list:
        if i not in u_int:
            u_int.append(i)
    sum_u_int = sum(u_int)
    return sum_u_int
