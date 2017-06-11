# coding=utf-8


from email import encoders
from email.header import Header
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText, MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')


# 用来格式化一个邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候...', 'utf-8').encode()

# 邮件正文是MIMEText
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase,从本地读取一个图片
with open('test.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-Id', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # Base编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart
    msg.attach(mime)