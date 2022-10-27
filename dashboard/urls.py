# FICHERO DE RUTAS EXCLUSIVAMENTE DE LA APLICACION, NO DEL PROYECTO

from django.urls import path
from . import views

app_name = "Gestion de Contactos"

urlpatterns = [
    path('', views.home, name = "home"),
    path('registrar_contactos', views.registrar_contactos, name = "registrar contactos"),
    path('registrar_contactos/', views.vista_registrar_contactos, name = "registrar contactos"),
    path('editar_contactos/<int:contactos_id>/', views.vista_editar_contactos, name = "editar contactos"),
    path('editar_contactos/', views.editar_contactos, name = "editar contactos"),
    path('eliminar_contactos/<int:contactos_id>', views.eliminar_contactos, name = "eliminar contactos"),
]
