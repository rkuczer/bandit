import unittest
import re


from bandit.plugins.general_hardcoded_password import RE_WORDS, RE_CANDIDATES


class TestRegex(unittest.TestCase):
    def test_valid_input(self):
        regex = re.compile(RE_CANDIDATES)
        valid_inputs = ["password", "passphrase", "pwd", "secrete", "pass", "token", "conn"]
        for input_str in valid_inputs:
            with self.subTest(input_str=input_str):
                self.assertIsNotNone(regex.search(input_str))


if __name__ == '__main__':
    unittest.main()