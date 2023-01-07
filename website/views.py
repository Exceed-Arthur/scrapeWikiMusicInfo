from urllib.parse import quote

import flask
import flask_login
import urllib3.packages.six
from flask import request as request2
from flask import session as session2
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, render_template_string
from flask_login import login_user, login_required, logout_user, current_user
import os
import dynamoAPINameGen
import server_funcs
import UIFuncs
import server_functions

views = Blueprint('views', __name__)

print(f"Running on http://127.0.0.1:3000/music-naming-tool")
print(f"Running on http://127.0.0.1:3000/music-naming-tool-saved")
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request2.method == 'POST':
        if request.form['home-redirecters'] == 'redirecter-download':
            return redirect(url_for('views.download_page'))
        elif request2.form['home-redirecters'] == 'redirecter-account':
            return redirect(url_for('views.account_page'))
        elif request2.form['home-redirecters'] == 'redirecter-membership':
            return redirect(url_for('views.membership_page'))

    return render_template("home.html", user=current_user)


@views.route('/Download', methods=['GET', 'POST'])
def download_page():
    if request2.method == 'POST':
        if request2.form['home-redirecters'] == 'redirecter-portal':
            return redirect(url_for('views.home'))
        elif request2.form['home-redirecters'] == 'redirecter-landing':
            return redirect(url_for('views.account_page'))
        elif request2.form['home-redirecters'] == 'pc_download':
            #webbrowser.open_new_tab('https://drive.google.com/uc?export=download&id=1qfThO9zAoY--VZy6jdwV2OMYlAJb5Q3R')
            #return redirect(url_for('views.download_pc'))
            return redirect('https://drive.google.com/uc?export=download&id=1qfThO9zAoY--VZy6jdwV2OMYlAJb5Q3R')
        elif request2.form['home-redirecters'] == 'mac_download':
            #webbrowser.open_new_tab('https://drive.google.com/uc?export=download&id=1fnN8fIr4yTIv5YTmI9kbGp39jLX5V861')
            #return redirect(url_for('views.download_mac'))
            return redirect('https://drive.google.com/uc?export=download&id=1fnN8fIr4yTIv5YTmI9kbGp39jLX5V861')
    return render_template("download_page.html", user=current_user)


@views.route('/Account', methods=['GET', 'POST'])
def account_page():
    username = flask_login.current_user.email
    favorites_count = len(server_funcs.get_favorites_list_user(username))
    if favorites_count == ("None" or None):
        favorites_count = 0
    membership_status = server_funcs.get_membership_status_user(username)
    credits_count = server_funcs.get_user_credit_count(username)
    if request2.method == 'POST':
        if request2.form['home-redirecters'] == 'redirecter-portal':
            return redirect(url_for('views.home'))
        elif request2.form['home-redirecters'] == 'redirecter-landing':
            return redirect(url_for('views.account_page'))
    return render_template("account_page.html", user=current_user, username=username, credits_count=credits_count,
                           favorites_count=favorites_count, membership_status=membership_status)


@views.route('/Pro', methods=['GET', 'POST'])
@login_required
def membership_page():
    membership_status = server_funcs.get_membership_status_user(flask_login.current_user.email)
    if membership_status not in ["Gold", "Silver"]:
        membership_status = "Free"
    if request2.method == 'POST':
        if request2.form['home-redirecters'] == 'silver':
            if membership_status.lower() == 'silver':
                flash("You already have a silver membership!")
            else:
                return redirect(url_for('views.activate_silver'))
        elif request2.form['home-redirecters'] == 'gold':
            if membership_status.lower() == 'gold':
                flash(
                    'You are already a gold-member. Manage your account in the user portal or use it in the desktop app.')
            else:
                return redirect(url_for('views.activate_gold'))
        elif request2.form['home-redirecters'] == 'cancel':
            if membership_status.lower() == 'free':
                flash('You are a free member. Nothing to cancel.')
            else:
                return redirect(url_for('views.cancel'))
        elif request2.form['home-redirecters'] == 'upgrade':
            if membership_status.lower() == 'gold':
                flash(
                    'You already have a gold membership. Manage your account in the user portal or use it in the desktop app.')
            else:
                return redirect(url_for('views.activate_gold'))
        elif request2.form['home-redirecters'] == 'redirecter-portal':
            return redirect(url_for('views.home'))
        elif request2.form['home-redirecters'] == 'redirecter-landing':
            return redirect(url_for('views.account_page'))
    return render_template("membership_page.html", user=current_user, membership_status=membership_status)


