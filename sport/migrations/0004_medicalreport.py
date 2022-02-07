# Generated by Django 3.2 on 2021-05-25 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport', '0003_sport_sport_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=6)),
                ('weight', models.IntegerField()),
                ('fat_percentage', models.FloatField()),
                ('muscle_percentage', models.FloatField()),
                ('disease', models.TextField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
