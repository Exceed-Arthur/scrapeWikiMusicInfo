import models
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


def getAllOriginalWorkTitles():
    driver = webdriver.Chrome()
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
            for source___ in source__:
                if "</a>" in source___ and (len(source___) < 50):
                    print(normalizeStringChars(source___), len(source___), source___)


    driver.quit()


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
getAllOriginalWorkTitles()

