from django.core.mail import send_mail

from blog.models import Blog
from config import settings


def send_post_email(obj: Blog):
    send_mail(
        'Просмотры',
        f'Статья {obj.title} набрала {obj.views_count} просмотров\n'
        f'Содержание: {obj.post}',
        settings.EMAIL_HOST_USER,
        ['parlamentsv@mail.ru']
    )

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# def send_post_email(obj: Blog):
#     fromaddr = "vakhrin.sv@mail.ru"
#     toaddr = "parlamentsv@mail.ru"
#     mypass = "FUqFwaFi7vVEnkaf8g8n"
#
#     msg = MIMEMultipart()
#     msg['From'] = fromaddr
#     msg['To'] = toaddr
#     msg['Subject'] = "Привет от питона"
#
#     body = "Это пробное сообщение"
#     msg.attach(MIMEText(body, 'plain'))
#
#     server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
#     server.login(fromaddr, mypass)
#     text = msg.as_string()
#     server.sendmail(fromaddr, toaddr, text)
#     server.quit()