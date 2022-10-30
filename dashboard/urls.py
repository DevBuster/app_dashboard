"""
dasboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# FICHERO DE RUTAS EXCLUSIVAMENTE DE LA APLICACION, NO DEL PROYECTO

from django.urls import path
# from . import viewsdos
from dashboard.views import Dashboard
from dashboard.views import ModelCreateViewMuertesViolentas
from dashboard.views import ModelUpdateViewMuertesViolentas
from dashboard.views import ModelDeleteViewMuertesViolentas


app_name = "dashboard"

urlpatterns = [
    path('', Dashboard.as_view(), name = "home"),
    path('registrar_muertes_violentas', ModelCreateViewMuertesViolentas.RegistrarMuertesViolentas, name = "registrar muertes violentas"),
    path('registrar_muertes_violentas/', ModelCreateViewMuertesViolentas.VistaRegistrarMuertesViolentas, name = "registrar muertes violentas"),
    path('editar_muertes_violentas/<int:muertesViolentas_id>/', ModelUpdateViewMuertesViolentas.VistaEditarMuertesViolentas, name = "editar muertes violentas"),
    path('editar_muertes_violentas/', ModelUpdateViewMuertesViolentas.EditarMuertesViolentas, name = "editar muertes violentas"),
    path('eliminar_muertes_violentas/<int:muertesViolentas_id>', ModelDeleteViewMuertesViolentas.get_context_data, name = "eliminar muertes violentas"),
    # #--------------------------------------------------------------------------------------------------------------------------------#
    # path('crear_muertes_accidentes', views.RegistrarMuertesAccidentes, name = "registrar muertes accidentes"),
    # path('crear_muertes_accidentes/', views.VistaRegistrarMuertesAccidentes, name = "registrar muertes accidentes"),
    # path('editar_muertes_accidentes/<int:muertesAccidentes_id>/', views.VistaEditarMuertesAccidentes, name = "editar muertes accidentes"),
    # path('editar_muertes_accidentes/', views.EditarMuertesAccidentes, name = "editar muertes violentas"),
    # path('eliminar_muertes_accidentes/<int:muertesAccidentes_id>', views.EliminarMuertesAccidentes, name = "eliminar muertes accidentes"),
    # #--------------------------------------------------------------------------------------------------------------------------------#
    # path('crear_muertes_accidentales', views.RegistrarMuertesAccidentales, name = "registrar muertes accidentales"),
    # path('crear_muertes_accidentales/', views.VistaRegistrarMuertesAccidentales, name = "registrar muertes accidentales"),
    # path('editar_muertes_accidentales/<int:muertesAccidentales_id>/', views.VistaEditarMuertesAccidentales, name = "editar muertes accidentales"),
    # path('editar_muertes_accidentales/', views.EditarMuertesAccidentales, name = "editar muertes violentas"),
    # path('eliminar_muertes_accidentales/<int:muertesAccidentales_id>', views.EliminarMuertesAccidentales, name = "eliminar muertes accidentales"),
    # #--------------------------------------------------------------------------------------------------------------------------------#
    # path('crear_muertes_homicidio', views.RegistrarMuertesHomicidios, name = "registrar muertes homicidio"),
    # path('crear_muertes_homicidio/', views.VistaRegistrarMuertesHomicidios, name = "registrar muertes homicidio"),
    # path('editar_muertes_homicidio/<int:muertesHomicidio_id>/', views.VistaEditarMuertesHomidicios, name = "editar muertes homicidio"),
    # path('editar_muertes_homicidio/', views.EditarMuertesHomicidios, name = "editar muertes homicidio"),
    # path('eliminar_muertes_homicidio/<int:muertesHomicidio_id>', views.EliminarMuertesHomidicios, name = "eliminar muertes homicidio"),
    # #--------------------------------------------------------------------------------------------------------------------------------#
    # path('crear_muertes_suicidios', views.RegistrarMuertesSuicidios, name = "registrar muertes suicidios"),
    # path('crear_muertes_suicidios/', views.VistaRegistrarMuertesSuicidios, name = "registrar muertes suicidios"),
    # path('editar_muertes_suicidios/<int:muertesSuicidios_id>/', views.VistaEditarMuertesSuicidios, name = "editar muertes suicidios"),
    # path('editar_muertes_suicidios/', views.EditarMuertesSuicidios, name = "editar muertes suicidios"),
    # path('eliminar_muertes_suicidios/<int:muertesSuicidios_id>', views.EliminarMuertesSuicidios, name = "eliminar muertes suicidios"),
]
