#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """ defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width retriver.
        Returns:
            int: the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height retriver.

            Returns:
                int: the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeters of a"""
        if self.__width == self.__height:
            return 4 * self.__width
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        hash = "#"
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for colum in range(self.__height):
            for row in range(self.__width):
                string += hash
            string += '\n'
        return string.strip()
