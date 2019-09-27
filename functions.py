import random


def randomrange(start, stop):
    r = list(range(0, 10))
    random.shuffle(r)
    return r


for num in range(0, 10):
    for play in range(0, 10):
        print(num, play)

