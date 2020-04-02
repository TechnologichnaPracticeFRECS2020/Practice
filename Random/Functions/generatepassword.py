import random

def genpassword():
    chars = '+-/*!@#$%^&?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = 10
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

