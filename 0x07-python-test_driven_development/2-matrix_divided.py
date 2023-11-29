#!/usr/bin/python3
def raiseErr():
    raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
def matrix_divided(matrix, div):
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_div = []
    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, list):
                tmp = []
                for element in row:
                    if isinstance(element, (float, int)):
                        tmp.append(round(element / div, 2))
                    else:
                        raiseErr()
                matrix_div.append(tmp)
            else:
                raiseErr()
    else:
        raiseErr()
    return matrix_div
