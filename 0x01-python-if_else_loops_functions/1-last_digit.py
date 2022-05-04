#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    abs = number * -1
else:
    abs = number
last = abs % 10
if number > 0 and last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif number > 0 and last > 0 and last < 6:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif number < 0 and last != 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is 0")
