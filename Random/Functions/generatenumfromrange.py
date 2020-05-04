import random

def genfromrange3(a, b, c):
    password=[]
    if a>b :
        b+=a
    for i in range(c):
        password.append(random.randint(a, b))
    return password


