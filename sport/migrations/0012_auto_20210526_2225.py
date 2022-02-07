# Generated by Django 3.2 on 2021-05-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0011_auto_20210526_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='sessions',
        ),
        migrations.AddField(
            model_name='trainer',
            name='session_choice',
            field=models.CharField(choices=[('9AM : 11AM', '09.00 : 11.00 AM'), ('11AM: 13PM', '11.00 AM: 13.00 PM'), ('13PM : 15PM', '13.00 : 15.00 PM'), ('15PM : 17PM', '15.00 : 17.00 PM'), ('17PM : 19PM', '17.00 : 19.00 PM')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='traineesport',
            name='session_choice',
            field=models.CharField(choices=[('9AM : 11AM', '09.00 : 11.00 AM'), ('11AM: 13PM', '11.00 AM: 13.00 PM'), ('13PM : 15PM', '13.00 : 15.00 PM'), ('15PM : 17PM', '15.00 : 17.00 PM'), ('17PM : 19PM', '17.00 : 19.00 PM')], max_length=30),
        ),
    ]
