import autocomplete
from autocomplete import models

DEFAULTPREDICTION = ['the', 'hello', 'oh yeah', 'wow', 'EMERGENCY']
lastWord = ''
currentWord = ''

#import 'file'
def startup():
    autocomplete.load()
    return DEFAULTPREDICTION




def makePrediction(character):
    global lastWord
    global currentWord
    #update lastWord, currentWord, lastString
    if(character != ' ' and lastWord == ''):
        currentWord += character
        return DEFAULTPREDICTION
    elif character == ' ' and currentWord != '':
        lastWord = currentWord
        currentWord = ''
        return pasturizeList(autocomplete.predict(lastWord, currentWord))
    else:
        currentWord += character
        return  pasturizeList(autocomplete.predict(lastWord, currentWord))

def flushPredictions():
    global lastString
    global lastWord
    global currentWord
    #restart prediction list, add the sentance to the big.txt file
    
    #add to predictive model
    if(len(lastString) > 30):
        ac.models.train_models(lastString)
        lastString = ''
    else:
        lastString = '\n'        
    #resets things
    lastWord = ''
    currentWord = ''
    return DEFAULTPREDICTION

def pasturizeList(wordList):
    return [i[0] for i in sorted(wordList, key=lambda tup: tup[1]) ]
