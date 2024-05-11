#!/usr/bin/python3
"""contain a function"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance"""
    if type(obj) is None:
        return False
    elif isinstance(obj, type) or issubclass(type(obj), a_class):
        return True
    else:
        return False
