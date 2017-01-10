from django.test import TestCase
from django.urls import reverse

class SignupTestCase(TestCase):
    def test_getSignupView__returns200(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

class SigninTestCase(TestCase):
    def test_getSigninView__returns200(self):
        response = self.client.get(reverse('users:signin'))
        self.assertEqual(response.status_code, 200)

class LogoutTestCase(TestCase):
    def test_getLogoutView_returns200(self):
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
