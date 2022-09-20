#!/usr/bin/python3
for value in range(0,10):
    for num in range(1,10):
        print("{0}{0}".format(value, num), end=" ")
        num += num
