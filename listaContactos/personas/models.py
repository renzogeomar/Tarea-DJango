from django.db import models
from django.urls import reverse

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    edad = models.IntegerField()#max_digits=3
    email = models.EmailField(null=True, blank=True) #afecta a la base de datos y al formulario
    activo = models.BooleanField(default=True) #por defecto es True, si no se especifica se guarda como True

    def get_absolute_url(self):
        return reverse('personas:persona-detail', kwargs={'pk': self.id})



