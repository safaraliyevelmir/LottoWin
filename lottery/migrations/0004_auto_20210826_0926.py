# Generated by Django 3.2.6 on 2021-08-26 09:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_delete_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottery',
            name='ticket_count',
        ),
        migrations.AddField(
            model_name='lottery',
            name='text',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lottery',
            name='text_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='lottery',
            name='text_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='lottery',
            name='text_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
