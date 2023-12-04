#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub
    
    count_args = len(sys.argv)
    if count_args > 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
        
    operator = sys.argv[2]
    if operator != operators:
        print('Unknown operator. Available operators: +, -, * and /')
        print(1)
        
    a = sys.argv[1]
    b = sys.argv[3]
    
    if operator == '+':
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif operator == '-':
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif operator == '*':
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    else:
        print('{} / {} = {}'.format(a, b, div(a, b)))
        