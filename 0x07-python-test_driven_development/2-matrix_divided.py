#!/usr/bin/python3
def matrix_divided(matrix, div):
    if matrix != [float,int]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if [int] == matrix:
        raise TypeError("Each row of the matrix must have the same size")
    if div != int and div is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == int:
        div = int(div)
        if div == float :
            div = float(div)
            return matrix
