from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_async_mail(subject, message_plain, from_email,reciption_list, html_message):
        
    send_mail(subject,message_plain,from_email,reciption_list,html_message)