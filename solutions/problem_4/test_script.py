#
# Tests for Problem 4 of Project Euler (https://projecteuler.net/problem=4)
#
# Rich Lewis on 2015-03-13
#

from __future__ import division
from .script import is_palindrome, possible_number_pairs_below, max_palindome_prod_below
import random
import math
import pytest

class TestIsPalindrome(object):

    def test_gold_standard(self):
        assert is_palindrome(9009)

    def test_negative(self):
        assert not is_palindrome(9008)

    def test_singleton(self):
        assert is_palindrome(1)

    def test_generated_palindromes(self):
        for _ in range(10000):
            i = str(random.randint(1, 1000000))
            j = int(i + i[::-1])
            assert is_palindrome(j)

class TestPossibleNumberPairs(object):

    def test_1(self):
        """ no positive numbers below 1, so no combinations possible """
        assert len(list(possible_number_pairs_below(1))) == 0

    def test_2(self):
        """ only one number below 2 (1), so only pair is 1 and 1"""
        assert len(list(possible_number_pairs_below(2))) == 1

    def test_2_contents(self):
        """ test that this is (1, 1)"""
        assert list(possible_number_pairs_below(2))[0] == (1, 1)

    def test_length(self):
        """ the number of combinations should be triangle numbers """

        def nCr(n,r):
            f = math.factorial
            return f(n) // f(r) // f(n-r)

        for i in range(2, 100):
            assert len(list(possible_number_pairs_below(i))) == nCr(i, 2)

    def test_has_random_pairs_contained(self):

        """ check to see that the iterator contains 1000 random pairs that it should do."""

        for i in range(1000):
            random_limit = random.randint(2, 200)
            random_pair = tuple(sorted((random.randint(1, random_limit - 1), random.randint(1, random_limit - 1)), reverse=True))
            assert random_pair in list(possible_number_pairs_below(random_limit))

    def test_has_random_pairs_not_contained(self):

        """ check to see that the interator doesn't contain 1000 random pairs that it shouldn't do."""

        for i in range(1000):
            random_limit = random.randint(2, 200)
            random_pair = tuple(sorted((random.randint(random_limit, 1000), random.randint(random_limit, 1000)), reverse=True))


class TestMaxPalindromeProdBelow(object):

    def test_gold_standard(self):
        assert max_palindome_prod_below(100) == 9009

    def test_eleven(self):
        """ To be 2 digit palindrome, must be multiple of 11. 
        Therefore can't have any 2 digit palindromes which are product of two numbers below eleven. 
        To be 3 digit palindrome, must be greater than 100. Biggest number possible is 9 x 9 = 81 < 100.
        So largest palindrome also a product of 2 numbers ten or less is a single digit.  
        Largest of these is 9."""

        assert max_palindome_prod_below(11) == 9

    def test_twelve(self):
        """ Largest possible number which is a product of 2 numbers below 12 is 11 x 11 = 121 
        which is a palindrome."""
        
        assert max_palindome_prod_below(12) == 121

    def test_one(self):

        with pytest.raises(ValueError):
            max_palindome_prod_below(1)