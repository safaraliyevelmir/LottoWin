from django.db import models



class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()

    subject = models.CharField(max_length=255)
    message = models.TextField()

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class ContactTitle(models.Model):

    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title


class ContactInformation(models.Model):

    title = models.CharField(max_length=255)
    information = models.CharField(max_length=255)


    def __str__(self):
        return self.title