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

