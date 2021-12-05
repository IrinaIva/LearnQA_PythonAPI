import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.invalid_email = f"{base_part}{random_part}{domain}"
        self.invalid_short_name = BaseCase.generate_random_string(1)
        self.invalid_long_name = BaseCase.generate_random_string(260)

    params = {
        'email',
        'username',
        'firstName',
        'lastName',
        'password'
    }

    def test_create_user_successfully(self):
        data = {
            'email': self.email,
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_json_has_key(response, "id")
        Assertions.assert_status_code(response, 200)

    def test_create_user_with_existing_email(self):
        email='vinkotov@example.com'
        data = {
            'email': email,
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"content = {response.content}"

    def test_create_user_invalid_email(self):
        data = {
            'email': self.invalid_email,
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"content = {response.content}"

    @pytest.mark.parametrize('condition', params)
    def test_create_user_missing_field(self, condition):

        data = {
            'email': self.email,
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234'
        }
        if condition == "email":
            del data['email']
        elif condition == "username":
            del data['username']
        elif condition == "firstName":
            del data['firstName']
        elif condition == "lastName":
            del data['lastName']
        elif condition == "password":
            del data['password']
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {condition}"

    def test_create_user_invalid_short_name(self):
        data = {
            'email': self.email,
            'username': self.invalid_short_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too short", f"Invalid content = {response.content}"

    def test_create_user_invalid_long_name(self):
        data = {
            'email': self.email,
            'username': self.invalid_long_name,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_status_code(response, 400)
        assert response.content.decode(
            "utf-8") == "The value of 'username' field is too long", f"Invalid content = {response.content}"



