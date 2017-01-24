import smtplib
import socks

fromaddr = input('sender email: ')
toaddrs  = input('receiver email: ')
msg = input('message')
username = input('your email: ')
password = input('your password: ')

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
print('email sent')
server.quit()
