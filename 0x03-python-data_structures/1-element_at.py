#!/usr/bin/python3
# function to print where element at
def element_at(my_list, idx):
    if idx < 0:
        print('None')
    list_c = len(my_list)
    if idx > list_c:
        print(None)  