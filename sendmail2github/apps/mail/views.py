import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib, ssl
from email.mime.text import MIMEText
from django.conf import settings
from .models import MailTicket


def send_mail(github_issue_number, message):

    try:
        mail_ticket = MailTicket.objects.get(githubIssueNumber=github_issue_number)

        msg = MIMEText(message, 'html', 'utf-8')
        msg['Subject'] = mail_ticket.mailTitle
        msg['From'] = settings.SMTP_FROM
        msg['To'] = mail_ticket.mailSenderAddress
        msg['Message-ID'] = mail_ticket.mailMessageId
        context = ssl.create_default_context()

        if settings.SMTP_SSL == "1":
            server = smtplib.SMTP_SSL(host=settings.SMTP_HOST, port=settings.SMTP_PORT)
        else:
            server = smtplib.SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT)
        server.co
        server.ehlo()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_FROM, [mail_ticket.mailSenderAddress, ], msg.as_string())
    except MailTicket.DoesNotExist:
        pass


@csrf_exempt
def webhook(request):

    if request.method == 'POST':
        ticket = {}
        json_data = json.loads(request.body)

        action = json_data['action']
        if action == 'created':
            if json_data['issue']['number']:
                ticket = {
                    'action': json_data['action'],
                    'number': json_data['issue']['number'],
                    'repository': json_data['repository']['full_name'],
                }
            send_mail(json_data['issue']['number'], json_data['comment']['body'])
        return JsonResponse(ticket)

