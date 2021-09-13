from django.db import models
from ckeditor.fields import RichTextField


class PrivacyPolicy(models.Model):

    text = RichTextField()


class TermAndCondition(models.Model):

    text = RichTextField()