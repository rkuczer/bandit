import unittest

from bandit.core.config import BanditConfig
from bandit.core.manager import BanditManager


class TestDiscoverFiles(unittest.TestCase):
    def setUp(self):
        self.b_conf = BanditConfig()
        self.b_mgr = BanditManager(self.b_conf, "non_aggressive")

    def test_nonexisting_target(self):
        with self.assertRaises(FileNotFoundError):
            self.b_mgr.discover_files(["nonexistant_file.py"])


if __name__ == "__main__":
    unittest.main()
