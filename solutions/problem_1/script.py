#
# Problem 1 of Project Euler (https://projecteuler.net/problem=1)
#
# Attempted by Rich Lewis on 2015-03-12
#

from __future__ import print_function

def is_multiple(x, y):
    return x % y == 0

def is_multiple_list(x, y_list):
    head, tail = y_list[0], y_list[1:]
    return is_multiple(x, head) if not tail else is_multiple(x, head) \
    or is_multiple_list(x, tail)

def sum_below_limit_mult_in_list(limit, y_list):
    return sum(filter(lambda i: is_multiple_list(i, y_list), range(limit)))

if __name__ == '__main__':
    print(sum_below_limit_mult_in_list(1000, [3, 5]))