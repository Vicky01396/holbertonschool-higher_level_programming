#!/usr/bin/python3
""" comment """
from .rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """comment"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, V):
        self.width = V
        self.height

    def __str__(self):
        """ shows the name of the class and its value """
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"

    def update(self, *args, **kwargs):
        """adding the method that an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary of Rectangle"""
        neko = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
        return neko
