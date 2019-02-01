from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP

message = MIMEText('Python mail text\r\n', 'plain', 'utf8')
message['From'] = Header('sd', 'utf8')
message['To'] = Header('root', 'utf8')
message['Subject'] = Header('welcome', 'utf8')
password = 'omfybni690416'
smtp = SMTP()
smtp.connect('smtp.qq.com')
smtp.starttls()
smtp.login('531589111@qq.com', password, )
sender = '531589111@qq.com'
receviers = ['531589111@qq.com']
smtp.sendmail(sender, receviers, message.as_bytes())
