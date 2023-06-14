#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wxs = 0
    w = 0
    for a in my_list:
        wxs += (a[0] * a[1])
        w += a[1]
    return wxs / w
