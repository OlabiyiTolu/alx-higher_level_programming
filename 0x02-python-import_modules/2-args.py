#!/usr/bin/python3
if __name__ = "__main__":
    "print number of arguments"
    import sys

    count = len(argv) - 1
    if count == 0:
        print(count " arguments.")
    elif count == 1:
        print(count " argument:") 
    else count > 1:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i + 1]))
