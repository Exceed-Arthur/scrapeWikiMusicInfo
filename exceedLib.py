import models


def buildStringCombos(string: str):
    stringSplices = list()
    for index in range(len(string)):
        for index2 in range(len(string)):
            if string[index:index2]:
                newString = string[index:index2 + 1]
                if newString not in stringSplices:
                    stringSplices.append(newString)
    strings = []
    for i in range(0, len(stringSplices) - 1, 2):
        strings.append(stringSplices[i + 1])
        strings.append(stringSplices[i])
    return strings


def countOccurences(string: str, target: str):
    count = 0
    if string:

        while target in string:
            string = string.replace(target, "", 1)
            count += 1
        return count


def removeDuplicateString(string: str):
    # print(f"FUNCTION removeDuplicateString ENTER__________________{string}")
    stringCombos = buildStringCombos(string)
    stringCombos = list(filter(lambda x: (countOccurences(string=string, target=x) > 1), stringCombos))
    stringCombos.sort(key=lambda x: len(x))
    stringCombos.reverse()
    proposals = []
    #stringCombos = filter(lambda x: (len(x) > 3), stringCombos)
    for target in stringCombos:
        if len(target) > 1:
            scanned = string
            reversed_scan = list(scanned)
            reversed_scan.reverse()
            reversed_scan = "".join(reversed_scan)
            reversed_target = list(target)
            reversed_target.reverse()
            reversed_target = "".join(reversed_target)
            proposal = scanned
            print(f"Target: {target}\nScanned: {scanned}\nReversed: {reversed_scan}\nReversed Target: {reversed_target}")
            if countOccurences(target=reversed_target, string=reversed_scan) > 1:
                proposal = list(reversed_scan.replace(reversed_target, "", 1))
                proposal.reverse()
                proposal = "".join(proposal)
            if proposal not in proposals:
                proposals.append(proposal)
                print(f"Proposed String: {proposal}")
                return proposal


# print(removeDuplicateString("pin family fam 9questMa"))


def filterTags(string: str):
    for tag in models.htmlTags:
        string = string.replace(tag, "")
    return string


def getIndex(string: str, target: str, occur: int):
    count, occur_ct = 0, 0
    for char in string:
        count += 1
        if char == target:
            occur_ct += 1
            if occur_ct == occur:
                return count


# Algorithm: Remove Any Word Contained Inside Parenthesis
def removeParenthetical(string: str):
    parenthetical = ""
    if countOccurences(string=string, target="(") == 1 and countOccurences(string=string, target=")") == 1:
        parenthetical = f'({string.split(")")[0].split("(")[1]})'
    if string:
        return string.replace(parenthetical, "").lstrip().rstrip()


def filterByPhraseModel(list_: list):
    for item in list_:
        for modelPhrase in models.filteredPhrasesWiki:
            if modelPhrase.lower() in item.lower():
                try:
                    list_.remove(item)
                except:
                    pass

    return list_


def finalPhraseFilter(list_: list):
    for item in list_:
        if "<a class" in item.lower():
            list_.remove(item)
            print(f"\nREMOVED: {item}")
    return list_
