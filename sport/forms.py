from django import forms
from django.contrib.auth.models import User
from .models import Sport, TraineeSport

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AddSportForm(forms.ModelForm):

    class Meta:
        model = TraineeSport
        fields = ['sport', 'session_choice']