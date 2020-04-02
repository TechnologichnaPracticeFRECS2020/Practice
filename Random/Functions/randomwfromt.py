import random
import re

def randomword():
    rep=re.compile("[^a-zA-Zа-яА-я,\d]")
    text=input()
    final=rep.sub(" ",text)
    def ran_word(string):
      word = string.split()
      return random.choice(word)
    varib=ran_word(final)
    return varib
