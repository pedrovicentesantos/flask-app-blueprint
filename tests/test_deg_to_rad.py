'''
Test case for the deg to rad function
'''
import math
import unittest

from utils.utils import deg_to_rad


class DegToRadTestCase(unittest.TestCase):
    def test_0_degree(self):
        expected = 0
        result = deg_to_rad(0)
        self.assertEqual(result, expected)

    def test_180_degrees(self):
        expected = math.pi
        result = deg_to_rad(180)
        self.assertEqual(result, expected)

    def test_negative_degree(self):
        expected = -math.pi
        result = deg_to_rad(-180)
        self.assertEqual(result, expected)

    def test_not_number(self):
        expected = None
        result = deg_to_rad('word')
        self.assertEqual(result, expected)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
