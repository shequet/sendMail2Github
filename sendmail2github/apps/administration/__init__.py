from django.apps import AppConfig


class AdministrationAppConfig(AppConfig):
    name = 'sendmail2github.apps.administration'
    label = 'administration'
    verbose_name = 'Administration'


default_app_config = 'sendmail2github.apps.administration.AdministrationAppConfig'
