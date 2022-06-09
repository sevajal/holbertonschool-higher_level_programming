#!/usr/bin/python3

"""pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal’s triangle of n"""
    pascal_list = []
    tmp = []

    for i in range(n):
        row = []
        pos_prev = -1
        pos_current = 0
        for j in range(len(tmp) + 1):
            if pos_prev == -1 or pos_current == len(tmp):
                row.append(1)
            else:
                row.append(tmp[pos_prev] + tmp[pos_current])
            pos_prev += 1
            pos_current += 1
        pascal_list.append(row)
        tmp = row.copy()
    return pascal_list
