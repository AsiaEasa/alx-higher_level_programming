#!/usr/bin/python3
'''Module Rectangle'''
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Tests to Base'''

    def test_instan(self):
        m = Rectangle(1, 30)
        self.assertEqual(str(type(m)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(m, Base))
        n = {'_Rectangle__height': 30, '_Rectangle__width': 1,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 7}
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
