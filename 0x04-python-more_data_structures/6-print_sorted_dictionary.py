#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return

    n = list(a_dictionary.keys())
    n.sort()
    for i in n:
        print(f"{i:s}: {a_dictionary[i]}")
