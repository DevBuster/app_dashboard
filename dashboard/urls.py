# FICHERO DE RUTAS EXCLUSIVAMENTE DE LA APLICACION, NO DEL PROYECTO

from django.urls import path
from . import views

app_name = "Dashboard"

urlpatterns = [
    path('', views.home, name = "home"),
    path('registrar_muertes_violentas', views.RegistrarMuertesViolentas, name = "registrar muertes violentas"),
    path('registrar_muertes_violentas/', views.VistaRegistrarMuertesViolentas, name = "registrar muertes violentas"),
    # path('editar_contactos/<int:contactos_id>/', views.vista_editar_contactos, name = "editar contactos"),
    # path('editar_contactos/', views.editar_contactos, name = "editar contactos"),
    # path('eliminar_contactos/<int:contactos_id>', views.eliminar_contactos, name = "eliminar contactos"),
]
