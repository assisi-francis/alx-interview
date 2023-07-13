#!/usr/bin/python3
"""
python script that computes a minimu operations
"""


def minOperations(n):
    """
    A method that computes the minimum number of operations
    for task copy ALL and Paste
    Returns the sum of the operations
    """
    if n < 2:
        return 0
    
    factor_list = []
    i = 1
    
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    
    return sum(factor_list)
