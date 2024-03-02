#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """ defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle."""

        self.__width = width
        self.__height = height
    
    
    @property
    def width(self):
        """Width retriver.
        Returns:
            int: the width of the rectangle."""
        return self.__width
    
    
    @width.setter
    def width(self, value):
        """Property setter for height of rectangle.

            Args:
                value (int): height of the rectangle.

            Raises:
                TypeError: if height is not an integer.
                ValueError: if height is less than 0.
        """
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
        """Property setter for height of rectangle.

            Args:
                value (int): height of the rectangle.

            Raises:
                TypeError: if height is not an integer.
                ValueError: if height is less than 0.
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
