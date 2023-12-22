#!/usr/bin/python3
def multiple_returns(sentences):
    mult = ()
    if len(sentences) == 0:
        mult = 0, "None"
    else:
        mult = len(sentences), sentences[0]
    return mult
