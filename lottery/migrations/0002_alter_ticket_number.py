# Generated by Django 3.2.6 on 2021-08-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.IntegerField(),
        ),
    ]