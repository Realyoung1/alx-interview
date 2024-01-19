#!/usr/bin/python3
"""
Minimum Operations 
there is a single character H. in a text file
my text editor can only execyte only two operations in this file
Copied and Pasted

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0

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
