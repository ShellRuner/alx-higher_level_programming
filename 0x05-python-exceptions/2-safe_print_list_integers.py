#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_1 = 0
    count_2 = 0
    while count_2 < x:
        try:
            print("{:d}".format(my_list[count_2]), end="")
            count_1 += 1
            count_2 += 1
        except (TypeError, ValueError):
            count_2 += 1
    print()
    return count_1
