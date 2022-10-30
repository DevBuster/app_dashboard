# FICHERO DE RUTAS EXCLUSIVAMENTE DE LA APLICACION, NO DEL PROYECTO

from django.urls import path
from . import views
from dashboard.views import Dashboard


app_name = "dashboard"

urlpatterns = [
    path('', Dashboard.as_view(), name = "home"),
    
    # muertes violentas #
    path('registrar_muertes_violentas', Dashboard.RegistrarMuertesViolentas, name = "registrar muertes violentas"),
    path('registrar_muertes_violentas/', Dashboard.VistaRegistrarMuertesViolentas, name = "registrar muertes violentas"),
    # path('editar_muertes_violentas/<int:muertesViolentas_id>/', views.VistaEditarMuertesViolentas, name = "editar muertes violentas"),
    # path('editar_muertes_violentas/', views.EditarMuertesViolentas, name = "editar muertes violentas"),
    # path('eliminar_muertes_violentas/<int:muertesViolentas_id>', views.EliminarMuertesViolentas, name = "eliminar muertes violentas"),
    
    # accidentes #
    path('crear_muertes_accidentes', Dashboard.RegistrarMuertesAccidentes, name = "registrar muertes accidentes"),
    path('crear_muertes_accidentes/', Dashboard.VistaRegistrarMuertesAccidentes, name = "registrar muertes accidentes"),
    # path('editar_muertes_accidentes/<int:muertesAccidentes_id>/', views.VistaEditarMuertesAccidentes, name = "editar muertes accidentes"),
    # path('editar_muertes_accidentes/', views.EditarMuertesAccidentes, name = "editar muertes violentas"),
    # path('eliminar_muertes_accidentes/<int:muertesAccidentes_id>', views.EliminarMuertesAccidentes, name = "eliminar muertes accidentes"),
    
    # accidentales #
    path('crear_muertes_accidentales', Dashboard.RegistrarMuertesAccidentales, name = "registrar muertes accidentales"),
    path('crear_muertes_accidentales/', Dashboard.VistaRegistrarMuertesAccidentales, name = "registrar muertes accidentales"),
    # path('editar_muertes_accidentales/<int:muertesAccidentales_id>/', views.VistaEditarMuertesAccidentales, name = "editar muertes accidentales"),
    # path('editar_muertes_accidentales/', views.EditarMuertesAccidentales, name = "editar muertes violentas"),
    # path('eliminar_muertes_accidentales/<int:muertesAccidentales_id>', views.EliminarMuertesAccidentales, name = "eliminar muertes accidentales"),
    
    # homicidios #
    path('crear_muertes_homicidio', Dashboard.RegistrarMuertesHomicidios, name = "registrar muertes homicidio"),
    path('crear_muertes_homicidio/', Dashboard.VistaRegistrarMuertesHomicidios, name = "registrar muertes homicidio"),
    # path('editar_muertes_homicidio/<int:muertesHomicidio_id>/', views.VistaEditarMuertesHomidicios, name = "editar muertes homicidio"),
    # path('editar_muertes_homicidio/', views.EditarMuertesHomicidios, name = "editar muertes homicidio"),
    # path('eliminar_muertes_homicidio/<int:muertesHomicidio_id>', views.EliminarMuertesHomidicios, name = "eliminar muertes homicidio"),
    
    # suicidios #
    path('crear_muertes_suicidios', Dashboard.RegistrarMuertesSuicidios, name = "registrar muertes suicidios"),
    path('crear_muertes_suicidios/', Dashboard.VistaRegistrarMuertesSuicidios, name = "registrar muertes suicidios"),
    # path('editar_muertes_suicidios/<int:muertesSuicidios_id>/', views.VistaEditarMuertesSuicidios, name = "editar muertes suicidios"),
    # path('editar_muertes_suicidios/', views.EditarMuertesSuicidios, name = "editar muertes suicidios"),
    # path('eliminar_muertes_suicidios/<int:muertesSuicidios_id>', views.EliminarMuertesSuicidios, name = "eliminar muertes suicidios"),
]
