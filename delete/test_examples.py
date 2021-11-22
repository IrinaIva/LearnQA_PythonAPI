class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        expected = 14
        assert a + b == expected, f"Exp not eq to {expected}"

    def test_check_math2(self):
        a = 5
        b = 11
        expected = 14
        assert a + b == expected, f"Exp not eq to {expected}"
