#!/usr/bin/python3
"""the class base file"""


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initioalization method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
