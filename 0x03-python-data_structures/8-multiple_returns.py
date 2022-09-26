#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    else:
        ch = sentence[0]
        return (len(sentence), ch)
