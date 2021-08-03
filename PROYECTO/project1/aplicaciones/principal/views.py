from django.shortcuts import render

# Create your views here.
from .models import Persona

def inicio(request):
    return render(request, 'index.html') # El template es index.html