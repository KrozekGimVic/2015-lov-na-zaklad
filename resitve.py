# -*- coding: utf-8 -*-

"""
Created on 2015-06-04
:author: Natan Žabkar (nightmarebadger)

Meant to be run in Python3, but can also be ran in Python2.
"""

from math import ceil
from math import e
from math import log
from math import pi
from sys import setrecursionlimit

# Set a higher recursion limit so we can do Fib recursivelly (we could also
# just do it iteratively)
setrecursionlimit(100000)

fib_memo = {}


def sieve(n):
    """Returns all primes <= n.

    To do this fast, we use the 'Sieve of Eratosthenes':
        http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """

    li = list(range(n+1))
    li[1] = 0
    limit = int(n**0.5)

    for i in range(2, limit + 1):
        if li[i] != 0:
            li[i*i:n+1:i] = [0] * len(range(i*i, n+1, i))

    return [i for i in li if i]


def mul_digits(n):
    """Multiply all non-zero digits in the number n.

    Repeat until the number is 3 digits or shorter."""

    tmp = 1

    # Get the length of the number
    # Python2 ceil returns a float, so int it
    l = int(ceil(log(n, 10)))

    for i in range(l):
        # Get the last digit and multiply if it's non-zero
        last_digit = n % 10
        if last_digit:
            tmp *= last_digit

        # Remove the last digit
        n //= 10

    # Get the length of the new number
    l = ceil(log(tmp, 10))

    # If it's 3 digits or shorter, return it, else run again
    if l <= 3:
        return tmp
    return mul_digits(tmp)


def fibonacci(n):
    """Get n-th Fibonacci number, memoized using an external dictionary."""

    # If it's first or second, return 1
    if n <= 2:
        return 1

    # Try to get it from the memo, if it's not there, calculate it
    try:
        return fib_memo[n]
    except KeyError:
        tmp = fibonacci(n-1) + fibonacci(n-2)
        fib_memo[n] = tmp
        return tmp


def sum_digits(n):
    """Create a sum of all digits in the number n.

    Repeat until the number is 2 digits or shorter."""

    tmp = 0

    # Get the length of the number
    # Python2 ceil returns a float, so int it
    l = int(ceil(log(n, 10)))

    for i in range(l):
        # Get the last digit and add it
        tmp += n % 10

        # Remove the last digit
        n //= 10

    # Get the length of the new number
    l = ceil(log(tmp, 10))

    # If it's 2 digits or shorter, return it, else run again
    if l <= 2:
        return tmp
    return sum_digits(tmp)


if __name__ == '__main__':
    # 1.
    primes = sieve(10000000)

    # 2.
    sum_of_primes = sum(primes)

    # 3.
    mul_of_digits = mul_digits(sum_of_primes)

    # 4.
    fourth = mul_of_digits * primes[99]

    # 5.
    fib = fibonacci(fourth)

    # 6.
    sum_of_digits = sum_digits(fib)

    # 7.
    seventh = sum_of_digits * pi

    # 8.
    eight = seventh / e

    # 9.
    ninth = ceil(eight)

    # 10.
    tenth = ninth * 2
    print(tenth)
