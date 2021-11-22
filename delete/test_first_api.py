from json.decoder import JSONDecodeError

import pytest
import requests

class TestFirstAPI:
    names = [
        "Irina",
        ""
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, f"Status code is not 200, it is {response.status_code}"
        response_dict = response.json()
        assert "answer" in response_dict, "There is no 'answer' in response_dict"
        if len(name) == 0:
            name = "someone"
        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict['answer']
        assert expected_response_text == actual_response_text, f"Response answer is wrong"
