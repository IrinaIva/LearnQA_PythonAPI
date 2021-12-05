import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime


class TestUserEdit(BaseCase):
    def test_1_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        id = self.get_json_vallue(response1, "id")
        password = register_data['password']
        email = register_data['email']
        firstname = register_data['firstName']

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid},
                                 data={"firstName":new_name}
                                 )
        Assertions.assert_status_code(response3, 200)

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            f"Wrong name of the user after edit"
        )


    def test_2_edit_just_created_user_no_auth(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        id = self.get_json_vallue(response1, "id")
        password = register_data['password']
        email = register_data['email']
        firstname = register_data['firstName']

        #EDIT
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{id}",
                                 data={"firstName": new_name}
                                 )
        assert response3.content.decode("utf-8") == f"Auth token not supplied", f"Invalid content = {response3.content}"
        Assertions.assert_status_code(response3, 400)

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            firstname,
            f"Wrong name of the user after edit"
        )


    def test_3_edit_just_created_user_auth_as_another_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        id = self.get_json_vallue(response1, "id")
        password = register_data['password']
        email = register_data['email']
        firstname = register_data['firstName']


        # LOGIN
        login_data_of_another_user = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data_of_another_user)
        auth_sid_of_another_user = self.get_cookie(response2, "auth_sid")
        token_of_another_user = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token_of_another_user},
                                 cookies={"auth_sid": auth_sid_of_another_user},
                                 data={"firstName": new_name}
                                 )
        Assertions.assert_status_code(response3, 400)

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response5 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response5, "auth_sid")
        token = self.get_header(response5, "x-csrf-token")

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            firstname,
            f"Wrong name of the user after edit"
        )


    def test_4_edit_just_created_user_set_invalid_email(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        id = self.get_json_vallue(response1, "id")
        password = register_data['password']
        email = register_data['email']
        firstname = register_data['firstName']

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_email = self.prepare_invalid_email()
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email}
                                 )
        Assertions.assert_status_code(response3, 400)
        assert response3.content.decode("utf-8") == f"Invalid email format", f"content = {response3.content}"

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_json_value_by_name(
            response4,
            "email",
            email,
            f"Wrong email of the user after edit"
        )

    def test_5_edit_just_created_user_set_short_name(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        id = self.get_json_vallue(response1, "id")
        password = register_data['password']
        email = register_data['email']
        firstname = register_data['firstName']

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_firstName = BaseCase.generate_random_string(1)
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid},
                                 data={"firstName":new_firstName}
                                 )

        Assertions.assert_status_code(response3, 400)
        assert self.get_json_vallue(response3, "error") == f"Too short value for field firstName", f"Invalid content = {response3.content}"

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            firstname,
            f"Wrong name of the user after edit"
        )









