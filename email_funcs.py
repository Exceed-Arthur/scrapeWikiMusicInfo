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
          <div class="container" style="background-image: url('https://img.freepik.com/free-vector/musical-pentagram-sound-waves-notes-background_1017-33911.jpg?w=2000'); background-repeat: no-repeat; padding: 25rem; background-color: #BF195A;">
            <head link rel="stylesheet" title="iToven Verification" href="file:///Users/celeryman/Desktop/iToven%20Verificator/verificator.css" type="text/css"><title>iToven Verification</title>
            </head>
              <body>
                <div class="title" style="font-family: Trebuchet MS;font-size: 36;text-align: center;background-color: #fad3bf;border-radius: 35rem;">
                  <h1 class="title" style="color: #1c4aCb;font-family: Trebuchet MS;font-size: 46; text-align: center;">Your iToven AI Verifier Code:</h1>
                </div>
                <div class="code" style="text-align: center;">
                  <h1 class="code" style="font-family: Trebuchet MS;color: #573fD3;font-size: 90; text-align: center;background-color: #aeda6f; border-radius: 35rem;">
                    {self.code}
                  </h1>
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
