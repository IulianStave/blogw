#python3 manage.py startapp users
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #import signal
    def ready(self):
        import users.signals
