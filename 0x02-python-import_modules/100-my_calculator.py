#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = int(argv[1])
        num2 = int(argv[3])
        operator = argv[2]

        if operator == '+':
            print(f"{num1} {operator} {num2} = {add(num1, num2)}")
        elif operator == '-':
            print(f"{num1} {operator} {num2} = {sub(num1, num2)}")
        elif operator == '*':
            print(f"{num1} {operator} {num2} = {mul(num1, num2)}")
        elif operator == '/':
            print(f"{num1} {operator} {num2} = {div(num1, num2)}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
