from django import forms
from .models import Place
#create class for Django to add desired fields and input type
class NewPlaceForm(forms.ModelForm):
  class Meta:
    model = Place
    fields = ('name', 'visited')
