import unittest

from name_not_found_exception import NameNotFoundException

class TestNameNotFoundException(unittest.TestCase):
    def test_exception_default(self):
        actual = NameNotFoundException().message
        expected = 'Flavor not found in list of available flavors'
        print(NameNotFoundException())
        self.assertEqual(actual, expected)

    def test_exception_custom(self):
        actual = NameNotFoundException('This is a test message').message
        expected = 'This is a test message'
        self.assertEqual(actual, expected)
