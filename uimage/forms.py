from django import forms 
from .models import *
  
class PictureForm(forms.ModelForm): 

   class Meta: 
        model = Pictures
        fields = ['skin_image'] 
