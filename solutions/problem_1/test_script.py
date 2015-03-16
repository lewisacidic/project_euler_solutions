#
# Tests for Problem 1 of Project Euler (https://projecteuler.net/problem=3)
#
# Rich Lewis on 2015-03-12
#

from .script import is_multiple, is_multiple_list, sum_below_limit_mult_in_list

import pytest

class TestIsMultiple(object):

    """tests for is_multiple"""

    def test_multiple_true(self):

        """ 10 is a multiple of 5 """

        assert is_multiple(10, 5)

    def test_multiple_false(self):

        """ 10 is not a multiple of 3 """

        assert not is_multiple(10, 3)

    def test_multiple_zero(self):

        """ Test edge case of zero. Mathematically dodgy, raise error """

        with pytest.raises(ZeroDivisionError):
            is_multiple(10, 0)

    def test_with_list(self):

        """ Make sure it doesn't work with lists """

        with pytest.raises(TypeError):
            is_multiple(10, [2])

class TestIsMultipleList(object):

    """tests for is_multiple_list"""

    def test_single_positive(self):

        """ 10 is a multiple of 5 """

        assert is_multiple_list(10, [5])

    def test_single_negative(self):

        """ 10 is not a multiple of 5 """

        assert not is_multiple_list(10, [3])

    def test_multi_positive(self):

        """ 10 is a multiple of 3 or 5 """

        assert is_multiple_list(10, [3, 5])

    def test_multi_negative(self):

        """ 11 is not a multiple of 3 or 5 """

        assert not is_multiple_list(11, [3, 5])

class TestSumBelowLimit(object):

    """tests for sum_below_limit_mult_in_list"""

    def test_for_given_example(self):

        """Test given fact that 23 is sum of multiples of 3 and 5 below 10"""

        assert(sum_below_limit_mult_in_list(10, [3, 5]) == 23)