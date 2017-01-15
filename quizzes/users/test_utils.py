from .models import create_user

USERNAME = 'testuser'
EMAIL = 'test@example.com'
PASSWORD = '123test123'

def create_test_user():
    return create_user(USERNAME, EMAIL, PASSWORD)

def create_and_login_test_user(client):
    user = create_test_user()
    client.login(username = USERNAME, password = PASSWORD)
    return user
