#!/usr/bin/python3
# function to replace element in a list
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(mylist) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
