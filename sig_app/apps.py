from django.apps import AppConfig


class SigAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sig_app'

    def ready(self):
        import sig_app.signals
