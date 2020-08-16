from email.mime.multipart import MIMEMultipart
#from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib

def send_mail(message):
    # create message object instance
    msg = MIMEMultipart()

    # setup the parameters of the message
    password = "Araceli0*"
    msg['From'] = "apoyotecno2015@gmail.com"
    msg['To'] = "morakurt@gmail.com"
    msg['Subject'] = "Melate para este dia"

    # attach image to message body
    #msg.attach(MIMEImage(file("google.jpg").read()))
    msg.attach(MIMEText(message, 'plain'))

    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()
    print ("successfully sent email to %s:" % (msg['To']))