#!/usr/bin/pthon3

"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    - n (int): The number of rows in the triangle.

    Returns:
    - list of lists: A list containing lists representing each row of Pascal's Triangle.
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
