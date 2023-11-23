#!/usr/bin/python3
"""
file that define class base
"""


class Base:
    """
    definition of the class 
    """
    __nb_objects = 0

    def __init__ (self, id=None):
        """
        contructor method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
