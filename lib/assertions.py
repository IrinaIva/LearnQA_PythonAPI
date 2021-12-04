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



