#!/usr/bin/python3
"""module documentation"""


from models.base import Base


class Rectangle(Base):
    """class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, data):
        self.validate("width", data)
        self.__width = data

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, data):
        self.validate("height", data)
        self.__height = data

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, data):
        self.validate("x", data)
        self.__x = data

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, data):
        self.validate("y", data)
        self.__y = data

    def validate(self, param, data):
        if type(data) is not int:
            raise TypeError(f'{param} must be an integer')
        if (param == "width" or param == "height") and data <= 0:
            raise ValueError(f'{param} must be > 0')
        if (param == "x" or param == "y") and data < 0:
            raise ValueError(f'{param} must be >= 0')

    def area(self):
        return self.__width * self.__height

    def display(self):
        for l in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}'

    def update(self, *args, **kwargs):
        l_update = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, l_update[i], args[i])

        if len(kwargs) > 0 and len(args) <= 0:
            for key, value in kwargs.items():
                if key in l_update:
                    setattr(self, key, value)

    def to_dictionary(self):
        self_dict = {
			"id" : self.id,
            "width" : self.width,
            "height" : self.height,
            "x" : self.x,
            "y" : self.y
		}

        return self_dict
