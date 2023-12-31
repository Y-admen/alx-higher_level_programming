#!/usr/bin/python3
'''
==============================
module with inherits_from func
==============================
'''
def inherits_from(obj, a_class):
    ''' returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False.'''
    return issubclass(obj, a_class)
