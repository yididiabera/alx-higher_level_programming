#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in range(len(matrix)):
        squared_matrix.append([j**2 for j in matrix[i]])
    return squared_matrix
