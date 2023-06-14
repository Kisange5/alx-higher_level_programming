#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nMatrix = []
    for i in range(len(matrix)):
        mat_in = []
        for j in matrix[i]:
            mat_in.append(j ** 2)
        nMatrix.append(mat_in)
    return nMatrix
