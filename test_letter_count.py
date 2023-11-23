import unittest
from letter_count import letter_count

class Test(unittest.TestCase):
    def test_01_letter_count(self):
        """Case 1: `Hola mundo` is the string, the result must be {h: 1, o: 2, l: 1, a: 1, m: 1, u: 1, n: 1, d: 1}"""
        expected_result = {'h': 1, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1, 'o': 2}
        result = letter_count('Hola mundo')
        self.assertEqual(
            result,
            expected_result,
            "Error! The result must be %s but get %s instead" % (expected_result, result)
        )

    def test_02_letter_count(self):
        """Case 2: `Hola mundo` is the string, the result must be {h: 1, o: 2, l: 1, a: 1, m: 1, u: 1, n: 1, d: 1}
        but the dict to be compared has less keys"""
        expected_result = {'h': 1, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
        result = letter_count('Hola mundo')
        self.assertNotEqual(
            result,
            expected_result,
            "Error! The result must be %s but get %s instead" % (expected_result, result)
        )

    def test_03_letter_count(self):
        """Case 3: `Hola mundo` is the string, the result must be {h: 1, o: 2, l: 1, a: 1, m: 1, u: 1, n: 1, d: 1}
        but the dict to be compared has more keys"""
        expected_result = {'h': 1, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1, 'o': 2, 'j': 2, 'k': 3}
        result = letter_count('Hola mundo')
        self.assertNotEqual(
            result,
            expected_result,
            "Error! The result must be %s but get %s instead" % (expected_result, result)
        )

    def test_04_letter_count(self):
        """Case 4: `Hola mundo` is the string, the result must be {h: 1, o: 2, l: 1, a: 1, m: 1, u: 1, n: 1, d: 1}
        but the dict to be compared has incorrect numbers of lettes"""
        expected_result = {'h': 10, 'l': 2, 'a': 1, 'm': 1, 'u': 1, 'n': 11, 'd': 6, 'o': 2}
        result = letter_count('Hola mundo')
        self.assertNotEqual(
            result,
            expected_result,
            "Error! The result must be %s but get %s instead" % (expected_result, result)
        )

    def test_05_letter_count(self):
        """Case 5: `Holamundooo O` is the string, the result must be {h: 1, o: 5, l: 1, a: 1, m: 1, u: 1, n: 1, d: 1}"""
        expected_result = {'h': 1, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1, 'o': 5}
        result = letter_count('Holamundooo O')
        self.assertEqual(
            result,
            expected_result,
            "Error! The result must be %s but get %s instead" % (expected_result, result)
        )

if __name__ == '__main__':
    unittest.main()
