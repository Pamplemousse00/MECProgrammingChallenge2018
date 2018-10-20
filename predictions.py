import autocomplete as ac
from autocomplete import models

#import 'file'
def startup():
    ac.load()

def makePrediction(character):
    wordList = ac.predict(currentString, currentWord)
    return wordList

def flushPredictions(flushedString):
    #restart prediction list, add the sentance to the big.txt file

    #add to predictive model
    bigtxtpath = os.path.join(os.path.dirname(__file__), 'big.txt')
    with open(bigtxtpath, 'a') as bigtxtfile:
        bigtxtfile.write(flushedString)

def pasturizeList(wordList):
    return sorted(wordList, key=lambda tup: tup[1])

    return newList

def debugStream():
    lastString = ''
    lastWord = ''
    currentWord = ''
    while(True):
        currentWord += input('give char')
        if(currentWord[-1] == ' '):
            lastString += lastWord
            lastWord = currentWord
            currentWord = ''
        else:
            wordList = pasturizeList(ac.predict(lastWord, currentWord))


#cannot pass space character into function as all things must be a word!
if __name__ == '__main__':
    startup()
    debugStream()
