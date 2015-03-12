from __future__ import print_function

def fib(n):
    """ Gives an iterator for all Fibonacci numbers at most equal to n, starting with 1, 2"""
    a, b = 1, 2
    while a <= n:
        yield a
        a, b = b, a + b

def is_even(x):
    """ Determines if x is even """
    return x % 2 == 0

if __name__ == "__main__":
    print(sum(i for i in fib(4000000) if is_even(i)))

