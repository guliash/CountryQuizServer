from django.test import TestCase
from .forms import SignupForm

class SignupFormTestCase(TestCase):

    def test_empty_name__not_valid(self):
        data = {'name':'', 'email': 'test@example.com', 'password': 'test'}
        self.assertFalse(SignupForm(data).is_valid())
