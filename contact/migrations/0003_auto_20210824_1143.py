# Generated by Django 3.2.6 on 2021-08-24 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinformation',
            name='information_az',
        ),
        migrations.RemoveField(
            model_name='contactinformation',
            name='information_en',
        ),
        migrations.RemoveField(
            model_name='contactinformation',
            name='information_ru',
        ),
    ]