import math

the = {}


def per(t, p=0.5):
    p = math.floor((p  * len(t)) + .5)
    return t[math.max(1, min(len(t), p))]

def