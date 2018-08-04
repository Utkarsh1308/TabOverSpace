from django.contrib.auth.models import User
from django import forms

class ContactForm(forms.Form):
    data = forms.CharField(label='data', max_length=100)
