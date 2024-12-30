from django.apps import AppConfig


class Adminv2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.adminv2'

    def ready(self):
        import apps.adminv2.signals.grupos