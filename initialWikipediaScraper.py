import wikiLib
import exceedLib
from removeDuplicates import removeDuplicateString
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


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
    for year in range(2022, 1945, -1):
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
                    isArtist, isSong, isAlbum = False, False, False
                    if "album" in source___.lower():
                        print(f"Album Source: {source___}")
                        isAlbum = True
                    elif "song" in source___.lower():
                        print(f"Song Source: {source___}")
                        isSong = True
                    elif not (isAlbum or isSong):
                        if wikiLib.isName(source___):
                            isArtist = True
                        else:
                            isSong = True
                        if isArtist:
                            print(f"Artist Source: {source___}")

                    string = exceedLib.filterTags(source___)
                    string = removeDuplicateString(string)
                    string = exceedLib.removeParenthetical(string)
                    if string:
                        print(f"Formatted String: {string}")
                        string = string.replace("&amp;", "&").replace("_", " ")
                        if string not in keywords_____:
                            keywords_____.append(string)
                            if isAlbum:
                                print(f"Album: {string}")
                            elif isSong:
                                print(f"Song: {string}")
                            elif isArtist:
                                print(f"Artist: {string}")
    driver.quit()
    keywords_____ = exceedLib.finalPhraseFilter(keywords_____)
    return keywords_____


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
        for outerCharIndex in range(len(string)-1):
            for innerCharIndex in range(1, len(string)):
                stringSmaller = string[outerCharIndex:innerCharIndex]
                if stringSmaller in string[innerCharIndex:]:
                    string = string.replace(stringSmaller, ""
                                                           "")
    return string


#print(removeDuplicates('"Lauren Alaina">Lauren Alaina</a>'))


print(getAllOriginalWorkTitles())