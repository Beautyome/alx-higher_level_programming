#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [(my_list[a] if my_list[a] != search else replace)
            for a in range(len(my_list))]
