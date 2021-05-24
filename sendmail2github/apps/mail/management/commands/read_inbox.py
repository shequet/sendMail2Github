from django.core.management.base import BaseCommand
from django.conf import settings
from imap_tools import MailBox, AND
from sendmail2github.apps.ticket.ticket_api import TicketApi


class Command(BaseCommand):
    """
    Command to recovery of incoming emails
    """

    help = 'Recovery of incoming emails'

    def handle(self, *args, **options):
        """
        Command processing
        """

        ticket_api = TicketApi()
        ticket_api.get_or_create_label_status_in_progress()
        label_new = ticket_api.get_or_create_label_status_new()

        with MailBox(settings.IMAP_HOST).login(
                settings.IMAP_USER,
                settings.IMAP_PASSWORD,
                initial_folder='INBOX'
        ) as mailbox:

            for msg in mailbox.fetch(AND(seen=False)):

                if msg.html != "":
                    body = msg.html
                else:
                    body = msg.text
                label_mail = ticket_api.get_or_create_label_user(mail=msg.from_)
                ticket_api.create_issue(
                    title=msg.subject,
                    body=body,
                    labels=[label_new, label_mail, ]
                )
