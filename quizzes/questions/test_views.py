from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Question
from quizzes.settings import MEDIA_ROOT

import os

TEST_IMAGE_PATH = MEDIA_ROOT + 'test/test.png'

class CreateTestCase(TestCase):

    def test_get__returns(self):
        response = self.client.get(reverse('questions:create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create question')

    def test_post__creates(self):
        response = self.client.post(reverse('questions:create'), {'name': 'test_name', 'description': 'test_description', 'image': testImage()})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('questions:question', args=[1]))
        self.assertEqual(Question.objects.count(), 1)
        question = Question.objects.get(id=1)
        self.assertEqual(question.name, 'test_name')
        self.assertEqual(question.description, 'test_description')
        removeTestImage(question.image.name)


class ViewTestCase(TestCase):

    def test_question_not_exists__not_found(self):
        question = createQuestion('name', 'description', timezone.now(), 'image')
        question.save()
        response = self.client.get(reverse('questions:question', args=[2]))
        self.assertEqual(response.status_code, 404)
        removeTestImage(question.image.name)

    def test_question_exists__returns(self):
        question = createQuestion('name', 'description', timezone.now(), 'test')
        question.save()
        response = self.client.get(reverse('questions:question', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.name)
        self.assertContains(response, question.description)
        removeTestImage(question.image.name)

class ViewAllTestCase(TestCase):
    def test__shows_all_questions(self):
        question1 = createQuestion('first', 'first_desc', timezone.now(), 'first')
        question2 = createQuestion('second', 'second_desc', timezone.now(), 'second')
        question1.save()
        question2.save()

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
    return Question(name=name, description=description, publish_date=publish_date, image=image)

def testImage():
    return open(TEST_IMAGE_PATH, 'rb')

def removeTestImage(image_name):
    path = MEDIA_ROOT + image_name;
    if os.path.exists(path):
        os.remove(path)
