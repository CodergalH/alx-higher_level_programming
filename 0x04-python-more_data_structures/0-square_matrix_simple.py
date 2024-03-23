#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[n**2 for n in i] for i in matrix]
    return new_matrix