@views.route("/DownloadingForPC", methods=['GET', 'POST'])
def download_pc():
    if not os.name == 'nt':
        flash('You are using a Mac. Please download the Mac version.')
        return redirect(url_for('views.download_page'))
    else:
        flash('Downloading PC Install Wizard!')
        if request2.method == 'POST':
            if request2.form['home-redirecters'] == 'redirecter-portal':
                return redirect(url_for('views.home'))
            elif request2.form['home-redirecters'] == 'redirecter-landing':
                return redirect(url_for('views.account_page'))
            elif request2.form['home-redirecters'] == 'redirecter-account':
                return redirect(url_for('views.account_page'))
    return render_template('download_success_pc.html', user=current_user)



@views.route("/DownloadingForMac", methods=['GET', 'POST'])
def download_mac():
    if not os.name == 'nt':
        flash('Downloading Mac Install Wizard')
        if request2.method == 'POST':
            if request2.form['home-redirecters'] == 'redirecter-portal':
                return redirect(url_for('views.home'))
            elif request2.form['home-redirecters'] == 'redirecter-landing':
                return redirect(url_for('views.account_page'))
            elif request2.form['home-redirecters'] == 'redirecter-account':
                return redirect(url_for('views.account_page'))
    else:
        flash('You are using a PC. This is the Mac Version. Please download the PC version.')
        return redirect(url_for('views.download_page'))
    return render_template('download_success_mac.html', user=current_user)


@login_required
@views.route(
    '/ExecuteSilver?00D0OD%OO8OO@!ii1IILIliIED36D807974A9BDA7Bi1230589ufyc??fculknig0154aq35115asfasfasfaq3219196349578D662C29BA9FAB14EFA55DF7341F8E3F6B5E01C572EB467DEB14CD08DC5D2F332991EF1CAE5DCC11AB422EC6A1E2AC1B268A6us6er?83381li02oiH8B9F68BD4BD1F9B5572F2D379128D062468C847DA4F9C2B379081F409A2589DA',
    methods=['POST', 'GET'])
def buy_silver():
    server_funcs.activate_subscription(flask_login.current_user.email, 'Silver')
    if request2.method == 'POST':
        if request2.form['home-redirecters'] == 'redirecter-portal':
            return redirect(url_for('views.home'))
        elif request2.form['home-redirecters'] == 'redirecter-landing':
            return redirect(url_for('views.account_page'))
        elif request2.form['home-redirecters'] == 'redirecter-account':
            return redirect(url_for('views.account_page'))
    return render_template('execute_silver.html', user=current_user)


def you_sure():
    return "Are you sure?"

@views.route("/scratchrtx", methods=['GET', 'POST'])
def support_scratchrtx():
    return render_template('scratchrtxsupport.html', user=current_user)

@login_required
@views.route(
    '/ExecuteGold?DE67000101010D0OD%OO8OO@!ii1IILIliIED36D807974A9BDA7Bi1230589ufyc??fculknig0154aq35115asfasfasfaq3219196349578D662C29BA010000010100101@932EE9B187E0048830A48F0134D5E217F1CDCA208D8797DC0D36825E6BB6DD00OLJLjlijOD%OO81liLLl?!%$%OO8083O543240OC943F91illiC5CAOD0B8FCB87C530DlI1@!0OO6C08BE0',
    methods=['POST', 'GET'])
def buy_gold():
    server_funcs.activate_subscription(flask_login.current_user.email, 'Gold')
    if request2.method == 'POST':
        if request2.form['home-redirecters'] == 'redirecter-portal':
            return redirect(url_for('views.home'))
        elif request2.form['home-redirecters'] == 'redirecter-landing':
            return redirect(url_for('views.account_page'))
        elif request2.form['home-redirecters'] == 'redirecter-account':
            return redirect(url_for('views.account_page'))
    return render_template('execute_gold.html', user=current_user)


