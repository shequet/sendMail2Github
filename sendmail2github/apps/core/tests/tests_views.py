from django.test import TestCase


class TestCoreView(TestCase):
    """
    Class TestCoreView
    """

    def test_core_home_page(self):
        """
        Test core home page
        """

        response = self.client.get('/')
        self.assertContains(response, 'GitHub pour les non-développeurs')

