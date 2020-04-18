import random
import re

def randomword(text):
    rep=re.compile("[^a-zA-Zа-яА-я,\d]")
    final=rep.sub(" ",text)
    def ran_word(string):
      word = string.split()
      return random.choice(word)
    varib=ran_word(final)
    return varib
