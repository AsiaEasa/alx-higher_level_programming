#!/usr/bin/python3
'''Module to Base class.'''
from json import dumps, loads
import csv


class Base:
    '''Base of our OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''The Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Json a dictionary.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves json to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''Unjson a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance.'''
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file_name = "{}.json".format(cls.__name__)
        if not path.isfile(file_name):
            return []
        with open(file_name, "r", encoding="utf-8") as m:
            return [cls.create(**n) for n in cls.from_json_string(m.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves the object to csv file.'''
        file_name = cls.__name__ + ".csv"
        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                list_objs = [[m.id, m.width, m.height, m.x, m.y]
                             for m in list_objs]
            else:
                list_objs = [[n.id, n.size, n.x, n.y]
                             for n in list_objs]
        with open(file_name, 'w', newline='',
                  encoding='utf-8') as f_csv:
            writer = csv.writer(f_csv)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads the object to csv file.'''
        file_name = cls.__name__ + ".csv"
        li_st = []
        with open(file_name, 'r', newline='',
                  encoding='utf-8') as f_csv:
            read = csv.reader(f_csv)
            for row in read:
                row = [int(m) for m in row]
                if cls.__name__ == "Rectangle":
                    x = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    x = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                li_st.append(cls.create(**x))
        return li_st

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b4573c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffdd")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
