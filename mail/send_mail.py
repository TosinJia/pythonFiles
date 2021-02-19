import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender = "1872275509@qq.com"
psw = "stwhalndkillcghc"
receiver = "18502905667@163.com"

message = MIMEMultipart('related')
subject = 'SCREEN_TEST'
message['Subject'] = subject
message['From'] = sender
message['To'] = receiver
content = MIMEText('<html><body>SCREEN_CONTENT<img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')
message.attach(content)
screen_dir = "D:\\python\\screens\\screen.jpg"
file = open(screen_dir, "rb")
img_data = file.read()
file.close()
img = MIMEImage(img_data)
img.add_header('Content-ID', 'imageid')
message.attach(img)
try:
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, psw)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()
except smtplib.SMTPException as e:
    print("Exception: %s: %s" %(e.errno, e.strerror))
