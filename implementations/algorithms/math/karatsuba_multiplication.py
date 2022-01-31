# Module Imports
from math import log10, ceil

# Implementation
def karatsuba(x, y):
    """The Karatsuba algorithm is a fast multiplication algorithm that uses a divide-and-conquer approach to multiply two numbers."""
    
    # The base case for recursion
    if x < 10 or y < 10:
        return x * y
    
    # Sets n, the number of digits in the highest input number
    n = max(int(log10(x) + 1), int(log10(y) + 1))
    
    # Rounds up n / 2
    n_2 = int(ceil(n / 2.0))
    
    # Adds 1 to n if n is odd
    n = n if n % 2 == 0 else n + 1
    
    # Splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y,10**n_2)

    # Applies the three recursive steps 
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # Performs the multiplication
    return (((10**n) * ac) + bd + ((10**n_2) * (ad_bc)))