from pyexpat import model
from django.db import models

# Create your models here.

# CREAMOS EL MODELO PARA DEFINIR LOS DATOS Y SU SCOPE DE USO
class Contactos(models.Model):
    nombres = models.TextField(max_length = 100, null = False)
    apellidos = models.TextField(max_length = 100 , null = False)
    telefono = models.CharField(max_length = 10 , null = False )
    email = models.EmailField(max_length = 20, null = False)
    class Meta:
        db_table = "contactos"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombres, self.apellidos, self.telefono, self.email)
