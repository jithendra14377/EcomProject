import smtplib
from email.message import EmailMessage
def send_email(to,subject,body):
    server =smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('trjr0905@gmail.com','vzfs nilp jenx mozk')
    msg=EmailMessage()
    msg['FROM']='trjr0905@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    print('Mail Sent')
    server.close()