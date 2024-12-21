from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'nombre', 'apellido_paterno', 'access_to_app', 'is_active', 'is_staff')
    search_fields = ('username', 'nombre', 'apellido_paterno')
    list_filter = ('is_active', 'access_to_app')

    # Muestra los permisos en el formulario de edición de usuario
    filter_horizontal = ('amigos',)

# Registra el modelo Usuario con el UsuarioAdmin
admin.site.register(Usuario, UsuarioAdmin)