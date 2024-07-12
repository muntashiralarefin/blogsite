from os import name
from django.shortcuts import render


# Create your views here.
def index(request):
  return render(request, 'blog/index.html')
