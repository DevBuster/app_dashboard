from django.contrib import admin
from .models import MuertesViolentas, MuertesAccidentes, MuertesAccidentales, MuertesHomicidios, MuertesSuicidios
# Register your models here.

admin.site.register(MuertesViolentas)
admin.site.register(MuertesAccidentes)
admin.site.register(MuertesAccidentales)
admin.site.register(MuertesHomicidios)
admin.site.register(MuertesSuicidios)