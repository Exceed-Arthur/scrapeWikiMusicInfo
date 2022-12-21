def buildStringCombos(string: str):
    stringSplices = list()
    for index in range(len(string)):
        for index2 in range(len(string)):
            if string[index:index2]:
                if string[index:index2+1] not in stringSplices:
                    stringSplices.append(string[index:index2+1])
    strings = []
    for i in range(0, len(stringSplices)-1, 2):
        strings.append(stringSplices[i+1])
        strings.append(stringSplices[i])
    return strings


def removeDuplicateString(string: str):
    print(f"FUNCTION removeDuplicateString ENTER__________________{string}")
    stringCombos = buildStringCombos(string)[0]
    proposals = list()
    for target in stringCombos:
        scanned = string
        reversed_scan = list(scanned)
        reversed_scan.reverse()
        reversed_scan = "".join(reversed_scan)
        reversed_target = list(target)
        reversed_target.reverse()
        reversed_target = "".join(reversed_target)
        print(f"\nTarget: {target}\nScanned: {scanned}\nReversed: {reversed_scan}\nReversed Target: {reversed_target}")
        proposal = list(reversed_scan.replace(reversed_target, "", 1))
        proposal.reverse()
        proposal = "".join(proposal)
        proposals.append(proposal)
        return proposal
    proposals = list(proposals)
    proposals.sort(key=lambda x: len(x))
    return proposals


print(removeDuplicateString("9questMappin our 9questMan"))
