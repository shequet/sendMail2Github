from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestAuthentificationView(TestCase):
    """
    Class TestAuthentificationView
    """

    def setUp(self):
        """
        Test setup
        """

        self.username = 'superuser'
        self.mail = 'superuser@gmail.com'
        self.password = 'password1AB'

        User.objects.create_superuser(self.username, self.mail, self.password)

    def test_account_login(self):
        """
        Test account login
        """

        csrf_client = Client(enforce_csrf_checks=False)
        response = csrf_client.post('/account/login/', {
            'username': self.username,
            'password': self.password,
        })

        self.assertEqual(response.status_code, 302)

    def test_account_profile(self):
        """
        Test account profile
        """

        self.client.login(
            username=self.username,
            password=self.password
        )
        response = self.client.get('/account/profile/')

        self.assertEqual(response.status_code, 200)

    def test_account_logout(self):
        """
        Test account logout
        """

        self.client.login(
            username=self.username,
            password=self.password
        )
        response = self.client.get('/account/logout/')
        self.assertContains(response, 'Cliquez ici pour vous reconnecter')
