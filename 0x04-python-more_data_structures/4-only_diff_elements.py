#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not(set_1.isdisjoint(set_2)) or len(set_1) >= 0 and len(set_2) >= 0:
        return set_1.symmetric_difference(set_2)
    else:
        return set()
