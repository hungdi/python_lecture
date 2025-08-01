import unittest

class TestIn(unittest.TestCase):
    def test_in(self):
        self.assertIn("apple", ["banana", "apple", "grape"])


unittest.main()