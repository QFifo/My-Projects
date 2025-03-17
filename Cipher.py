import nltk
from nltk.corpus import words    #Not my own code
nltk.download('words', quiet=True)
word_list=set(words.words())
def is_real_word(TheWord):
    return all(word.lower() in word_list for word in TheWord.split())   


def CaesarCipher(Word, Shift):
    List=[]
    for letter in Word:
        offset=97
        offsets=65
        value=ord(letter)
        if value==32:
            space=chr(value)
            List.append(space)
        elif value>=97 and value<=122:
            value=(value+Shift-offset)%26+offset
            new_word=chr(value)
            List.append(new_word)
        else:
            value=(value+Shift-offsets)%26+offsets
            new_word=chr(value)
            List.append(new_word)
    return "".join(List)


def VigenereCipher(Word, Key):
    n=-1
    List=[]
    off=97
    offs=65
    for item in word:
        if ord(item)==32:
            List.append(item)
        elif ord(item)>=97 and ord(item)<=122:
            n+=1
            index=key[n]
            value=ord(index)-off
            number=(ord(item)+value-off)%26+off
            List.append(chr(number))
        else:
            n+=1
            index=key[n]
            value=ord(index)-offs
            number=(ord(item)+value-offs)%26+offs
            List.append(chr(number))        
    
    return"".join(List)  


def CaesarDecipher(Word, Shift):
    List=[]
    for letter in word:
        offset=97
        offsets=65
        value=ord(letter)
        if value==32:
            space=chr(value)
            List.append(space)
        elif value>=97 and value<=122:
            value=(value-Shift-offset)%26+offset
            new_word=chr(value)
            List.append(new_word)
        else:
            value=(value-Shift-offsets)%26+offsets
            new_word=chr(value)
            List.append(new_word)
    
    return"".join(List)  



def CaesarDecipherer(Word):
    Shift=0
    while Shift<26:
        Shift+=1
        List=[]
        List1=[]
        for letter in Word:
            offset=97
            offsets=65
            value=ord(letter)
            if value==32:
                space=chr(value)
                List.append(space)
            elif value>=97 and value<=122:
                value=(value-Shift-offset)%26+offset
                new_word=chr(value)
                List.append(new_word)
            else:
                value=(value-Shift-offsets)%26+offsets
                new_word=chr(value)
                List.append(new_word)
        new= "".join(List)
        if is_real_word(new)==True:
            List1.append(new)
            return "".join(List1), Shift