from django.apps import AppConfig


# Import signals module to ensure signals are registered when the app is ready
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
