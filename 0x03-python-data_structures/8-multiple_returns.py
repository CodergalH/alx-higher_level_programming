#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        ret = (len(sentence), None)
    else:
        ret = (len(sentence), sentence[0])

    return ret
