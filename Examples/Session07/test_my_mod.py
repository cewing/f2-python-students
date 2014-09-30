#!/usr/bin/env python

"""
test module for my_mod.py
"""


import unittest
from my_mod import my_func


class MyFuncTestCase(unittest.TestCase):
    def test_my_func(self):
        test_vals = (2, 3)
        expected = reduce(lambda x, y: x * y, test_vals)
        actual = my_func(*test_vals)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
