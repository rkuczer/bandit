import os
import unittest
import subprocess

# Change to the "core" directory
os.chdir("/Users/omar/PycharmProjects/bandit2/bandit/core")

class TestBanditCommand(unittest.TestCase):

    def test_bandit_command(self):

        # Run the bandit command
        command = "bandit -r . -f json -q > output.json"
        subprocess.run(command, shell=True, check=True)

        # Check that the output file exists
        self.assertTrue(os.path.exists("output.json"))

        # Check that the output file is not empty
        self.assertGreater(os.path.getsize("output.json"), 0)


if __name__ == '__main__':
    unittest.main()
