#!/usr/bin/python3

"""pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    pascal_list = []
    if n <= 0:
        return pascal_list
    for i in range(n):
        pascal_list.append([])
        string = str(11**i)
        for char in string:
            pascal_list[i].append(int(char))
    return pascal_list
