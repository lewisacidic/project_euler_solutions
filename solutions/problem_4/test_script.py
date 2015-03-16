#
# Tests for Problem 4 of Project Euler (https://projecteuler.net/problem=4)
#
# Rich Lewis on 2015-03-13
#

from .script import is_palindrome, max_palindome_prod_below
import random
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