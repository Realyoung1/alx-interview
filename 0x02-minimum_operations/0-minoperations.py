#!/usr/bin/python3
"""
Minimum Operations 
there is a single character H. in a text
my text editor can only execyte only two
Prototype: def minOperations(n)
Returns an integer

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
