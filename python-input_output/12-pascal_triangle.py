#!/usr/bin/python3
"""
Module for Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists that resemble
    Pascal's Triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)
        pascal.append(row)

    return pascal
