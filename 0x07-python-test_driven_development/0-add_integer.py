#!/usr/bin/python3
"""adder function for testing"""

def add_integer(a, b=98):
    """ 
        add integers
        Arguments:
        @a: first argument
        @b: second argument, defaults as 98 if no arg
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
