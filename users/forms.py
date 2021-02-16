from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Appointment


class UserRegisterForm(UserCreationForm):
   email = forms.EmailField()

   class Meta:
      model = User
      fields = ['username','email','password1', 'password2']


class AppontmentForm(forms.ModelForm):
   class Meta:
      model = Appointment
      fields = '__all__'
