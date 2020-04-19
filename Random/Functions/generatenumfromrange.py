import random

def genfromrange(a, b, c):
    password=[]
    for i in range(c):
        password.append(random.randint(a, b))
    return password


