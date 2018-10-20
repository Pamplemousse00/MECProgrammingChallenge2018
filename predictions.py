import autocomplete as ac
from autocomplete import models


#import 'file'
def startup():
    ac.load()

def makePrediction(character):
    wordList = ac.predict(currentString, currentWord)
    wordList.sort()
    return wordList

def flushPredictions(flushedString):
    #restart prediction list, add the sentance to the big.txt file

    #add to predictive model
    bigtxtpath = os.path.join(os.path.dirname(__file__), 'big.txt')
    with open(bigtxtpath, 'a') as bigtxtfile:
        bigtxtfile.write(flushedString)
