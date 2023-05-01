import unittest

from bandit.plugins.asserts import assert_used
from bandit.plugins.asserts import gen_config


class TestAssertUsed(unittest.TestCase):
    def test_assert_used(self):
        context = {"filename": "test_file.py"}
        # testing the result from context of a test file
        result = assert_used(context, gen_config("assert_used"))
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

#test for fixes for the Multiline docstrings exclusion error #836 andit incorrectly marking an B101 assert used error with a  #nosec comment in this code assert yaml.load("""{ # nosec
#         }""") == []
