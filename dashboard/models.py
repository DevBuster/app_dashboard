from pyexpat import model
from django.db import models

# Create your models here.

# CREAMOS EL MODELO PARA DEFINIR LOS DATOS Y SU SCOPE DE USO
class muertesViolentas(models.Model):
    tipoMuerte = models.TextField(max_length = 100, null = False)
    
    class Meta:
        db_table = "muertes_violentas"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoMuerte)
    
class muertesAccidentes(models.Model):
    tipoVehiculo = models.TextField(max_length = 100, null = False)
    
    class Meta:
        db_table = "muertes_accidentes"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoVehiculo)

class muertesAccidentales(models.Model):
    tipoAccidente = models.TextField(max_length = 100, null = False)

    class Meta:
        db_table = "muertes_accidentales"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoAccidente)
    
class muertesHomicidios(models.Model):
    tipoHomicidio = models.TextField(max_length = 100, null = False)

    class Meta:
        db_table = "homicidios"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoHomicidio)

class muertesSuicidios(models.Model):
    tipoSuicidio = models.TextField(max_length = 100, null = False)

    class Meta:
        db_table = "suicidios"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoSuicidio)
