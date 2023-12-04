#!/usr/bin/pythom3
if __name__ = "__main__":
    from calculator_1 import add
    import sys

    count = len(sys.argv)
    sum = 0
    for i in range(count - 1):
        sum += int(sys.argv[i] + 1)
    print(f'{}'.format(sum))
