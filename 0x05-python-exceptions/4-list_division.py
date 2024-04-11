#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    pos_1 = 0
    pos_2 = 0
    while pos_1 < list_length and pos_2 < list_length:
        try:
            result = my_list_1[pos_1] / my_list_2[pos_2]
            new_list.append(result)
            pos_1 += 1
            pos_2 += 1
        except TypeError:
            result = 0
            new_list.append(result)
            pos_1 += 1
            pos_2 += 1
            print("wrong type")
        except IndexError:
            result = 0
            new_list.append(result)
            pos_1 += 1
            pos_2 += 1
            print("out of range")
        except ZeroDivisionError:
            result = 0
            new_list.append(result)
            pos_1 += 1
            pos_2 += 1
            print("division by 0")
#        finally:
#            return new_list
    return new_list
