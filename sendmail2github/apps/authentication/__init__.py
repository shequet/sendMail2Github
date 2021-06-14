from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'sendmail2github.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'


default_app_config = 'sendmail2github.apps.authentication.AuthenticationAppConfig'
