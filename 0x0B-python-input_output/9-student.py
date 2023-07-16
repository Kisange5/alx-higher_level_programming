#!/usr/bin/python3
"""module documentation"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """class initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrievs dict rep of the class"""
        return self.__dict__
