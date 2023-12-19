#!/usr/bin/python3
"""class MagicClass"""

import math


class MagicClass:
    """Class that defines properties of MagicClass."""

    def __init__(self, radius=0):
        """Creates new instances of MagicClass.
        Args:
            radius: radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns circumference."""
        return 2 * math.pi * self.__radius
