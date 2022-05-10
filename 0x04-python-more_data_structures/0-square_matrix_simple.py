#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for x in matrix:
        a = []
        for y in x:
            a.append(int(y**2))
        squares.append(a)
    return (squares)
