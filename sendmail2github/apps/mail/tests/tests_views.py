import json
import requests
import unittest.mock
from django.test import TestCase
import httpretty
from sendmail2github.apps.mail.models import MailTicket
from sendmail2github.apps.mail.views import webhook


class TestMailViewTests(TestCase):
    """
    Class TestMailViewTests
    """

    @httpretty.activate(verbose=False, allow_net_connect=False)
    def test_mail_webhook_created(self):
        """
        Test mail webhook created
        """

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

            self.assertEqual(len(result.content), len(json.dumps({
                    'action': 'created',
                    'number': 1,
                    'repository': "shequet/sendMail2Github",
                })))

    @httpretty.activate(verbose=False, allow_net_connect=False)
    def test_mail_webhook_labeled(self):
        """
        Test mail webhook labeled
        """

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
              "action": "labeled",
              "issue": {
                "number": 1
              },
              "label": {
                "name": "buf",
                "color": "d73a4a"
              },
              "repository": {
                "full_name": "shequet/sendMail2Github"
              }
            }))

        with unittest.mock.patch("smtplib.SMTP", autospec=True) as mock_smtp:
            result = webhook(httpretty.last_request())
            mock_smtp.assert_called()

            self.assertEqual(len(result.content), len(json.dumps({
                    'action': 'labeled',
                    'number': 1,
                    'repository': "shequet/sendMail2Github",
                })))

    @httpretty.activate(verbose=False, allow_net_connect=False)
    def test_mail_webhook_closed(self):
        """
        Test mail webhook closed
        """

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
              "action": "closed",
              "issue": {
                "number": 1
              },
              "comment": {
                "body": "Nous avons corrigé le problème",
              },
              "repository": {
                "full_name": "shequet/sendMail2Github"
              }
            }))

        with unittest.mock.patch("smtplib.SMTP", autospec=True) as mock_smtp:
            result = webhook(httpretty.last_request())
            mock_smtp.assert_called()

            self.assertEqual(len(result.content), len(json.dumps({
                    'action': 'closed',
                    'number': 1,
                    'repository': "shequet/sendMail2Github",
                })))

    @httpretty.activate(verbose=False, allow_net_connect=False)
    def test_mail_webhook_none(self):
        """
        Test mail webhook none
        """

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
              "action": "other",
              "issue": {
                "number": 1
              },
              "comment": {
                "body": "Nous avons corrigé le problème",
              },
              "repository": {
                "full_name": "shequet/sendMail2Github"
              }
            }))

        with unittest.mock.patch("smtplib.SMTP", autospec=True) as mock_smtp:
            result = webhook(httpretty.last_request())

            self.assertEqual(len(result.content), len(json.dumps({
                    'action': 'other',
                    'number': 1,
                    'repository': "shequet/sendMail2Github",
                })))

    @httpretty.activate(verbose=False, allow_net_connect=False)
    def test_mail_webhook_get_is_none(self):
        """
        Test mail webhook get is none
        """

        httpretty.register_uri(
            uri="http://127.0.0.1/",
            method='GET',
            status=200,)

        requests.get('http://127.0.0.1/')

        result = webhook(httpretty.last_request())
        self.assertIsNone(result)
