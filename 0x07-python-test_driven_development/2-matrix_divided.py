#!/usr/bin/python3

"""2-matrix_divided module that contain the function matrix_divided"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    if type(matrix) is not list or type(matrix[0]) is not list \
            or type(matrix[1]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
            of integers/floats")
    for x in matrix[0]:
        if type(x) not in [int, float]:
            raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    for x in matrix[1]:
        if type(x) not in [int, float]:
            raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    if len(matrix[0]) is not len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for x in range(2):
        result.append([])
    for x in range(len(matrix[0])):
        result[0].append(round(float(matrix[0][x] / div), 2))
    for x in range(len(matrix[1])):
        result[1].append(round(float(matrix[1][x] / div), 2))
    return (result)
