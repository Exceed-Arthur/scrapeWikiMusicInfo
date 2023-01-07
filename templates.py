htmlMainMusicNamesGuest = """

  <div id="HeaderSection" style="background-color: red; min-height: 160px; min-width: 
    800px; max-width: 840px; max-height: 160px;"> </div>
  <div id="MainContainer" style="background-color: green; 
    min-height: 500px; min-width: 800px; max-width: 840px;">
    <form>
    <div id="TrioGeneratorRow" style="display: inline-flex; 
      background-color: blue; min-width: 840px; max-width: 840px; padding-left: auto; padding-right: auto;">
      <div 
        id="SongIdeaBlock" style="padding-left: 2rem; padding-right: rem; padding-bottom: 1rem;">
        <div 
          id="TrioGeneratorRowC1" style="background-color: purple; min-height: 250px; min-width: 250px;">
          <p 
            id="generatedSongIdea" style="padding: 1rem; border: 1px solid black;background-color: white; text-align: center; 
            font-family: arial; font-size: 1.25rem;  vertical-align: center; max-width: 255px; min-width: 241px; 
            ">{{ songTitle }}</p>

          <div id ="SingularActionsRow" style="padding-left: 1.7rem; padding-bottom: 1.3rem;padding-top: 
            0.5rem; padding-bottom: 1.7rem"> <button id="copySongTitleButton" onClick=CopyToClipboard("generatedSongIdea")
            style="min-width: 4rem; min-height: 4rem; border-radius: 1.75rem; max-height: 4rem; font-family: arial; font-size: 
            1rem;">Copy </button> <button id="newSongTitleButton" name="mainInterfaceButtons" value="newSongIdea" style="background-color: lime; min-width: 4rem; min-height: 
            4rem; border-radius: 1.75rem; max-height: 4rem; font-size: 1rem; font-family: arial;">New </button> <button 
            id="saveSongTitleButton" onClick=saveUnloggedIn() style="min-width: 4rem; min-height: 4rem; border-radius: 1.75rem; max-height: 4rem; 
            font-size: 1.rem; font-family: arial;">Save </button></div>
          <div style="padding-left: 1.7rem; padding-top: 0.3rem;">
            <div id="semiCircleTitle1" style="background-color: yellow; font-size: 1.5rem; font-family: arial; text-align: center; 
              position: absolute; border-radius: 10rem 10rem 0 0; min-width: 194px; min-height: 5px;">Song Names</div>
          </div>
        </div>
      </div>
      <div id="AlbumIdeaBlock" style="padding-left: 0.25rem; padding-right: 
        0.25rem;">
        <div id="TrioGeneratorRowC2" style="background-color: violet; min-height: 250px; max-height: 120px;; 
          min-width: 250px;">
          <p id="generatedAlbumIdea" style="padding: 1rem;background-color: white; border: 1px solid black; 
            text-align: center; font-family: arial; ; min-width: 230px;; max-width: 255px;font-size: 1.25rem;  vertical-align: 
            center; ">{{ albumTitle }}</p>
          <div id ="SingularActionsRowAlbum" style="padding-left: 1.7rem; padding-bottom: 
            1.47rem;padding-top: 0.6rem;"> <button id="copyAlbumTitleButton" onClick=CopyToClipboard("generatedAlbumIdea") 
            style="min-width: 4rem; min-height: 4rem; border-radius: 1.75rem; max-height: 4rem; font-family: arial; font-size: 
            1rem;">Copy </button> <button id="newAlbumTitleButton" name="mainInterfaceButtons" value="newAlbumIdea" style="background-color: lime; min-width: 4rem; min-height: 
            4rem; border-radius: 1.75rem; max-height: 4rem; font-size: 1rem; font-family: arial;">New </button> <button 
            id="saveAlbumTitleButton" onClick=saveUnloggedIn() style="min-width: 4rem; min-height: 4rem; border-radius: 1.75rem; max-height: 4rem; 
            font-size: 1.rem; font-family: arial;">Save </button> </div>
          <div style="padding-left: 1.7rem; padding-top: 
            0.39rem;">
            <div id="semiCircleTitle2" style="background-color: yellow; font-size: 1.5rem; font-family: arial; 
              text-align: center; position: absolute; border-radius: 10rem 10rem 0 0; min-width: 200px;">Album Names</div>
          </div>
        </div>
      </div>
      <div id="ArtistIdeaBlock" 
        style="padding-left: 0.25rem; padding-right: 0.25rem;">
        <div id="TrioGeneratorRowC3" style="background-color: purple; 
          min-height: 250px; max-height: 120px;; min-width: 250px;">
          <p id="generatedArtistIdea" style="padding: 1rem; border: 
            1px solid black;background-color: white; text-align: center; font-family: arial; ; min-width: 230px;; max-width: 
            255px; font-size: 1.25rem;  vertical-align: center; ">{{ artistTitle }}</p>
          <div id ="SingularActionsRowArtist" 
            style="padding-bottom: 1.65rem; padding-left: 1.3rem; padding-top: 0.7rem;"> <button id="copyArtistTitleButton" 
            onClick=CopyToClipboard("generatedArtistIdea") style="min-width: 4rem; min-height: 4rem; border-radius: 1.75rem; 
            max-height: 4rem; font-family: arial; font-size: 1rem;">Copy </button> <button id="newArtistTitleButton" name="mainInterfaceButtons" value="newArtistIdea"
            style="background-color: lime; min-width: 4rem; min-height: 4rem; border-radius: 1.75rem; max-height: 4rem; 
            font-size: 1rem; font-family: arial;">New </button> <button id="saveArtistTitleButton" onClick=saveUnloggedIn() style="min-width: 4rem; 
            min-height: 4rem; border-radius: 1.75rem; max-height: 4rem; font-size: 1.rem; font-family: arial;">Save </button> </div>
          <div style="padding-left: 1.6rem; padding-bottom: 0.1rem; padding-top: 0.15rem;">
            <div id="semiCircleTitle3" style="background-color: yellow; font-size: 
              1.5rem; font-family: arial; text-align: center; position: absolute; border-radius: 10rem 10rem 0 0; min-width: 200px;">Artist Names</div>
          </div>
        </div>
      </div>
    </div>
    </form>
    <div 
      id="IdeaImproverSection" style="background-color: orange; min-width: 340px; min-height: 300px; border-radius: 2rem; 
      font-family: Garamond; background-color: gray;">
      <div id="UserFieldIdea" style="background-color: pink; min-width: 
        800px; max-width: 840px;min-height: 50px;font-family: Garamond; padding: 1rem;text-align: center;"> <input 
        id="UserInputFieldIdeaInput" placeholder="Your Idea To Improve" style="font-family: arial; font-size: 2rem; 
        text-align: center; padding-top: 0.5rem; min-width: 32rem;"> </div>
      <div id="embeddedModulatorSection" 
        style="display: inline-flex; background-color: yellow; padding-left: 13.78rem; min-width: 350px; max-width: 600px">
        <div id="buttonBlockFrameModulator" style="display: inline-block; background-color: yellow; ">
          <div 
            id="BuilderStatusFrame" style="background-color: white; padding: 0.5rem; padding-right;text-align: center; 
            font-family: arial; font-weight: bold; font-size: 1.3rem;">Building: Songs</div>
          <div 
            id="ModulatorSectionActionButtons" style="background-color: red; max-width: 300px;min-width: 100px; min-height: 30px; 
            padding-bottom: 1rem;font-family: Garamond; padding-top: 1rem;text-align: center;"> <button id="copyButton" 
            onClick=CopyToClipboard("userOutputField") style="background-color: white; color: green; max-height: 3rem; 
            border-radius: 0.5rem; shadow;box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);; position: relative; font-family: 
            Garamond; min-width: 3rem; min-height: 3rem; border-radius: 1rem; font-size: 1rem;">Copy</button> <button 
            id="saveButton" onClick=saveUnloggedIn() style="background-color: white; color: green; max-height: 3rem; border-radius: 0.5rem; 
            shadow;box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); max-width: 4rem; position: relative; font-family: Garamond; 
            min-height: 3rem; border-radius: 1rem; font-size: 1rem;">Save</button> <button id="resetButton" 
            onClick=ResetMainSection() style="background-color: white; color: green; max-height: 3rem; border-radius: 0.5rem; 
            shadow;box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); max-width: 4rem; position: relative; font-family: Garamond;  
            min-width: 3rem; min-height: 3rem; border-radius: 1rem; font-size: 1rem;">Reset</button> </div>
          <div 
            id="ModulatorSectionTypeButtons" style="background-color: red; max-width: 300px; min-width: 300px; min-height: 30px; 
            padding-bottom: 1rem;font-family: Garamond; padding-top: 1rem;;text-align: center;">
            <button id="artistSelector" onClick=SelectMediaTypeArtist() style="background-color: white; color: green; max-height: 3rem; border-radius: 0.5rem; 
              min-height: 3rem;box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); position: relative; font-family: Garamond; min-width: 
              3rem; min-width: 3rem; font-weight: bold;">Artist</button> </a> <button id="songSelector" onClick=SelectMediaTypeSong() style="background-color: 
              white; color: green; max-height: 3rem; border-radius: 0.5rem; shadow;box-shadow: 0px 8px 15px rgba(0, 0, 0, 
              0.1); max-width: 4rem; position: relative; font-family: Garamond; min-width: 3rem; max-height: 3rem; border-radius: 
              0.5rem; min-height: 3rem;font-weight: bold;">Song</button> <button id="albumSelector" onClick=SelectMediaTypeAlbum() style="background-color: white; 
              color: green; max-height: 3rem; border-radius: 0.5rem; shadow;box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1); max-width: 
              4rem; position: relative; font-family: Garamond; min-width: 3rem; max-height: 3rem; border-radius: rem; min-height: 
              3rem; font-weight: bold;">Album</button> 
          </div>
        </div>
        <div id="GoButtonFrame" style="min-width: 3rem; min-height:3rem; background-color: green; padding-top:3rem; padding-left: 2rem; padding-right: 2rem;">
          <button id="AIBoostButton" onClick=aiBoostRedirect() style="min-width: 6rem; min-height: 6rem; max-width: 6rem; max-height: 5rem; 
          border-radius: 2.5rem; font-family: futura; font-size: 1rem;">AI Boost</button></div>
      </div>
      <div 
        id="UserOutputFieldIdea" style="min-width: 492px; min-height: 20px; font-family: Garamond; padding: 0.1rem; 
        text-align: center; background-color: pink; padding-left: 10.4rem; padding-top: 1rem; padding-bottom: 0.5rem;">
        <h3 id="userOutputField" style="font-family: 
          arial; background-color: white; font-size: 2rem; text-align: center; text-align: center; min-width: 32rem; max-width: 
          32rem; max-height: rem;"> {{outputField}} </h3>
      </div>
    </div>
  </div>

"""

