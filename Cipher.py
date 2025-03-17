import nltk
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer

nltk.download('words', quiet=True)        #Not my own code
nltk.download('wordnet', quiet=True)

word_list = set(words.words())
lemmatizer = WordNetLemmatizer()

def is_real_word(TheWord):
    return all(word.lower() in word_list or 
        lemmatizer.lemmatize(word.lower(), 'v') in word_list or 
        lemmatizer.lemmatize(word.lower(), 'n') in word_list
        for word in TheWord.split())



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
        Dic={}
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
            Dic[new]=Shift
            return Dic
        
        
        
        
def CaesarDynamicDecipherer(Word):
        Shift=0
        n=0
        List=[]
        Dic={}
        offset=97
        offsets=65        
        List1=Word.split()
        Length=len(List1)
        for item in List1:
            n+=1
            while n<=Length:
                Shift+=1
                for letter in item:
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
                    Dic[new]=Shift
                    List.clear()
                    Shift=0
                    break
                else:
                    List.clear()
        return Dic
