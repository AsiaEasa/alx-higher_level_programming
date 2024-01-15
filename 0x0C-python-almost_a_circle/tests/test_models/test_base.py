#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_from_json_string_l(self):
        '''Tests to_json_string() signature:'''
        with self.assertRaises(TypeError) as m:
            Base.from_json_string()
        n = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(m.exception), n)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        n = '[{"x": 4, "y": 4, "width": 4, "id": 4, "height": 4}, \
{"x": 10, "y": 20, "width": 34, "id": 44, "height": 340}]'
        k = [{'x': 4, 'y': 4, 'width': 4, 'id': 4, 'height': 4},
             {'x': 10, 'y': 20, 'width': 34, 'id': 44,
             'height': 340}]
        self.assertEqual(Base.from_json_string(n), k)

        m = [{}, {}]
        n = '[{}, {}]'
        self.assertEqual(Base.from_json_string(n), m)
        m = [{}]
        n = '[{}]'
        self.assertEqual(Base.from_json_string(n), m)

        m = [{"hi": 90}, {"hello": 15}, {"HI": 9}]
        n = '[{"hi": 90}, {"hello": 15}, {"HI": 9}]'
        self.assertEqual(Base.from_json_string(n), m)

 
    def test_from_json_string_t(self):
        list_in = [{"id": 80, "width": 20, "height": 74}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list, type(list_out))

    def test_from_json_string_one_rectangle(self):
        list_in = [{"id": 80, "width": 20, "height": 74, "x": 97}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two_rectangles(self):
        list_in = [
            {"id": 80, "width": 20, "height": 74, "x": 97, "y": 88},
            {"id": 80, "width": 57, "height": 62, "x": 51, "y": 33},
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)
