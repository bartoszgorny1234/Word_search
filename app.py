import random

def randomrange(start, stop):
    r = list(range(0, 10))
    random.shuffle(r)
    return r

print(randomrange(0,10))