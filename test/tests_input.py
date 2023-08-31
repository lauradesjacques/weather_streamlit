import unittest

def is_input_empty(input_string):
    return input_string.strip() == ""

class TestInputIsEmpty(unittest.TestCase):

    def test_empty_input(self):
        self.assertTrue(is_input_empty(""))
        self.assertTrue(is_input_empty("   "))  # Test with whitespace

    def test_non_empty_input(self):
        self.assertFalse(is_input_empty("hello"))
        self.assertFalse(is_input_empty("   hello   "))  # Test with whitespace


if __name__ == '__main__':
    unittest.main()
