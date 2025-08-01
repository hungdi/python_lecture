import unittest

class TestIs(unittest.TestCase):
    def test_is_same_object(self):
        a = [1, 2]
        b = a
        self.assertIs(a, b)


unittest.main()