#!/usr/bin/python3
"""
Pascal_triangle
"""


def pascal_triangle(n):
    """Pascal triangle"""
    triangle = []

    def get_row(n):
        """Get nth term of row"""
        row = []
        for i in range(n+1):
            result = math.comb(n, i)
            row.append(result)
        return row

    for i in range(n):
        triangle.append(get_row(i))
    return triangle
