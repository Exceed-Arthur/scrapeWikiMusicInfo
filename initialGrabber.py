import random
import string
import time

import chromedriver_autoinstaller
from selenium import webdriver

import nonsense

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

keywords = []
albumKeyWords = []
songKeyWords = []
artists = set()
prepositions = ["you", "of", "and", "with", "your", "my", "if", "is", "to", "a", "for", "I", "i", "we", "We", "N'", "n'", "What's", "what's", "i'm", "'round", "i've", "this", "for"]
prepositionsF = ["you", "of", "and", "with", "your", "my", "if", "is", "to", "a", "N'", "n'", "What's", "what's", "'round"]
ideas = []

def getRealWord():
    global keywords
    word = ""
    while (not word) or (word.lower() in prepositions):
        word = random.choice(keywords).replace(",", "").replace("&", "")
    return word


def appendRealWord(original):
    originalString = original
    original = original.split(" ")
    try:
        original = original.remove("")
    except:
        pass
    if original:
        if original[len(original) - 1].lower() in prepositions:
            originalString = originalString + " " + getRealWord()
            appendRealWord(originalString)
    return originalString.replace("The The", "The").replace("My My", "my").replace("Me Been", getRealWord())


def buildPhrase(listOfWords):
    newWord = ""

    listOfWords2 = []
    for word in listOfWords:
        word = word.replace("&quot;", "").replace("(", "")
        listOfWords2.append(word)
    listOfWords = listOfWords2
    for wordIndex in range(0, len(listOfWords)-2):
        if listOfWords[wordIndex] == listOfWords[wordIndex+1]:
            del listOfWords[wordIndex]
    # print(listOfWords)
    for wordIndex in range(0, len(listOfWords)):
        if wordIndex == len(listOfWords) - 1:
            newWord += listOfWords[wordIndex]
        else:
            newWord += listOfWords[wordIndex] + " "
    return newWord


def filterPhrases(phrasesList):
    phraseLists = []
    for phrased in phrasesList:
        phrased = phrased.replace("!", "").replace(",", "")

        phrasesLocal = phrased.split(" ")
        if phrasesLocal[len(phrasesLocal) - 1] == "The":
            phrasesLocal = phrasesLocal[:len(phrasesLocal) - 1]
        if phrasesLocal[len(phrasesLocal) - 1] == "The":
            phrasesLocal = phrasesLocal[:len(phrasesLocal) - 1]

        phraseLists.append(phrasesLocal)
    return phraseLists


def cleanKeys():
    global artists
    global songKeyWords
    global albumKeyWords
    global keywords
    for kwList in [keywords, albumKeyWords, songKeyWords]:
        for itemized in kwList:
            for artist in artists:
                if artist.lower() in kwList or artist.lower().split(" ")[1] in kwList:
                    kwList.remove(itemized)
                    print(itemized)


def cleanAlbums():
    global albumKeyWords
    nonsensical = ["In-a-gadda-da-vida", "eminem", "hits"]
    for keyworded in albumKeyWords:
        for nonsenser in nonsensical:
            if nonsenser.lower() in keyworded.lower():
                albumKeyWords.remove(keyworded)


def cleanSongs():
    global songKeyWords
    nonsensical = ["In-a-gadda-da-vida", "eminem"]
    for keyworded in albumKeyWords:
        for nonsenser in nonsensical:
            if nonsenser.lower() in keyworded.lower():
                songKeyWords.remove(keyworded)


def averageCharCount(stringer):
    words = stringer.split(" ")
    wordCount = len(words)
    charCount = 0
    for word in words:
        charCount += len(word)
    return charCount / wordCount


