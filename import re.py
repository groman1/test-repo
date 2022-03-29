import re
import uuid

class multiregex(object):
    
    def __init__(self,rules):
        merge = []
        self._messages = {}

        for regex,text in rules:
            name = "g"+str(uuid.uuid4()).replace('-','')
            merge += ["(?P<%s>%s)" % (name,regex)]
            self._messages[name] = text

        self._re=re.compile('|'.join(merge))

    def __call__(self,s):
        result = self._re.search(s)
        if result:
            groups = result.groupdict()
            return (next((self._messages[x], groups[x]) for x in groups.keys() if groups[x]))

rules = [("foobar", "Hit a foobar"),
         ("f.*b.*r", "fbr"),
         ("foob.z", "Frobination"),
         ("baz", "Hit a baz"),
         ("b(ingo)?", "b with optional ingo")]

m=multiregex(rules)   
tests=["foobar", "foobaz", "foobazr", "b", "bingo"]

for hit,text in (m(x) for x in tests):
    print("Message: '%s' (because of '%s')" % (hit,text))