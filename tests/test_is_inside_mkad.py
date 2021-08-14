'''
Test case for the is inside mkad function
'''
import unittest

from utils.utils import is_inside_mkad


class IsInsideMKADTestCase(unittest.TestCase):
    def test_inside(self):
        expected = True
        result = is_inside_mkad(10)
        self.assertEqual(result, expected)

    def test_outside(self):
        expected = False
        result = is_inside_mkad(30)
        self.assertEqual(result, expected)

    def test_border(self):
        expected = True
        result = is_inside_mkad(29.05)
        self.assertEqual(result, expected)

    def test_not_number(self):
        expected = None
        result = is_inside_mkad('word')
        self.assertEqual(result, expected)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
