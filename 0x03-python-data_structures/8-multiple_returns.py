#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        tuple = (len(sentence), sentence[0])
        return tuple
    else:
        return None
