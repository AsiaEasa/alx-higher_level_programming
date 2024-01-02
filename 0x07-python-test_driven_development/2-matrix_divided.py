#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix (list of lists): The matrix containing integers or floats.
    div (int or float): The number to divide the matrix elements by.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If each row of the matrix does not have the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """

    # Validate matrix
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate matrix rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
