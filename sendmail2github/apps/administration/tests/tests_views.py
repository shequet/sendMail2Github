from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestAdministrationView(TestCase):
    def setUp(self):
        self.username = 'superuser2'
        self.mail = 'superuser2@gmail.com'
        self.password = 'password1A'

        # Create super user
        User.objects.create_superuser(self.username, self.mail, self.password)
        self.client = Client(enforce_csrf_checks=False)
        self.client.login(
            username=self.username,
            password=self.password
        )

    def test_admin_add_page(self):
        response = self.client.get('/admin/add/')
        self.assertContains(response, 'Ajouter un utilisateur')

    def test_admin_add_user(self):
        response = self.client.post('/admin/add/', {
            'email': 'user1@gmail.com',
            'username': 'user1',
            'password1': self.password,
            'password2': self.password,
            'is_active': 1,
            'is_superuser': 0
        })
        self.assertEqual(response.status_code, 302)

    def test_admin_add_user_password_error(self):
        response = self.client.post('/admin/add/', {
            'email': 'user2@gmail.com',
            'username': 'user2',
            'password1': 'aa',
            'password2': 'bb',
            'is_active': 1,
            'is_superuser': 0
        })
        self.assertContains(response, 'Les deux mots de passe ne correspondent pas')
