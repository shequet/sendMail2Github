import json
from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from .models import MailTicket


def sendMail(github_issue_number, message):

    mail_ticket = MailTicket.objects.get(githubIssueNumber=github_issue_number)

    if mail_ticket is not None:
        msg = MIMEText(message, 'html', 'utf-8')
        msg['Subject'] = mail_ticket.mailTitle
        msg['From'] = settings.SMTP_FROM
        msg['To'] = mail_ticket.mailSenderAddress
        msg['Message-ID'] = mail_ticket.mailMessageId

        server = smtplib.SMTP(host=settings.SMTP_HOST, port=587)
        server.set_debuglevel(True)
        server.starttls()
        server.ehlo()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_FROM, [mail_ticket.mailSenderAddress, ], msg.as_string())


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
                    #'comment': json_data['comment']['body'],
                }
            sendMail(json_data['issue']['number'], json_data['comment']['body'])
        return JsonResponse(ticket)

