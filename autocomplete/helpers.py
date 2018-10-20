import re

def norm_rsplit(text,n): return text.lower().rsplit(' ', n)[-n:]

#http://norvig.com/spell-correct.html
def re_split(text): return re.findall('[a-z]+', text.lower()) #returns a lowercase version of each of the words

#http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
#https://github.com/rrenaud/Gibberish-Detector/blob/master/gib_detect_train.py#L16
def chunks(l, n):
    for i in range(0, len(l) - n + 1):
        yield l[i:i+n]
