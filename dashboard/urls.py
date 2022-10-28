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
    #--------------------------------------------------------------------------------------------------------------------------------#
    path('crear_muertes_accidentes', views.RegistrarMuertesAccidentes, name = "registrar muertes accidentes"),
    path('crear_muertes_accidentes/', views.VistaRegistrarMuertesAccidentes, name = "registrar muertes accidentes"),
    path('editar_muertes_accidentes/<int:muertesAccidentes_id>/', views.VistaEditarMuertesAccidentes, name = "editar muertes accidentes"),
    path('editar_muertes_accidentes/', views.EditarMuertesViolentas, name = "editar muertes violentas"),
    path('eliminar_muertes_accidentes/<int:muertesAccidentes_id>', views.EliminarMuertesAccidentes, name = "eliminar muertes accidentes"),
]
