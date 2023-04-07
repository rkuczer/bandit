import unittest
from bandit.core.utils import get_nosec

class TestGetNosec(unittest.TestCase):
    def test_nested_dict_nosec(self):
        # Mock the nosec lines and context with nested dictionary annotations
        nosec_lines = {
            5: "# nosec B101",
            10: {
                15: "# nosec B303"
            }
        }
        context = {
            "lineno": 10,
            "linerange": [15]
        }

        # Mock the expected result
        expected_result = {15: "# nosec B303"}
        print(expected_result)

        # Call the function and check the result
        result = get_nosec(nosec_lines, context)
        self.assertEqual(result, expected_result)

    def test_higher_nosec_ignored(self):
        # Mock the nosec lines and context with a higher level nosec annotation
        nosec_lines = {
            5: "# nosec B101",
            10: "# nosec B303"
        }
        # Mock the context with a nested dictionary annotation
        context = {
            "lineno": 10,
            "linerange": [15]
        }

        # Mock the expected result
        expected_result = "# nosec B303"
        print(expected_result)

        # Call the function and check the result
        result = get_nosec(nosec_lines, context)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
