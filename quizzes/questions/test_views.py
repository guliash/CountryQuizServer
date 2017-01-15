from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User, Group, Permission

from .models import Question
from users import test_utils

from quizzes.settings import MEDIA_ROOT

import os

TEST_IMAGE_PATH = MEDIA_ROOT + 'test/test.png'

class CreateTestCase(TestCase):
    def setUp(self):
        group = Group.objects.create(name='questions_moderators')
        group.permissions.add(Permission.objects.get(codename='add_question'))
        group.save()

    def test_get_user_has_permission__200(self):
        user = self.create_moderator_user_and_login()

        response = self.client.get(reverse('questions:create'))

        self.assertEqual(response.status_code, 200)

    def test_get_user_has_no_permission__403(self):
        user = test_utils.create_and_login_test_user(self.client)

        response = self.client.get(reverse('questions:create'))

        self.assertEqual(response.status_code, 403)

    def test_post__creates(self):
        user = self.create_moderator_user_and_login()

        response = self.client.post(reverse('questions:create'), {'name': 'test_name', 'description': 'test_description', 'image': testImage()})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('questions:question', args=[1]))
        self.assertEqual(Question.objects.count(), 1)
        question = Question.objects.get(id=1)
        self.assertEqual(question.name, 'test_name')
        self.assertEqual(question.description, 'test_description')
        removeTestImage(question.image.name)

    def create_moderator_user_and_login(self):
        user = test_utils.create_and_login_test_user(self.client)
        self.add_to_moderators(user)

    def add_to_moderators(self, user):
        group = Group.objects.get(name='questions_moderators')
        user.groups.add(group)

class ViewTestCase(TestCase):

    def test_question_not_exists__not_found(self):
        user = test_utils.create_and_login_test_user(self.client)

        question = createQuestion('name', 'description', timezone.now(), 'image')

        response = self.client.get(reverse('questions:question', args=[2]))
        self.assertEqual(response.status_code, 404)
        removeTestImage(question.image.name)

    def test_question_exists__returns(self):
        user = test_utils.create_and_login_test_user(self.client)
        question = createQuestion('name', 'description', timezone.now(), 'test')

        response = self.client.get(reverse('questions:question', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.name)
        self.assertContains(response, question.description)

        removeTestImage(question.image.name)

class ViewAllTestCase(TestCase):
    def test__shows_all_questions(self):
        user = test_utils.create_and_login_test_user(self.client)

        question1 = createQuestion('first', 'first_desc', timezone.now(), 'first')
        question2 = createQuestion('second', 'second_desc', timezone.now(), 'second')

        response = self.client.get(reverse('questions:all'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question1.name)
        self.assertContains(response, question1.description)
        self.assertContains(response, question2.name)
        self.assertContains(response, question2.description)
        removeTestImage(question1.image.name)
        removeTestImage(question2.image.name)

def createQuestion(name, description, publish_date, image_name):
    image = SimpleUploadedFile(name=image_name, content=testImage().read(), content_type='image/png')
    question = Question(name=name, description=description, publish_date=publish_date, image=image)
    question.save()
    return question

def testImage():
    return open(TEST_IMAGE_PATH, 'rb')

def removeTestImage(image_name):
    path = MEDIA_ROOT + image_name;
    if os.path.exists(path):
        os.remove(path)
