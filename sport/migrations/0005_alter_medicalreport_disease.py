# Generated by Django 3.2 on 2021-05-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_medicalreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalreport',
            name='disease',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
