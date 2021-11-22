from json.decoder import JSONDecodeError

import pytest
import requests


class TestUserAuth:
    def test_user_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is no auth_sid in response1 cookie"
        assert "x-csrf-token" in response1.headers, "There is no x-csrf-token in response1 headers"
        assert "user_id" in response1.json(), "There is no user_id in response1"

        auth_sid=response1.cookies.get('auth_sid')
        csrf_token=response1.headers.get("x-csrf-token")
        user_id = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":csrf_token},
            cookies={"auth_sid":auth_sid}
        )

        assert "user_id" in response2.json(), "There is no user_id in response2"
        user_id2 = response2.json()["user_id"]
        assert user_id==user_id2, "user_id2 are different"


    def test_negative_auth_check(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is no auth_sid in response1 cookie"
        assert "x-csrf-token" in response1.headers, "There is no x-csrf-token in response1 headers"
        assert "user_id" in response1.json(), "There is no user_id in response1"

        auth_sid=response1.cookies.get('auth_sid')
        csrf_token=response1.headers.get("x-csrf-token")
        user_id = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":csrf_token},
            cookies={"auth_sid":auth_sid}
        )

        assert "user_id" in response2.json(), "There is no user_id in response2"
        user_id2 = response2.json()["user_id"]
        assert user_id==user_id2, "user_id2 are different"




