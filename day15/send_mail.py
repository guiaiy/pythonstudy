import getpass
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def send_mail(text, subject, sender, receivers, mail_host, password):
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')
    smtp = SMTP()
    smtp.connect(mail_host)
    # smtp.starttls()
    smtp.login(sender, password, )
    smtp.sendmail(sender, receivers, message.as_bytes())


if __name__ == '__main__':
    mail_host = ''
    sender = ''
    password = getpass.getpass()
    receivers = []
    subject = ''
    text = ''
    send_mail(text, subject, sender, receivers, mail_host, password)
