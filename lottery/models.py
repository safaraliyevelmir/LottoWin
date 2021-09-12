from django.db import models

from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone

User = get_user_model()


STATUS = (
    ('Waiting For Draw','Waiting For Draw'),
    ('Running','Running'),
)


class Lottery(models.Model):

    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date  = models.DateTimeField()
    price = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS,max_length=255)


    text = RichTextField()



    def get_absolute_url(self):
        return reverse("lottery:lotto_single", kwargs={"pk": self.pk})
    
    @property
    def count_ticker(self):
        lottery = Ticket.objects.filter(lottery=self.pk).count()
        return 100 - lottery


    def active_status(self):
        time = timezone.now()
        if self.end_date > time:
            return True
        else:
            return False

    def __str__(self):
        return self.title



class Ticket(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lottery = models.ForeignKey(Lottery,on_delete=models.CASCADE)
    number = models.IntegerField()


    def __str__(self):
        return f"{self.user} {self.lottery}"

