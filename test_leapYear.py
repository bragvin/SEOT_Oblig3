# test_leapYear.py

import pytest
from leapYear import isLeapYear


def test_leap_year_divisible_by_4_not_dividable_by_100():
    assert not isLeapYear(2003) == True
    assert isLeapYear(2011) == False
    assert isLeapYear(2012) == True

def test_year_is_not_leap_year(): #Feilende test
    assert isLeapYear(2011) == True


def test_leap_year_divisible_by_400():
    assert not isLeapYear(1998) == True
    assert isLeapYear(2000) == True


def test_non_leap_year_not_divisible_by_4():
    assert isLeapYear(2003) == False
    assert isLeapYear(2021) == False


def test_non_leap_year_divisible_by_100_not_divisible_by_400():
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
