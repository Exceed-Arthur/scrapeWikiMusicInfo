from periphServerFuncs import *


def getMediaNameIdea(mediaType=None, words=None, length=None, iterations=0):
    table = dynamodb.Table(iTovenNamingTable)
    iterations += 1
    try:
        print(iterations)
        response = table.get_item(
            Key={
                'id': random.randrange(1111111, 9999999, 1),
            })["Item"]
        print(response)
        if mediaType or words or length:
            if mediaType:
                if response['category'] != mediaType:
                    raise KeyError
                if mediaType == "artist":
                    if "remix" in str(response['title']).lower():
                        return getMediaNameIdea(mediaType="artist", words=words, length=length)
                    return {'title': response['title'],
                       'mediaType': response['category']}
            if words:
                print(f"Words = True")
                if iterations > 1000 or words > 10:
                    return "Error Too Many Words"
                if " " not in response['title']:
                    raise KeyError
                if len(response['title'].split(" ")) < words:
                    raise KeyError
            if length:
                if iterations > 1000 or length > 50:
                    return "Error Too Long"
                if length > len(response['title']):
                    raise KeyError
        newResponse = {'title': response['title'],
                       'mediaType': response['category']}

        if words:
            newResponse.update(dict(words=len(response['title'].split(" "))))
        if length:
            newResponse.update(dict(length=len(response['title'])))
        return newResponse
    except KeyError:
        return getMediaNameIdea(mediaType, iterations=iterations, words=words, length=length)

