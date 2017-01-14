from .models import create_user

USERNAME = 'testuser'
EMAIL = 'test@example.com'
PASSWORD = '123test123'

def create_test_user():
    return create_user(USERNAME, EMAIL, PASSWORD)
