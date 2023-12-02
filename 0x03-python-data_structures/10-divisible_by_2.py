#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x_boolist = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            x_boolist[count] = True
        else:
            x_boolist[count] = False
    return (x_boolist)
