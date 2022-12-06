import datetime
import math
import random
import time
import math

chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
         "u", "v", "w", "x", "y", "z"]


def extractDigits(var):
    newString = ""
    for char in str(var):
        if char.isdigit():
            newString += char
    newString = int(newString)
    return newString


def salty(val):

    newChars = {}
    for char in chars:
        charIndex = chars.index(char)
        newChars.update({char+char: charIndex*2})
    "{aa: 00}"
    "{zz: 50}"
    digits = extractDigits(val)
    digits = int(str(math.sqrt(digits)).replace(".", ""))
    #print(digits)
    parsedDigits = str(digits)

    pairSums = []
    for charPair in range(0, len(parsedDigits)-2, 2):
        pairSums.append(int(parsedDigits[charPair]+parsedDigits[charPair+1]))
    #print(pairSums)
    modifier = ""
    count = 0
    for pairSum in pairSums:
        for letterPair in list(newChars.keys()):
            count += 1
            if int(newChars[letterPair]) == int(pairSum):
                #print(letterPair[0] + str(count) + letterPair[1])
                modifier += letterPair[0] + chars[count % 3] + chars[(len(chars)-1) - count % 25] + letterPair[1]
            else:
                modifier = modifier.replace(chars[count % 3] + chars[(len(chars)-1) - count % 25], letterPair[0] + chars[count % 3])
    parsedDigits = f"{modifier}{math.sqrt(int(parsedDigits))}".replace(".", "")[38:] + f"{modifier}{math.sqrt(int(parsedDigits))}".replace(".", "")[0:9]
    return parsedDigits[0:-4]


class Browns:
    def __init__(self):
        self.kw = str(datetime.datetime.today().date()).replace(" ", "").replace("-", "")
        self.originalAxo = self.kw

    @staticmethod
    def hashBrick(dater):
        uc = []
        for char in chars:
            uc.append(char.upper())
        uc = uc + chars
        newc = []
        uc.reverse()
        for char in uc:
            for char2 in uc:
                newc.append(char2 + char)
        dater = pow(int(dater), 55) - int(dater) - pow(int(dater) % 55, 3)
        dater = int(str(dater)[:-125])
        keys = []
        maxe = 0
        for indexes in range(1, len(str(dater)) - 2, 2):
            index1 = int(str(dater)[indexes])
            index2 = int(str(dater)[indexes]) + 1
            for charPair in newc:
                totalval = 0
                for char in charPair:
                    charIndex = chars.index(char.lower())
                    totalval += int(charIndex)
                if totalval != 0:
                    if totalval < 50:
                        maxe += 1
                        if maxe >= 22:
                            break
                        newGuy = f"{charPair}{totalval}"
                        if newGuy not in keys:
                            keys.append(newGuy)
        og = ""
        for j in keys:
            og += j
        return og


    @staticmethod
    def op(val):
        import gaktriz
        return gaktriz.op(val)


kw2 = Browns()
kw2.originalAxo = kw2.hashBrick(kw2.kw)

randVals = []
newVals = []
count = 0
maxIndex = 20301230
minIndex = 20221130
keyStore = []
addedAlready = []
d = {}
""""""
i = int(kw2.kw)

count += 1
ace = kw2.hashBrick(str(i))
dated = i
i = pow(i, 4)

i = str(i)
chars_ = chars * 3
per = ""
for charpar in range(0, len(str(i)) - 2, 2):
    low = charpar
    hi = charpar + 1
    adjustment = (str(int(int(i) / 25)))
    per += chars_[low] + str(i)[charpar] + chars_[hi] + str(i)[hi]
# print(per)
per_ = per
numbers = ""
for p in per:
    if p.isdigit():
        numbers += p
per = int(numbers)
digiform = str(per / dated).split(".")[1].split("e")[0]
valued = (digiform + per_)[4:15] + (digiform + per_)[1:3] + (digiform + per_)[15:35]
newString = list(valued)
valuedStr = str(valued)
for indexer, char in enumerate(list(valuedStr)):
    if char.isalpha():
        newString[indexer] += char

x = "".join([str(i) for i in newString])
valued = str(x)[:24]
valued = salty(valued)[:8] + salty(valued[12:20]) + salty(valued)[8:12] + salty(valued[15:19]) + salty(
    valued[:11]) + salty(valued)[8:12] + salty(valued[15:19])

kw2.originalAxo = valued


def createDictionary():
    randVals = []
    newVals = []
    count = 0
    d = {}
    alreadyAdded = []
    for year in range(2022, 2030, 1):
        for month in range(1, 13, 1):
            for day in range(0, 32, 1):
                if len(str(month)) == 1:
                    month = str(f"0{month}")
                if len(str(day)) == 1:
                    day = str(f"0{day}")

                i = str(year) + str(month) + str(day)
                i = int(i)
                count += 1

                dated = i
                if dated not in alreadyAdded:
                    alreadyAdded.append(dated)
                    i = pow(i, 4)

                    i = str(i)
                    chars_ = chars * 3
                    per = ""
                    for charpar in range(0, len(str(i))-2, 2):
                        low = charpar
                        hi = charpar + 1
                        adjustment = (str(int(int(i)/25)))
                        per += chars_[low] + str(i)[charpar] + chars_[hi] + str(i)[hi]
                    #print(per)
                    per_ = per
                    numbers = ""
                    for p in per:
                        if p.isdigit():
                            numbers += p
                    per = int(numbers)
                    digiform = str(per / dated).split(".")[1].split("e")[0]
                    valued = (digiform + per_)[4:15] + (digiform + per_)[1:3] + (digiform + per_)[15:35]
                    newString = list(valued)
                    valuedStr = str(valued)
                    for indexer, char in enumerate(list(valuedStr)):
                        if char.isalpha():
                            newString[indexer] += char

                    x = "".join([str(i) for i in newString])
                    valued = str(x)[:24]
                    valued = salty(valued)[:8] + salty(valued[12:20]) + salty(valued)[8:12] + salty(valued[15:19]) + salty(valued[:11]) + salty(valued)[8:12] + salty(valued[15:19])
                    stored = {str(dated): str(valued)}
                    d.update(stored)
                    newVals.append((str(dated), str(valued)))
                    print(valued)
    return newVals


def storeKeys(storageTuples):

    with open("keystoreapi.py", 'w') as f:
        stringer = "keystore = {"
        string = ""
        for key in storageTuples:
            string += f'"{key[0]}": "{key[1]}", '
        string = string[0: len(string) - 2]
        string += "}"
        f.write(stringer + string)

    with open("keystoreapi_.swift", 'w') as f:
        stringer = "let keystore: [String: String] = ["
        string = ""
        for key in storageTuples:
            string += f'"{key[0]}" : "{key[1]}", '
        string = string[0: len(string) - 2]
        string += "]"
        f.write(stringer + string)


#storeKeys(createDictionary())
print(kw2.originalAxo)