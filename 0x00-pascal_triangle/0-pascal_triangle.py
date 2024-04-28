#!/usr/bin/python3
"""Pascal's triangle solution."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        - n (int): The number of rows in the triangle.

    Returns:
        - list of lists: A list containing lists representing each row of Pascal's Triangle.
    """
    triangle = []
    
    for i in range(1, n + 1):
        row = [1] * i
        for j in range(2, i):
            row[j - 1] = triangle[i - 2][j - 2] + triangle[i - 2][j - 1]
        triangle.append(row)
    
    return triangle
