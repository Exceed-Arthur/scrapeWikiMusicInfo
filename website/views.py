import random

import flask

import UIFuncs
import dynamoAPINameGen
import templates
from periphServerFuncs import *

keys = ["mediaType", "artistTitle", "songTitle", "albumTitle", "userField", "outputField"]


def decodeQueryToJSON(queryString: str):
    jsonDict = {}
    for key in keys:
        try:
            if key in queryString:
                val = queryString.split(f'{key}=')[1].split('&')[0]
                if '"' in val:
                    val = val.replace('"', "")
                jsonDict.update({key: val})
        except IndexError:
            print(f"index error for {key} on {queryString}")
    return jsonDict


@views.route('/', methods=["GET", "POST"])
def MusicNameGen(mediaType=None):

    queryString = flask.request.query_string.decode("utf-8").replace("+", " ")
    queryString = queryString.replace("%C3%A9", "é").replace("%20", " ")
    jsonDict = {}
    if queryString:
        jsonDict = decodeQueryToJSON(queryString)
        print(jsonDict, "decoded dict")
        if "albumTitle" in list(jsonDict.keys()):
            albumTitle = jsonDict["albumTitle"]
    preHTML = templates.htmlMainMusicNames
    for key in list(jsonDict.keys()):
        print(f"Analyzing Key: {key} --> found: {jsonDict[key]}")
        preHTML = preHTML.replace(f"{key}Replace", jsonDict[key])
    if "outputFieldReplace" in preHTML:
        preHTML = preHTML.replace("outputFieldReplace", "AI Boosted Idea Here")
    if "songTitleReplace" in preHTML:
        preHTML = preHTML.replace("songTitleReplace", "Song Name Generated Here")
    if "albumTitleReplace" in preHTML:
        preHTML = preHTML.replace("albumTitleReplace", "Album Name Generated Here")
    if "artistTitleReplace" in preHTML:
        preHTML = preHTML.replace("artistTitleReplace", "Artist Name Generated Here")
    html = f"<html>{UIFuncs.addJavaScript(scripts=templates.javascriptMainSection)}{preHTML}</html>"
    print(f"Decoded JSON: {jsonDict}")
    print(f"Query String: {queryString}")
    if "mediaType=" in queryString:
        mediaType = queryString.split("mediaType")[1]
        if "&" in mediaType:
            mediaType = mediaType.split("&")[0]
            if "&" in mediaType:
                mediaType = mediaType.split("&")[0]
        print(f"Formulated mediaType={mediaType}")
        if mediaType == "artist":
            html = html.replace("Building: Songs", "Building: Artists")
            print(html)
        if mediaType == "album":
            html = html.replace("Building: Songs", "Building: Albums")
    if "userField=" in queryString:
        userField = queryString.split("userField")[1]
        if "&" in mediaType:
            userField = mediaType.split("&")[0]
        print(f"Formulated userField={userField}")
        if len(userField) > 2:
            html = html.replace('placeholder=Your Idea To Improve', f"placeholder={userField}")

        time.sleep(5)

        return render_template_string(html)
    time.sleep(5)

    return flask.render_template_string(html)
    # return render_template_string(f"{UIFuncs.addJavaScript(scripts=templates.javascriptMainSection)}{preHTML}")


