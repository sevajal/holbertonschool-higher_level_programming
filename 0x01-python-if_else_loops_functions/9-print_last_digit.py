#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        abs = number * -1
    else:
        abs = number
    last = abs % 10
    print(last, end='')
    return(last)
