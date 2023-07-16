#!/usr/bin/python3
"""module documentation"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """class initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrievs dict rep of the class"""
        rep = self.__dict__.copy()
        if type(attrs) is list:
            n_rep = {}
            for i in attrs:
                if type(i) is not str:
                    return rep
                if i in rep:
                    n_rep[i] = rep[i]
                    return n_rep
                return rep
