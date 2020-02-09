from django import forms
from django.forms import ModelForm
from .models import Url

class UrlForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        labels = {'long_url':""}
        widgets = {
            'long_url': forms.TextInput(attrs={'placeholder': 'Shorten your link'})
        }