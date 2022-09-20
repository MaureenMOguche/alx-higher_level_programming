#!/usr/bin/python3
for ch in range(97, 123):
    if chr(ch) == 'e' or chr(ch) == 'q':
        continue
    else:
        print(chr(ch), end="")
