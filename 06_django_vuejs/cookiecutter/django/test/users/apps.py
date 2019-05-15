from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "test.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import test.users.signals  # noqa F401
        except ImportError:
            pass
