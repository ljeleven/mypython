#__author:"longjin"
#date:  2019/8/18
# -*- coding: UTF-8 -*-

#发送邮件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import  baseinfo
from email.mime.text import MIMEText
from email import header

mail_host = baseinfo.Smtp_Server
receiver = baseinfo.Smtp_Receiver
password = baseinfo.Smtp_Sender_Password
sender = baseinfo.Smtp_Sender
# contents = '明天加班！'

# msg = MIMEText(contents, 'plain', 'utf-8')
# msg['Subject'] = Header('放假通知', 'utf-8')
# msg['From'] = sender
# msg['To'] = receiver
# msg['Subject'] = header.Header('加班通知', 'utf-8')

#发送文字邮件
# try:
#     server = smtplib.SMTP()
#     server.connect(mail_host, 25)
#     server.login(sender, password)
#     server.sendmail(sender, receiver, msg.as_string())
#     server.close()
#     print('success!')
# except smtplib.SMTPException as e:
#     print(e)
#     print('failed!')

#发送带附件的邮件
# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = receiver
# msg['Subject'] = '放假通知'
# #邮件正文
# msg.attach(MIMEText('端午节放假三天', 'plain', 'utf-8'))
#
#
# #构造附件1
# att1 = MIMEText(open('C:/Users/lj/Desktop/软件测试-龙瑾.pdf', 'rb').read(), 'base64', 'utf-8')
# att1['Content-Type'] = 'application/octet-stream'
# att1['Content-Disposition'] = 'attachment; filename = "软件测试-龙瑾.pdf"'
# msg.attach(att1)
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)
#     smtpObj.login(sender, password)
#     smtpObj.sendmail(sender, receiver, msg.as_string())
#     print('sucess!')
# except smtplib.SMTPException as e:
#     print(e)
#     print('failed')


msg3 = MIMEMultipart('alternative')
msg3['From'] = sender
msg3['To'] = receiver
msg3['Subject'] = '图片附件'

msg3.attach(MIMEText('<html><body><h1>0</h1>' + '<p><img src = "cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
file_path = 'C:/Users/lj/Desktop/IMG_20170507_152731.jpg'
with open(file_path, 'rb') as f:
    mm = MIMEBase('image', 'jpg', filename='IMG_20170507_152731.jpg')
    mm.add_header('Content-Disposition', 'attachment', filename='IMG_20170507_152731.jpg')
    mm.add_header('Content-ID', '<0>')
    mm.add_header('X-Attachment-ID', '0')
    mm.set_payload(f.read())
    encoders.encode_base64(mm)
    msg3.attach(mm)

try:
    server = smtplib.SMTP()
    server.set_debuglevel(1)
    server.connect(mail_host, 25)
    server.login(sender, password)
    sender.sendmail(sender, receiver, msg3.as_string())
    server.close()
    print('success')
except smtplib.SMTPException as e:
    print(e)
    print('error')


























