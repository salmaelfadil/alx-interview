#!/usr/bin/python3
"""
minimum operations"""


def minOperations(n):
    """minimum possible operations"""
    if n <= 1:
        return n

    operations = 0
    current_char = 1

    clipboard = 0

    while current_char < n:
        if n % current_char == 0:
            clipboard = current_char
            operations += 2
            current_char += clipboard
        else:
            operations += 1
            current_char += clipboard

    return operations
