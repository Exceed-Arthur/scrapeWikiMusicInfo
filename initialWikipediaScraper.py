import wikiLib
import exceedLib
from removeDuplicates import removeDuplicateString
from selenium import webdriver
import textblob

import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

dictionary = dict(CC=[], CD=[], DT=[], EX=[], IN=[], JJ=[], JJR=[], JJS=[], LS=[], MD=[], NN=[], NNP=[], NNS=[], PDT=[], POS=[], PRP=[], RB=[], RBR=[], TO=[], UH=[], VB=[], VBN=[], WP=[], VBD=[], VBP=[], VBZ=[], WRB=[], WDT=[])
wordTagIndex = {}
tagWordsIndex = {}


def normalizeStringChars(string: str):
    string = list(string)
    stringer = []
    for char in string:
        if char.isalpha() or char.isdigit() or char in [",", "(", ")", " ", "!"]:
            stringer.append(char)
    print("".join(stringer))
    return "".join(stringer)


def getAllKeywords():
    driver = webdriver.Chrome()
    keywords_____ = []
    albums, songs, artists = [], [], []
    for year in range(2022, 2019, -1):
        urlForData = ""
        if year > 1957:
            urlForData = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}"
        elif year > 1955:
            urlForData = f"https://en.wikipedia.org/wiki/Billboard_year-end_top_50_singles_of_{year}"
        elif year > 1948:
            urlForData = f"https://en.wikipedia.org/wiki/Billboard_year-end_top_30_singles_of_{year}"
        elif year > 1939:
            urlForData = f"https://en.wikipedia.org/wiki/Billboard_year-end_top_singles_of_{year}"
        driver.get(urlForData)
        source = driver.page_source.split("title=")
        for source_ in source:
            source__ = source_.split("\n")
            source__ = exceedLib.filterByPhraseModel(source__)
            source__ = exceedLib.finalPhraseFilter(source__)
            for source___ in source__:
                if "</a>" in source___ and (len(source___) < 50):
                    print()
                    print(f"Source: {source___}")
                    source___ = source___.replace("&amp;", "&").replace("&amp;", "&")
                    isArtist, isSong, isAlbum = False, False, False
                    if "album" in source___.lower():
                        print(f"Album Source: {source___}")
                        isAlbum = True

                    string = exceedLib.filterTags(source___)
                    string = removeDuplicateString(string)
                    string = exceedLib.removeParenthetical(string)
                    if not isAlbum:
                        if wikiLib.isName(string):
                            isArtist = True

                        else:
                            isSong = True
                        if isArtist:
                            print(f"Artist Source: {string}")

                    if string:
                        print(f"Formatted String: {string}")
                        string = string.replace("&amp;", "&").replace("_", " ")
                        if string not in keywords_____:
                            keywords_____.append(string)
                            if isAlbum:
                                print(f"Album: {string}")
                                albums.append(string)
                            elif isSong:
                                print(f"Song: {string}")
                                songs.append(string)
                            elif isArtist:
                                print(f"Artist: {string}")
                                artists.append(string)
    keywords_____ = exceedLib.finalPhraseFilter(keywords_____)
    albumKeyWords = []
    songKeyWords = []
    artistKeyWords = []
    artistTagSequences = []
    songTagSequences = []
    albumTagSequences = []

    # Below lines add all key words for each type into keyword array for that type
    for typed in [(albums, albumKeyWords), (songs, songKeyWords), (artists, artistKeyWords)]:

        for data in typed[0]:
            keys_ = exceedLib.splitByWords(data)
            for key_ in keys_:
                print(f"Typed: {typed}")
                print(f"Data: {data}")

                print(f"Keys: {keys_}")
                print()
                typed[1].append(key_)   # albums=[albums]  select item in nested array
    # Below lines add all key words to dictionary of tags

    for typed in [(albumKeyWords, albumTagSequences), (songKeyWords, songTagSequences), (artistKeyWords, artistTagSequences)]:
        for kw in typed[0]:
            blobTag = textblob.TextBlob(kw).tags[0][1]
            blobWord = textblob.TextBlob(kw).tags[0][0]
            wordTagIndex.update({blobWord:blobTag})
            try:
                tagWordsIndex[blobTag].append(blobWord)
            except KeyError:
                tagWordsIndex.update({blobTag: [blobWord]})

    driver = webdriver.Chrome()

    albums = []
    for year in range(2022, 2019, -1):
        urlForData = ""
        if year > 1957:
            urlForData = f"https://en.wikipedia.org/wiki/List_of_Billboard_200_number-one_albums_of_{year}"
        elif year > 1955:
            urlForData = f"https://en.wikipedia.org/wiki/List_of_Billboard_number-one_albums_of_{year}"
        elif year > 1948:
            urlForData = f"https://en.wikipedia.org/wiki/List_of_Billboard_number-one_albums_of_{year}"
        elif year > 1939:
            urlForData = f"https://en.wikipedia.org/wiki/List_of_Billboard_Best-Selling_Popular_Record_Albums_number_ones_of_{year}"
        driver.get(urlForData)
        source = driver.page_source.split("title=")
        for source_ in source:
            source__ = source_.split("\n")
            source__ = exceedLib.filterByPhraseModel(source__)
            source__ = exceedLib.finalPhraseFilter(source__)
            for source___ in source__:
                if "Records" not in source___:
                    if "</a>" in source___ and (len(source___) < 50):
                        print()
                        print(f"Source: {source___}")
                        source___ = source___.replace("&amp;", "&").replace("&amp;", "&")
                        isArtist, isSong, isAlbum = False, False, False
                        for albumTerm in ["soundtrack", "album"]:
                            if albumTerm in source___.lower():
                                isAlbum = True
                        string = source___
                        string = exceedLib.filterTags(string)
                        string = exceedLib.removeDuplicateString(string)
                        string = exceedLib.removeParenthetical(string)
                        if string:
                            string = string.replace("&amp;", "&").replace("_", " ")
                            if string not in keywords_____:
                                keywords_____.append(string)
                            if isAlbum:
                                print(f"Album: {string}")
                                albums.append(string)
    for typed in [(albums, albumTagSequences), (songs, songTagSequences), (artists, artistTagSequences)]:
        for compoundPhrase in typed[0]:
            tagSequence = ""
            blobTags = textblob.TextBlob(compoundPhrase).tags
            print(f"Blob: {blobTags}")
            for tagPair in blobTags:
                tagSequence += tagPair[1]
            typed[1].append(tagSequence)

    driver.quit()
    keywords_____ = {"keywords": artistKeyWords + songKeyWords + albumKeyWords}
    dictToReturn = {}
    dictToReturn.update(keywords_____)
    dictToReturn.update({"tagWordsIndex": tagWordsIndex, "wordTagIndex": wordTagIndex, "albumTagSequences": albumTagSequences, "songTagSequences": songTagSequences, "artistTagSequences": artistTagSequences})

    return dictToReturn


def getAllOriginalWorkTitles():
    keywordsByYear = getAllKeywords()
    print(keywordsByYear)


def countCharacter(char: str, string: str):
    count = 0
    for letter in string:
        if char[0].lower() == letter.lower():
            count += 1
    return count


def removeDuplicates(string: str):
    if len(string) > 1:
        for outerCharIndex in range(len(string) - 1):
            for innerCharIndex in range(1, len(string)):
                stringSmaller = string[outerCharIndex:innerCharIndex]
                if stringSmaller in string[innerCharIndex:]:
                    string = string.replace(stringSmaller, ""
                                                           "")
    return string


# print(removeDuplicates('"Lauren Alaina">Lauren Alaina</a>'))
# print(getAllAlbums())
getAllOriginalWorkTitles()
