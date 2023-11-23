#!/usr/bin/python3
""" the class Rectangle that inherits from Base """
from .base import Base


class Rectangle(Base):
    """ ... """
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
        self.__width = V

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, V):
        self.__height = V

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, V):
        self.__x = V

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, V):
        self.__y = V
