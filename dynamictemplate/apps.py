from django.apps import AppConfig


class DynamictemplateConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamictemplate'

    def ready(self):
        import dynamictemplate.signals