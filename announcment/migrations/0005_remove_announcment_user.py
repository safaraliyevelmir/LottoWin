# Generated by Django 3.2.6 on 2021-08-18 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcment', '0004_alter_announcment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcment',
            name='user',
        ),
    ]