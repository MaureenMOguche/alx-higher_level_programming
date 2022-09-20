#!/usr/bin/python3
for value in range(0,10):
    for num in range(1,10):
        if num == value:
            continue
        else:
            print(f"{value}{num}", end=" ")
