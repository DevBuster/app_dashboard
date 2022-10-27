# CREAMOS UN NUEVO FICHERO DONDE SE VA A CONTROLAR EL FORMULARIO
from django import forms

# DESDE LA CARPETA DE LA APLICACION.FICHERO_DEL_MODELO, 
# IMPORTAMOS LA CLASE CONTACTOS
from dashboard.models import muertesViolentas
from dashboard.models import muertesAccidentes
from dashboard.models import muertesAccidentales
from dashboard.models import muertesHomicidios
from dashboard.models import muertesSuicidios

class muertesViolentasFormulario(forms.ModelForm):
    class Meta:
        
        modelo = muertesViolentas
        
        campos = "__all__"

class muertesAccidentesFormulario(forms.ModelForm):
    class Meta:
        
        modelo = muertesAccidentes 
        
        campos = "__all__"
        
class muertesAccidentalesFormulario(forms.ModelForm):
    class Meta:
        
        modelo = muertesAccidentales 
        
        campos = "__all__"

class muertesHomicidiosFormulario(forms.ModelForm):
    class Meta:
        
        modelo = muertesHomicidios 
    
        campos = "__all__"
        
class muertesSuicidiosFormulario(forms.ModelForm):
    class Meta:
        
        modelo = muertesSuicidios 
        
        campos = "__all__"