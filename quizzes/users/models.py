from django.db import models
from django.contrib.auth.models import User

def create_user(username, email, password):
    return User.objects.create_user(username, email, password)
