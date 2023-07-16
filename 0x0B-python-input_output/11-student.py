#!/usr/bin/python3
"""module documentation"""


class Student:
    def __init__(self, first_name, last_name, age):
        """class initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of the class"""
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

    def reload_from_json(self, json):
        """Replaces all attributes of the student class"""
        rep = self.__dict__
        for i in rep:
            for j in json:
                if i == j:
                    rep[i] = json[j]
