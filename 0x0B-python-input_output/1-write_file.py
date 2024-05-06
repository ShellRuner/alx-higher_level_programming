#!/usr/bin/python3
"""Module that contain a function"""


def write_file(filename="", text=""):
    """A function that writes into a text file
    an returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as myfile:
        myfile.write(text)
        nb = myfile.tell()

    return nb
