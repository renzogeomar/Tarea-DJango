from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()#max_digits=3
    email = models.EmailField(null=True, blank=True)

