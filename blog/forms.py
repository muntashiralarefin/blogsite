from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import blog
from django.contrib.auth.models import User

class blogForm(forms.ModelForm):
  class Meta:
    model = blog
    fields = ['user', 'test', 'photo']


class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')