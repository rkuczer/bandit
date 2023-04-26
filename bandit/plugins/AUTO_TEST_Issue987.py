import unittest
import re
from bandit.plugins.general_hardcoded_password import RE_WORDS, RE_CANDIDATES
class TestRegex(unittest.TestCase):
    def test_RE_WORDS(self):
        # Test that RE_WORDS matches only complete words
        pattern = re.compile(r"\b" + RE_WORDS + r"\b", re.IGNORECASE)
        matches = pattern.findall("The password is 'password'")
        self.assertEqual(matches, ['password'])

        # Test that RE_WORDS does not match parts of words
        matches = pattern.findall("The password is 'passcode'")
        self.assertEqual(matches, [])

    def test_RE_CANDIDATES(self):
        # Test that RE_CANDIDATES matches only candidate strings that are not part of larger words
        pattern = re.compile(
            r"(?<!\w)(" + RE_WORDS + r"$|_" + RE_WORDS + r"_|^" + RE_WORDS + r"_|_" + RE_WORDS + r"$)",
            re.IGNORECASE
        )
        matches = pattern.findall("The password is 'password'")
        self.assertEqual(matches, ["'password'"])

        # Test that RE_CANDIDATES does not match candidate strings that are part of larger words
        matches = pattern.findall("The password is 'passcode'")
        self.assertEqual(matches, [])

if __name__ == '__main__':
    unittest.main()
