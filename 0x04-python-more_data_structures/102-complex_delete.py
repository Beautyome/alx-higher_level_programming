#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for a in a_dictionary:
        if a_dictionary[a] == value:
            keys.append(a)

    for a in keys:
        a_dictionary.pop(a)

    return a_dictionary
