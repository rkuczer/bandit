import unittest

from bandit.core.utils import get_nosec


class TestGetNosec(unittest.TestCase):
    def test_nested_dict_nosec(self):
        # Mock the nosec lines and context with nested dictionary annotations
        nosec_lines = {5: "# nosec B101", 10: {15: "# nosec B303"}}
        context = {"lineno": 10, "linerange": [15]}

        # Mock the expected result
        expected_result = {15: "# nosec B303"}

        # Call the function and check the result
        result = get_nosec(nosec_lines, context)
        self.assertEqual(result, expected_result)

    def test_higher_nosec_ignored(self):
        # Mock the nosec lines and context with a higher level nosec annotation
        nosec_lines = {5: "# nosec B101", 10: "# nosec B303"}
        # Mock the context with a nested dictionary annotation
        context = {"lineno": 10, "linerange": [15]}

        # Mock the expected result
        expected_result = "# nosec B303"

        # Call the function and check the result
        result = get_nosec(nosec_lines, context)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
# test for fixes to the  Using # nosec BXXX annotation in a nested dict causes "higher" annotations to be ignored #1003 where
# Summary: Using a # nosec BXXX annotation inside a nested data structure appears to cause "higher" nosec annotations to be ignored.
# Summary: nosec BXX- tells the program to ignore certain issues or error; in this case security issues.  issue is if we use this notation in nested dictionary, it may not work properly and will only ignore security issues for nested dict, not the whole dictionary
