import textblob
#import initialWikipediaScraper


def getTagIndex():
    tagIndex = []
import exceedLib
def isName(string: str):
    if string:
        blob = textblob.TextBlob(string).tags
        print(f"Blob: {blob}")
        stringTags = "".join([x[1] for x in blob])
        print(f"{string} is derived of tags: {stringTags}")
        print(string, "has", exceedLib.countOccurences(string=stringTags, target="NN"), 'NN(s)')
        print(string, "has", exceedLib.countOccurences(string=string, target=" "), 'space(s)')
        if string and stringTags:
            if exceedLib.countOccurences(string=string, target=" ") < exceedLib.countOccurences(string=stringTags, target="NN"):
                print(string, "is a name")
                return True
        else:
            print(string, "is not a name")
            return False


artistDump = ["Drake", "Dua Lipa", "Jason Derulo", "Selena Gomez", "Blueberry Faygo", "10,000 Hours"]
"""
for artist in artistDump:
    print()
    isName(artist)
"""
"""
Fail to find array for IN
Fail to find array for PRP
Fail to find array for NN
Fail to find array for JJ
Fail to find array for RB
Fail to find array for NNS
Fail to find array for WP
Fail to find array for VB
Fail to find array for VBG
Fail to find array for CC
Fail to find array for CD
Fail to find array for DT
Fail to find array for NNP
Fail to find array for VBP
Fail to find array for PRP$
Fail to find array for UH
Fail to find array for VBN
Fail to find array for RBR
Fail to find array for TO
Fail to find array for VBD
Fail to find array for MD
Fail to find array for JJS
"""

dictionary = dict( CC=[], CD=[], DT=[], EX=[], IN=[], JJ=[], JJR=[], JJS=[], LS=[], MD=[], NN=[], NNP=[], NNS=[], PDT=[], POS=[], PRP=[], RB=[], RBR=[], TO=[], UH=[], VB=[], VBN=[], WP=[], VBD=[], VBP=[], VBZ=[], WRB=[], WDT=[])


