import random

def gensetpassword(number, length):
    chars = '+-/*!@#$%^&?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = []
    for m in range(number):
        password1 = ''
        for i in range(length):
            password1 += random.choice(chars)
        password.append(password1)
    return password


