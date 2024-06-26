#!/usr/bin/python3
"""Class square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition for the class of Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Intializer"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter , for a square width == height"""
        return self.width

    @size.setter
    def size(self, value):
        """setter and validater for the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """do the assignment for the attributes"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns rep of dict for the square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """rep for the print"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
