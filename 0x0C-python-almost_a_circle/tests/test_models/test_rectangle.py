#!/usr/bin/python3
'''Module Rectangle'''
import os
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
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 31}
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


    def test_rectangle_exists(self):
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(1, 0)

        self.assertEqual(str(context.exception), 'height must be > 0')

    def test_area_exists(self):
        with self.assertRaises(ValueError) as context:

            rect = Rectangle(1, 0)
        self.assertEqual(str(context.exception), 'height must be > 0')

    def test_area_calculation(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

   
    def test_str_exists(self):
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(1, 0)

        self.assertEqual(str(context.exception), 'height must be > 0')

    def test_str_representation(self):
        with self.assertRaises(ValueError) as context:
            rect = Rectangle(1, 0)

        self.assertEqual(str(context.exception), 'height must be > 0')

    def test_create_with_id(self):
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.id, 89)

    def test_create_with_id_and_width(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_create_with_id_width_and_height(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_create_with_all_parameters(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)



    def setUp(self):
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_create(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_load_from_file_no_file(self):
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 0)

    def test_load_from_file(self):
        r1 = Rectangle(1, 2, 3, 4, 89)
        r2 = Rectangle(5, 6, 7, 8, 90)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].id, 89)
        self.assertEqual(rectangles[1].id, 90)
        self.assertEqual(rectangles[0].width, 1)
        self.assertEqual(rectangles[0].height, 2)
        self.assertEqual(rectangles[0].x, 3)
        self.assertEqual(rectangles[0].y, 4)
        self.assertEqual(rectangles[1].width, 5)
        self.assertEqual(rectangles[1].height, 6)
        self.assertEqual(rectangles[1].x, 7)
        self.assertEqual(rectangles[1].y, 8)

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 89)
        dictionary = r.to_dictionary()
        self.assertEqual(dictionary['id'], 89)
        self.assertEqual(dictionary['width'], 1)
        self.assertEqual(dictionary['height'], 2)
        self.assertEqual(dictionary['x'], 3)
        self.assertEqual(dictionary['y'], 4)

    def test_update(self):
        r = Rectangle(1, 2, 3, 4, 89)
        r.update(id=90, width=5, height=6, x=7, y=8)
        self.assertEqual(r.id, 90)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 7)
        self.assertEqual(r.y, 8)


if __name__ == "__main__":
    unittest.main()
