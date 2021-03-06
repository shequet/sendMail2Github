from django.contrib.auth.models import User
from django.test import Client, TestCase
from mock import MagicMock
from sendmail2github.apps.ticket.ticket_api import TicketApi


class TestTicketApiTests(TestCase):
    """
    Class TestTicketApiTests
    """

    def setUp(self):
        """
        Test setup
        """

        self.username = 'superuser2'
        self.mail = 'superuser2@gmail.com'
        self.password = 'password1A'

        # Create super user
        self.superuser = User.objects.create_superuser(self.username, self.mail, self.password)
        self.client = Client(enforce_csrf_checks=False)
        self.client.login(
            username=self.username,
            password=self.password
        )

    def test_ticket_api_get_label(self):
        """
        Test ticket api get label
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'new'

        ticket_api = TicketApi(mock_github)

        label = ticket_api.get_label('new').return_value
        self.assertEqual(label, 'new')

    def test_ticket_api_get_or_create_label_exist(self):
        """
        Test ticket api get or create label exist
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'new'
        ticket_api = TicketApi(mock_github)

        label = ticket_api.get_or_create_label('new', '#f0f0f0').return_value
        self.assertEqual(label, 'new')

    def test_ticket_api_get_or_create_label_not_exist(self):
        """
        Test ticket api get or create label not exist
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'new'
        ticket_api = TicketApi(mock_github)

        label = ticket_api.get_or_create_label('new', '#f0f0f0').return_value
        self.assertEqual(label, 'new')

    def test_ticket_api_get_or_create_label_user(self):
        """
        Test ticket api get or create label_user
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'test@gmail.com'
        ticket_api = TicketApi(mock_github)

        user = ticket_api.get_or_create_label_user('test@gmail.com').return_value
        self.assertEqual(user, 'test@gmail.com')

    def test_ticket_api_get_or_create_label_status_new(self):
        """
        Test ticket api get or create label status new
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'Status: New'
        ticket_api = TicketApi(mock_github)

        status = ticket_api.get_or_create_label_status_new().return_value
        self.assertEqual(status, 'Status: New')

    def test_ticket_api_get_or_create_label_status_in_progress(self):
        """
        Test ticket api get or create label status in progress
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'Status: Progress'
        ticket_api = TicketApi(mock_github)

        status = ticket_api.get_or_create_label_status_in_progress().return_value
        self.assertEqual(status, 'Status: Progress')

    def test_ticket_api_create_issue(self):
        """
        Test ticket api create issue
        """

        mock_github = MagicMock()
        mock_github.get_repo().get_label().return_value = 'new'
        mock_github.get_repo().create_issue().return_value.number = 1
        ticket_api = TicketApi(mock_github)

        new_ticket = ticket_api.create_issue('title', 'body', ['new']).return_value

        self.assertEqual(new_ticket.number, 1)

    def test_ticket_api_get_ticket(self):
        """
        Test ticket api get ticket
        """
        mock_github = MagicMock()
        mock_github.get_repo().get_issue().return_value.number = 1
        mock_github.get_repo().get_issue().return_value.title = 'title'
        ticket_api = TicketApi(mock_github)

        ticket = ticket_api.get_ticket(1).return_value
        self.assertEqual(ticket.number, 1)
        self.assertEqual(ticket.title, 'title')
