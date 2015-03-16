#
# Problem 3 of Project Euler (https://projecteuler.net/problem=3)
#
# Attempted by Rich Lewis on 2015-03-12
#

from __future__ import print_function

def is_factor(i, x):
    """ returns True if i is a factor or x """
    return x % i == 0

def prime_factors(x):
    """ returns an iterator of all the prime factors of x """
    fact, rem = 2, x
    while fact * fact <= x:
        if is_factor(fact, rem):
            rem = int(rem/fact)
            yield fact
        else:
            fact += 1
    if rem >= fact:
        yield rem

if __name__ == "__main__":
    print(max(prime_factors(600851475143)))