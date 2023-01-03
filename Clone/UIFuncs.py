import templates


def MainSection(artist=None, album=None, song=None, userField=None, mediaType=None, outputField=None):
    if not artist:
        artist = "Artist Name Generated Here"
    if not album:
        album = "Album Name Generated Here"
    if not song:
        song = "Song Name Generated Here"
    if not userField:
        userField = "Your Idea To Improve Here"
    if not outputField:
        outputField = "AI Boosted Idea Here"
    if not mediaType or mediaType not in ["artist", "song", "album"]:
        mediaType = "song"
    MainSectionHTML = templates.htmlMainMusicNames.replace("Building: Songs", f"Building: {mediaType.capitalize()}s")
    MainSectionHTML = MainSectionHTML.replace("{aiBoostedIdea}", outputField)
    MainSectionHTML = MainSectionHTML.replace("{artistIdeaGenerated}", artist)
    MainSectionHTML = MainSectionHTML.replace("{albumIdeaGenerated}", album)
    MainSectionHTML = MainSectionHTML.replace("{songIdeaGenerated}", song)
    return MainSectionHTML


def addJavaScript(scripts: str):
    return f"<head>{scripts}</head>"