from django.apps import AppConfig


class VideostreamAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videostreamApp'
    def ready(self):
        from . import singals
