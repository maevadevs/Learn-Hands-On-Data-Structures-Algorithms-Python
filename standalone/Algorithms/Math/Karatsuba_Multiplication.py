from math import log10, ceil

def karatsuba(x: int, y: int) -> int:
    # The base cases for recursion:
    # x or y is a single digit => Plain multiplication
    if x < 10 or y < 10:
        return x * y

    # sets n: the number of digits in the highest input number
    n: int = max(int(log10(x) + 1), int(log10(y) + 1))

    # roundsup n/2
    n_2: int = int(ceil(n / 2.0))

    # adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1

    # splits the input numbers
    a: int
    b: int
    c: int
    d: int
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)

    # applies the three recursive steps
    ac: int
    bd: int
    ad_bc: int
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # performs the multiplication
    return ((10**n) * ac) + bd + ((10**n_2) * (ad_bc))
