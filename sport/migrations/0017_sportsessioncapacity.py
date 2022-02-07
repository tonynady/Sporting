# Generated by Django 3.2 on 2021-05-30 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0016_trainer_trainer_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportSessionCapacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_max_cap', models.IntegerField()),
                ('session_current_cap', models.IntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.session')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.sport')),
            ],
        ),
    ]