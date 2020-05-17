import smtplib, ssl, getpass
sender = 'quangthuyueb@gmail.com'
receiver = 'tuantran14041996@gmail.com'
subject = 'Test email'
body = '''
Test send email with pyton 
Using smtp and ssl lib
'''
password = getpass.getpass('Password:')
from email.mime.text import MIMEText
msg = MIMEText(body)
msg['subject'] = subject
msg['From'] = sender
msg['To'] = receiver

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())