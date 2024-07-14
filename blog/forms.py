from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import blog

class blogForm(forms.ModelForm):
  class Meta:
    model = blog
    fields = ['user', 'test', 'photo']