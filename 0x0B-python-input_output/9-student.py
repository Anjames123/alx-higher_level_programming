#!/usr/bin/env python3
"""Module containing the Student class"""


class Student:
    """A class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new instance of the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of the Student instance"""
        return self.__dict__
