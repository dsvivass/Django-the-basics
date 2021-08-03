from django.db import models

# Create your models here.

# aqui es donde vamos a escribir la interpretacion de las tablas de nuestra base de datos

class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=120)
    correo = models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre