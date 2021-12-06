import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
from lib.my_requests import MyRequests


class TestUserDelete(BaseCase):

    def test_delete_not_allowed_user(self):

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        #DELETE
        new_name = "Changed Name"
        response2 = MyRequests.delete(f"/user/2",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid}
                                 )

        Assertions.assert_status_code(response2, 400)
        assert response2.content.decode("utf-8") == f"Please, do not delete test users with ID 1, 2, 3, 4 or 5.", f"Invalid content = {response3.content}"

        #GET
        response3 = MyRequests.get(f"/user/2",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_status_code(response3, 200)
        keys = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response3, keys)

    def test_delete_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
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
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        new_name = "Changed Name"
        response2 = MyRequests.delete(f"/user/{id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_status_code(response2, 200)

        #GET
        response3 = MyRequests.get(f"/user/{id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_status_code(response3, 404)
        assert response3.content.decode("utf-8") == f"User not found", f"User is found = {response3.content}"

    @pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
    def test_delete_just_created_user_auth_as_another_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)
        Assertions.assert_status_code(response1, 200)
        Assertions.assert_json_has_key(response1, "id")
        id = self.get_json_vallue(response1, "id")

        # LOGIN
        login_data_of_another_user = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data_of_another_user)
        auth_sid_of_another_user = self.get_cookie(response2, "auth_sid")
        token_of_another_user = self.get_header(response2, "x-csrf-token")

        #DELETE
        response3 = MyRequests.delete(f"/user/{id}",
                                 headers={"x-csrf-token": token_of_another_user},
                                 cookies={"auth_sid": auth_sid_of_another_user}
                                 )
        Assertions.assert_status_code(response3, 400)

        #GET
        response4 = MyRequests.get(f"/user/{id}",
                                 headers={"x-csrf-token": token_of_another_user},
                                 cookies={"auth_sid": auth_sid_of_another_user}
                                 )
        Assertions.assert_json_has_key(response4, "username")
        keys = ["email", "firstName", "lastName", "password"]
        Assertions.assert_json_has_no_keys(response4, keys)
