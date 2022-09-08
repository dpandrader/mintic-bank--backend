from email.policy import default
from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default = False
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authApp'
