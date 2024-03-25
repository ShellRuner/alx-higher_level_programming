#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) > 0 and len(matrix[0]) > 0:
        new_matrix = []
        for row in matrix:
            square_row = []
            for elemt in row:
                square_row.append(elemt ** 2)
            new_matrix.append(square_row)
        return new_matrix
    else:
        return matrix
