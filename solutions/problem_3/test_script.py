#
# Tests for Problem 3 of Project Euler (https://projecteuler.net/problem=3)
#
# Rich Lewis on 2015-03-12
#

from .script import is_factor, prime_factors
import pytest
import random
import functools

class TestFactor(object):
    def test_positive(self):
        assert is_factor(2, 10)

    def test_negative(self):
        assert not is_factor(3, 10)

    def test_inverted(self):
        assert not is_factor(10, 2)

    def test_zero(self):
        with pytest.raises(ZeroDivisionError):
            is_factor(0, 2)

class TestPrimeFactors(object):
    def test_gold_standard(self):
        gold_standard = [5, 7, 13, 29]
        assert list(prime_factors(13195)) == gold_standard

    def test_zero(self):
        assert not list(prime_factors(0))

    def test_random(self):
        """ the prime factors should multiply together to give the number.
        One should not be included, as it has no prime factors. """
        for i in range(2, 10000):
            assert functools.reduce(lambda x, y: x * y, prime_factors(i)) == i