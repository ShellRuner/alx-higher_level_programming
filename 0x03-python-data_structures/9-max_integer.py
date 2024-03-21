#!/usr/bin/python3
def max_integer(my_list=[]):
    max = -1
    if not my_list:
        return None
    else:
        for i in my_list:
            if max <= i:
                max = i
        return max
