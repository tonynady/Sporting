from django.contrib import admin
from .models import Sport, TraineeSport, Day, MedicalReport, Trainer, Session, SportSessionCapacity

admin.site.register(Sport)
admin.site.register(TraineeSport)
admin.site.register(Day)
admin.site.register(MedicalReport)
admin.site.register(Trainer)
admin.site.register(Session)
admin.site.register(SportSessionCapacity)
