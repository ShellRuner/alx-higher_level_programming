#!/usr/bin/python3
"""Contain a class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Sort list in ascending sort"""
        print(sorted(self))
