import random


def randomrange(start, stop):
    r = list(range(start, stop))
    random.shuffle(r)
    return r


