import unittest
from prime_numbers import is_prime_number

class Test(unittest.TestCase):

    def test_01_is_prime_number(self):
        """Case 1: 1 has only one factor therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(1),
            "The number 1 isn't prime.",
            "Error! The result should be False")

    def test_02_is_prime_number(self):
        """Case 2: 2 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(2),
            "The number 2 is prime.",
            "Error! The result should be True")

    def test_03_is_prime_number(self):
        """Case 3: 3 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(3),
            "The number 3 is prime.",
            "Error! The result should be True")

    def test_04_is_prime_number(self):
        """Case 4: 4 is divisible by 1, 2 and 4 thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(4),
            "The number 4 isn't prime.",
            "Error! The result should be False")

    def test_05_is_prime_number(self):
        """Case 5: 5 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(5),
            "The number 5 is prime.",
            "Error! The result should be True")

    def test_06_is_prime_number(self):
        """Case 6: 6 is divisible by 1, 2, 3 and 6 thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(6),
            "The number 6 isn't prime.",
            "Error! The result should be False")

    def test_07_is_prime_number(self):
        """Case 7: 7 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(7),
            "The number 7 is prime.",
            "Error! The result should be True")

    def test_08_is_prime_number(self):
        """Case 8: 8 is divisible by 1, 2, 4 and 8 thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(8),
            "The number 8 isn't prime.",
            "Error! The result should be False")

    def test_09_is_prime_number(self):
        """Case 9: 9 is divisible by 1, 3, and 9 thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(9),
            "The number 9 isn't prime.",
            "Error! The result should be False")

    def test_10_is_prime_number(self):
        """Case 10: 17 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(17),
            "The number 17 is prime.",
            "Error! The result should be True")

    def test_11_is_prime_number(self):
        """Case 11: 18 last digit is pair thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(18),
            "The number 18 isn't prime.",
            "Error! The result should be False")

    def test_12_is_prime_number(self):
        """Case 12: 89 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(89),
            "The number 89 is prime.",
            "Error! The result should be True")

    def test_13_is_prime_number(self):
        """Case 13: 95 last digit is 5 thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(95),
            "The number 95 isn't prime.",
            "Error! The result should be False")

    def test_14_is_prime_number(self):
        """Case 14: 97 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(97),
            "The number 97 is prime.",
            "Error! The result should be True")

    def test_15_is_prime_number(self):
        """Case 15: 673 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(673),
            "The number 673 is prime.",
            "Error! The result should be True")

    def test_16_is_prime_number(self):
        """Case 16: 674 last digit is pair thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(674),
            "The number 674 isn't prime.",
            "Error! The result should be False")

    def test_17_is_prime_number(self):
        """Case 17: 997 has 2 factors therefore is a prime number."""
        self.assertEqual(
            is_prime_number(997),
            "The number 997 is prime.",
            "Error! The result should be True")

    def test_18_is_prime_number(self):
        """Case 18: 998 last digit is pair thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(998),
            "The number 998 isn't prime.",
            "Error! The result should be False")

    def test_19_is_prime_number(self):
        """Case 19: 678 last digit is pair thus has more than 2 factors therefore isn't a prime number."""
        self.assertEqual(
            is_prime_number(678),
            "The number 678 isn't prime.",
            "Error! The result should be False")

if __name__ == '__main__':
    unittest.main()
