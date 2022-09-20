#!/usr/bin/python3

alphabet = []
def print_az_reverse():
    '''prints the alphabets in reverse'''
    for i in range(122, 96, -1):
        alphabet.append(chr(i))
    alphabets = ''.join(alphabet)
    return alphabets

def alternate():
    '''prints the alphabets in reverse order'''
    alphabets = print_az_reverse()
    for ch in range(0, len(alphabets), 2):
        ch = chr(ord(ch - 32))
    print(alphabets)

    alternate()

