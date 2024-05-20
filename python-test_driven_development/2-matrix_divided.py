#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: a matrix of ints and floats.
        div: the number to divide by.

    Returns:
        A new matrix with all the elements divided by div.

    Raises:
        TypeError: If matrix is not a list ints or floats,
                    or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix of ints/floats")

    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix of ints/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
