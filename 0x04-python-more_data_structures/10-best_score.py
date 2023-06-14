#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = None
    for a in a_dictionary:
        best = a if best is None else best
        if a_dictionary[a] > a_dictionary[best]:
            best = a

    return best
