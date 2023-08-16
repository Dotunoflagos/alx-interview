#!/usr/bin/python3
"""b"""

def minOperations(n: int) -> int:
    """b"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
