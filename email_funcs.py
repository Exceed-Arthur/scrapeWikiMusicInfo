import datetime
import smtplib
from website import cred_web
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import threading


def itoven_send_email_str(to, subject, message):
    server = smtplib.SMTP_SSL("itoven-ai.co", 465)
    server.login(cred_web.username, cred_web.password)
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = cred_web.username
    server.send_message(msg)
    server.quit()


htmlVerifyString = f"""<html title="iToven Verification">
    <head link rel="stylesheet" title="iToven Verification" href="file:///Users/celeryman/Desktop/iToven%20Verificator/verificator.css" type="text/css"><title>iToven Verification</title>
      </head>
        <body>
        <div class="container" style="width: 100%; background-image: url('https://images.pond5.com/futuristic-digital-blue-rave-music-footage-085833520_prevstill.jpeg'); background-repeat: no-repeat;"><img style="padding-left: 1rem; padding-top: 1rem;" src="https://www.itoven-ai.co/images/logo-white.png">
          <div id="trioContainer" style="font-family: Trebuchet MS;font-size: 36;text-align: center;border-radius: 2rem; padding: 0.2rem;">
          <div class="title" style="font-family: Trebuchet MS;font-size: 25;text-align: center;border-radius: 2rem; width: 70%; padding-left: 5rem; padding-right: 5rem">
            <h1 id="tryUpdate" class="title" style="padding: 1rem; color: white; border-radius: 3rem; font-family: Trebuchet MS; background: linear-gradient(45deg, #c31432, #240b36); font-size: 46; text-align: center;">Your Verification Code:</h1>
          </div>
            <div style="padding-bottom: 1rem">              
                <div>
                    <label class="code" style="font-family: Trebuchet MS; padding: .7rem; color: #3c; background: linear-gradient(-05deg, yellow, red);font-size: 1.5rem; text-align: center;background-color: #01acdf; border-radius: 5rem;">Replace Me</label>
                </div>

                
            </div>
          </div>
          <p style="font-size: .5rem; color: white;">Sent from main server at {datetime.datetime.now()}</p>
        </body>
    </div>
</html>
"""



class EmailHTMLCodeThread(threading.Thread):
    def __init__(self, to, subject, code):
        self.to = to
        self.subject = subject
        self.code = code
        threading.Thread.__init__(self)
    def run(self):
        server = smtplib.SMTP_SSL("itoven-ai.co", 465)
        server.login(cred_web.username, cred_web.password)
        msg = MIMEMultipart('alternative')
        msg.content_subtype = 'html'
        msg['Subject'] = self.subject
        msg['To'] = self.to
        msg['From'] = cred_web.username
        me = cred_web.username
        # Create the body of the message (a plain-text and an HTML version).
        text = f"Enjoy our service! Here is your iToven verification code: {self.code}"
        html = f'''<html title="iToven Verification">
                    <head link rel="stylesheet" title="iToven Verification" href="file:///Users/celeryman/Desktop/iToven%20Verificator/verificator.css" type="text/css"><title>iToven Verification</title>
                    </head>
                    <body>
                    <div class="container" style="position: relative; ;width: 100%; background-image: url('https://images.pond5.com/futuristic-digital-blue-rave-music-footage-085833520_prevstill.jpeg'); background-repeat: no-repeat;"><img style="padding-left: 1rem; padding-top: 1rem;" src="https://www.itoven-ai.co/images/logo-white.png">
                     <div id="trioContainer" style="font-family: Trebuchet MS;font-size: 36;text-align: center;border-radius: 2rem; padding: 0.2rem;">
                    <div class="title" style="font-family: Trebuchet MS;font-size: 25;text-align: center;border-radius: 2rem; width: 70%; padding-left: 5rem; padding-right: 5rem">
                    <h1 id="tryUpdate" class="title" style="padding: 1rem; color: white; border-radius: 3rem; font-family: Trebuchet MS; background: linear-gradient(45deg, #c31432, #240b36); font-size: 46; text-align: center;">Your Verification Code:</h1>
                     </div>
                     <div style="padding-bottom: 1rem">              
                        <div>
                            <label class="code" style="font-family: Trebuchet MS; padding: .7rem; color: #3c; background: linear-gradient(-05deg, yellow, red);font-size: 1.5rem; text-align: center;background-color: #01acdf; border-radius: 5rem;">{self.code}</label>
                        </div>
        
                        
                                </div>
                              </div>
                              
                            </body>
                        </div>
                    </html>
        '''
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)
        server.sendmail(me, self.to, msg.as_string())


