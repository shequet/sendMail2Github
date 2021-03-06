from django.contrib.auth.models import User
from django.test import Client, TestCase


class TestAdministrationViewTests(TestCase):
    """
    Class TestAdministrationViewTests
    """

    def setUp(self):
        """
        setUp Test
        """

        self.username = 'superuser2'
        self.mail = 'superuser2@gmail.com'
        self.password = 'password1A'

        self.superuser = User.objects.create_superuser(self.username, self.mail, self.password)
        self.client = Client(enforce_csrf_checks=False)
        self.client.login(
            username=self.username,
            password=self.password
        )

    def test_admin_add_page(self):
        """
        Test admin add page
        """

        response = self.client.get('/admin/add/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ajouter un utilisateur')

    def test_admin_add_user(self):
        """
        Test admin add user
        """

        response = self.client.post('/admin/add/', {
            'email': 'user1@gmail.com',
            'username': 'user1',
            'password1': self.password,
            'password2': self.password,
            'is_active': 1,
            'is_superuser': 0
        })
        self.assertEqual(response.status_code, 302)

    def test_admin_show_user(self):
        """
        Test admin show user
        """

        response = self.client.post('/admin/{user_id}'.format(user_id=self.superuser.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username)

    def test_admin_show_user_not_exist(self):
        """
        Test admin show user not exist
        """

        response = self.client.post('/admin/99999999')
        self.assertEqual(response.status_code, 200)

    def test_admin_add_user_password_error(self):
        """
        Test admin add user password error
        """

        response = self.client.post('/admin/add/', {
            'email': 'user2@gmail.com',
            'username': 'user2',
            'password1': 'aa',
            'password2': 'bb',
            'is_active': 1,
            'is_superuser': 0
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Les deux mots de passe ne correspondent pas')

    def test_admin_edit_user_get(self):
        """
        Test admin edit user get
        """

        response = self.client.get('/admin/edit/{user_id}'.format(user_id=self.superuser.id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username)

    def test_admin_edit_user_post(self):
        """
        Test admin edit user post
        """

        response = self.client.post('/admin/edit/{user_id}'.format(user_id=self.superuser.id), {
            'email': 'superuser3@gmail.com',
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'is_active': 1,
            'is_superuser': 0
        })
        self.assertEqual(response.status_code, 302)

    def test_admin_edit_user_post_not_valid(self):
        """
        Test admin edit user post not valid
        """

        response = self.client.post('/admin/edit/{user_id}'.format(user_id=self.superuser.id), {
            'email': 'superuser3@gmail.com',
            'username': self.username,
            'password1': '1',
            'password2': '2',
            'is_active': 1,
            'is_superuser': 0
        })
        self.assertEqual(response.status_code, 200)

    def test_admin_index_page(self):
        """
        Test admin index page
        """

        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_user_exist(self):
        """
        Test admin delete user exist
        """

        response = self.client.get('/admin/delete/{user_id}'.format(user_id=self.superuser.id))
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_user_not_exist(self):
        """
        Test admin delete user not exist
        """

        response = self.client.get('/admin/delete/9999999')
        self.assertEqual(response.status_code, 200)
