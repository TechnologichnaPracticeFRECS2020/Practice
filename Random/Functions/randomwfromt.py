import random
import re

def randomword(text):
    if re.match("[\s*]",text):
                return "Текст не повинет бути порожнім"
    else :
        rep=re.compile("[^a-zA-Zа-яА-я,\d,!,@,#,$,%,^,&,*,(,),{,},_,+,=,~,`,§,±,|,.,\",',\s,:,;,\-,/,\\,<,>, ☻,]")
        final=rep.sub(" ",text)
        def ran_word(string):
            word = string.split()
            return random.choice(word)
        varib=ran_word(final)
        return varib
        
    

