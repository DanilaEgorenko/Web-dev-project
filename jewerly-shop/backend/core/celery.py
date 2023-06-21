from celery import Celery, shared_task
from django.core.mail import send_mail
from smtplib import SMTP
from email.utils import formataddr
from email.message import EmailMessage

app = Celery('tasks', broker='redis://redis:6379/0')

@shared_task
def add():
    print("hi")

@shared_task
def adv_mail():
    try:
        msg = EmailMessage()
        msg['From'] = formataddr(('2', '2@mail.ru'))
        msg['To'] = formataddr(('1', '1@mail.ru'))
        msg.set_content('This is our advertisement!')
        msg['Subject'] = "ADV!!!"

        with SMTP("mailhog", port=1025) as smtp:
            smtp.send_message(msg)
    except Exception as e:
        print(e)
    
app.conf.beat_schedule = {
    'advertisment-message-mail': {
        'task': 'core.celery.adv_mail',
        'schedule': 100.0,
    },
}
app.conf.timezone = 'UTC'
