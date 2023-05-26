from django.apps import AppConfig


class AccountAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account_app'

    def ready(self):
        import account_app.signals

