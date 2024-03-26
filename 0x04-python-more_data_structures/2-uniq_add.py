#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) > 0:
        add_list = set()
        for i in my_list:
            add_list.add(i)
        res = 0
        for i in list(add_list):
            res += i
        return res
    elif len(my_list) == 0:
        return 0
    else:
        return None
