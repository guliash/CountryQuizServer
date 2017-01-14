from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.models import User

class SignupTestCase(TestCase):
    def test_get__returns(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_post_correct_data__redirects_to_questions(self):
        response = self.client.post(
            reverse('users:signup'),
            {'username': 'testuser', 'password': 'test123test',
                'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)

    def test_post_not_correct_data__200(self):
        response = self.client.post(
            reverse('users:signup'),
            {'username': 'testuser', 'password': 'test',
                'email': 'test@example.com'})
        self.assertEqual(response.status_code, 200)

    def test_get_user_authenticated__redirects(self):
        user = User.objects.create_user('testuser', 'test@example.com',
                                        '123test123')
        self.client.login(username = 'testuser', password = '123test123')

        response = self.client.get(reverse('users:signup'))

        self.assertEqual(response.status_code, 302)

class SigninTestCase(TestCase):
    def test_get__returns(self):
        response = self.client.get(reverse('users:signin'))
        self.assertEqual(response.status_code, 200)

    def test_post_not_correct_data__200(self):
        response = self.client.post(reverse('users:signin'),
                                    {'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)

    def test_post_correct_data__302(self):
        user = User.objects.create_user('testuser', 'test@example.com',
                                        '123test123')

        response = self.client.post(reverse('users:signin'),
            {'username': 'testuser', 'password': '123test123'})

        self.assertEqual(response.status_code, 302)

    def test_post_correct_data_and_next__redirects_to_next(self):
        user = User.objects.create_user('testuser', 'test@example.com',
                                        '123test123')

        response = self.client.post(reverse('users:signin'),
            {'username': 'testuser', 'password': '123test123',
            'next': '/test_url/'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/test_url/')

    def test_get_user_authenticated__redirects(self):
        user = User.objects.create_user('testuser', 'test@example.com',
                                        '123test123')

        self.client.login(username = 'testuser', password = '123test123')

        response = self.client.get(reverse('users:signin'))

        self.assertEqual(response.status_code, 302)

    def test_get_user_authenticated_next__redirects_to_next(self):
        user = User.objects.create_user('testuser', 'test@example.com',
                                        '123test123')

        self.client.login(username = 'testuser', password = '123test123')

        response = self.client.get("%s?next=/test_url/" % reverse('users:signin'))

        self.assertEqual(response.status_code, 302);
        self.assertEqual(response.url, '/test_url/')

    def test_get_with_next__has_next(self):
        response = self.client.get("%s?next=/test_url/" % reverse('users:signin'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/test_url/', 1)

class LogoutTestCase(TestCase):
    def test_get__returns(self):
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
