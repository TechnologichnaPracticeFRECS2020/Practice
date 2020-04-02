import random

def gensetpassword():
    chars = '+-/*!@#$%^&?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = 5
    length = 10
    password = ''
    for m in range(number):
        for i in range(length):
            password += random.choice(chars)
        password += '\n'
    print(password)
    return password


