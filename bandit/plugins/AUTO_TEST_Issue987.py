import unittest
import ast
import re

from unittest.mock import patch, Mock

from bandit.plugins.general_hardcoded_password import RE_WORDS, RE_CANDIDATES, hardcoded_password_string, \
    hardcoded_password_funcarg


class TestHardcodedPassword(unittest.TestCase):

    def test_hardcoded_password_string(self):
        node_mock = Mock()
        node_mock._bandit_parent = ast.Assign()
        node_mock.s = 'password'
        node_mock._bandit_parent.targets = [ast.Name(id='password')]
        with patch('file_to_test.RE_CANDIDATES', re.compile(
                r"(\b(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)\b$|_(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)_|^_(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)_|_(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)_$)",
                re.IGNORECASE)):
            result = hardcoded_password_string(ast.parse('password').body[0].value)
            self.assertIsNotNone(result)
            self.assertEqual(result.severity, 'LOW')
            self.assertEqual(result.confidence, 'MEDIUM')
            self.assertEqual(result.cwe, '259')
            self.assertEqual(result.text, "Possible hardcoded password: 'password'")

    def test_hardcoded_password_funcarg(self):
        node_mock = Mock()
        node_mock._bandit_parent = ast.Call()
        node_mock._bandit_parent.keywords = [ast.keyword(arg='password', value=ast.Str(s='secret'))]
        node_mock._bandit_parent.args = []
        node_mock._bandit_parent.func = ast.Name(id='some_function')
        node_mock._bandit_parent.func.id = 'some_function'
        with patch('file_to_test.RE_CANDIDATES', re.compile(
                r"(\b(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)\b$|_(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)_|^_(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)_|_(pas+wo?r?d|pass(phrase)?|pwd|secrete|password|pass|to+k?en|conn?)_$)",
                re.IGNORECASE)):
            result = hardcoded_password_funcarg(node_mock)
            self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
