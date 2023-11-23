import unittest
from letter_count import letter_count

def test_01_letter_count(self):
    """Case 1: Hola mundo is the string, the result must be {h: 1, o: 2, l: 1, a: 1, m: 1, u: 1, n: 1, d: 1}"""
    print(letter_count('Hola mundo'))

if __name__ == '__main__':
    unittest.main()