import unittest
import ast
from bandit.plugins.general_hardcoded_password import hardcoded_password_string

PASSWORD_STRINGS = ['password', 'secret', '123456']


class TestHardcodedPasswordString(unittest.TestCase):
    def test_str(self):
        node = ast.parse("'password'")
        self.assertTrue(hardcoded_password_string(node.body[0].value, _file="dummy_file.py"))

    def test_joined_str(self):
        node = ast.parse("f'password{123}'")
        self.assertTrue(hardcoded_password_string(node.body[0].value, _file="dummy_file.py"))

    def test_literal(self):
        node = ast.parse("Literal['password']")
        self.assertTrue(hardcoded_password_string(node.body[0].value, _file="dummy_file.py"))

    def test_final(self):
        node = ast.parse("Final['password']")
        self.assertTrue(hardcoded_password_string(node.body[0].value, _file="dummy_file.py"))

    def test_not_password_string(self):
        node = ast.parse("'username'")
        self.assertFalse(hardcoded_password_string(node.body[0].value, _file="dummy_file.py"))


if __name__ == '__main__':
    unittest.main()
