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
    def test_J_display_no_args(self):
        '''Tests display() method signature.'''
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
