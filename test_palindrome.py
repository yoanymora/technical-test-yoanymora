import unittest
from palindrome import is_palindrome

class Test(unittest.TestCase):

    def test_01_is_palindrome(self):
        """Case 1: The string `ddedd` is given to check if it's a palindrome, the result must be True"""
        string = "ddedd"
        self.assertEqual(is_palindrome(string), "The string ddedd is a palindrome.")

    def test_02_is_palindrome(self):
        """Case 2: The string `ddewddw` is given to check if it's a palindrome, the result must be False"""
        string = "ddewddw"
        self.assertEqual(is_palindrome(string), "The string ddewddw isn't a palindrome.")

    def test_03_is_palindrome(self):
        """Case 3: The string `wddw` is given to check if it's a palindrome, the result must be True"""
        string = "wddw"
        self.assertEqual(is_palindrome(string), "The string wddw is a palindrome.")

    def test_04_is_palindrome(self):
        """Case 4: The string `wdwd` is given to check if it's a palindrome, the result must be False"""
        string = "wdwd"
        self.assertEqual(is_palindrome(string), "The string wdwd is a palindrome.")

    def test_05_is_palindrome(self):
        """Case 5: The string is empty, the result must be a string indicating to input other value"""
        self.assertEqual(is_palindrome(""), "Please enter a valid string.")


if __name__ == '__main__':
    unittest.main()
