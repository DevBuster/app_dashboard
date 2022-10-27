# CREAMOS UN NUEVO FICHERO DONDE SE VA A CONTROLAR EL FORMULARIO
from django import forms

# DESDE LA CARPETA DE LA APLICACION.FICHERO_DEL_MODELO, 
# IMPORTAMOS LA CLASE CONTACTOS
from gestion_contactos.models import Contactos

class ContactosFormulario(forms.ModelForm):
    class Meta:
        
        modelo = Contactos 
        
        # RECIBIMOS TODOS LOS CAMPOS QUE ESPECIFICAMOS
        # DENTRO DEL MODELO 
        campos = "__all__"