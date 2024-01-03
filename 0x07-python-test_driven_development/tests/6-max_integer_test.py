#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""
    def test_no_arg(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([]), None)

    def test_identical(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([80, 80]), 80)

    def test_max_start(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([8, 6, 3]), 8)
    
    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 0]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, -2.5, 3.5]), 3.5)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([50, 50.8, -500, -0.5, 5000, 7000, -500000]), 7000)

    def test_one(self):
        self.assertEqual(max_integer([200]), 200)
