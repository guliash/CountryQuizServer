from django.db import models

class Question(models.Model):
    name = models.TextField()
    publish_date = models.DateTimeField()
    description = models.TextField(default='')
    image = models.ImageField(upload_to='images/')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    correct = models.BooleanField()

