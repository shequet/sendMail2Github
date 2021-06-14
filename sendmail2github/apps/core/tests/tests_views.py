from django.test import TestCase


class TestCoreView(TestCase):

    def test_core_home_page(self):
        response = self.client.get('/')
        self.assertContains(response, 'GitHub pour les non-développeurs')

