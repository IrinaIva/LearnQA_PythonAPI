from json.decoder import JSONDecodeError

import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAgent(BaseCase):
    exclude_params = {
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }


    @pytest.mark.parametrize('condition',exclude_params)
    def test_user_auth_check_platform(self, condition):
        responseM = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                 headers={
                                     "User-Agent": condition}
                                 )
        # user_agent = BaseCase.get_json_vallue(responseM, "user_agent")
        # print(user_agent)

        if "Mobile" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "platform",
                "Mobile",
                f"platform is not Mobile in response, condition = {condition}"
            )
        elif "Googlebot" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "platform",
                "Googlebot",
                f"platform is not Googlebot in response, condition = {condition}"
            )
        elif "Windows" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "platform",
                "Web",
                f"platform is not Web in response, condition = {condition}"
            )
        else:
            Assertions.assert_json_value_by_name(
                responseM,
                "platform",
                "Unknown",
                f"platform is not Unknown in response, condition = {condition}"
            )


    @pytest.mark.parametrize('condition', exclude_params)
    def test_user_auth_check_device(self, condition):
        responseM = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                 headers={
                                     "User-Agent": condition}
                                 )

        if "Android" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "device",
                "Android",
                f"device is not Android in response, condition = {condition}"
            )
        elif "iPhone" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "device",
                "iPhone",
                f"device is not iPhone in response, condition = {condition}"
            )
        elif "iPad" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "device",
                "iOS",
                f"device is not iOS in response, condition = {condition}"
            )
        elif "Edg" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "device",
                "No",
                f"device is not No in response, condition = {condition}"
            )
        else:
            Assertions.assert_json_value_by_name(
                responseM,
                "device",
                "Unknown",
                f"device is not Unknown in response, condition = {condition}"
            )


    @pytest.mark.parametrize('condition', exclude_params)
    def test_user_auth_check_browser(self, condition):
        responseM = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                 headers={
                                     "User-Agent": condition}
                                 )

        if "Chrome" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "browser",
                "Chrome",
                f"browser is not Chrome in response, condition = {condition}"
            )
        elif "CriOS" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "browser",
                "Chrome",
                f"browser is not Chrome in response, condition = {condition}"
            )
        elif "like Gecko" in condition:
            Assertions.assert_json_value_by_name(
                responseM,
                "browser",
                "No",
                f"browser is not No in response, condition = {condition}"
            )
        else:
            Assertions.assert_json_value_by_name(
                responseM,
                "browser",
                "Unknown",
                f"browser is not Unknown in response, condition = {condition}"
            )
