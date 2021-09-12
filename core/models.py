from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.conf import settings




class Country(models.Model):
    name = models.CharField(max_length=255)
    phone_code = models.CharField(max_length=5,blank=True,null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'

class Service(models.Model):

    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):

        return self.title

class FaqImage(models.Model):

    image = models.ImageField(upload_to='faq_image/')


    def __str__(self):
        return "Faq Image"

    class Meta:
        verbose_name_plural = 'Faq Image'

class AboutUs(models.Model):

    image = models.ImageField(upload_to='about/')
    text = RichTextField()


    class Meta:
        verbose_name_plural = "About Us"

    def __str__(self):
        return "About Us"

class Visitors(models.Model):

    views = models.IntegerField(default=0)
    
class Index(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=127)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Index'

class Join(models.Model):
    title = models.CharField(max_length=127)
    short_description = models.TextField(max_length=127)
    number = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['number']

class JoinTitle(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField(max_length=127)
    
    def __str__(self):
        return self.title



    class Meta:
        verbose_name_plural = 'Join Title'

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


    def __str__(self):
        return self.question

class RecentWinner(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    price = models.IntegerField()
    img = models.ImageField(upload_to='user/')
    time = models.DateTimeField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


