#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_num = "-" + str(number)[-1:]
elif number >= 0:
    last_num = str(number)[-1:]
if int(last_num) > 5:
    print(f"Last digit of {number} is {last_num} and is greater than 5")
elif int(last_num) == 0:
    print(f"Last digit of {number} is {last_num} and is 0")
else:
    print(f"Last digit of {number} is {last_num} and is less than 6 and not 0")
