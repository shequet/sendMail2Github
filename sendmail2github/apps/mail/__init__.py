from django.apps import AppConfig


class MailAppConfig(AppConfig):
    name = 'sendmail2github.apps.mail'
    label = 'mail'
    verbose_name = 'Mail'


default_app_config = 'sendmail2github.apps.mail.MailAppConfig'
