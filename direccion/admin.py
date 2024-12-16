from django.contrib import admin
from .models import Estado, Municipio,CodigoPostal,Colonia


admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(CodigoPostal)
admin.site.register(Colonia)
# Register your models here.
