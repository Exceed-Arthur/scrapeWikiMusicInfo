import random
import time
import textblob

import removeDuplicatesStrings
import templates


def MainSection(artist=None, album=None, song=None, userField=None, mediaType=None, outputField=None):
    if not artist:
        artist = "Artist Name Generated Here"
    if not album:
        album = "Album Name Generated Here"
    if not song:
        song = "Song Name Generated Here"
    if not userField:
        userField = "Your Idea To Improve Here"
    if not outputField:
        outputField = "AI Boosted Idea Here"
    if not mediaType or mediaType not in ["artist", "song", "album"]:
        mediaType = "song"
    MainSectionHTML = templates.htmlMainMusicNames.replace("Building: Songs", f"Building: {mediaType.capitalize()}s")
    MainSectionHTML = MainSectionHTML.replace("{aiBoostedIdea}", outputField)
    MainSectionHTML = MainSectionHTML.replace("{artistIdeaGenerated}", artist)
    MainSectionHTML = MainSectionHTML.replace("{albumIdeaGenerated}", album)
    MainSectionHTML = MainSectionHTML.replace("{songIdeaGenerated}", song)
    return MainSectionHTML


def getDictionary(key="keywords"):
    import indexer
    if key == "artistTagSequences":
        index = indexer.indexed['artistTagSequences']
        return index
    if key == "songTagSequences":
        return indexer.indexed['songTagSequences']
    if key == "albumTagSequences":
        return indexer.indexed['albumTagSequences']
    if key == "artistTagSequences":
        return indexer.indexed['artistTagSequences']
    if key == "wordTagIndex":
        return indexer.indexed['wordTagIndex']
    if key == "tagWordsIndex":
        return indexer.indexed['tagWordsIndex']
    if key == "all":
        return indexer.indexed
    return indexer.indexed["keywords"]





def blobTagsToTags(userTags):
    tags = [x[1] for x in userTags]
    return tags

def tagSequences(mediaType: str):
    return getDictionary(f"{mediaType}TagSequences")

def getAllTags():
    d4 = getDictionary("wordTagIndex")

import indexer
def getKeyWordByCategory(category="NN"):
    try:
        kws = getDictionary("tagWordsIndex")[category]
    except KeyError:
        print("KEY ERROR GENERATING RANDOM WORD INSTEAD")
        kws = indexer.indexed["keywords"]
    return random.choice(kws)

def sortTags(userTags: list):
    userTags.sort(key=len)
    # print(userTags)
    return userTags






def calcSimilarity(str1="NNPNNPVBGNNPNNPNNP", str2="INPRP$NNPPRPVBPJJNNVNNN"):
    totalChars = len(max([str2, str1], key=len))
    str2 = str2.replace("$", "")
    str1 = str1.replace("$", "")
    matchingChars = 0
    for charIndex, char in enumerate(min([str2, str1], key=len)):
        if char == max([str2, str1], key=len)[charIndex]:
            matchingChars += 1
    simRatio = matchingChars/totalChars
    return simRatio


calcSimilarity()


def similarityIndex(str1="asser", str2="assner"):
    matchingChars = 0
    strMax = max(str1, str2)
    strMin = min(str1, str2)
    if strMin == strMax:
        strMax = str1
        strMin = str2
    for c, char in enumerate(strMin):
        if char.lower() == strMax[c].lower():
            matchingChars += 1
    return matchingChars/len(strMax)


def mostSimilar(userTags: list, tagSeqs: list):
    mostSimilarOne = tagSeqs[0]
    highestindex = 0
    print(f"Scanning {len(tagSeqs)} words")
    for i in range(len(tagSeqs)):
        comparedTo = tagSeqs[i]
        for j, tag in enumerate(comparedTo):
            try:
                charMatches = 0
                tagSelected = userTags[j][1]
                tagSelected = tagSelected.replace("$", "")
                minString = min(tagSelected, tag)
                maxString = tag
                pairOfComparisons = ("".join(comparedTo), "".join([x[1] for x in userTags] + [x[0] for x in comparedTo]))
                # print(pairOfComparisons)
                similarity = calcSimilarity(pairOfComparisons[0], pairOfComparisons[1])
                if highestindex < similarity:
                    highestindex = similarity
                    mostSimilarOne = comparedTo
            except:
                pass
    print(mostSimilarOne, "Most Similar Row", str(highestindex) + "%")

    return mostSimilarOne


def listToTitle(listed = ['it', 'do', 'only', 'came']):
    sentence = "".join([f"{x} " for x in listed])
    sentence = sentence.rstrip().capitalize()
    letters = list(sentence)
    letters.reverse()
    letters = "".join(letters).split(" ")[0]
    letters = list(letters)
    letters.reverse()
    lastWord = "".join(letters)
    sentence = sentence.replace(lastWord, lastWord.capitalize())
    print(sentence)
    return sentence

