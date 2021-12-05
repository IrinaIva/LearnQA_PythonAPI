from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in the json format, response text is {response.text}"

        assert name in response_as_dict, f"Response json does not have key {name}"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in the json format, response text is {response.text}"

        assert name in response_as_dict, f"Response json does not have key {name}"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in the json format, response text is {response.text}"
        for name in names:
            assert name in response_as_dict, f"Response json does not have key {name}"

    @staticmethod
    def assert_json_has_no_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in the json format, response text is {response.text}"
        for name in names:
            assert name not in response_as_dict, f"Response json has key {name}"

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in the json format, response text is {response.text}"

        assert name not in response_as_dict, f"Response json has key {name}"

    @staticmethod
    def assert_status_code(response: Response, expected):
        assert response.status_code == expected, \
            f"Unexpected status_code {response.status_code}, expected {expected}"



