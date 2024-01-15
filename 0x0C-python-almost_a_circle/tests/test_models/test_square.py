#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Tests the Base class.'''
    def test_I_area_no_args(self):
        m = Square(7)
        with self.assertRaises(TypeError) as e:
            Square.area()
        n = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), n)

