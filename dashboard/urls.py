# FICHERO DE RUTAS EXCLUSIVAMENTE DE LA APLICACION, NO DEL PROYECTO

from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.home, name = "home"),
    path('registrar_muertes_violentas', views.RegistrarMuertesViolentas, name = "registrar muertes violentas"),
    path('registrar_muertes_violentas/', views.VistaRegistrarMuertesViolentas, name = "registrar muertes violentas"),
    path('editar_muertes_violentas/<int:muertesViolentas_id>/', views.VistaEditarMuertesViolentas, name = "editar muertes violentas"),
    path('editar_muertes_violentas/', views.EditarMuertesViolentas, name = "editar muertes violentas"),
    path('eliminar_muertes_violentas/<int:muertesViolentas_id>', views.EliminarMuertesViolentas, name = "eliminar muertes violentas"),
]
