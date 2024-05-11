#!/usr/bin/python3
"""Contain function"""


def lookup(obj):
    """Returns the list of availble attributes and methods of
    an object
    """
#    methods = []
#    for method in dir(obj):
#        if callable(getattr(obj, method)):
#            methods.append(method)
    return dir(obj)
