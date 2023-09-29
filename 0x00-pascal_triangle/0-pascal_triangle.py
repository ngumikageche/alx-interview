#!/usr/bin/python3
"""
a function that returns a list of lists
of integer rep the Pascals's triangle of n
"""


def pascal_triangle(n):
    """func to rep the pascals's triangle
    n (int)
    returns an empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)

    return triangle
