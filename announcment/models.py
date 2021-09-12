from django.db import models
from django.contrib.auth import get_user_model

from django.core.mail import send_mail
from django.conf import settings

from django.db.models.signals import post_save

User= get_user_model()

class Announcment(models.Model):

    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


    def __str__(self):
        return self.title


class Subscriber(models.Model):

    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email



def send_announcment(sender,instance,created,using,**kwargs):
    subscribers = Subscriber.objects.all()
    announcment = Announcment.objects.filter(id=instance.id).first()
    
    rec_list = []

    for subscriber in subscribers:
        rec_list.append(subscriber.email)
    

    subject = announcment.title
    message = announcment.text
    from_email = settings.EMAIL_HOST_USER
    recipient_list = rec_list

    send_mail(subject,message,from_email,recipient_list)


post_save.connect(send_announcment,sender=Announcment)






