from pyexpat import model
from django.db import models

# Create your models here.

# CREAMOS EL MODELO PARA DEFINIR LOS DATOS Y SU SCOPE DE USO
class MuertesViolentas(models.Model):
    tipoMuerte = models.TextField(max_length = 100, null = False)
    numeroVictimas = models.CharField(max_length = 100, null = False)
    
    class Meta:
        db_table = "muertesViolentas"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoMuerte, self.numeroVictimas)
    
class MuertesAccidentes(models.Model):
    tipoVehiculo = models.TextField(max_length = 100, null = False)
    numeroVictimas = models.CharField(max_length = 100, null = False)
    
    class Meta:
        db_table = "muertesAccidentes"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoMuerte, self.numeroVictimas)

class MuertesAccidentales(models.Model):
    tipoAccidente = models.TextField(max_length = 100, null = False)
    numeroVictimas = models.CharField(max_length = 100, null = False)

    class Meta:
        db_table = "muertesAccidentales"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoMuerte, self.numeroVictimas)
    
class MuertesHomicidios(models.Model):
    tipoHomicidio = models.TextField(max_length = 100, null = False)
    numeroVictimas = models.CharField(max_length = 100, null = False)

    class Meta:
        db_table = "muertesHomicidios"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoMuerte, self.numeroVictimas)

class MuertesSuicidios(models.Model):
    tipoSuicidio = models.TextField(max_length = 100, null = False)
    numeroVictimas = models.CharField(max_length = 100, null = False)

    class Meta:
        db_table = "muertesSuicidios"
    
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.id, self.tipoMuerte, self.numeroVictimas)
