import re
def repeated_word(string):
    
    santance = re.findall('[\w\']+',string)
    repeated_word = {}
    for word in santance:
        if not word:
            return {}
        elif word in repeated_word:
            if repeated_word[word] >= 1:
                return word
            else:
              repeated_word[word]+= 1
        else:
            repeated_word[word]=1

 
print(repeated_word(" most common word in games names : last of us / god of war / gta / counter strick / house of card  / uncharted"))