import smtplib
import socks
from smtplib import SMTPAuthenticationError

fromaddr = input('sender email: ')
toaddrs  = input('receiver email: ')
msg = input('message')
username = input('your email: ')
password = input('your password: ')

try:
 server = smtplib.SMTP('smtp.gmail.com:587')
 server.ehlo()
 server.starttls()
 server.login(username,password)
 server.sendmail(fromaddr, toaddrs, msg)
 print('email sent')
except SMTPAuthenticationError:
    print('Error: \n Possible Reasons: \n->invalid username/pswd \n->Login using less secured app has been turned off.')
    

server.quit()
