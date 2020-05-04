import random

def genpassword(length):
    chars = '+-/*!@#$%^&?=<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    password = ''
    for i in range(int(length)):
        password += random.choice(chars)
    return password

