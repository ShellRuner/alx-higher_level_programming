#!/usr/bin/python3
"""A Module for integer addition
It contain a function add_integer
that receive arguments
a (int) and b (int)
"""


def add_integer(a, b=98):
    """A function that adds 2 integers
    Args:
        a (int): the first parameter.
        b (int): the second parameter.
    Returns:
        int: return the addition of a and b.Or
        raises TypeError message.
    """
    if type(a) is None:
        raise TypeError('a must be an integer')
    if type(b) is None:
        raise TypeError('b must be an integer')
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)
    return a + b
