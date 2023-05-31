from celery import Celery, shared_task
from django.core.mail import send_mail
from smtplib import SMTP
from email.utils import formataddr
from email.message import EmailMessage
import smtplib

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
    'add-every-10-seconds': {
        'task': 'core.celery.adv_mail',
        'schedule': 10.0,
    },
}
app.conf.timezone = 'UTC'

def get_celery_worker_status():
    i = app.control.inspect()
    availability = i.ping()
    stats = i.stats()
    registered_tasks = i.registered()
    active_tasks = i.active()
    scheduled_tasks = i.scheduled()
    result = {
        'availability': availability,
        'stats': stats,
        'registered_tasks': registered_tasks,
        'active_tasks': active_tasks,
        'scheduled_tasks': scheduled_tasks
    }
    return result