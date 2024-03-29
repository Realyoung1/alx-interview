#!/usr/bin/python3
"""

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
