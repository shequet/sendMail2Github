import json

import requests
from django.test import TestCase
from sendmail2github.apps.mail.views import webhook
import httpretty
from sendmail2github.apps.mail.models import MailTicket
import unittest.mock


class TestMailViewTests(TestCase):
    @httpretty.activate(verbose=False, allow_net_connect=False)
    def test_mail_webhook(self):
        mail_ticket = MailTicket()
        mail_ticket.mailTitle = "Test"
        mail_ticket.mailMessageId = '123456'
        mail_ticket.mailSenderAddress = 'test@example.com'
        mail_ticket.githubIssueNumber = 1
        mail_ticket.save()

        httpretty.register_uri(
            uri="http://127.0.0.1/",
            method='POST',
            status=200,)

        requests.post('http://127.0.0.1/', data=json.dumps({
              "action": "created",
              "issue": {
                "number": 1
              },
              "comment": {
                "body": "User: test@example.com<br><br>Comment ticket",
              },
              "repository": {
                "full_name": "shequet/sendMail2Github"
              }
            }))

        with unittest.mock.patch("smtplib.SMTP", autospec=True) as mock_smtp:
            result = webhook(httpretty.last_request())
            mock_smtp.assert_called()
            mock_smtp.return_value.__enter__.return_value

            self.assertEqual(len(result.content), len(json.dumps({
                    'action': 'created',
                    'number': 1,
                    'repository': "shequet/sendMail2Github",
                })))



