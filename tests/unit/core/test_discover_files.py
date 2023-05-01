import unittest
from unittest import mock

from bandit.core.config import BanditConfig
from bandit.core.manager import BanditManager


class TestManager(unittest.TestCase):
    def setUp(self):
        self.b_conf = BanditConfig()
        self.manager = BanditManager(self.b_conf, "non_aggressive")

    def test_discover_files_empty_targets(self):
        self.manager.discover_files([])
        self.assertEqual([], self.manager.files_list)
        self.assertEqual([], self.manager.excluded_files)

    @mock.patch("sys.exit")
    @mock.patch("builtins.print")
    def test_discover_files_nonexistent_file(self, mock_print, mock_exit):
        self.manager.discover_files(["nonexistent_file.py"])
        mock_print.assert_called_with(
            "Error: nonexistent_file.py does not exist"
        )
        mock_exit.assert_called_with(1)


if __name__ == "__main__":
    unittest.main()
#test for fixes for Alex individual issue where bandit prints too much information about issues even on a file that doesnt even exist.
