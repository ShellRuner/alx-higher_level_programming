#!/usr/bin/python3
def no_c(my_string):
    nw_string = ""
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            nw_string += my_string[i]
    return nw_string
