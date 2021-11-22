from json.decoder import JSONDecodeError

import pytest
import requests

class TestPhrase:
    def test_phrase(self):

        phrase = input("Set a phrase with less than 15 symbols length: ")
        assert len(phrase) < 15, "Entered phrase length is higher than 15 symbols."
