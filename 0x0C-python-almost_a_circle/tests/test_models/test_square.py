#!/usr/bin/python3
'''ModuleSquare'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io
import os

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


    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_update_id(self):
        self.square.update(89)
        self.assertEqual(self.square.id, 89)

    def test_update_id_size(self):
        self.square.update(89, 1)
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 1)

    def test_update_id_size_x(self):
        self.square.update(89, 1, 2)
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 1)
        self.assertEqual(self.square.x, 2)

    def test_update_id_size_x_y(self):
        self.square.update(89, 1, 2, 3)
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 1)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_update_kwargs_id(self):
        self.square.update(**{'id': 89})
        self.assertEqual(self.square.id, 89)

    def test_update_kwargs_id_size(self):
        self.square.update(**{'id': 89, 'size': 1})
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 1)

    def test_update_kwargs_id_size_x(self):
        self.square.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 1)
        self.assertEqual(self.square.x, 2)

    def test_update_kwargs_id_size_x_y(self):
        self.square.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(self.square.id, 89)
        self.assertEqual(self.square.size, 1)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_save_to_file_with_none(self):
        m = Square(5)
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        m = Square(5)
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")


    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertEqual(dictionary, expected_dict)


    def test_square_exists(self):
        square = Square(1, 2, 3, 4)
        self.assertIsInstance(square, Square)

    def test_str_exists(self):
        square = Square(1, 2, 3, 4)
        self.assertTrue(hasattr(square, '__str__'))

    def test_str_representation(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(str(square), '[Square] (4) 2/3 - 1')

    def test_to_dictionary_exists(self):
        square = Square(1, 2, 3, 4)
        self.assertTrue(hasattr(square, 'to_dictionary'))


    def setUp(self):
        self.file_name = "Square.json"
        self.square = Square(5, 2, 3, 1)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_create_with_id(self):
        square = Square.create(**{'id': 89})
        self.assertEqual(square.id, 89)

    def test_create_with_id_size(self):
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_create_with_id_size_x(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_create_with_id_size_x_y(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)


    def test_save_to_file_with_square_instance(self):
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists(self.file_name))

    def test_load_from_file_nonexistent_file(self):
        squares = Square.load_from_file()
        self.assertEqual(squares, [])

    def test_load_from_file_existing_file(self):
        Square.save_to_file([Square(1)])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)

if __name__ == "__main__":
    unittest.main()
