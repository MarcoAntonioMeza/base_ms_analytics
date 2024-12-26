from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Cliente  # Asegúrate de que este modelo sea el correcto

@receiver(post_migrate)
def crear_permisos_personalizados(sender, **kwargs):
    #print("Señal post_migrate recibida.")
    #print(sender.name, 'es el remitente.')
    #if sender.name == "apps.clientes":  # Asegúrate de usar el nombre correcto de tu app
    #    pass
    content_type = ContentType.objects.get_for_model(Cliente)
    permisos = [
        ("can_view_cliente", "VER USUARIO"),
        ("can_update_cliente", "ACTUALIZAR USUARIO"),
        ("can_create_cliente", "CREAR USUARIO"),
        ("can_delete_cliente", "ELIMINAR USUARIO"),
    ]
    for codename, name in permisos:
        permiso, created = Permission.objects.get_or_create(
            codename=codename,
            name=name,
            content_type=content_type,
        )
        if created:
            print(f"Permiso '{name}' creado automáticamente.")