def getAlbumsAndSongs():
    global albumKeyWords
    global artists
    global songKeyWords
    filteredArtists = []
    driver.get("https://en.wikipedia.org/wiki/List_of_Billboard_Year-End_number-one_singles_and_albums")
    freshHTML = (driver.page_source.split('<table class="wikitable">')[1])
    freshHTML = freshHTML.split('</tbody></table>')[0]
    freshVals = freshHTML.split("td>")
    artists = set()
    songs = []
    albums = set()
    for cell in freshVals:

        artist = "Drake"
        try:
            trackDetailCombo = cell.split('title="')[1]
            # print(trackDetailCombo, "trackDetails")

            try:

                song = trackDetailCombo.split('"')[0].replace("\n", "").replace("</", "").replace("&amp;", "")
                if "album" in song:
                    album = song
                    # print(f"ALBUM: {song}")
                    albums.add(album)
                else:
                    # print(f"SONG: {song}")
                    songs.append(song)

            except:
                print("232 error")
                time.sleep(3)

            try:
                artist = trackDetailCombo.split("")
                if len(artist) > 3:
                    # print("ARTIST ++++++ " + str(artist))
                    pass
            except:
                try:
                    artist = trackDetailCombo.split("br>")[1]
                    try:
                        artist = artist.split("/wiki/")[1].replace('"', "").replace("_", " ").replace("\n", "")

                    except:
                        if artist == "Drake":
                            artists.add(artist)
                        if " " in artist:
                            artists.add(artist)
                        else:
                            artist = artist.replace("\n", "")
                           # print(fr"ERROR 450 {artist}")
                    artist = artist.replace("<", "").replace("/", "").replace("\n", "")
                    artists.add(artist)
                    # print(f"ARTIST?: {artist}")

                except:
                    pass
                    # print("ERROR 629")
                    #print(trackDetailCombo, "ERROR 303")


        except:
            if "<th" in cell or "<tr" in cell or "/tr" in cell or "</" in cell:
                time.sleep(0)
                # print("ERROR 706")
            else:

                try:
                    album = cell.split("<i>")[1]

                    try:
                        album = album.split("</i>")[0]
                        # print("ALBUM?: album")
                    except:
                        print("ERROR 123")
                        #print(album, "album try 1")
                        # time.sleep(5)
                except:
                    cell = list(cell.replace("\n", ""))
                    for char in cell:
                        if not str(char).isalpha() and not str(char) == " ":
                            cell.remove(char)
                    celly = ""
                    for char in cell:
                        celly += char
                    cell = celly
                    if len(cell):
                        pass
        if artist[len(artist) - 1] == " ":
            artist = artist[0:len(artist) - 1]
        artist = artist.split(" (")[0]
        artist = artist.replace("%26", " & ")
        artist = artist.replace("%27", " & ")
        if artist[0:3] == " & ":
            artist = artist[3:]
        artist = artist.split(" class=")[0]
        artist = artist.replace("%C3%AD", "i")
        artist = artist.replace("%C3%A9", "e")
        artist = artist.replace("  ", " ").replace("  ", " ")
        filteredArtists.append(artist)

        for song in songs:
            if song.lower() in filteredArtists:
                songs.remove(song)
                albums.add(song)

    #print(f"Songs count: {len(songs)}")

    filteredSongs = []
    songCount = 0
    for song in songs:
        songCount += 1
        song = song.split(" (")[0]
        # print(f'Song #{songCount}: {song}')
        filteredSongs.append(song)

    filteredAlbums = []
    albumCount = 0
    try:
        albums = albumKeyWords.remove("Beyonce")
    except:
        pass
    try:
        albumKeyWords = albumKeyWords.remove("Hits")
    except:
        pass
    try:
        albumKeyWords = albumKeyWords.remove("Orleans")
    except:
        pass
    try:
        songKeyWords = albumKeyWords.remove("Orleans")
    except:
        pass

    for album in albums:
        albumCount += 1
        album = album.split(" (")[0]
        filteredAlbums.append(album)
        # print(f'Album #{albumCount}: {album}')
    artists = list(set(filteredArtists))
    cleanKeys()
    return dict({"Songs": filteredSongs, "Albums": filteredAlbums, "Artists": artists})


def getKeywordAvg(choiced=" All Releases "):
    global keywords
    global MainDirectory
    cleanAlbums()
    cleanSongs()
    if "song" in choiced.lower():
        projectNames = MainDirectory["Songs"]
    elif "album" in choiced.lower():
        projectNames = MainDirectory["Albums"]
    else:
        projectNames = MainDirectory["Songs"] + MainDirectory["Albums"]
    titleCount = 0
    keywordCount = 0

    for title in projectNames:
        title = title.replace("  ", " & ")
        if choiced.lower() in ["albums", "album", "songs", "song"]:
            # print(f"{choiced.capitalize()} Title: {title} -- KEYWORDS: {len(title.split(' '))}")
            pass
        titleCount += 1
        keywordsLocal = title.split(' ')
        keywordCtLocal = len(keywordsLocal)
        keywordCount += keywordCtLocal
        for keyworded in keywordsLocal:
            keywords.append(keyworded)
        if "album" in choiced.lower():
            for keyworded in keywordsLocal:
                albumKeyWords.append(keyworded)
        if "song" in choiced.lower():
            for keyworded in keywordsLocal:
                songKeyWords.append(keyworded)
    kwdAVG = keywordCount / titleCount
    #print(f"AVERAGE NUMBER OF KEYWORDS IN {choiced.upper()} = {kwdAVG}")
    MainDirectory.update(dict(keywords=keywords))
    MainDirectory.update(dict(keywordAvg=kwdAVG))


def displayKeyWordAvgs():
    choices = ["Albums", "Songs"]
    for choicer in choices:
        getKeywordAvg(choicer)


MainDirectory = dict(getAlbumsAndSongs())
getKeywordAvg()
displayKeyWordAvgs()
# print(MainDirectory)
driver.quit()

