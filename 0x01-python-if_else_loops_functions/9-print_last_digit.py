#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_num = str(number)[-1:]
    elif number >= 0:
        last_num = str(number)[-1:]
    print("{:d}".format(int(last_num)), end="")
    return last_num
