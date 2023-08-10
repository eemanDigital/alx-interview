#!/usr/bin/python3

"""
This module contains a function to calculate  Minimum Operations
"""


def minOperations(n):
    """
    Calculates the minimum number of operations
    needed to obtain 'n' occurrences of the character 'H'
    using the operations "Copy All" and "Paste".

    Args:
        n (int): The target number of occurrences
        of the character 'H'.

    Returns:
        int: The minimum number of operations required
        to achieve 'n' occurrences of 'H'.
        Returns 0 if n is less than or equal to 1.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations

# Test cases
# n = 4
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

# n = 12
# print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
