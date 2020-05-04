import random

def genfromrange(a, b):
    if a>b :
        b+=a
    return random.randint(a, b)

