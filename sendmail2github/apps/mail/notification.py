import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from .models import MailTicket


class Notification:

    def generate_message(self, action, json_data=None):

        if action == 'new':
            return 'Bonjour,<br>' \
                      'Nous avons bien pris en compte votre demande<br>' \
                      'Cordialement,<br>' \
                      'Le service support'
        elif action == 'created':
            return 'Bonjour,<br>un commentaire a été ajouté : <hr>{comment}'.format(
                comment=json_data['comment']['body'])

        elif action == 'labeled':
            return 'Bonjour,<br>Votre ticket {number} à changé d\'état <b>{stat}</b>.'.format(
                number=json_data['issue']['number'],
                stat=json_data['label']['name'])

        elif action == 'closed':
            comment = ''
            if 'comment' in json_data:
                comment = json_data['comment']['body']
            return 'Bonjour,<br>Votre ticket {number} est <b>terminé</b><hr>{comment}.'.format(
                number=json_data['issue']['number'],
                comment=comment)

        return None

    def send(self, number, message):

        try:
            mail_ticket = MailTicket.objects.get(githubIssueNumber=number)

            msg = MIMEText(message, 'html', 'utf-8')
            msg['Subject'] = mail_ticket.mailTitle
            msg['From'] = settings.SMTP_FROM
            msg['To'] = mail_ticket.mailSenderAddress
            msg['Message-ID'] = mail_ticket.mailMessageId

            if settings.SMTP_SSL == "1":
                server = smtplib.SMTP_SSL(host=settings.SMTP_HOST, port=settings.SMTP_PORT)
            else:
                server = smtplib.SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT)

            server.ehlo()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.sendmail(settings.SMTP_FROM, [mail_ticket.mailSenderAddress, ], msg.as_string())
        except MailTicket.DoesNotExist:
            pass
