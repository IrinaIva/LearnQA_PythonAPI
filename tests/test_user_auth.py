from json.decoder import JSONDecodeError

import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAuth(BaseCase):
    exclude_params = {
        'no_cookie',
        'no_token'
    }

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"User-Agent": "Some value here"}
        )

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.csrf_token = self.get_header(response1, "x-csrf-token")
        self.user_id = self.get_json_vallue(response1, "user_id")

    def test_user_auth(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.csrf_token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id,
            "user_id are different"
    )

    @pytest.mark.parametrize('condition',exclude_params)
    def test_negative_auth_check(self, condition):
        if condition=="no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": self.csrf_token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"user_id is not 0 in response, condition = {condition}"
    )



