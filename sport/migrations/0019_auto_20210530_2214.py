# Generated by Django 3.2 on 2021-05-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0018_auto_20210530_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsessioncapacity',
            name='session_current_cap',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sportsessioncapacity',
            name='session_max_cap',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
