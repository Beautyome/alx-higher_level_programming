#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    for a in copy:
        copy[a] = copy.get(a) * 2

    return copy
