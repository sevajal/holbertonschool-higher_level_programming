#!/usr/bin/python3

"""2-matrix_divided module that contain the function matrix_divided"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    e = "matrix must be a matrix (list of lists) of integers/floats"
    result = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not matrix[0]:
        raise TypeError(e)
    if type(matrix) is not list:
        raise TypeError(e)
    if not all([len(x) == len(matrix[0]) for x in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    for x in matrix:
        if type(x) is not list:
            raise TypeError(e)
        for element in x:
            if type(element) not in [int, float]:
                raise TypeError(e)
        row = [round(element / div, 2) for element in x]
        result.append(row)
    return (result)
