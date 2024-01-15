#!/usr/bin/python3
'''ModuleSquare'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Tests Base class.'''

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 20)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 36, complex(45))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(16, 10, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(16, 1, [10, 20, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 107, {16, 2, 73})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (8, 2, 93))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({17, 26, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def invalid_types(self):
        n = (3.1, -1.51, float('inf'), float('-inf'), True, "hi", (4,),
             [4], {4}, {9: 77}, None)
        return n

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 4, "b": 5}, 6)

    def test_display(self):
        m = Square(10)
        with self.assertRaises(TypeError) as e:
            Square.display()
        n = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), n)

    def test_display_s(self):
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

    def test_B_inheritance(self):
        self.assertTrue(issubclass(Square, Base))

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([8, 7, 6])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({7, 2, 7}, 9)

    def test_J_display_no_args(self):
        m = Square(3)
        with self.assertRaises(TypeError) as e:
            Square.display()
        p = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), p)

if __name__ == "__main__":
    unittest.main()
