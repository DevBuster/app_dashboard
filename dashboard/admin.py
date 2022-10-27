from django.contrib import admin
from .models import muertesViolentas
from .models import muertesAccidentes
from .models import muertesAccidentales
from .models import homicidios
from .models import suicidios
# Register your models here.

admin.site.register(muertesViolentas)
admin.site.register(muertesAccidentes)
admin.site.register(muertesAccidentales)
admin.site.register(homicidios)
admin.site.register(suicidios)