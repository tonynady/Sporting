# Generated by Django 3.2 on 2021-05-30 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0017_sportsessioncapacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsessioncapacity',
            name='session_current_cap',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sportsessioncapacity',
            name='session_max_cap',
            field=models.IntegerField(null=True),
        ),
    ]
