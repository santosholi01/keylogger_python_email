from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os


email_address="email address of the sender"
password="generate from app password(sender email)"
toaddr="email address of the receiver"

def send_email(filename, attachment, toaddr):
    fromaddr=email_address

    msg=MIMEMultipart()
    msg['From']=fromaddr

    msg['To']=toaddr

    msg['Subject']='open the file'

    body="body_of_email"

    msg.attach(MIMEText(body, 'plain'))

    filename=filename
    attachment=open(attachment, 'rb')

    p=MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment: filename= %s" % filename)
    msg.attach(p)


    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    
    text=msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()


