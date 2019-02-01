from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP

message = MIMEText('Python mail text\r\n', 'plain', 'utf8')
message['From'] = Header('sd', 'utf8')
message['To'] = Header('root', 'utf8')
message['Subject'] = Header('welcome', 'utf8')

smtp = SMTP('localhost')
sender = 'sd'
receviers = ['root@localhost']
smtp.sendmail(sender, receviers, message.as_bytes())
