def buildStringCombos(string: str):
    stringSplices = list()
    for index in range(len(string)):
        for index2 in range(len(string)):
            if string[index:index2]:
                newString = string[index:index2+1]
                if newString not in stringSplices:
                    stringSplices.append(newString)
    strings = []
    for i in range(0, len(stringSplices)-1, 2):
        strings.append(stringSplices[i+1])
        strings.append(stringSplices[i])
    return strings


def countOccurences(string:str, target:str):
    count = 0
    while target in string:
        string = string.replace(target, "", 1)
        count += 1
    return count


def removeDuplicateStringSpatial(string: str):
    return string
    if " " not in string:
        return string

    print(f"FUNCTION removeDuplicateString ENTER__________________{string}")
    stringCombos = buildStringCombos(string)
    stringCombos = list(filter(lambda x: (countOccurences(string=string, target=x) > 1), stringCombos))
    stringCombos.sort(key=lambda x: len(x))
    stringCombos.reverse()
    proposals = []
    for target in stringCombos:
        scanned = string
        reversed_scan = list(scanned)
        reversed_scan.reverse()
        reversed_scan = "".join(reversed_scan)
        reversed_target = list(target)
        reversed_target.reverse()
        reversed_target = "".join(reversed_target)
        proposal = scanned
        print(f"\nTarget: {target}\nScanned: {scanned}\nReversed: {reversed_scan}\nReversed Target: {reversed_target}")
        if countOccurences(target=reversed_target,string=reversed_scan) > 1:
            proposal = list(reversed_scan.replace(reversed_target, "", 1))
            proposal.reverse()
            proposal = "".join(proposal)
        if proposal not in proposals:
            proposals.append(proposal)
            return proposal


#print(removeDuplicateString("pin famour fam 9questMa"))