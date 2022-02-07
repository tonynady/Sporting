from django.urls import path
from . import views

app_name = 'sport'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('index/', views.index, name='index'),

    path('<int:tr_sport_id>/', views.detail, name ='detail'),

    path('<int:trainer_id>/detail_trainer/', views.detail_trainer, name='detail_trainer'),

    path('<int:sport_id>/detail_not_user/', views.detail_not_user, name ='detail_not_user'),

    path('schedule/', views.schedule, name ='schedule'),

    path('financial_status/', views.financial_status, name ='financial_status'),

    path('medical_report/', views.medical_report, name ='medical_report'),

    path('add_sport/', views.add_sport, name ='add_sport'),

    path('<int:tr_sport_id>/delete_sport', views.delete_sport, name ='delete_sport'),
    
    path('register/', views.register, name ='register'),
    
    path('login_user/', views.login_user, name ='login_user'),
    
    path('logout_user/', views.logout_user, name ='logout_user'),
]