def mostSimilarString(target="PRP", possibilities=("ACT", "PRN", "NNP", "NN")):
    highestMatches, mostSimilar_ = 0, possibilities[0]
    for tag in possibilities:
        matchingChars = 0
        tag, target = tag.replace("$", ""), target.replace("$", "")
        for i, char in enumerate(tag):

            if len(tag) >= len(target):
                if char == target[i]:
                    matchingChars += 1
            if matchingChars > highestMatches:
                highestMatches = matchingChars
                mostSimilar_ = tag
    print(f"Most similar string is {mostSimilar_} between {target} and {possibilities}")
    return mostSimilar_



from PyDictionary import PyDictionary
def aiBoost(userField="In Her Metropolis", mediaType="song"):
    if len(userField.split(" ")) > 3:
        mode = "subtractive"
    tagWordsIndex = getDictionary("tagWordsIndex")
    #print(tagWordsIndex)
    userTags = textblob.TextBlob(userField).tags
    words = [x[0] for x in userTags]
    originalWords = words
    originalTags = userTags
    tags = [x.replace("$", "") for x in blobTagsToTags(userTags)]
    wordTagIndex = getDictionary("wordTagIndex")
    for word in list(wordTagIndex.keys()):
        wordTagIndex.update({word.lower():wordTagIndex[word]})
    #print(wordTagIndex)
    iterationLimit = 10
    ts = tagSequences(mediaType=mediaType)
    lenWords = len(words) - 1
    filteredTagSequences = [x for x in ts if len(x) >= lenWords]
    mostSimilarRow = mostSimilar(userTags, filteredTagSequences)
    syntheticText = [getKeyWordByCategory(category=tag).lower() for tag in mostSimilarRow]

    incongruentWords = {}
    for w, word in enumerate(words):
        try:
            realTag = wordTagIndex[word.lower()].replace('$', "")
            idealTag = mostSimilarRow[w]
            if realTag.lower() != idealTag.lower():
                incongruentWords.update({word.lower():idealTag})
        except KeyError:
            realTag = "NNP"

    for word in list(incongruentWords.keys()):
        userField = userField.lower().replace(word, getKeyWordByCategory(incongruentWords[word]).lower())

        userTags = textblob.TextBlob(userField).tags
        words = [x[0] for x in userTags]
        originalWords = words
        originalTags = userTags
        tags = [x.replace("$", "") for x in blobTagsToTags(userTags)]
        wordTagIndex = getDictionary("wordTagIndex")
        for wordy in list(wordTagIndex.keys()):
            wordTagIndex.update({wordy.lower(): wordTagIndex[wordy]})
        ts = tagSequences(mediaType=mediaType)
        lenWords = len(words) - 1
        filteredTagSequences = [x for x in ts if len(x) >= lenWords]
        mostSimilarRow = mostSimilar(userTags, filteredTagSequences)
        syntheticText = list(set([getKeyWordByCategory(category=tag).lower() for tag in mostSimilarRow]))
        syntheticText = listToTitle(syntheticText)
        syntheticText = removeDuplicatesStrings.removeDuplicateStringSpatial(syntheticText)
        print(words, "words")
        print(tags, "userTags")
        print(syntheticText, "synthetic text")



    maxI = len(filteredTagSequences)
    maxJ = len(userTags)
    for i, professionalSequence in enumerate(filteredTagSequences):
        print(professionalSequence, "professional sequences")
        sentence = ""

        for j, tagCat in enumerate(userTags):
            print(tagCat, filteredTagSequences[i][j])
            tagCategory = tagCat[1]
            if tagCategory != filteredTagSequences[i][j]:
                try:
                    sentence += getKeyWordByCategory(tagCategory) + " "
                except:
                    print(("error 104"))
            else:
                sentence += (tagCat[0] + " ").lower()
                print(sentence)
        sentence = sentence.rstrip()
        print("sentence", sentence)
        newSentenceTags = blobTagsToTags(textblob.TextBlob(sentence).tags)
        sentence = list(sentence)
        sentence.reverse()
        sentence = "".join(sentence)
        finalWord = sentence.split(" ")[0].lower()
        finalWord = list(finalWord)
        finalWord.reverse()
        finalWord = "".join(finalWord)
        reversed(finalWord)
        sentence = list(sentence)
        sentence.reverse()              
        sentence = "".join(sentence)
        print(finalWord, "final Word")
        sentence = sentence.capitalize().replace(finalWord, finalWord.capitalize())
        print(sentence.replace(" i ", " I "), newSentenceTags, "sentence", 'newSentence')

        isValid = False
        if newSentenceTags in filteredTagSequences:
            isValid = True
            print(f"Is Valid: {isValid}, {sentence}")

            return sentence
        else:
            if sentence:
                print("returning recursion")
                return aiBoost(userField=sentence, mediaType=mediaType)
            else:
                print("returning synthetic")
                return syntheticText


def addJavaScript(scripts: str):
    return f"<head>{scripts}</head>"
