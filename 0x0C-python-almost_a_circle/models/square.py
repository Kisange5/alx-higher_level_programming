#!/usr/bin/python3
"""module documentation"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """a class that inherits from the rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """instant initi"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, data):
        self.width = data
        self.height = data

    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.height}'

    def update(self, *args, **kwargs):
        l_update = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, l_update[i], args[i])
        if len(kwargs) > 0 and len(args) <= 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
