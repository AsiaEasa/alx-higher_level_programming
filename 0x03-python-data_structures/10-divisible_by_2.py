#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x_boolist = my_list[:]
    for y, i in enumerate(my_list):
        if i % 2 == 0:
            x_boolist[y] = True
        else:
            x_boolist[y] = False
    return (x_boolist)
