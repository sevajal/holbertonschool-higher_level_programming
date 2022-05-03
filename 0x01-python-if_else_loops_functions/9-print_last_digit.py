#!/usr/bin/python3
def print_last_digit(number):
    str_number = str(number)
    last_digit_str = str_number[-1]
    last = int(last_digit_str)
    print(last, end='')
