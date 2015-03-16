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

def possible_number_pairs_below(n):

    """ returns an iterator over all possible pairs of numbers below a certain number, as tuples. 
    Pairs should not be duplicated such as (2, 1) (1, 2), and higher one is first i.e. (2, 1)."""

    return itertools.combinations_with_replacement(range(n - 1, 0, -1), 2) 

def max_palindome_prod_below(n):

    """ returns the maximum length palindrome that is a product of two numbers below a specified number"""

    return max(i * j for i, j in possible_number_pairs_below(n) if is_palindrome(i*j))

if __name__ == "__main__":
    print(max_palindome_prod_below(1000))