def itoven_send_html_verification(to, subject, code):
    EmailHTMLCodeThread(to, subject, code).start()
    print(f"Successfully sent verification code {code} to {to}. May take up to 3 minutes.")


from datetime import datetime
htmlUpdateString = f"""<html title="iToven Verification">
    <div class="container" style="border-radius: 2rem; width: 70%; background-image: url('https://images.pond5.com/futuristic-digital-blue-rave-music-footage-085833520_prevstill.jpeg'); background-repeat: no-repeat;"><img style="padding-left: 1rem; padding-top: 1rem;" src="https://www.itoven-ai.co/images/logo-white.png"></img>
      <head link rel="stylesheet" title="iToven Verification" href="file:///Users/celeryman/Desktop/iToven%20Verificator/verificator.css" type="text/css"><title>iToven Verification</title>
      </head>
        <body>
          <div id="trioContainer" style="font-family: Trebuchet MS;font-size: 36;text-align: center;border-radius: 2rem; padding: 0.2rem;">
          <div class="title" style="font-family: Trebuchet MS;font-size: 25;text-align: center;border-radius: 2rem;">
            <h1 id="tryUpdate" class="title" style="padding: 3rem; color: white; border-radius: 3rem; font-family: Trebuchet MS; background: linear-gradient(45deg, #c31432, #240b36); font-size: 46; text-align: center;">Hey, might as well download our iToven Sounds update...you've been gifted over 1000 download credits!</h1>
          </div>
            <div style="padding-bottom: 1rem">              
                <a href="https://portal.itoven-ai.co/Download">
                <button class="code" style="font-family: Trebuchet MS; padding: 1.5rem; color: #0de332; background: linear-gradient(45deg, blue, red);font-size: 1.3rem; text-align: center;background-color: #01acdf; border-radius: 5rem;">
                Download New Version (Mac or PC)
              </button></a></div>
              <div style="padding: 0.3rem; font-family: Trebuchet MS;color: #573fD3; text-align: center;background:linear-gradient(45deg, pink, orange); border-radius: 2rem;">
                <ul class="code" style="font-family: Trebuchet MS; font-size: 1.3rem; color: #573fD3; text-align: center;background: linear-gradient(45deg, pink, orange); border-radius: 3rem;">
                  <li style="font-family: Trebuchet MS;color: #2c5364; text-align: center;">Updated November 24th</li>
                  <li style="font-family: Trebuchet MS;color: #2c5364; text-align: center;" >Play/Pause button for better control.</li>
                  <li style="font-family: Trebuchet MS;color: #2c5364; text-align: center;">General stability improvements</li>
                  <li style="font-family: Trebuchet MS;color: #2c5364; text-align: center;">Bug fixes: file loading error, start error, etc.</li>
                </ul>
              </div>
            </div>
          </div>
          <p style="font-size: .5rem; color: white; padding-left: 2rem;">Sent from main server at {datetime.now()}</p>
        </body>
    </div>
</html>
"""


class UpdateAnnouncementEmailHTMLCodeThread(threading.Thread):
    def __init__(self, to, subject):
        self.to = to
        self.subject = subject
        threading.Thread.__init__(self)

    def run(self):
        server = smtplib.SMTP_SSL("itoven-ai.co", 465)
        server.login(cred_web.username, cred_web.password)
        msg = MIMEMultipart('alternative')
        msg.content_subtype = 'html'
        msg['Subject'] = self.subject
        msg['To'] = self.to
        msg['From'] = "iToven@itoven-ai.co"
        me = "iToven@itoven-ai.co"
        # Create the body of the message (a plain-text and an HTML version).
        text = f"We released an update!"
        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        withUser = htmlUpdateString.replace("{userEmail}", self.to)
        part2 = MIMEText(withUser, 'html')
        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)
        server.sendmail(me, self.to, msg.as_string())


def itoven_send_html_update_announcement(to, subject):
    UpdateAnnouncementEmailHTMLCodeThread(to, subject).start()
    print(f"Successfully sent update announcement to {to}. May take up to 3 minutes.")
    

#itoven_send_html_update_announcement(to="arthurlee99087@gmail.com", subject="Free Credits + The software update you asked for!")