@views.route('/Support', methods=['POST', 'GET'])
def support():
    if request2.method == 'POST':
        if request2.form['home-redirecters'] == 'redirecter-account':
            return redirect(url_for('views.home'))
    return render_template('support_page.html', user=current_user)


@views.route('/Silver', methods=['POST', 'GET'])
def activate_silver():
    return render_template('activate_silver.html', user=current_user)


@views.route('/Gold', methods=['POST', 'GET'])
def activate_gold():
    return render_template('activate_gold.html', user=current_user)


def confirmation_required(desc_fn):
    def inner(f):
        @urllib3.packages.six.wraps(f)
        def wrapper(*args, **kwargs):
            if request2.args.get('confirm') != '1':
                desc = desc_fn()
                return redirect(url_for('confirm',
                                        desc=desc, action_url=quote(request2.url)))
            return f(*args, **kwargs)

        return wrapper

    return inner


@login_required
@confirmation_required(you_sure)
@views.route(
    '/CancelA@IIi10OOo83889RPrnm9B187E0048830A48F0134D5E217F1CDCA208D8797DC0D36825E6BB6DD00OLJLjlijOD%OO81liLLl?!%$%OO8083E3E838380OOOO5432mnnmnIl1i1lIlLO8D0D0D')
def cancel():
    server_funcs.cancel_membership(username=flask_login.current_user.email)
    flash("Cancelled Paid Membership! Taking you to your free account details now.")
    return redirect(url_for('views.account_page'))


@views.route("/scratchertx", methods=['GET', 'POST'])
def scratcherPortal():
    return redirect('http://scratchrtxpy.herokuapp.com/scratchr_tx')

import templates
from periphServerFuncs import *

keys = ["mediaType", "artistTitle", "songTitle", "albumTitle", "userField", "outputField", "user"]


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


@views.route('/current_naming_idea', methods=["GET", "POST"])
def CurrentNamingIdea():
    currentIdea = jsonify(session2["current_naming_idea"])
    print(f"CURRENT NAMING IDEA FOUND: {currentIdea}")
    return currentIdea


