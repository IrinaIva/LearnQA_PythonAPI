import json.decoder
import random
import string

from requests import Response


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookie {cookie_name} in response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find header {header_name} in response"
        return response.headers[header_name]

    def get_json_vallue(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in the json format, response text is {response.text}"

        assert name in response_as_dict, f"Response json does not have key {name}"

        return response_as_dict[name]

    def generate_random_string(length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string
