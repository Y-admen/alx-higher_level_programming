#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """ defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def check(self):
        if self.height < 0 or self.width < 0:
            raise ValueError("width must be >= 0")
        


@property
def width(self):
    return self._width


@width.setter
def width(self, value):
    if type(value) != int:
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value


@property
def height(self):
    return self._height


@height.setter
def height(self, value):
    if type(value) != int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._height = value
