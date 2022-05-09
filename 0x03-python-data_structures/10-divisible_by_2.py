#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    confirmation = []
    for x in my_list:
        if x % 2 == 0:
            confirmation.append(True)
        else:
            confirmation.append(False)
    return (confirmation)
