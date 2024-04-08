#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    @property
    def y(self):
        """y retriver.

            Returns:
                int: the y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """x retriver.

            Returns:
                int: the x of the rectangle."""
        return self.__X

    @x.setter
    def x(self, value):
        """Set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    def area(self):
        """Calculate the area of a rectangle"""
        return self.__width * self.__height
    def display(self):
        hash = "#"
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for colum in range(self.__height):
            for row in range(self.__width):
                string += hash
            string += '\n'
        return string.strip()
