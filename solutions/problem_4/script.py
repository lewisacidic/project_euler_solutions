#
# Problem 4 of Project Euler (https://projecteuler.net/problem=4)
#
# Attempted by Rich Lewis on 2015-03-13
#

from __future__ import print_function
import itertools

def is_palindrome(x):

    """ returns True if x is palindrome """

    return x == int(str(x)[::-1])

def max_palindome_prod_below(n):
    return max(i * j for i, j in itertools.combinations_with_replacement(range(n - 1, 0, -1), 2) if is_palindrome(i*j))

if __name__ == "__main__":
    print(max_palindome_prod_below(1000))