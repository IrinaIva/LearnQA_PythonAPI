from json.decoder import JSONDecodeError

import pytest
import requests


class TestCookie:
    def test_cookie(self):
        response1 = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        print(response1.cookies)
        assert "HomeWork" in response1.cookies, "There is no HomeWork in response1 cookie"
        expected_homeWork = "hw_value"
        actual_homeWork = response1.cookies.get('HomeWork')
        assert expected_homeWork == actual_homeWork, "HomeWork cookie is wrong"