for choice in ["Album", "Song"]:
    for i in range(200):
        # noinspection PyRedeclaration
        builtPhrase = ""
        firstPhrase = ""
        secondPhrase = ""
        for keywordComponentIndex in range(0, round(float(str(MainDirectory["keywordAvg"])))):
            if "album" in choice.lower():
                randomWord = random.choice(albumKeyWords)
                if len(randomWord) > 2:
                    randomWord = randomWord.capitalize()
                    builtPhrase += f"{randomWord} "
                else:
                    builtPhrase += f"{randomWord} "

            if "song" in choice.lower():
                randomWord = random.choice(songKeyWords)
                if len(randomWord) > 2:
                    randomWord = randomWord.capitalize()
                    builtPhrase += f"{randomWord} "
                else:
                    builtPhrase += f"{randomWord} "

        builtPhrase = builtPhrase[0: len(builtPhrase) - 1].capitalize()  # Trim trailing space
        formattedPhrase = ""
        for phrase in builtPhrase.split(" "):
            if phrase == "i":
                phrase = "I"
            if len(phrase) > 2:
                phrase = phrase.capitalize()
            phrase = f"{phrase} "
            formattedPhrase += phrase
        formattedPhrase = formattedPhrase.replace("  ", "")
        formattedPhrase = appendRealWord(formattedPhrase)
        phrases = formattedPhrase.split(" ")

        while phrases[len(phrases) - 1].lower() in prepositions:
            formattedPhrase += random.choice(keywords)
        if phrases[0].lower() in prepositionsF:
            formattedPhrase += random.choice(keywords)
        if formattedPhrase[len(formattedPhrase) - 1] == " ":
            formattedPhrase = formattedPhrase[0:len(formattedPhrase) - 1]
        formattedPhrase = formattedPhrase.replace(" The i", "")
        formattedPhrase = formattedPhrase.replace(" The me", "")
        formattedPhrase = formattedPhrase.replace(" The you", "")
        formattedPhrase = formattedPhrase.replace("me", "Me")
        formattedPhrase = formattedPhrase.replace("if", "If")
        formattedPhrase = string.capwords(formattedPhrase)

        if averageCharCount(formattedPhrase) > 3:
            firstPhrase = formattedPhrase
        builtPhrase = ""

        for keywordComponentIndex in range(0, random.randrange(2, 6)):
            if "album" in choice.lower():
                randomWord = random.choice(albumKeyWords)
                if randomWord == "Featuring":
                    randomWord = random.choice(albumKeyWords)
                if len(randomWord) > 2:
                    randomWord = randomWord.capitalize()
                    builtPhrase += f"{randomWord} "
                else:
                    builtPhrase += f"{randomWord} "

            if "song" in choice.lower():
                randomWord = random.choice(songKeyWords)
                if len(randomWord) > 2:
                    randomWord = randomWord.capitalize()
                    builtPhrase += f"{randomWord} "
                else:
                    builtPhrase += f"{randomWord} "

        builtPhrase = builtPhrase[0: len(builtPhrase) - 1].capitalize()  # Trim trailing space
        formattedPhrase = ""
        formattedPhrase = formattedPhrase.replace("  ", "")
        formattedPhrase = appendRealWord(formattedPhrase)

        for phrase in builtPhrase.split(" "):
            if len(phrase) > 2:
                phrase = phrase.capitalize()
            phrase = f"{phrase} "
            formattedPhrase += phrase
        phrases = formattedPhrase.split(" ")
        while phrases[len(phrases) - 1] in prepositions:
            formattedPhrase += " " + random.choice(keywords)
            phrases = formattedPhrase.split(" ")
        if formattedPhrase[len(formattedPhrase) - 1] == " ":
            formattedPhrase = formattedPhrase[0:len(formattedPhrase) - 1]
        formattedPhrase = formattedPhrase.replace(" The i", "")
        formattedPhrase = formattedPhrase.replace(" The me", "")
        formattedPhrase = formattedPhrase.replace(" The you", "")
        formattedPhrase = formattedPhrase.replace("me", "Me")
        formattedPhrase = formattedPhrase.replace("if", "If")
        formattedPhrase = appendRealWord(formattedPhrase)

        formattedPhrase = string.capwords(formattedPhrase)
        if averageCharCount(formattedPhrase) > 3:
            # print(f"{choice.upper()} NAME IDEA #{i}: {formattedPhrase}")
            secondPhrase = formattedPhrase

        if firstPhrase and secondPhrase:
            o = i

            phrasePair = filterPhrases([firstPhrase, secondPhrase])
            for item in phrasePair:
                #print(f"{choice.upper()} NAME IDEA #{o}: {buildPhrase(item)}")
                o += 1
                if item[0] not in nonsense.nonsense:
                    ideas.append((choice.upper(), buildPhrase(item)))
                else:
                    print(item[0])
"""
print(MainDirectory["keywords"])
print(albumKeyWords)
print(songKeyWords)
"""

