#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n H characters
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to get n H characters.
    
    Args:
        n (int): The target number of H characters
        
    Returns:
        int: Minimum number of operations needed, or 0 if impossible
    """
    if n <= 1:
        return 0
        
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
        
    return operations 