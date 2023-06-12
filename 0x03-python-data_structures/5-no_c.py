#!/usr/bin/python3
def no_c(my_string):
    s = f""
    for a in my_string:
        if a != 'c' and a != 'C':
            s += f"{a}"
    return s
