#!/usr/bin/python3
from sys import argv

length = len(argv)

if length == 1:
    print("0 arguments.")
elif length == 2:
    print(f"{length - 1} argument:")
    for i in range(1, length):
        print(f"{i}: {argv[i]}")
else:
    print(f"{length - 1} arguments:")
    for i in range(1, length):
        print(f"{i}: {argv[i]}")
