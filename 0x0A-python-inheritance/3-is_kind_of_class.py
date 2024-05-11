#!/usr/bin/python3
"""contain a function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance"""
    if isinstance(obj, type) and issubclass(type(obj), a_class):
        return True
    else:
        False
