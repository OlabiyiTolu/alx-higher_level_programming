#!/usr/bin/python3
# function to print a copy of original list and a new list
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        my_list[idx] = element
        return my_list