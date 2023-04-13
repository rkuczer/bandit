import unittest

from bandit.plugins.asserts import assert_used, gen_config


class TestAssertUsed(unittest.TestCase):
    def test_assert_used(self):
        context = {"filename": "test_file.py"}

        result = assert_used(context, gen_config("assert_used"))
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