current_idea = None
@views.route('/music-naming-tool', methods=["GET", "POST"])
def MusicNameGenGuest():
    outputField = "AI Boosted Idea Generated Here"
    albumTitle = "Album Idea Generated Here"
    artistTitle = "Artist Idea Generated Here"
    songTitle = "Song Idea Generated Here"
    global current_idea
    queryString = request2.query_string.decode("utf-8").replace("+", " ")
    queryString = queryString.replace("%C3%A9", "é").replace("%20", " ")
    jsonDict = {}
    print(f"CURRENT USER 256: {session2.items()}")
    if queryString:
        jsonDict = decodeQueryToJSON(queryString)
        print(jsonDict, "decoded dict")
        if "albumTitle" in list(jsonDict.keys()):
            albumTitle = jsonDict["albumTitle"]
    preHTML = templates.htmlMainMusicNamesGuest
    if "mainInterfaceButtons=" in queryString:
        chosenButton = queryString.split("mainInterfaceButtons=")[1]
        if "&" in chosenButton:
            chosenButton = chosenButton.split("&")[0]
        print(f"CHOSEN BUTTON: {chosenButton}")
        if chosenButton == "newAlbumIdea":
            newIdea = dynamoAPINameGen.getMediaNameIdea(mediaType="album")['title']
            current_idea = newIdea
            session2['current_naming_idea'] = [newIdea, "album"]
            albumTitle = newIdea
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            print(f"Generated new album idea: {newIdea}")
            return render_template("musicNamingTemplate.html", user=current_user, songTitle=songTitle,
                                   artistTitle=artistTitle, albumTitle=albumTitle, outputField=outputField)

        elif chosenButton == "newArtistIdea":
            newIdea = dynamoAPINameGen.getMediaNameIdea(mediaType="artist")['title']
            current_idea = newIdea
            artistTitle = newIdea
            session2['current_naming_idea'] = [newIdea, "artist"]
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            print(f"Generated new artist idea: {newIdea}")
            return render_template("musicNamingTemplate.html", user=current_user, songTitle=songTitle,
                                   artistTitle=artistTitle, albumTitle=albumTitle, outputField=outputField)
        elif chosenButton == "newSongIdea":
            newIdea = dynamoAPINameGen.getMediaNameIdea(mediaType="song")['title']
            current_idea = newIdea
            session2['current_naming_idea'] = [newIdea, "song"]
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            songTitle = newIdea
            print(f"Generated new song idea: {newIdea}")
            return render_template("musicNamingTemplate.html", user=current_user, songTitle=songTitle,
                                   artistTitle=artistTitle, albumTitle=albumTitle, outputField=outputField)

    html = f"<html>{UIFuncs.addJavaScript(scripts=templates.javascriptMainSection)}{preHTML}</html>"
    print(f"Decoded JSON: {jsonDict}")
    print(f"Query String: {queryString}")
    mediaType = "song"
    if "mediaType=" in queryString:
        mediaType = queryString.split("mediaType")[1]
        if "&" in mediaType:
            mediaType = mediaType.split("&")[0]
            if "&" in mediaType:
                mediaType = mediaType.split("&")[0]
        print(f"Formulated mediaType={mediaType}")
        if mediaType == "artist":
            html = html.replace("Building: Songs", "Building: Artists")
            idea = dynamoAPINameGen.getMediaNameIdea(mediaType=mediaType)['title']
            session2['current_naming_idea'] = [idea, "artist"]
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            html = html.replace("Artist Name Generated Here", idea)
            print(html)
            htmlPreStringBlock = r'''{% extends "base.html" %} {% block title %}iToven Sign-In{% endblock %} {% block content
            %}'''
            html = htmlPreStringBlock + html + "\n{% endblock %}"
        elif mediaType == "album":
            html = html.replace("Building: Songs", "Building: Albums")
            idea = dynamoAPINameGen.getMediaNameIdea(mediaType=mediaType)['title']
            session2['current_naming_idea'] = [idea, "album"]
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            html = html.replace("Album Name Generated Here", idea)
            htmlPreStringBlock = r'''{% extends "base.html" %} {% block title %}iToven Sign-In{% endblock %} {% block content
            %}'''
            html = htmlPreStringBlock + html + "\n{% endblock %}"
        else:
            idea = dynamoAPINameGen.getMediaNameIdea(mediaType="song")['title']
            session2['current_naming_idea'] = [idea, "song"]
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            html = html.replace("Song Name Generated Here", idea)
            htmlPreStringBlock = r'''{% extends "base.html" %} {% block title %}iToven Sign-In{% endblock %} {% block content
            %}'''
            html = htmlPreStringBlock + html + "\n{% endblock %}"
    if "userField=" in queryString:
        userField = queryString.split("userField")[1]
        if "&" in userField:
            userField = mediaType.split("&")[0]
        print(f"Formulated userField={userField}")
        if len(userField) > 2:
            html = html.replace('placeholder=Your Idea To Improve', f"placeholder={userField}")
            aiBoostedIdea = UIFuncs.aiBoost(userField=userField, mediaType=mediaType)
            session2['current_naming_idea'] = [aiBoostedIdea, "customIdea"]
            print(f"Saved Session Data: {session2['current_naming_idea']}")
            print(f"AI Boosted Idea: {aiBoostedIdea}")
            html = html.replace("AI Boosted Idea Here", aiBoostedIdea)
            htmlPreStringBlock = r'''{% extends "base2.html" %} {% block title %}iToven Naming Tool{% endblock %} {% block content
            %}'''
        return render_template("musicNamingTemplate.html", user=current_user, songTitle=songTitle,
                               artistTitle=artistTitle, albumTitle=albumTitle, outputField=outputField)
    print("REACHED END OF FUNCTION CHECK TEMPLATE AND ARGS!")
    return render_template("musicNamingTemplate.html", user=current_user, songTitle=songTitle,
                           artistTitle=artistTitle, albumTitle=albumTitle, outputField=outputField)
    #return render_template_string(html)
    # return render_template_string(f"{UIFuncs.addJavaScript(scripts=templates.javascriptMainSection)}{preHTML}")



