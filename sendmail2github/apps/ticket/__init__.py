from django.apps import AppConfig


class TicketAppConfig(AppConfig):
    name = 'sendmail2github.apps.ticket'
    label = 'ticket'
    verbose_name = 'Ticket'


default_app_config = 'sendmail2github.apps.ticket.TicketAppConfig'
