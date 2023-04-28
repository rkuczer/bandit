import re
import unittest

from bandit.plugins.general_hardcoded_password import RE_CANDIDATES
from bandit.plugins.general_hardcoded_password import RE_WORDS


class TestRegex(unittest.TestCase):
    def test_valid_input(self):
        regex = re.compile(RE_CANDIDATES)
        valid_inputs = [
            "password",
            "passphrase",
            "pwd",
            "secrete",
            "pass",
            "token",
            "conn",
        ]
        for input_str in valid_inputs:
            with self.subTest(input_str=input_str):
                self.assertIsNotNone(regex.search(input_str))


class MyTestCase(unittest.TestCase):
    def test_complete_words(self):
        test_strings = [
            "passwords",
            "secretpassword",
            "pword",
            "secret",
            "pas",
            "token",
            "connection",
            "my password is secret",
            "secrete",
        ]
        expected_result = [
            "password",
            "secrete",
            "pwd",
            "secret",
            "pass",
            "token",
            "conn",
            "password",
            "secrete",
        ]

        for index, string in enumerate(test_strings):
            match = re.search(RE_CANDIDATES, string)
            if match:
                assert match.group(1).lower() == expected_result[index]

    def test_false_positives(self):
        test_strings = [
            "passenger",
            "compass",
            "passport",
            "complicated",
            "passive",
            "passworded",
        ]

        for string in test_strings:
            match = re.search(RE_CANDIDATES, string)
            assert match is None

    def test_RE_WORDS(self):
        # Test with a word that contains 'password' as a substring
        assert not re.search(RE_WORDS, "notmypassword")
        # Test with a word that contains 'pass' as a substring
        assert not re.search(RE_WORDS, "passenger")
        # Test with a complete word 'password'
        assert re.search(RE_WORDS, "password")
        # Test with a complete word 'secrete'
        assert re.search(RE_WORDS, "secrete")
        # Test with a complete word 'token'
        assert re.search(RE_WORDS, "token")


if __name__ == "__main__":
    unittest.main()
