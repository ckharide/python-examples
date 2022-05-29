
import re
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python 
    if you do not love something which can give you all the capabilities to develop an application what 
    else can you love'''

def find_all_frequent(text):
    text_words = text.split()   
    myworddict = {} 
    for word in text_words:
        matches = re.findall(word , text )
        count = len(matches)
        myworddict[word] = count
    
    
    sorted_list = sorted(myworddict.items(), key=lambda k: (k[1], k[0]), reverse= True)
    return sorted_list

def isvalidpythonvariable(vartext):
    matches = bool(re.match("^[A-Za-z0-9_]*$",vartext))
    return matches

x = find_all_frequent(paragraph)
print(x)

x1 = isvalidpythonvariable('first-name')
print(x1)
    



