import ast
import unittest


def extract_strings(node):
    class StringVisitor(ast.NodeVisitor):
        def __init__(self):
            self.strings = []

        def visit_Str(self, node):
            self.strings.append(node.s)

    visitor = StringVisitor()
    visitor.visit(node)
    result = (node, " ".join(visitor.strings))
    return result


class TestExtractStrings(unittest.TestCase):
    def test_extract_strings(self):
        # Create a simple AST node with two string literals
        node = ast.parse("print('john,')\nprint('santore!')")
        result = extract_strings(node)
        # Verify that the result tuple contains the original node object
        self.assertEqual(result[0], node)
        # Verify that the result tuple contains a string with both
        # string literals
        self.assertEqual(result[1], "john, santore!")


if __name__ == "__main__":
    unittest.main()
# Test for Warren's individual issue where the
# concat strings function adds a space that should
# not be there
