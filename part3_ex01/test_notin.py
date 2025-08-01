import unittest

class TestNotIn(unittest.TestCase):
    def test_not_in(self):
        self.assertNotIn("watermelon", ["apple", "grape", "cherry"])


unittest.main()