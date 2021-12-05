import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserGet(BaseCase):
    class TestUserRegister(BaseCase):
        def setup(self):
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            self.email = f"{base_part}{random_part}@{domain}"

    def test_get_user_details_not_auth(self):
        response = requests.get(f"https://playground.learnqa.ru/api/user/2")
        Assertions.assert_json_has_key(response, "username")
        keys = ["email", "firstName", "lastName", "password"]
        Assertions.assert_json_has_no_keys(response, keys)

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        id = self.get_json_vallue(response1, "user_id")
        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid}
                                 )
        keys = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, keys)


    def test_get_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        id = 1
        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid}
                                 )
        Assertions.assert_json_has_key(response2, "username")
        keys = ["email", "firstName", "lastName", "password"]
        Assertions.assert_json_has_no_keys(response2, keys)










