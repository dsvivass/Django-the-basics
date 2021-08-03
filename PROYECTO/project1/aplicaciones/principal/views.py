from django.shortcuts import render

# Create your views here.
from .models import Persona

def inicio(request):
    personas = Persona.objects.all() # select * from persona
    context = {
        'people': personas
        }# Representa la informacion que va a ser enviada al template en forma de diccionario
    return render(request, 'index.html', context)
    # return render(request, 'index.html') # El template es index.html