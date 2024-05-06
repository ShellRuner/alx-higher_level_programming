#!/usr/bin/python3
""" A module that contain a function"""


def read_file(filename=""):
    """A function that reads a text file(UTF8)"""
    with open(filename, 'r', encoding='utf-8') as myfile:
        print(myfile.read(), end='')
