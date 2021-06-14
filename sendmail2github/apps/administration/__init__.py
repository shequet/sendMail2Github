from django.apps import AppConfig


class AdministrationAppConfig(AppConfig):
    """
    Class AdministrationAppConfig
    """

    name = 'sendmail2github.apps.administration'
    label = 'administration'
    verbose_name = 'Administration'


default_app_config = 'sendmail2github.apps.administration.AdministrationAppConfig'
