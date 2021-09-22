import smtplib, ssl
from email_credentials import username, password

# class Mail:
#
#     def __init__(self):
#         self.port = 587
#         self.smtp_server_domain_name = "smtp.gmail.com"
#         self.ehlo()
#         self.starttls()
#         self.sender_mail = username
#         self.password = password
#
#     def send(self, emails, subject, content):
#         service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port)
#         service.login(self.sender_mail, self.password)
#
#         for email in emails:
#             result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")
#
#         service.quit()
#
#
# if __name__ == '__main__':
#     mails = input("Enter emails: ").split()
#     subject = input("Enter subject: ")
#     content = input("Enter content: ")
#
#     mail = Mail()
#     mail.send(mails, subject, content)

# import smtplib
#
# try:
#     server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     server_ssl.ehlo()   # optional
#     server_ssl.starttls()  # optional
#     # ...send emails
# except:
#     print('Something went wrong...')

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = 'Hello, This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.Thank You'

#The mail addresses and password
sender_address = username
sender_pass = password
receiver_address = 'kvangraafeiland@esri.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')