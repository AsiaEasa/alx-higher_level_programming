#!/usr/bin/python3
'''Module Base'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    def test_instantiation(self):

        with self.assertRaises(ValueError) as e:
            m = Square(-71)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            m = Square(16, -662)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            m = Square(1, 23, -83)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            m = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_no_arg(self):
        m = Base()
        b = Base()
        self.assertEqual(m.id, b.id - 1)

    def test_three_bases(self):
        m = Base()
        n = Base()
        r = Base()
        self.assertEqual(m.id, n.id - 1)

    def test_None_id(self):
        m = Base(None)
        b = Base(None)
        self.assertEqual(m.id, b.id - 1)

    def test_unique_id(self):
        self.assertEqual(11, Base(11).id)

    def test_nb_instances(self):
        m = Base()
        n = Base(11)
        r = Base()
        self.assertEqual(m.id, n.id - 4)

    def test_class(self):
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_inheritance(self):
        self.assertTrue(issubclass(Square, Base))

    def test_constructor(self):
        with self.assertRaises(TypeError) as e:
            m = Square()
        n = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), n)

    def test_from_json_string_l(self):
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

 
    def test_from_json_string_t(self):
        list_in = [{"id": 80, "width": 20, "height": 74}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list, type(list_out))

    def test_from_json_string_o(self):
        list_in = [{"id": 80, "width": 20, "height": 74, "x": 97}]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

    def test_from_json_string_two(self):
        list_in = [
            {"id": 80, "width": 20, "height": 74, "x": 97, "y": 88},
            {"id": 80, "width": 57, "height": 62, "x": 51, "y": 33},
        ]
        json_list_in = Rectangle.to_json_string(list_in)
        list_out = Rectangle.from_json_string(json_list_in)
        self.assertEqual(list_in, list_out)

        m = [{"hi": 90}]
        n = '[{"hi": 90}]'
        self.assertEqual(Base.from_json_string(n), m)

        m = [{'x': 11, 'y': 22, 'width': 33, 'id': 44, 'height': 55}]
        n = '[{"x": 11, "y": 22, "width": 33, "id": 44, "height": 55}]'
        self.assertEqual(Base.from_json_string(n), m)

        m = [{'x': 1, 'y': 20, 'width': 31, 'id': 52,
             'height': 33}]
        n = '[{"x": 1, "y": 20, "width": 31, "id": 52, \
"height": 33}]'
        self.assertEqual(Base.from_json_string(n), m)

    def test_o_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        m = Rectangle(10, 7, 6, 9)
        m1 = Rectangle(2, 5)
        Rectangle.save_to_file([m, m1])

        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 107)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
