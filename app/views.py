from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    cars = Cars.objects.all()
    
    
    return render(request, 'home.html', {'cars':cars})