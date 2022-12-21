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

        if exceedLib.countOccurences(string=string, target=" ") < exceedLib.countOccurences(string=stringTags, target="NN"):
            print(string, "is a name")
            return True
        else:
            print(string, "is not a name")
            return False


artistDump = ["Drake", "Dua Lipa", "Jason Derulo", "Selena Gomez", "Blueberry Faygo", "10,000 Hours"]

for artist in artistDump:
    print()
    isName(artist)
