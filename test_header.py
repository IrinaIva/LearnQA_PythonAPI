from json.decoder import JSONDecodeError

import pytest
import requests


class TestHeader:
    def test_header(self):
        response1 = requests.post("https://playground.learnqa.ru/api/homework_header")
        print(response1.cookies)
        assert "x-secret-homework-header" in response1.headers, "There is no x-secret-homework-header in response1 headers"
        expected_header = "Some secret value"
        actual_header = response1.headers.get("x-secret-homework-header")
        assert expected_header == actual_header, "Header value cookie is wrong"
