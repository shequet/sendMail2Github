from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    """
    Class AuthenticationAppConfig
    """

    name = 'sendmail2github.apps.core'
    label = 'core'
    verbose_name = 'Core'


default_app_config = 'sendmail2github.apps.core.AuthenticationAppConfig'
