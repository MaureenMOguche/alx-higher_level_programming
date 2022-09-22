#!/usr/bin/python3
# if __name__ == "__main__":
import hidden_4

list_funcs = dir(hidden_4)
new_list = []

for func in list_funcs:
    if func[:2] != '__':
        new_list.append(func)

for function in new_list:
    print(function)
