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
        m = Square(10)
        with self.assertRaises(TypeError) as e:
            Square.display()
        n = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), n)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        m = Square(1)
        n = io.StringIO()
        with redirect_stdout(n):
            m.display()
        p = "#\n"
        self.assertEqual(n.getvalue(), p)

        m.size = 2
        n = io.StringIO()
        with redirect_stdout(n):
            m.display()
        p = "\
##\n\
##\n\
"
        self.assertEqual(n.getvalue(), p)

        m = Square(5, 5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            m.display()
        p = """\





     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), p)

        m = Square(8, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            m.display()
        n = """\
        ########
        ########
        ########
        ########
        ########
        ########
        ########
        ########
"""
        self.assertEqual(f.getvalue(), n)
