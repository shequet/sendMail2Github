from django.core.management.base import BaseCommand
from django.conf import settings
from imap_tools import MailBox, AND
from sendmail2github.apps.ticket.ticket_api import TicketApi
from sendmail2github.apps.mail.models import MailTicket
from sendmail2github.apps.mail.notification import Notification


class Command(BaseCommand):
    """
    Class Command to recovery of incoming emails
    """

    help = 'Recovery of incoming emails'

    def handle(self, *args, **options):
        """
        Command processing
        """

        ticket_api = TicketApi()
        notification = Notification()
        ticket_api.get_or_create_label_status_in_progress()
        label_new = ticket_api.get_or_create_label_status_new()

        with MailBox(
                host=settings.IMAP_HOST,
                port=settings.IMAP_PORT
        ).login(
                settings.IMAP_USER,
                settings.IMAP_PASSWORD,
                initial_folder='INBOX',
        ) as mailbox:
            for msg in mailbox.fetch(AND(seen=False)):
                print('!!!!!!!!!!!!! Fetch')
                mid = None
                if 'message-id' in msg.headers:
                    mid = msg.headers['message-id'][0]

                if 'in-reply-to' in msg.headers:
                    mid = msg.headers['in-reply-to'][0]

                if msg.html != "":
                    body = msg.html
                else:
                    body = msg.text

                try:
                    mail_ticket = MailTicket.objects.get(mailMessageId=mid)
                    ticket = ticket_api.get_ticket(mail_ticket.githubIssueNumber)
                    ticket.create_comment(body)
                except MailTicket.DoesNotExist:
                    label_mail = ticket_api.get_or_create_label_user(mail=msg.from_)
                    new_ticket = ticket_api.create_issue(
                        title=msg.subject,
                        body=body,
                        labels=[label_new, label_mail, ]
                    )

                    mail_ticket = MailTicket()
                    mail_ticket.githubIssueNumber = new_ticket.number
                    mail_ticket.mailTitle = msg.subject
                    mail_ticket.mailMessageId = mid
                    mail_ticket.mailSenderAddress = msg.from_
                    mail_ticket.save()

                    notification.send(new_ticket.number, notification.generate_message('new'))
