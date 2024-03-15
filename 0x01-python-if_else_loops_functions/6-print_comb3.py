#!/usr/bin/python3
for i in range(10):
    for b in range(10):
        if i >= b:
            pass
        elif i == 8 and b == 9:
            print("{}{}".format(i, b))
        else:
            print("{}{}".format(i, b), end=", ")
