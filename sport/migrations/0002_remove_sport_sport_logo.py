# Generated by Django 3.2 on 2021-05-25 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='sport_logo',
        ),
    ]
