from django.apps import AppConfig


class DireccionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'direccion'
    
    def ready(self):
        import direccion.signals  # Importar las señales de la aplicación correcta
