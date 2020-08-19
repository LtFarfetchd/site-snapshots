import ssl, smtplib

username, password = tuple([cred.strip() for cred in open('emailCredentials.config').readlines()])
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtpServer:
    smtpServer.login(username, password)