from django.apps import AppConfig


class LoggingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.logging_app'

    def ready(self):
        import apps.logging_app.signals  # Импортируйте здесь, чтобы сигналы были зарегистрированы