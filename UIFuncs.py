import random
import time

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
        return indexer.indexed['artistTagSequences']
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



import textblob


def blobTagsToTags(userTags):
    tags = [x[1] for x in userTags]
    return tags

def tagSequences(mediaType: str):
    return getDictionary(f"{mediaType}TagSequences")

def getAllTags():
    d4 = getDictionary("wordTagIndex")

def getKeyWordByCategory(category="NN"):
    print(category)
    kws = getDictionary("tagWordsIndex")[category]
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
    print(simRatio)
    return simRatio

calcSimilarity()


def mostSimilar(userTags: list, tagSeqs: list):
    mostSimilarOne = tagSeqs[0]
    highestindex = 0
    for i in range(len(tagSeqs)):
        comparedTo = tagSeqs[i]
        for j, tag in enumerate(comparedTo):
            try:
                charMatches = 0
                tagSelected = userTags[j][1]
                tagSelected = tagSelected.replace("$", "")

                minString = min(tagSelected, tag)
                maxString = tag
                print(minString, maxString, charMatches/len(maxString))
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


def mostSimilarString(target="PRP", possibilities=("ACT", "PRN", "NNP", "NN")):
    highestMatches, mostSimilar_ = 0, possibilities[0]
    for tag in possibilities:
        matchingChars = 0
        print(f"tag = {tag}, target={target}")
        tag, target = tag.replace("$", ""), target.replace("$", "")
        for i, char in enumerate(tag):
            print(i, char)
            if len(tag) >= len(target):
                if char == target[i]:
                    matchingChars += 1
            if matchingChars > highestMatches:
                highestMatches = matchingChars
                mostSimilar_ = tag

        print(f"Matches={matchingChars}")
    print(f"Most similar string is {mostSimilar_} between {target} and {possibilities}")
    return mostSimilar_


mostSimilarString()
time.sleep(10)
from PyDictionary import PyDictionary
def aiBoost(userField="In Her Hands We Are Extravagant", mediaType="song", mode="additive"):
    if len(userField.split(" ")) > 3:
        mode = "subtractive"
    tagWordsIndex = getDictionary("tagWordsIndex")
    #print(tagWordsIndex)
    print(userField)
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
    filteredTagSequences = [x for x in ts if len(x) > lenWords]
    mostSimilarRow = mostSimilar(userTags, filteredTagSequences)
    print(words, "words")

    print(tags, "userTags")

    for w, word in enumerate(words):
        try:
            realTag = wordTagIndex[word.lower()].replace('$', "")
        except KeyError:
            realTag = "NNP"
        idealTag = mostSimilarRow[w].replace('$', "")

    """
    maxI = len(filteredTagSequences)
    maxJ = len(userTags)
    for i, professionalSequence in enumerate(filteredTagSequences):
        print(professionalSequence)
        sentence = ""
        if maxI - i < 2:
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
            sets = [list(set(x)) for x in filteredTagSequences] + [newSentenceTags]
            print("invalid you punk", sets)
            print("SETS", sets)
            return aiBoost(userField=sentence, mediaType=mediaType, mode=mode)
        print(filteredTagSequences, "filtered tag sequence")
    """


getKeyWordByCategory()
aiBoost()
def addJavaScript(scripts: str):
    return f"<head>{scripts}</head>"
