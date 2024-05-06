#!/usr/bin/python3
"""A module that contain a function"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a
    text file and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as myfile:
        myfile.write(text)

    return len(text)
