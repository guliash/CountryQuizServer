from django.test import TestCase
from .forms import SignupForm

class SignupFormTestCase(TestCase):

    def test_empty_name__not_valid(self):
        data = {'name':'', 'email': 'test@example.com', 'password': 'test'}
        self.assertFalse(SignupForm(data).is_valid())

    def test_empty_email__not_valid(self):
        data = {'name': 'test', 'email': '', 'password': 'test'}
        self.assertFalse(SignupForm(data).is_valid())

    def test_empty_password__not_valid(self):
        data = {'name': 'test', 'email': 'test@example.com', 'password': ''}
        self.assertFalse(SignupForm(data).is_valid())

    def test_bad_email__not_valid(self):
        data = {'name': 'test', 'email': '@example.com', 'password': 'test'}
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('email', 'invalid'))
