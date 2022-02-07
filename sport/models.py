from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission, User



class Session(models.Model):
    session = models.CharField(max_length=20)

    def __str__(self):
        return self.session



class Day(models.Model):
    day_name = models.CharField(max_length=20)

    def __str__(self):
        return self.day_name



class Sport(models.Model):
    sport_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fee = models.FloatField()
    max_capacity = models.IntegerField()
    current_capacity = models.IntegerField(default=0)
    days = models.ManyToManyField(Day)
    sport_logo = models.FileField(null=True)

    def __str__(self):
        return self.sport_name
   

class SportSessionCapacity(models.Model):
    sport = models.ForeignKey(Sport, on_delete = models.CASCADE)
    session = models.ForeignKey(Session, on_delete = models.CASCADE)
    session_max_cap = models.IntegerField(null=True, blank=True)
    session_current_cap = models.IntegerField(default=0,null=True, blank=True) 

    def __str__(self):
        return str(self.sport) + '-' +str(self.session) + "- capacity"


class TraineeSport(models.Model):
    user = models.ForeignKey(User, default=1, on_delete = models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete = models.CASCADE)
    session_choice = models.ForeignKey(Session, on_delete = models.CASCADE)
    is_paid = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.sport)



class Trainer(models.Model):
    trainer_name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete = models.CASCADE)
    sessions = models.ManyToManyField(Session)
    phone_number = models.CharField(max_length=11, null=False, unique=True)
    date_of_birth = models.DateField()
    trainer_photo = models.FileField(null=True)

    def __str__(self):
        return self.trainer_name + '-' + str(self.sport)




class MedicalReport(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    height = models.IntegerField()
    gender_choices = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=6, choices=gender_choices)
    weight = models.IntegerField()
    fat_percentage = models.FloatField()
    muscle_percentage = models.FloatField()
    disease = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.user) + " -  Medical report "





