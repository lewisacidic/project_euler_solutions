#
# Tests for Problem 2 of Project Euler (https://projecteuler.net/problem=2)
#
# Rich Lewis on 2015-03-12
#

from .script import fib, is_even

class TestFib(object):

    """ Test the fib iterator from problem 2 """

    def test_against_standard(self):

        """ check the gold standard is retrieved """
    
        gold_standard = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #from PE
        assert list(fib(100)) == gold_standard

    def test_zero(self):
        
        """ edge case of zero, should not give any items"""
        
        assert len(list(fib(0))) == 0

    def test_never_give_higher(self):

        """ should never get a higher number than supplied """

        for i in range(1, 100):
            assert max(fib(i)) <= i

    def test_will_give_equal(self):

        """ should get an equal, if supplied """

        assert max(fib(89)) == 89

class TestIsEven(object):

    """ Test the is_even function from problem 2 """
    
    def test_positive(self):

        """ check that a few even numbers are given even """

        for i in [2, 4, 10, 18, 47006654]:
            assert is_even(i)

    def test_negative(self):

        """ check that a few odd numbers are given not even """

        for i in [5, 17, 43, 109439243]:
            assert not is_even(i)

    def test_zero(self):

        """ edge case, check that zero is even"""

        assert is_even(0)