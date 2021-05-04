from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'sendmail2github.apps.core'
    label = 'core'
    verbose_name = 'Core'

# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'sendmail2github.apps.core.AuthenticationAppConfig'
