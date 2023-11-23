#!/usr/bin/python3
""" the class Rectangle that inherits from Base """
from .base import Base


class Rectangle(Base):
    """ class rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """contructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, V):
        if not isinstance(V, int):
            raise TypeError("width must be an integer")
        if V <= 0:
            raise ValueError("width must be > 0")
        self.__width = V

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, V):
        if not isinstance(V, int):
            raise TypeError("height must be an integer")
        if V <= 0:
            raise ValueError("height must be > 0")
        self.__height = V

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, V):
        if not isinstance(V, int):
            raise TypeError("x must be an integer")
        if V < 0:
            raise ValueError("x must be >= 0")
        self.__x = V

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, V):
        if not isinstance(V, int):
            raise TypeError("y must be an integer")
        if V < 0:
            raise ValueError("y must be >= 0")
        self.__y = V

    def area(self):
        """ returns the value of the area of the Rectangle instance """
        return self.width * self.height
