#!/usr/bin/python3
'''Module Rectangle'''
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Tests to Base'''

    def test_D_instantiation(self):
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 3}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

