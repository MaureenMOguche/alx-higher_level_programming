#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) < 1:
            tuple_a = tuple_a + (0, 0,)
        else:
            tuple_a = tuple_a + (0,)
    if len(tuple_b) < 2:
        if len(tuple_b) < 2:
            if len(tuple_b) < 1:
                tuple_b = tuple_b + (0, 0,)
            else:
                tuple_b = tuple_b + (0,)

    x, y = tuple_a
    i, j = tuple_b

    new_tuple = ()

    for u in range(len(tuple_a)):
        new_tuple = x + i, y + j
    return new_tuple
