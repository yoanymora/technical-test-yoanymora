import unittest
from palindrome import is_palindrome

class Test(unittest.TestCase):

    def test_01_is_palindrome(self):
        """Case 1: The string `ddedd` is given to check if it's a palindrome, the result must be True"""
        self.assertEqual(
            is_palindrome("ddedd"),
            "The string ddedd is a palindrome.",
            "Error! The result should be a palindrome.")

    def test_02_is_palindrome(self):
        """Case 2: The string `ddewddw` is given to check if it's a palindrome, the result must be False"""
        self.assertEqual(
            is_palindrome("ddewddw"),
            "The string ddewddw isn't a palindrome.",
            "Error! The result shouldn't be a palindrome.")

    def test_03_is_palindrome(self):
        """Case 3: The string `wddw` is given to check if it's a palindrome, the result must be True"""
        self.assertEqual(
            is_palindrome("wddw"),
            "The string wddw is a palindrome.",
            "Error! The result should be a palindrome.")

    def test_04_is_palindrome(self):
        """Case 4: The string `wdwd` is given to check if it's a palindrome, the result must be False"""
        self.assertEqual(
            is_palindrome("wdwd"),
            "The string wdwd is a palindrome.",
            "Error! The result shouldn't be a palindrome")

    def test_05_is_palindrome(self):
        """Case 5: The string is empty, the result should be a string indicating to input other value"""
        self.assertEqual(
            is_palindrome(""),
            "Please enter a valid string.",
            "Error! The result should be an indication to input other string.")

    def test_06_is_palindrome(self):
        """Case 6: The string `wDdw` is given to check if it's a palindrome, the result must be True, even with upper
        case letters"""
        self.assertEqual(
            is_palindrome('wdDdw'),
            "The string wdDdw is a palindrome.",
            "Error! The result should be a palindrome.")

    def test_07_is_palindrome(self):
        """Case 7: The string `wdDdw a` is given to check if it's a palindrome, the result must be False"""
        self.assertEqual(
            is_palindrome('wdDdw a'),
            "The string wdDdw a isn't a palindrome.",
            "Error! The result shouldn't be a palindrome")


if __name__ == '__main__':
    unittest.main()
