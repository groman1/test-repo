import re
import uuid

class multiregex(object):
    def __init__(self,rules):
        merge = []
        for regex in rules:
            merge += [(regex)]

        self._re=re.compile('|'.join(merge))


    def __call__(self,s):
        result = self._re.search(s)
        if result:
            groups = result.groupdict()
            return(next((groups[x]) for x in groups.keys() if groups[x]))

#key:1 with our rules in the string?
rules = [("foobar", "Hit a foobar"),
         ("f.*b.*r", "fbr"),
         ("foob.z", "Frobination"),
         ("baz", "Hit a baz"),
         ("b(ingo)?", "b with optional ingo")]

#Spits out match
m=multiregex(rules)   
tests=["foobar", "foobaz", "foobazr", "b", "bingo"]
for hit in (m(x) for x in tests):
    print("Message: '%s' (because of '%s')" % (hit))
    #printing text in rules based on 'tests'