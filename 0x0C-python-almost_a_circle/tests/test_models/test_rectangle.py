#!/usr/bin/python3
'''Module Rectangle'''

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from contextlib import redirect_stdout

class TestRectangle(unittest.TestCase):
    '''Tests to Base'''

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 25)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.05, 17)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(56), 26)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 15, "b": 62}, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 22, 33], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 22, 33}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 22, 33), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({41, 25, 63, 61}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(57), 26)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'P', 32)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 26)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 26)
    def invalid_types(self):
        m = (3.1, -1.221, float('inf'), float('-inf'), True, "hi", (6,),
             [7], {5}, {6: 7}, None)
        return m

    def test_J_display_no_args(self):
        m = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        n = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), n)

    def test_J_display(self):
        m = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            m.display()
        p = "#\n"
        self.assertEqual(f.getvalue(), p)
        m.width = 2
        m.height = 6
        f = io.StringIO()
        with redirect_stdout(f):
            m.display()
        p = "\
##\n\
##\n\
##\n\
##\n\
##\n\
##\n\
"
        self.assertEqual(f.getvalue(), p)

    def test_instan(self):
        m = Rectangle(1, 30)
        self.assertEqual(str(type(m)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(m, Base))
        n = {'_Rectangle__height': 30, '_Rectangle__width': 1,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 24}
        self.assertDictEqual(m.__dict__, n)

        with self.assertRaises(TypeError) as e:
            m = Rectangle("11", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            m = Rectangle(11, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(11, 2, "43")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_to_dictionary_out(self):
        m = Rectangle(101, 22, 11, 89, 5)
        c = {'x': 11, 'y': 89, 'id': 5, 'height': 22, 'width': 101}
        self.assertDictEqual(c, m.to_dictionary())

    def test_to_dictionary_no(self):
        m1 = Rectangle(1, 3, 11, 8, 6)
        m2 = Rectangle(6, 8, 11, 3, 1)
        m2.update(**m1.to_dictionary())
        self.assertNotEqual(m1, m2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 20, 6, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
