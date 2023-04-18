#!/usr/bin/python3
"""
Pascal_triangle
"""


def pascal_triangle(n):
    """Pascal triangle"""
    triangle = []
    def coefficient(n, k):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1

        numerator = 1
        denominator = 1
        for i in range(k):
            numerator *= n - i
            denominator *= i + 1

        return numerator // denominator

    def get_row(n):
        """Get nth term of row"""
        row = []
        for i in range(n+1):
            result = coefficient(n, i)
            row.append(result)
        return row

    for i in range(n):
        triangle.append(get_row(i))
    return triangle
