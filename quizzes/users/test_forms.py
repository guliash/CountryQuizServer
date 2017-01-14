from django.test import TestCase
from .forms import SignupForm

class SignupFormTestCase(TestCase):

    def test_empty_name__not_valid(self):
        data = {'username':'', 'email': 'test@example.com', 'password': 'test123'}
        self.assertFalse(SignupForm(data).is_valid())

    def test_empty_email__not_valid(self):
        data = {'username': 'test', 'email': '', 'password': 'test'}
        self.assertFalse(SignupForm(data).is_valid())

    def test_empty_password__not_valid(self):
        data = {'username': 'test', 'email': 'test@example.com', 'password': ''}
        self.assertFalse(SignupForm(data).is_valid())

    def test_bad_email__not_valid(self):
        data = {'username': 'test', 'email': '@example.com', 'password': 'test123'}
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('email', 'invalid'))

    def test_short_password__not_valid(self):
        data = {'username': 'test', 'email': 'test@example.com', 'password': 'test'}
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('password', 'password_too_short'))

    def test_only_digits_password__not_valud(self):
        data = {'username': 'test', 'email': 'test@example.com', 'password': '123'}
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('password', 'password_entirely_numeric'))

    def test_common_password__not_valid(self):
        data = {'username': 'test', 'email': 'test@example.com', 'password': 'password'}
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('password', 'password_too_common'))