htmlMainMusicNames = """"""

javascriptMainSection = '''

<script id="mainScriptNameGenUI">

    function CopyToClipboard(containerid="id", elementText="Text") {
      if (document.selection) {
          var range = document.body.createTextRange();
          range.moveToElementText(document.getElementById(containerid));
          range.select().createTextRange();
          document.execCommand("copy");
      } else if (window.getSelection) {
          var range = document.createRange();
          range.selectNode(document.getElementById(containerid));
          window.getSelection().addRange(range);
          document.execCommand("copy");
          alert("${elementText} has been copied, now paste in the text-area");
      }
    }


    function aiBoostRedirect() { // Slightly modify state and redirect with new state elements var queryStringToSend = "?"; 
        var mediaType = document.getElementById("BuilderStatusFrame").innerText.replace("Building: ", "").toLowerCase();
        mediaType = mediaType.replace("songs", "song").replace("artists", "artist").replace("albums", "album");

        var songTitle = document.getElementById("generatedSongIdea").innerText.replace("%20");
        var queryStringToSend = "";
        if (!(songTitle.includes("Generated Here"))) {
            queryStringToSend = "songTitle=" + songTitle + "&";
        }
        var albumTitle = document.getElementById("generatedAlbumIdea").innerText;
        if (!(albumTitle.includes("Generated Here"))) {
            queryStringToSend = "albumTitle=" + albumTitle + "&";
        }
        var artistTitle = document.getElementById("generatedArtistIdea").innerText;
        if (!(artistTitle.includes("Generated Here"))) {
            queryStringToSend = "artistTitle=" + artistTitle + "&";
        }
        var userField = document.getElementById("UserInputFieldIdeaInput").value;
        if (userField == null) {
            alert("Enter an idea first before you can improve it.");
        }
        if (userField != null) {
            console.log("User String: " + userField);
            if (!(userField.includes("Generated Here"))) {
                queryStringToSend = queryStringToSend + "userField=" + userField + "&";
                document.getElementById("userOutputField").innerText = "Changed it mate!";
            }

        }

        var outputField = document.getElementById("userOutputField").innerText;
        if (!(outputField.includes("Generated Here"))) {
            outputField = "outputField=" + outputField + "&";
        }
        console.log("IM a dirty boi" + userField);
        queryStringToSend = queryStringToSend + ("mediaType=" + mediaType);
        queryStringToSend = queryStringToSend.replace("&&", "&");
        queryStringToSend = queryStringToSend.replace("userField=&", "");
        console.log(queryStringToSend);
        console.log("Query String");
        window.location.replace("/?" + queryStringToSend);
      }

  function SelectMediaTypeArtist() {
    console.log("selected media type: artist");
    window.location.replace("/?" + "mediaType=artist");
  }

  function SelectMediaTypeAlbum() {
    console.log("selected media type: artist");
    window.location.replace("/?" + "mediaType=album");
  }

  function SelectMediaTypeSong() {
    console.log("selected media type: song");
    window.location.replace("/?" + "mediaType=song");
  }

  function ResetMainSection() {
    window.location.replace("/");    
  }

  function saveUnloggedIn() {
    window.location.replace("/music-naming-tool-logged-in?save=True&");    
  }


  function SaveAIBoostedIdeaJS() {
      var queryStringToSend = "?";
      if (document.selection) {
          document.getElementById(elementID).innerText = elementText;
          var songTitle = document.getElementById("generatedSongIdea").innerText;
          queryStringToSend = queryStringToSend + ("songTitle=" + songTitle);
          var albumTitle = document.getElementById("generatedAlbumIdea").innerText;
          queryStringToSend = queryStringToSend + ("albumTitle=" + albumTitle);
          var artistTitle = document.getElementById("generatedArtistIdea").innerText;
          queryStringToSend = queryStringToSend + ("artistTitle=" + artistTitle);
          var userField = document.getElementById("userOutputField").innerText;
          queryStringToSend = queryStringToSend + ("userField=" + userField);
          var outputField = document.getElementById("userOutputField").innerText;
          queryStringToSend = queryStringToSend + ("outputField=" + outputField);
          var mediaType = document.getElementById("BuilderStatusFrame").innerText.replace("Building: ", "").toLowerCase();
          queryStringToSend = queryStringToSend + ("mediaType=" + mediaType);
          queryStringToSend = queryStringToSend + ("saveBoostedIdea=" + document.getElementById("userOutputField").innerText);
          console.log(queryStringToSend);
          console.log("Query String");
          window.location.replace("/"+queryStringToSend);  
          alert("Saved " + "AI Boosted Idea: " + document.getElementById("userOutputField").innerText);
      }  
  }

console.log("done man");

</script>'''
