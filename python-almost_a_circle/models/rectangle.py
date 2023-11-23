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

    def display(self):
        """ prints in stdout the Rectangle """
        for y in range(self.y):
            print()
        for h in range(1, self.height + 1):
            for x in range(self.x):
                print(" ", end=(""))
            for w in range(1, self.width + 1):
                if w == self.width:
                    print("#")
                else:
                    print("#", end=(""))

    def __str__(self):
        """ shows the name of the class and its value """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """adding the method that an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary of Rectangle"""
        neko = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
        return neko
