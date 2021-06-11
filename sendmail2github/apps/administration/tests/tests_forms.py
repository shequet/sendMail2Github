from django.test import TestCase
from sendmail2github.apps.administration.forms import CustomUserCreationForm


class AddUserFormTests(TestCase):
    def test_user_form(self):
        form = CustomUserCreationForm()

        self.assertTrue(form.fields["email"])
        self.assertTrue(form.fields["username"])
        self.assertTrue(form.fields["password1"])
        self.assertTrue(form.fields["password2"])

    def test_user_submit_form(self):
        form = CustomUserCreationForm(data={'email': ''})

        self.assertEqual(form.errors["email"], ["Ce champ est obligatoire."])
        self.assertEqual(form.errors["username"], ["Ce champ est obligatoire."])
        self.assertEqual(form.errors["password1"], ["Ce champ est obligatoire."])
        self.assertEqual(form.errors["password2"], ["Ce champ est obligatoire."])
