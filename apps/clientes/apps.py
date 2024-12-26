from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.clientes'

    def ready(self):
        import apps.clientes.signals  # Importa las señales al iniciar la aplicación
