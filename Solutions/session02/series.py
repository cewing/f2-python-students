#!/usr/bin/env python

"""
series.py

solutions to the Fibonacci Series and Lucas numbers
"""


def fibonacci(n):

    """ compute the nth Fibonacci number """

    if n < 1:
        return None
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):

    """ compute the nth Lucas number """

    if n < 1:
        return None
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n1=0, n2=1):
    """
    compute the nth value of a summation series.

    :param n1=0: value of first element in the series
    :param n2=1: value of second element in the series

    if n1 == 0 and n2 == 1, the result is the Fibbonacci series

    if n1 == 2 and n2 == 1, the result is the Lucas series
    """
    if n < 1:
        return None
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        return sum_series(n - 1, n1, n2) + sum_series(n - 2, n1, n2)


if __name__ == "__main__":
    # run some tests

    assert fibonacci(0) is None
    assert fibonacci(-23) is None

    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8
    assert fibonacci(8) == 13

    assert lucas(0) is None
    assert lucas(-23) is None

    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(3) == 3
    assert lucas(4) == 4
    assert lucas(5) == 7
    assert lucas(6) == 11
    assert lucas(7) == 18
    assert lucas(8) == 29

    # test if sum_series matched Fibonacci
    for n in range(1, 10):
        assert sum_series(n) == fibonacci(n)

    # test if sum_series matched lucas
    for n in range(1, 10):
        assert sum_series(n, 2, 1) == lucas(n)

    print "tests passed"
