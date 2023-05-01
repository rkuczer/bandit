import ast
import unittest

from bandit.core.utils import linerange


class TestLineRange(unittest.TestCase):
    def test_linerange(self):
        content = (
            "def func():\n    print('hello world')\n\nx = 5\nif x > 3:\n    "
            "print('x is greater than 3')\n"
        )
        node = ast.parse(content)
        self.assertEqual(linerange(node), [0, 1])


if __name__ == "__main__":
    unittest.main()