@views.route('/music-naming-tool-logged-in', methods=["GET", "POST"])
@login_required
def MusicNameGen():
    print(session2["CurrentUser"])
    print(current_user.email)

    print("LOL ")
    queryString = request2.query_string.decode("utf-8").replace("+", " ")
    queryString = queryString.replace("%C3%A9", "é").replace("%20", " ")
    jsonDict = {}
    saved = False
    if queryString:
        jsonDict = decodeQueryToJSON(queryString)
        print(jsonDict, "decoded dict")
        if "save=True" in queryString:
            saved = True
        if "albumTitle" in list(jsonDict.keys()):
            albumTitle = jsonDict["albumTitle"]
    preHTML = templates.htmlMainMusicNames
    if saved:  # Result of a redirect from a non logged in user, save current idea from session
        sessionData = None
        try:
            sessionData = session2["current_naming_idea"]
            print(f"Current session data: {sessionData}")
        except:
            print("No session data for this context: saved idea")
        if sessionData:
            flash(f"Saving {sessionData} to {session2['CurrentUser']}'s Account")

            print(f"Saving {sessionData} to {session2['CurrentUser']}'s Account")
            server_functions.addMusicNamingIdea(username=flask_login.current_user.email, ideaTitle=sessionData[0], mediaType=sessionData[1])
    if "mainInterfaceButtons=" in queryString:
        chosenButton = queryString.split("mainInterfaceButtons=")[1]
        if "&" in chosenButton:
            chosenButton = chosenButton.split("&")[0]
        if chosenButton == "newAlbumIdea":
            newIdea = dynamoAPINameGen.getMediaNameIdea(mediaType="album")['title']
            preHTML = preHTML.replace("albumTitleReplace", newIdea)
            print(f"Generated new album idea: {newIdea}")
        elif chosenButton == "newArtistIdea":
            newIdea = dynamoAPINameGen.getMediaNameIdea(mediaType="artist")['title']
            preHTML = preHTML.replace("artistTitleReplace", newIdea)
            print(f"Generated new artist idea: {newIdea}")
        elif chosenButton == "newSongIdea":
            newIdea = dynamoAPINameGen.getMediaNameIdea(mediaType="song")['title']
            preHTML = preHTML.replace("songTitleReplace", newIdea)
            print(f"Generated new song idea: {newIdea}")
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
    print("HOTDOG MAN")
    print(f"Query String: {queryString}")
    mediaType = "song"
    if "mediaType=" in queryString:
        mediaType = queryString.split("mediaType")[1]
        if "&" in mediaType:
            mediaType = mediaType.split("&")[0]
            if "&" in mediaType:
                mediaType = mediaType.split("&")[0]
        print(f"Formulated mediaType={mediaType}")
        if mediaType == "artist":
            html = html.replace("Building: Songs", "Building: Artists")
            idea = dynamoAPINameGen.getMediaNameIdea(mediaType=mediaType)['title']
            html = html.replace("Artist Name Generated Here", idea)
            print(html)
        elif mediaType == "album":
            html = html.replace("Building: Songs", "Building: Albums")
            idea = dynamoAPINameGen.getMediaNameIdea(mediaType=mediaType)['title']
            html = html.replace("Album Name Generated Here", idea)
        else:
            idea = dynamoAPINameGen.getMediaNameIdea(mediaType="song")['title']
            html = html.replace("Song Name Generated Here", idea)
    if "userField=" in queryString:
        userField = queryString.split("userField")[1]
        if "&" in userField:
            userField = mediaType.split("&")[0]
        print(f"Formulated userField={userField}")
        if len(userField) > 2:
            html = html.replace('placeholder=Your Idea To Improve', f"placeholder={userField}")
            aiBoostedIdea = UIFuncs.aiBoost(userField=userField, mediaType=mediaType)
            print(f"AI Boosted Idea: {aiBoostedIdea}")
            html = html.replace("AI Boosted Idea Here", aiBoostedIdea)
        return render_template_string(html)
    return render_template_string(html, user=current_user)
    # return render_template_string(f"{UIFuncs.addJavaScript(scripts=templates.javascriptMainSection)}{preHTML}")

