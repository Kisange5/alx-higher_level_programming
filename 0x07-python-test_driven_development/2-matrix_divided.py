#!/usr/bin/python3
"""module documentation"""


def matrix_divided(matrix, div):
    """returns a matrix with values divided by div
    Args:
        matrix (list): the matrix to divide
        div (int)/(float): the divider
    Return:
          new matrix with values
    """
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(error1)
    num_item = []
    i = 0
    for item in matrix:
        if type(item) is not list:
            raise TypeError(error1)
        for n in item:
            num_item.append(len(item))
            i += 1
            if type(n) is not int and type(n) is not float:
                raise TypeError(error1)
    size_list = num_item[0]
    for n in num_item:
        if n != size_list:
            raise TypeError(error2)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for in_list in matrix:
        inner_list = []
        new_matrix.append(inner_list)
        for num in in_list:
            new_num = round(num / div, 2)
            inner_list.append(new_num)
    return new_matrix
